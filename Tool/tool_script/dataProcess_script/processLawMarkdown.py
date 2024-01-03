"""
处理markdown格式的法律条款，可以转换成json或jsonlines格式

"""

import re
import os
import json

import jsonlines

template = "{law_name}的{law_chapter}的内容是什么？"


def convertLawMDToJson(md_path: str, save_path: str = None) -> dict:
    """
    将md格式的法律条款转换为json格式
    :param md_path: 需要转换的法律条款md文件地址
    :param save_path: 可选，保存为json文件的地址
    :return:
    """
    with open(md_path, "r") as f:
        all_row = f.readlines()

    res_dict = {}
    level2_title = ""
    level3_title = ""
    level4_title = ""
    not_save = True
    key = ""

    for row in all_row:
        if row.startswith("# "):
            not_save = True
            level1_title = row.strip("#").strip()  # xxx法
            key = level1_title
        elif row.startswith("## "):
            not_save = False
            level2_title = re.findall("第.{1,7}(?:编|章|节)", row)  # 第xxx章
            if len(level2_title) < 1:
                not_save = True
                level2_title = [row.strip("## ").strip()]
            # print("level2_title", level2_title)
            level2_title = level2_title[0]
            key = level2_title
        elif row.startswith("### "):
            level3_title = re.findall("第.{1,7}(?:编|章|节)", row)[0]  # 第xxx节
            if len(level3_title) < 1:
                level3_title = [row.strip("## ").strip()]
            # print("level3_title", level3_title)
            key = level2_title + level3_title
        elif row.startswith("#### "):
            level4_title = re.findall("第.{1,7}(?:编|章|节)", row)[0]  # 第xxx节
            if len(level4_title) < 1:
                level4_title = [row.strip("## ").strip()]
            # print("level4_title", level4_title)
            key = level2_title + level3_title + level4_title
        else:
            level5_title_list = re.findall("第.{1,7}条", row)
            if len(level5_title_list) > 0:  # 第xxx条
                level5_title = level2_title + level3_title + level4_title + level5_title_list[0]
                res_dict[level5_title] = [row.replace(level5_title_list[0], "").strip()]
                # print("level5_title_1", level5_title)
                key = level5_title
            elif not_save:
                continue
            else:  # 正文
                row = row.strip()
                if not row or "-- INFO END --" in row or "-- FORCE BREAK --" in row:
                    continue
                if res_dict.get(key):
                    res_dict[key].append(row)
                else:
                    # print("level5_title_2", key)
                    res_dict[key] = [row]

    json_data = json.dumps(res_dict, ensure_ascii=False)
    print(json_data)

    if save_path:
        with open(save_path, "w") as f:
            f.write(json_data)

    return res_dict


def convertDictToJsonl(input_data: dict, save_dir: str, law_name: str):
    save_path = os.path.join(save_dir, law_name + ".jsonl")
    jsonl_file = jsonlines.open(save_path, 'a')
    for legal_provisions, content_lst in input_data.items():
        dict_row = {
            "instruction": "{}的{}的内容是什么？".format(law_name, legal_provisions),
            "input": "",
            "output": "\n".join(content_lst)
        }
        jsonlines.Writer.write(jsonl_file, dict_row)
    jsonl_file.close()


def processLawMarkdown(input_path: str, output_dir: str, law_name: str):
    if os.path.isfile(input_path):
        files = [input_path.split("/")[-1]]
        input_path = os.path.dirname(input_path)
    else:
        files = os.listdir(input_path)

    for file in files:
        law_name_list = re.findall(".*法", file)
        if len(law_name_list) < 1 or "修正案" in file:
            continue
        if law_name == law_name_list[0]:
            current_law_name = law_name
        else:
            current_law_name = law_name + law_name_list[0]
        print("===== 当前文件：{}，法律名：{} =====".format(file, current_law_name))
        file_path = os.path.join(input_path, file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        if file.endswith(".md"):
            dict_data = convertLawMDToJson(md_path=file_path)
            convertDictToJsonl(input_data=dict_data, save_dir=output_dir, law_name=current_law_name)
        print()


if __name__ == '__main__':
    inputPath = os.path.join(os.path.dirname(__file__), 'test_data/宪法.md')
    outputPath = os.path.join(os.path.dirname(__file__), "output")
    processLawMarkdown(input_path=inputPath, output_dir=outputPath, law_name="宪法")
