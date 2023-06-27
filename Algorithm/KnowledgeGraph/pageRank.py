"""
pip install networkx==3.1
https://networkx.org/documentation/stable/tutorial.html
"""
import logging
from typing import Union
import json
import os

import numpy as np
import pandas as pd
import networkx as nx
from networkx.algorithms.link_analysis import pagerank

N_START = "n_start"
ALPHA = "alpha"
MAX_ITER = "max_iter"
TOL = "tol"
ORIGIN_COL = "origin_col"
TARGET_COL = "target_col"
WEIGHT_COL = "weight_col"
LABEL = "label"

NODES = 'nodes'
SCORES = 'scores'

SAVE_FILE = "meta.json"


class PageRank:
    def __init__(self, origin_col=None, target_col=None, weight_col=None, label=None,
                 n_start=None, alpha=0.85, max_iter=100, tol=1e-6):
        """
        origin_col : string, optional
            当输入的是pd.dataframe 起始顶点列

        target_col : string, optional
            当输入的是pd.dataframe 目标顶点列

        weight_col : string, optional
            当输入的是pd.dataframe 权重列

        label : string, optional
            当输入的是gml文件路径时 顶点的便签

        alpha : float, optional
            Damping parameter for PageRank, default=0.85.

        max_iter : integer, optional
            Maximum number of iterations in power method eigenvalue solver.

        tol : float, optional
            Error tolerance used to check convergence in power method solver.

        nstart : dictionary, optional
            Starting value of PageRank iteration for each node.

        """
        self.origin_col = origin_col
        self.target_col = target_col
        self.weight_col = weight_col
        self.label = label
        self.n_start = n_start
        self.alpha = alpha
        self.max_iter = max_iter
        self.tol = tol

    @staticmethod
    def check_input(data, origin, target, weight):  # type:(Union[pd.DataFrame, str], str, str, str)->None
        """

        :param data:
        :param origin:
        :param target:
        :param weight:
        :return:
        """
        if isinstance(data, pd.DataFrame):
            cols = data.columns.tolist()
            msg = "特征列{col}不存在于输入的数据集中！"
            if origin is not None and origin not in cols:
                raise ValueError(msg.format(col=origin))
            if target is not None and target not in cols:
                raise ValueError(msg.format(col=target))
            if weight is not None and weight not in cols:
                raise ValueError(msg.format(col=weight))
        elif isinstance(data, str):
            if not data.endswith(".gml"):
                raise ValueError("输入的数据文件不是gml格式！")
            if not os.path.exists(data):
                raise ValueError("文件：{} 不存在！")
        else:
            raise ValueError("数据只支持输入pd.Dataframe或gml文件路径！")

    def fit(self, dataset):  # type:(Union[pd.DataFrame,str])->PageRankModel
        """

        :param dataset:
        :return:
        """
        PageRank.check_input(data=dataset, origin=self.origin_col, target=self.target_col, weight=self.weight_col)
        param = {
            N_START: self.n_start,
            ALPHA: self.alpha,
            MAX_ITER: self.max_iter,
            TOL: self.tol,
            ORIGIN_COL: self.origin_col,
            TARGET_COL: self.target_col,
            WEIGHT_COL: self.weight_col,
            LABEL: self.label
        }

        return PageRankModel(param=param)


