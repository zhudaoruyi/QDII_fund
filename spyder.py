# -*- coding: utf-8 -*-
# @Author  : Randy Pen
# @Email   : randy86@gmail.com

import re
import os
import json
import time
import codecs
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


def spyder(url):
    res = requests.get(url, headers=headers)
    html_con = res.content
    # print(html_con)
    con = BeautifulSoup(html_con, 'html.parser')
    vms = con.find_all("tr", class_="px12line21")
    # print(vms)
    lines = list()
    for i, vm in enumerate(vms):
        if i == 0:
            continue
        tds = vm.find_all("td")
        # print(tds)
        date = tds[0].find_all("a")[0].get_text()
        qishu = tds[1].get_text()
        code = tds[2].get_text()
        try:
            # code = code.replace("&nbsp", "").replace(";", "").replace("\xa0", "")
            code = code.replace("&nbsp;+", "")
        except:
            pass
        sum = tds[3].get_text().strip()
        details = tds[0].find_all("a")[0].get("href")
        lines.append("|".join([qishu, date, code, sum, details]))
    return lines


def main():
    # 双色球
    # for page in range(1, 87):
    #     if os.path.exists("lottery/ssq/%s.txt" % page):
    #         continue
    #     url = "http://zjflcp.zjol.com.cn/fcweb/ssq.shtml?&pageNum=%s" % page
    #     lines = spyder(url)
    #     for line in lines:
    #         with codecs.open("lottery/ssq/%s.txt" % page, "a", encoding="utf-8") as fw:
    #             fw.write("%s\n" % line)
    #     time.sleep(2)
    # 3D
    # for page in range(1, 188):
    #     if os.path.exists("lottery/3d/%s.txt" % page):
    #         continue
    #     url = "http://zjflcp.zjol.com.cn/fcweb/sd.shtml?&pageNum=%s" % page
    #     lines = spyder(url)
    #     for line in lines:
    #         with codecs.open("lottery/3d/%s.txt" % page, "a", encoding="utf-8") as fw:
    #             fw.write("%s\n" % line)
    #     time.sleep(2)
    # 东方6+1
    for page in range(1, 64):
        if os.path.exists("lottery/ljy/%s.txt" % page):
            continue
        url = "http://zjflcp.zjol.com.cn/fcweb/ljy.shtml?&pageNum=%s" % page
        lines = spyder(url)
        for line in lines:
            with codecs.open("lottery/ljy/%s.txt" % page, "a", encoding="utf-8") as fw:
                fw.write("%s\n" % line)
        time.sleep(2)
    return 0


if __name__ == '__main__':
    main()
