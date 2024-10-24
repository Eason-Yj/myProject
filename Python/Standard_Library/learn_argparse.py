import argparse
import time


def get_args():
    parse = argparse.ArgumentParser(description="参数")
    parse.add_argument("path1", type=str, help="原始数据集路径")
    parse.add_argument("path2", type=str, help="对比数据集路径")
    parse.add_argument("parse_3", type=int, help="测试参数3", default=100)
    parse.add_argument("parse_4")
    return parse.parse_args()


if __name__ == '__main__':
    args = get_args()
    print(args.path1)
    print(args.path2)
    print()
