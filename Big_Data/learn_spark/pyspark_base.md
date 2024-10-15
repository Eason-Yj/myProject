# PySpark 基础

## 1 创建DataFrame

流程：初始化sparkSession -> 创建DataFrame

### 1.1 初始化sparkSession

#### 1.1.1 config

```python

```

```python

from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

```

### 1.2 创建DataFrame

- 通过 list 创建DataFrame

```python
from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

data = [
    (1, 2, 3.1, "a"),
    (2, 4, 2.2, "b"),
    (1, 2, 1.2, "c"),
]
cols = ["col1", "col2", "col3", "target"]
df = sparkSession.createDataFrame(data=data, schema=cols)
df.show()
df.printSchema()
```

- 通过 dict 创建DataFrame

```python
from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

data = [
    {"col1": 1, "col2": 2, "col3": 3.1, "col4": "a"},
    {"col1": 2, "col2": 4, "col3": 2.2, "col4": "b"},
    {"col1": 1, "col2": 2, "col3": 1.2, "col4": "c"}
]
df = sparkSession.createDataFrame(data=data)
df.show()
df.printSchema()
```

- 通过 rdd 创建DataFrame

```python
from pyspark.sql import Row
from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

data = [
    Row(1, 2, 3.1, "a"),
    Row(2, 4, 2.2, "b"),
    Row(1, 2, 1.2, "c")
]
rdd = sparkSession.sparkContext.parallelize(data)
print(rdd.glom().collect())
cols = ["col1", "col2", "col3", "target"]
df = sparkSession.createDataFrame(data=rdd, schema=cols)
df.show()
df.printSchema()
```

- 读取外部数据创建DataFrame

```python
from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

df = sparkSession.read.csv("../dataset/v_train_dataset.csv", header=True)
df.show()
df.printSchema()
```

- 设置DataFrame schema

```python
from pyspark.sql.types import StructType, StructField, IntegerType, ShortType, FloatType, StringType
from pyspark.sql import SparkSession

# 初始化sparkSession
sparkSession = SparkSession.builder.appName("exp").master("local").config("spark.driver.cores", "2").getOrCreate()

data = [
    (1, 2, 3.1, "a"),
    (2, 4, 2.2, "b"),
    (1, 2, 1.2, "c"),
]
schema = StructType([
    StructField(name="col1", dataType=ShortType()),
    StructField(name="col2", dataType=IntegerType()),
    StructField(name="col3", dataType=FloatType()),
    StructField(name="target", dataType=StringType()),
])
df = sparkSession.createDataFrame(data=data, schema=schema)
df.show()
df.printSchema()
```

