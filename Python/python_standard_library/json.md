# json库

## 报错

```
1、json.decoder.JSONDecodeError: Unexpected UTF-8 BOM (decode using utf-8-sig): line 1 column 1 (char 0)：
解：因为 utf-8 和 utf-8-sig 是不一样的，我们将 其改成  utf-8-sig  就可以运行了。

jsonl_file = jsonlines.open(output_file_path, 'a')
read_f = open(file_path, "r", encoding='utf-8-sig')

```