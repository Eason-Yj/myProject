# PageRank

[代码](pageRank.py)

## 1 概念

PageRank算法的基本想法是在有向图上定义一个随机游走模型，即一阶马尔可夫链，描述随机游走者沿着有向图随机访问各个结点的行为。在一定条件下，极限情况访问每个结点的概率收敛到平稳分布，这时各个结点的平稳概率值就是其PageRank值，表示结点的重要度。PageRank
是递归定义的，PageRank 的计算可以通过迭代算法进行。

## 2 相关Python库

- scikit-network: https://scikit-network.readthedocs.io/en/latest/tutorials/ranking/pagerank.html?highlight=pagerank#PageRank
- networkx: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#pagerank
- igraph: https://python.igraph.org/en/stable/api/igraph.Graph.html#pagerank