class PageRankModel(object):
    """
    Sklearn 自定义算法代码
    """

    def __init__(self, param=None):
        """
        类的构造函数
        """
        self.param = param
        if param is None:
            self.param = PageRankModel.load()
        self.origin_col = self.param.get(ORIGIN_COL)
        self.target_col = self.param.get(TARGET_COL)
        self.weight_col = self.param.get(WEIGHT_COL)
        self.label = self.param.get(LABEL)
        self.n_start = self.param.get(N_START)
        self.alpha = self.param.get(ALPHA, 0.85)
        self.max_iter = self.param.get(MAX_ITER, 100)
        self.tol = self.param.get(TOL, 1e-6)

    def transform(self, dataset):  # type:(Union[pd.DataFrame,str])->pd.DataFrame
        """

        :param dataset:
        :return:
        """
        PageRank.check_input(data=dataset, origin=self.origin_col, target=self.target_col, weight=self.weight_col)
        msg = "只支持.gml数据或pd.Dataframe数据"
        if isinstance(dataset, str):
            # 当dataset为文件路径时
            logging.info("数据集路径为：{}".format(dataset))
            if dataset.endswith(".gml"):
                graph = nx.read_gml(dataset, label=self.label)
            else:
                raise ValueError(msg)

        elif isinstance(dataset, pd.DataFrame):
            # 当dataset为pd.dataframe时
            cols = dataset.columns.tolist()
            if self.weight_col is not None and self.weight_col in cols:
                weights = dataset[self.weight_col].values
            else:
                weights = None
            edges_cols = [self.origin_col, self.target_col]
            graph = nx.Graph()  # 创建空图
            if weights is not None:
                edges_data = dataset[edges_cols + [self.weight_col]].values
                for edge in edges_data:
                    graph.add_edge(edge[0], edge[1], weight=edge[2])
            else:
                edges_data = dataset[edges_cols].values
                for edge in enumerate(edges_data):
                    graph.add_edge(edge[0], edge[1])

            self.names = graph.nodes
            if len(self.names) <= 0:
                self.names = np.unique(dataset[edges_cols].values.reshape(1, -1)[0])

        else:
            raise ValueError(msg)

        self.graph = graph

        # 获取邻接矩阵
        self.adjacency = [(n, nbrdict) for n, nbrdict in graph.adjacency()]

        # 计算pageRank值
        self.scores = pagerank(G=graph, nstart=self.n_start, alpha=self.alpha, max_iter=self.max_iter,
                               tol=self.tol)
        # 输出
        res_data = [[res[0], res[1]] for res in self.scores.items()]
        res = pd.DataFrame(res_data, columns=[NODES, SCORES])

        return res

    def save(self, save_dir=None):  # type:(str)->None
        """
        save model
        :return:
        """
        if save_dir is None:
            save_dir = os.path.dirname(__file__)

        save_path = os.path.join(save_dir, SAVE_FILE)
        with open(save_path, "w") as f:
            f.write(json.dumps(self.param))

    @staticmethod
    def load(load_dir=None):  # type:(str)->Union[dict, PageRankModel]
        """
        load model
        :return:
        """
        if load_dir is None:
            current_path = os.path.dirname(__file__)
            load_path = os.path.join(current_path, SAVE_FILE)
            with open(load_path, "r") as f:
                param = json.loads(f.read())
            return param
        else:
            load_path = os.path.join(load_dir, SAVE_FILE)
            with open(load_path, "r") as f:
                param = json.loads(f.read())
            return PageRankModel(param=param)

    def plot(self, fig_size=(8, 8), k=None, node_size=6000, node_color="m"):
        """

        :param fig_size:
        :param k:
        :param node_size:
        :param node_color:
        :return:
        """

        import matplotlib.pyplot as plt
        plt.figure(figsize=fig_size)
        layout = nx.spring_layout(self.graph, k=k)
        nx.draw(self.graph, pos=layout, node_size=[x * node_size for x in self.scores.values()],
                node_color=node_color, with_labels=True)
        plt.show()


if __name__ == '__main__':
    # 通过csv文件
    df_data = pd.read_csv("data/edges_weight_data.csv")
    csv_model = PageRank(origin_col="src", target_col="dst", weight_col="weights").fit(df_data)
    csv_model.save()  # 默认保存到当前目录
    csv_model = PageRankModel()  # 默认从当前目录load模型
    print(csv_model.transform(df_data))

    # 通过gml文件
    gml_data = "data/test.gml"
    save_path = "data"
    gml_model = PageRank(label="label").fit(gml_data)
    gml_model.save(save_dir=save_path)  # 指定保存路径
    load_model = PageRankModel.load(load_dir=save_path)  # 指定load路径
    print(load_model.transform(gml_data))
    load_model.plot(k=1.5, node_size=8000)
