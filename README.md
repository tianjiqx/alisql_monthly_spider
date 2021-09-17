# alisql_monthly_spider



由于原始文档，分级，无法直接获得所有文章名称，不方便查,于是写该爬虫避免重复点击回退，形成文章目录md文件，便于查看


阿里数据库内核组月报地址：
http://mysql.taobao.org/monthly/

(TODO: 增量爬取：解析文档已经爬取文档时间，爬取增量的部分，合并输出，避免网络问题，以及加快文档输出)

## 使用


- ubuntu16.04 环境下执行 `python3 alisql_weekly_spider/main.py` 即可

- 使用IntelliJ IDEA 社区版 导入该python项目，然后run main文件，即可。
