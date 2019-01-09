# -*- coding: utf-8 -*-
import argparse
import sys

from CrawSwtc import CrawSwtc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="数据抓取")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    # parser.add_argument("url",  help="input url ")
    args = parser.parse_args()
    # url = args.url
    url = 'https://state.jingtum.com/init'

    if args.verbose:
        print('开始')
        crawswtc = CrawSwtc(url)
        crawswtc.craw_swtc()
    else:
        print('直接')
        


    