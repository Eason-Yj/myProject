# 机器学习

## [统计分析指标](statistical_analysis%2FREADME.md)

## 数据预处理(PreProcessing)
- 数据采样：主要用来处理样本不平衡问题或切分数据集
  - 随机采样：按样本数，样本比例进行随机采样
  - 分层采样：按某个特征的唯一值将样本集划分为多个子样本集，再对每个子样本集进行随机采样
  - SMOTE过采样：从样本集的少数类样本中选一部分样本，这部分样本中每个样本采用knn算法找出其k个最近邻样本，再随机选择一个最近邻样本，最后在两者之间随机生成一个新样本
  - 欠采样：对多的一类进行少量随机选择
- 缺失值处理
  - 删除缺失行：某行的多个特征都为缺失值时删除该行
  - 删除缺失列：某列有大量缺失值时可考虑删除该列
  - 缺失值填充：
    - 常值填充：0值、均值、众数、中位数等
    - 滑动平均窗口法：取缺失值前后n个值，用这些值的均值填充
    - 向前/向后填充：使用缺失值的后一个值或前一个值填充
    - KNN填充：使用n个最近邻样本的对应位置的非空数值的均值填补缺失值。
- 异常值
  - 异常值识别：
    - 箱线图人工判断
    - KSigma(默认3σ)：当样本集符合正态分布时，异常值的判定为样本值与平均值的偏差超过k倍标准差
    - IQR(四分位距异常检测):上界为「Q3 + 1.5 \times IQR」，下界为「Q1 - 1.5 \times IQR」，「IQR = Q3 - Q1」在上下边界之外的则为异常值
    - IForest(孤立森林 IsolationForest)：
      - 原理：该算法使用iTree的二叉搜索树结构来孤立样本。由于异常值的数量较少且与大部分样本的疏离性，因此，异常值会被更早的孤立出来，也即异常值会距离iTree的根节点更近，而正常值则会距离根节点有更远的距离。
      - ① 从训练集中选出n个样本作为根节点，随机选择一个维度，在该维度上随机选择一点生成超平面将样本空间切分为两个子空间，重复上述过程不断构建子节点直到达到限定目标进而生成一颗iTree；
      - ② 再重复上述所有过程构建多棵iTree
      - ③ 预测集样本，将单个样本遍历过每颗iTree获取该样本在所有树中的平均高度，进而计算出每个样本的异常值得分，分值越小表示数据越为异常。
    - LOF(局部异常因子)：
  - 异常值处理：
    - 删除异常值：当异常值较少，且数据量较大时
    - 异常值替换：使用固定值或均值、中位数、其他分位数等统计值替换缺失值
    - 模型预测

## [特征工程](feature_engineering%2FREADME.md)
- 特征编码：onehot(独热)、dummy(哑变量)、ordinal-encoder(顺序)、woe
- 特征标量化：指数变换、z-score(标准化), min-max(归一化)，robust-scaler
- 特征选择：相关性系数筛选，特征重要性筛选、多重共线性、逐步回归、嵌入式特征选择、包装式特征选择
- 特征降维：因子分析、PCA(主成分分析)、LDA(线性判别分析)
- 特征衍生：特征交叉、多项式衍生

## 模型建模
- [Classification(分类模型)](Classification%2FREADME.md)
    - KNN
    - 逻辑回归
    - 决策树
    - 随机森林
    - GBDT
    - XGBoost
    - CatBoost
    - LightGBM
    - AdaBoost
    - Bagging
    - Stacking
    - SVM


- [Regression(回归模型)](Regression%2FREADME.md)
    - 线性回归
    - 随机森林
    - GBDT
    - XGBoost
    - CatBoost
    - LightGBM
    - AdaBoost
    - Bagging
    - Stacking

- [Cluster(聚类模型)](Cluster%2FREADME.md)
    - Kmeans
    - DBSCAN
    - AP聚类
    - 凝聚层次聚类
    - 谱聚类

- [TimeSeries(时序模型)](Time_Series%2FREADME.md)
    - arima
    - DeepFM
- [KnowledgeGraph(知识图谱模型)](Knowledge_Graph%2FREADME.md)
- [Evaluation(模型评估)](model_evaluation%2FREADME.md)

## 模型评估
- 二分类评估：准确率、均衡准确率、平均精确率、F1-score、召回率、对数损失、roc_auc
- 多分类评估：准确率、均衡准确率、对数损失
- 回归评估：最大残差(max_error)、平均绝对误差(MAE)、均方误差(MSE)、均方根误差(RMSE)、均方对数损失(MSLE)、中值绝对误差、判定系数(r2)
- 聚类评估：轮廓系数、CH系数、戴维森堡丁指数

## 模型可解释性
- SHAP
- LIME
- PDP
- ICE
- 特征重要性
