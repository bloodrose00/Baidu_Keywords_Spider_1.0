import requests
import random
from fake_useragent import UserAgent
from urllib.parse import quote
from lxml import etree
import os

'''
Date: 2019年12月15日
Author: AG_Ajax
Description: baidu_keywords_spider_1.0
'''


class K_Spider():

    def __init__(self):
        self.url = 'http://www.baidu.com/s?wd={}&pn={}&oq={}&ie=utf-8&usm=3&rsv_idx=1&rsv_pq=80dd' \
                   'cec60005682b&rsv_t=81e1sx%2FSjWJTFD%2BseJ7mJngykUUIJGfQzel3wMCUOMhxtOeHyHA6oJe%2Bt5M'
        self.count = 0



    def get_headers(self):
        ua = UserAgent()
        headers = {'user-agent': ua.random}
        return headers



    def get_page(self, url, headers):
        html = requests.get(url=url, headers=headers).text
        # 测试打印源码
        # print(html)
        # print(type(html))
        return html



    def parse_page(self, html):
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath("//div[@id='container']/div[@id='content_left']/div")
        # 带有空的列表
        list_empty = []
        # 传递的列表
        list_title = []
        for title in r_list:
            # print('title_type:',type(title))  ---测试打印title_type
            t = title.xpath("string(./h3[@class='t']/a)")
            if t is not None:
                # print('t_type:',type(t))   ---测试打印t_type
                # print(t)   --- lxml 类型
                list_empty.append(t)
        # print(list_empty)
        # 二次过滤去掉多余的空
        for i in list_empty:
            if i == '':
                pass
            else:
                list_title.append(i)
        # print(list_title)
        # print(type(list_title))
        return list_title



    # ******************************************************************************************************************
    # def parse_keywords函数对应run函数的精准匹配关键字,如不需要精准匹配,可一起注释!****************************************
    def parse_keywords(self,raw_keyword,a):
        raw_keywords_list = []
        keywords_list = []
        for b in a:
            # print(i)   # str
            if '' in b:
                # print(str(i.split()).strip())  # 根据'' 拆分去掉两边空格
                c = b.split()
                # print(c)
                # print(type(c))
                for d in c:
                    # print(w)
                    # print(type(w))
                    # print(d)
                    if raw_keyword in d:
                        raw_keywords_list.append(d)
                        e = d.split('_')
                        for f in e:
                            # print(f)
                            if raw_keyword in f:
                                # print(f)
                                # print(type(f))
                                g = f.split('|')
                                # print(g)
                                # print(type(g))
                                for h in g:
                                    if raw_keyword in h:
                                        # print(h)
                                        # print(type(h))
                                        i = h.split('-')
                                        # print(i)
                                        # print(type(i))
                                        for j in i:
                                            if raw_keyword in j:
                                                # print(j)
                                                keywords_list.append(j)

            # elif '-' in i :
            #     print(str(i.split()).strip())  # 根据'-' 拆分去掉两边空格
            #     keywords_list.append(str(i.split()).strip())
            # elif '|' in i :
            #     print(str(i.split()).strip())  # 根据'|' 拆分去掉两边空格
            #     keywords_list.append(str(i.split()).strip())
            # elif '_' in i:
            #     print(str(i.split()).strip())  # 根据'_' 拆分去掉两边空格
            #     keywords_list.append(str(i.split()).strip())
            else:
                pass

        # print(raw_keywords_list)
        # print(keywords_list)
        return keywords_list



    def write_txt(self, keyword_list, raw_keyword):

        with open('title_' + str(raw_keyword) + '.txt', 'a+') as f:
            for title in keyword_list:

                try:
                    f.writelines(title + '\n')
                except Exception as e:
                    print(e,'打印出了小问题...')
                self.count += 1



    def run(self):
        # 判断可传入列表后分词
        keywords_list = input('keywords:')
        raw_keywords = keywords_list.split()  # ---分词
        page = int(input('page:'))
        for raw_keyword in raw_keywords:
            comp_keyword = quote(raw_keyword)
            for i in range(page):
                i *= 10
                # 拼接url
                url = self.url.format(comp_keyword, i, comp_keyword)
                headers = self.get_headers()
                # 解析的标题列表
                title_list = self.parse_page(self.get_page(url, headers))
                # 判断-如果关键字不在title里则pass
                if raw_keyword not in title_list:
                    pass
                # ************************************************************************************************************
                keyword_list = self.parse_keywords(raw_keyword,title_list)   # 返回精准关键字,不需要可注释!
                # ************************************************************************************************************
                self.write_txt(keyword_list, raw_keyword)

                print('打印完毕!一共打印', self.count, '次.')


if __name__ == '__main__':
    spider = K_Spider()
    spider.run()

'''
html=lxml.etree.parse("test.html")
res=html.xpath("//a[@heaf='baidu.com']")
# info=res[0].xpath('string(.)')
for i in res:
    i = i[0].xpath('string(.)')
'''
