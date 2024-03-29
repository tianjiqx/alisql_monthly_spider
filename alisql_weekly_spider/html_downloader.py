# -*- coding: utf-8 -*-
from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        req = request.Request(url)
        # response = request.urlopen(url)
        # 模拟真实的浏览器
        req.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
        try:
            resp = request.urlopen(req)
        except:
            print("urlopen "+ url + " failed.")
            return None
        if resp.getcode() != 200:  # response.getcode() != 200:
            print("urlopen "+ url + " failed.")
            print("Get failed, resp code: " + str(resp.getcode()))
            return None

        return resp.read().decode("utf-8")  # response.read()
