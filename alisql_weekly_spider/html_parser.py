# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import parse
#引入正则模块
import re

from monthly import monthly
from monthly import weekly
#from alisql_weekly_spider.monthly import monthly,weekly

# 解析网页中的内容
class HtmlParser(object):

    # 获得新的url,所有月报的url
    def __get_new_urls(self, page_url, soup):
        new_urls=[]
        # 获取月报url
        if re.match(r".*/monthly/",page_url):
            links =soup.find_all('a',href=re.compile(r".*/monthly/[0-9]+/[0-9]+"))
            for link in links:
                new_url=link['href']
                full_url=page_url+new_url[len("/monthly/"):]
                new_urls.append(full_url)
        return new_urls
    # 获取网页的数据
    def __get_new_data(self, page_url, soup):
        m = monthly()
        m.weekly_list=[]
        if re.match(r".*/monthly/", page_url):
            pass
        if re.match(r".*/monthly/[0-9]+/[0-9]+.*", page_url):
            # 设置月报标题和连接地址
            m.monthly_title=soup.find('title').get_text().strip()
            m.monthly_link=page_url
            weeknodes= soup.find_all("li")
            i=1
            for weeknode in weeknodes:
                weeknode=repr(weeknode)
                subsoup=BeautifulSoup(weeknode,"html.parser")
                w = weekly()
                tx=subsoup.find('h3').get_text().strip().split('\n')
                w.weekly_title=str(i)+"."+tx[len(tx)-1].strip()
                i+=1
                w.weekly_link= page_url+subsoup.find('a')["href"][len("/monthly/2016/08"):]
                #print(w.weekly_title)
                #print(w.weekly_link)
                m.add(w)
            pass
        print("week list len="+str(len(m.weekly_list)))
        return m


    # 解析
    def parse(self, page_url, html_cont,open):
        if page_url is None or html_cont is None:
            return
            # print("begin parse...")
        soup = BeautifulSoup(html_cont, 'html.parser')
        print("begin get_urls...")
        print("解析："+page_url)
        new_urls=""
        new_data=""
        try:
            if open:
                new_urls = self.__get_new_urls(page_url, soup)
                print(new_urls)
        except:
            print('parse new urls fail.')

        print("begin get_data...")
        try:
            new_data = self.__get_new_data(page_url, soup)
        except:
            print('parse new datas fail.')
        print("end get_parse...")



        return new_urls,new_data




