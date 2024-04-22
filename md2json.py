# python3
# -*- coding: utf-8 -*-
# @Time    : 2024-04-22 7:42
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : md2json.py
# @Software: PyCharm
import re
import json
from pathlib import Path


def md2json(md_file: Path, out:str):
    with open(md_file, "r", encoding="utf-8") as f:
        txt = f.read().strip().split("\n")
    data = {}
    for i in txt:
        if "|" not in i:
            continue
        i = i.split("|")
        title = i[1].strip()
        try:
            url = re.compile(r"\((.*?)\)").findall(i[2].strip())[0]
        except IndexError:
            continue
        data[title] = url
    with open(f"{out}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"已生成{out}.json")


if __name__ == '__main__':
    md2json(Path("README.md"), "itpanda")
