# -*- coding:utf-8 -*-
"""
@author:jieshukai
@file: phoenix_ancient_town.py
@time: 2019/05/01
"""
from Tripadvisor2.spiders.yuyan import TripsSpider


class FhgcTripsSpider(TripsSpider):
    name = 'fhgc'
    allowed_domains = []
    start_urls = [
        'https://www.tripadvisor.cn/Attraction_Review-g660726-d505448-Reviews-Phoenix_Ancient_Town-Fenghuang_County_Hunan.html'
    ]
    verbose_name = '凤凰古城'
    language = 'en'
    start_url = 'https://www.tripadvisor.cn/Attraction_Review-g660726-d505448-Reviews-Phoenix_Ancient_Town-Fenghuang_County_Hunan.html'
