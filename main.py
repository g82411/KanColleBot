# -*- coding: utf-8 -*-
import requests
import ConfigParser
import json
import re
class KanCello:
    def __init__(self):
        link = raw_input("Swf Link:")
        self.api_token = re.findall("api_token=(\w+)",link)
        self.api_starttime = re.findall("api_starttime=(\d+)",link)
        self.server = "203.104.209.23"
        self.referer = "http://{0}/kcs/mainD2.swf?api_token={1}&api_starttime={2}/[[DYNAMIC]]/1".format(self.server,self.api_token,self.api_starttime)
        self.header = {
        "Origin":"http://{0}".format(self.server),
        "Accept-Encoding":"gzip, deflate",
        "X-Requested-With":"ShockwaveFlash/17.0.0.134",
        "Host":self.server,
        "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
        "Accept":"*/*",
        "Referer":self.referer
        }
        self.__initStat()
    def __initStat(self):
        initPath = ["api_start2","api_req_member/get_incentive","api_get_member/basic"]
        for path in initPath:
            print "開始階段:api 路徑:{0}......".format(path).decode("utf-8","ignore")
            payload = {
            "api_token":self.api_token,
            "api_verno":1
            }
            res = requests.post("http://{0}/kcsapi/{1}".format(self.server,path),data=payload,headers=self.header).text

            res = json.loads(re.findall("svdata=(.+)",res)[0])
            print res["api_result_msg"]
        self.__mainProcess()
    def __getMaterial(self):
        payload = {
        "api_token":self.api_token,
        "api_verno":1
        }
        path = "/kcsapi/api_get_member/material"
        res = requests.post("http://{0}{1}".format(self.server,path),data=payload,headers=self.header).text
        res = json.loads(re.findall("svdata=(.+)",res)[0])
        for material in res["api_data"]:
            if material["api_id"] == 1:
                print "油:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 2:
                print "鋼:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 3:
                print "彈:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 4:
                print "鋁:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 5:
                print "快速艦造:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 6:
                print "桶:%d".decode("utf-8","ignore") % material["api_value"]
            elif material["api_id"] == 7:
                print "開發資才:%d".decode("utf-8","ignore") % material["api_value"]
    def __getQuestList(self):
        path = "/kcsapi/api_get_member/questlist"
        payload = {
        "api_token":self.api_token
        "api_page_no":1,
        "api_verno":1,
        }
        res = requests.post("http://{0}{1}".format(self.server,path),headers=self.header,data=payload).text
        res = json.loads(re.findall("svdata=(.+)",res)[0])
        if res["api_result"] == 1:
            res = res["api_data"]
            print "未完成任務總數:%d".encode("utf-8","ignore") % res["apt_count"]
            for i in range(1,(res["api_page_count"]+1)):
                payload["api_page_no"] = i
                missions = requests.post("http://{0}{1}".format(self.server,path),headers=self.header,data=payload).text
                missions = json.loads(re.findall("svdata=(.+)",missions)[0])
                if missions["api_result"] == 1:
                    missions = missions["api_data"]["api_list"]
                    for mission in missions:
                        print "任務ID:%d" % mission["api_no"]
                        print "任務名稱:%s".encode("utf-8","ignore") % mission["api_title"]
                        print "任務內容:%s".encode("utf-8","ignore") % mission["api_detail"]
                        if mission["api_state"] == 2:
                            print "任務接取".encode("utf-8","ignore")
                        elif mission["api_state"] == 3:
                            print "任務完成".encode("utf-8","ignore")
                else:
                    print "連線失敗".encode("utf-8","ignore")
        else:
            print "連線失敗".encode("utf-8","ignore")


    def __getDeck(self):
        path = "/kcsapi/api_get_member/deck"
        payload = {
        "api_token":self.api_token,
        "api_verno":1
        }
        res = requests.post("http://{0}{1}".format(self.server,path),headers=self.header,data=payload).text
        res = json.loads(re.findall("svdata=(.+)",res)[0])
        return res
    def __
    def __mainProcess(self):
        self.__getMaterial()

KanCello()
