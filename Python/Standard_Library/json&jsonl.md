# json 和 jsonl
```shell script
pip install jsonlines
conda install jsonlines
```
## json


## jsonl
- 读取文件

```python
import jsonlines

f_path = "宪法.jsonl"
f_out = "exp.jsonl"

# ========== 方法1 ==========
# 读数据
f_r = open(f_path, "r")
jlr = jsonlines.Reader(f_r).iter(skip_invalid=True)

# 写数据
f_w = open(f_out, "a")
jlw = jsonlines.Writer(f_w)

# 逐行读取和写入
for row in jlr:
    jlw.write(row)

# ========== 方法2 ==========
# 读数据
j_r = jsonlines.open(f_path, mode="r")
# 写数据
j_w = jsonlines.open(f_out, mode="a")

# 逐行读取和写入
res = []
for idx, row in enumerate(j_r.iter()):
    res.append(row)
    j_w.write(row)
# 批量写入
j_w.write_all(res)

j_r.close()
j_w.close()
```
