# markdown 学习

## 1 上下角标

- 格式：

```
上角标：a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>
下角标：2KClO<sub>3</sub> == 2KCl + 3O<sub>2</sub>↑
嵌套：a<sup>b<sub>c<sup>d</sup></sub></sup>
```

- 例：
    - a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>
    - 2KClO<sub>3</sub> == 2KCl + 3O<sub>2</sub>↑
    - a<sup>b<sub>c<sup>d</sup></sub></sup>

## 2 代码块（高亮）

- 格式|例子：

```python
# Python
print("Hello, world!")

# ```python
# print("Hello, world!")
# 删除#号
# ```
```

## 3 超链接

```
行内定义方式: [百度](www.baidu.com)
全局声明方式: 
[百度][baidu] 

[baidu]:www.baidu.com
```

- 行内定义方式: [百度](www.baidu.com)
- 全局声明方式: [百度][baidu]

[baidu]: www.baidu.com

## 4 字体

### 4.1 强调语法

- 斜体
    - *星号表示的斜体* : \*星号表示的斜体*
    - _下划线表示的斜体_ : \_下划线表示的斜体_
- 粗体
    - **星号表示的粗体** : \*\*星号表示的粗体**
    - __下划线表示的粗体__ : \_\_下划线表示的粗体__
- 粗斜体
    - ***星号表示的粗斜体*** ：\*\*\*星号表示的粗体***
    - ___下划线表示的粗斜体___ ：\_\_\_下划线表示的粗体___
- html语法
    - <em>斜体</em> ： \<em>斜体\</em>
    - <strong>粗体</strong> ： \<strong>粗体\</strong>

### 4.2 字体属性

- <font color="red" size="2" face="HEI">2号字-黑体</font>： \<font size="2" face="HEI">2号字-黑体\</font>
- <font color="gree" size="3" face="KAI">3号字-楷体</font>： \<font size="3" face="KAI">3号字-楷体\</font>

```
#### 使用 `style` 全局修改字体字号

# WORD中常用的一号宋体标题

## WORD中常用的二号宋体标题

### WORD中常用的三号宋体标题

Word 中常用的四号正文楷体

<style>
h1 { font: 26pt song !important; }
h2 { font: 22pt song !important; }
h3 { font: 16pt song !important; }
p { font: 14pt kai !important; }
</style>
```

## 辅助线

- ~~删除线~~ : \~~删除线\~~
- <ins>下划线</ins> : \<ins>下划线\</ins>
