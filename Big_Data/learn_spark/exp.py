from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, IntegerType, ShortType, FloatType, StringType

# # 初始化sparkSession
# sparkSession = SparkSession.builder.appName("wyj-exp").master("local").config("spark.driver.cores", "2").getOrCreate()
#
# # 通过 list 创建DataFrame
# data = [
#     (1, 2, 3.1, "a"),
#     (2, 4, 2.2, "b"),
#     (1, 2, 1.2, "c"),
# ]
# schema = StructType([
#     StructField(name="col1", dataType=ShortType()),
#     StructField(name="col2", dataType=IntegerType()),
#     StructField(name="col3", dataType=FloatType()),
#     StructField(name="target", dataType=StringType()),
# ])
# df = sparkSession.createDataFrame(data=data, schema=schema)
# df.show()
# df.printSchema()

# # 读取外部数据创建DataFrame
# df = sparkSession.read.csv("../dataset/v_train_dataset.csv", header=True)
# df.show()
# df.printSchema()

from pyspark.conf import SparkConf

sc = SparkConf().setAll([
    ("spark.driver.host", "localhost"),  # 配置driver地址
    ("spark.driver.cores", "2"),  # 设置driver使用的核心数
    ("spark.driver.memory", "1g"),  # driver给的内存大小
    ("spark.driver.maxResultSize", "20g"),  # 设置driver端结果存放的最大容量，这里设置成为20G，超过20G的数据, job就直接放弃
    ("spark.executor.instances", "2"),  # 设置executor个数
    ("spark.executor.cores", "2"),  # 每个executor的内存
    ("spark.executor.memory", "2g"),  # 每个executor的内存
    ("spark.submit.deployMode", "cluster"),  # spark任务提交模式，线上使用cluster模式，开发使用client模式
    ("spark.worker.timeout", "500"),  # 基于standAlone模式下提交任务，worker的连接超时时间
    ("spark.cores.max", "10"),  # 基于standAlone和mesos模式下部署，最大的CPU和数量
    ("spark.rpc.askTimeout", "600s"),  # spark任务通过rpc拉取数据的超时时间
    ("spark.locality.wait", "5s"),  # 每个task获取本地数据的等待时间，默认3s钟，如果没获取到，依次获取本进程，本机，本机架数据
    ("spark.task.maxFailures", "5"),  # 允许最大失败任务数，根据自身容错情况来定
    ("spark.serializer", "org.apache.spark.serializer.KryoSerializer")  # 配置序列化方式
])

print(sc.getAll())
