"""
pip install jsonpath-rw jsonpath-rw-ext
pip install jsonpath_ng
pip install jsonpath
"""
import jsonpath
from jsonpath_rw import Index, Fields
from jsonpath_rw_ext import parse


# 提取json的值
def extract_json(json_object, express, index=0):
    res = jsonpath.jsonpath(json_object, express)
    try:
        if res:
            # 如果index小于0,则认为你是要所有的匹配结果
            if index < 0:
                return res
            # 如果不小于0，那么你传几，就代表你要的是匹配结果的某一个
            else:
                return res[index]
        print(f'通过{express}提取到的结果是：{res}')
    except:
        print(f'通过表达式{express}没有提取到值！')


# 修改JSON的值
def update_value_to_json(json_object, json_path, new_value):
    json_path_expr = parse(json_path)
    for match in json_path_expr.find(json_object):
        print("match.value: ", match.value)
        path = match.path
        if isinstance(path, Index):
            match.context.value[match.path.index] = new_value
        elif isinstance(path, Fields):
            match.context.value[match.path.fields[0]] = new_value
    return json_object


if __name__ == '__main__':
    s = {
        "store":
            {
                "book": [
                    {"category": "reference",
                     "author": "Nigel Rees",
                     "title": "Sayings of the Century",
                     "price": 8.95
                     },
                    {"category": "fiction",
                     "author": "Evelyn Waugh",
                     "title": "Sword of Honour",
                     "price": 12.99
                     }
                ]
            }
    }
    # 注意：jsonpath一旦能匹配到数据，不管数据是几个，返回结果都是个列表
    # 注意：jsonpath一旦匹配不到数据，那么结果是False
    res = extract_json(s, '$..title', 3)
    print(res)

    # 修改s这个json里的第一个category
    s = update_value_to_json(s, '$..book[0].category', 'aaaaaaaaaa')
    print(s)
