#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2025/3/18 16:12
# @Author :  Allen
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from fetch.spiders.example import ExampleSpider

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ExampleSpider)
    process.start()

if __name__ == '__main__':
    run_spider()
