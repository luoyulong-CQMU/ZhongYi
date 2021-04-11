# -*- coding:utf-8 -*- 

"""
作者：luoyu
日期：2021年04月08日
"""

import requests
import time
import json
from classInfo import *
"""
此为自动学习https://www.tcmjy.org/的视频！
基本每个视频5-10秒即可完成！
食用方法：
通过地址“https://curl.trillworks.com/”取到cookies、headers
各个类的header需要单独提取，在network里面查看
其中在get_examid中的data为需要回答课程的data，在network--detail里面提取
在下面的projectID 要替换成data中的proJectID，运行即可！
"""


def get_examid():
    data = class_data
    response = requests.post(get_class_url, headers=class_headers, cookies=class_cookies, data=data)
    dic = response.json()
    ids = dic['data']['courseList']
    for item in ids:
        examId = item['examId']
        title = item['title']
        courseId = item['id']
        projectId = projectId_parm
        print(f"学习课程：{title}")
        # print(f"课程信息：examId--{examId}|courseId--{courseId}|projectId--{projectId}")
        token = get_token(courseId=courseId, projectId=projectId)
        for i in range(1,5000000,500):
            statue = start(projectId=projectId,playerToken=token, playerTime=i, courseId=courseId)
            time.sleep(0.5)
            if statue['data']['status'] >= 2:
                print("本课学习完成！")
                break
            else:
                print(f"快速学习中. . .\r")
    print("全部学习完成！")

def get_token(courseId, projectId):
    data = {"courseInfo": {}, "projectId": projectId, "courseId": courseId}
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(get_token_url, headers=token_headers, cookies=class_cookies, data=data)
    token = response.json()['data']['playerToken']
    return token

def start(projectId, playerToken, playerTime, courseId):
    data = {"projectId": projectId,
            "playerToken": playerToken,
            "playerTime": playerTime,
            "courseId": courseId}
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(play_video_url, headers=token_headers, cookies=class_cookies, data=data)
    return response.json()

if __name__ == '__main__':
    get_examid()


