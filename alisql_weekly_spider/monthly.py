# -*- coding: utf-8 -*-
# 周报类
class weekly:
    # 周报标题
    weekly_title=""
    # 周报链接
    weekly_link=""

# 月报类
class monthly:
    # 月报标题
    monthly_title=""
    monthly_link=""
    # 周报列表
    weekly_list=[]


    def getMonthly(self):
        print(self.monthly_title)
        print(self.monthly_link)
        str="### ["+self.monthly_title+"]("+self.monthly_link+")\n"
        i=0
        while i< len(self.weekly_list):
            str+=self.get(i)+"\n"
            i+=1
        return str

    def add(self,weekly):
        self.weekly_list.append(weekly)

    def get(self,index):
        str=""
        if index >= len(self.weekly_list):
            return str
        str += "- ["+self.weekly_list[index].weekly_title + "]("+self.weekly_list[index].weekly_link+")"
        return str
