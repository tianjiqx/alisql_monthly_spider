
###############################
# 程序说明：
# 爬取阿里巴巴数据库内核组月报的文章
# 由于原始文档，分级，无法直接获得所有文章名称，不方便查阅
# 于是写该爬虫避免重复点击回退，形成文章目录md文件，便于查看
# 阿里数据库内核组月报地址：
# http://mysql.taobao.org/monthly/
###############################

# -*- coding: utf-8 -*-

from alisql_weekly_spider.monthly import monthly
from alisql_weekly_spider.html_downloader import HtmlDownloader
from alisql_weekly_spider.html_parser import HtmlParser

# 单线程的爬虫，因为内容并不多
class Spider:

    def __init__(self,url):
        self.url=url

    def craw(self):
        # 下载
        downloader = HtmlDownloader()

        root_cont = downloader.download(self.url)
        parser=HtmlParser()
        urls,data=parser.parse(self.url,root_cont,True)
        result=""
        for url in urls:
            cont = downloader.download(url)
            newurls, month = parser.parse(url, cont,False)

            result+=month.getMonthly()
            month=None
            #print(month.getMonthly())


        f=open("阿里巴巴数据库内核组月报.md","w+",encoding='utf-8')
        result="## 阿里巴巴数据库内核月报\n\n"+result
        f.write(result)
        f.close()

        pass





if __name__ == "__main__":

    # 初始化地址：
    root_url="http://mysql.taobao.org/monthly/"

    s = Spider(root_url)
    s.craw()



