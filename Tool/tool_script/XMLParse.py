"""
1 在xml文件中定位目标值
2 找到英文和中文的对应文件
3 将英文中的目标值和中文中目标值对应起来，并保存到jsonl文件中
"""
from typing import Dict
import random
import json
import os
from xml.etree.ElementTree import parse


def get_val_dict(path: str) -> Dict:
    """

    :param path:
    :return:
    """
    with open(path, 'r') as f:
        # 第1个参数为输入源，返回一个ElementTree对象
        root = parse(f).getroot()
        s_all = root.findall('text/body/p/s')
        s_dict = {s.attrib['id']: s.text.strip() for s in s_all}
        print(s_dict)
        return s_dict


def merge_save(zh_values: Dict, en_values: Dict, output_path: str):
    """

    :param zh_values: 中文语句字典
    :param en_values: 英文语句字典
    :param output_path: 保存路径
    :return:
    """
    if os.path.exists(output_path):
        os.remove(output_path)

    prompt_list = ["将下面句子翻译成英文：\n{chinese}\n{english}", "{chinese}\n翻译成英文：\n{english}"]
    with open(output_path, "a") as f:
        id = 0
        for key, zh_val in zh_map.items():
            en_val = en_map.get(key)
            if en_val is None:
                continue
            id += 1
            prompt = random.choice(prompt_list)
            res = {"id": id, "text": prompt.format(chinese=zh_val, english=en_val)}
            json_res = json.dumps(res, ensure_ascii=False)
            print(json_res)
            f.write(json_res + "\n")


if __name__ == '__main__':
    en_path = 'exp_data/xml_exp_en.xml'
    zh_path = 'exp_data/xml_exp_zh.xml'

    en_map = get_val_dict(en_path)
    zh_map = get_val_dict(zh_path)

    # save_path = 'exp_data/output.jsonl'
    # merge_save(zh_values=zh_map, en_values=en_map, output_path=save_path)
