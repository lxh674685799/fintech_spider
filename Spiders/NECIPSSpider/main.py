#!/usr/bin/env python3
# coding: utf-8
# File: main.py
# Author: chenhe
# Date: 5/9/17 3:30 PM

# Supporting:
# 0. CAPTCHA(2nd Generation)
# 1. PhantomJS
# 2. User-Agent
# 3. IP Proxy(API: http://datazhiyuan.com:60001/plain)

from scrapy import cmdline
# import sys
# print(sys.path)

cmdline.execute(["scrapy", "crawl", "gsxt", "-L", "WARNING"])