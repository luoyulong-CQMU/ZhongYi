# -*- coding:utf-8 -*- 

"""
作者：luoyu
日期：2021年04月08日
"""

import requests
import time
import json
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
    cookies = {
        'JSESSIONID': 'DBD8EA7C0000F5EC4F93C87EA01D9AB2',
        '_ga': 'GA1.2.1896986469.1617799600',
        '_gid': 'GA1.2.1695136715.1617799600',
        'p_h5_u': 'D014C9B0-4727-4CE8-9C7E-79876E4CF1FC',
        'selectedStreamLevel': 'LD',
        'TOKEN': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Hm_lvt_3332a41b27280e2252d205a35b0f3b5b': '1617808453,1617808564,1617808651,1617872404',
        'Hm_lpvt_3332a41b27280e2252d205a35b0f3b5b': '1617873336',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'DNT': '1',
        'formData': 'undefined',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'ProvinceId': '50',
        'Origin': 'https://www.tcmjy.org',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.tcmjy.org/player?projectId=JM3l2G4P',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = '{projectId: "7GDzOJ4N"}'
    response = requests.post('https://www.tcmjy.org/api/portal/detail', headers=headers, cookies=cookies, data=data)
    dic = response.json()
    ids = dic['data']['courseList']
    for item in ids:
        # print(item)
        examId = item['examId']
        title = item['title']
        courseId = item['id']
        projectId = "7GDzOJ4N"
        print(f"学习课程：{title}")
        print(f"课程信息：examId--{examId}|courseId--{courseId}|projectId--{projectId}")
        token = get_token(courseId=courseId, projectId=projectId)
        for i in range(1,5000000,500):
            statue = start(projectId=projectId,playerToken=token, playerTime=i, courseId=courseId)
            # print(statue)
            time.sleep(0.5)
            if statue['data']['status'] == 2:
                print("本课学习完成！")
                break
    print("全部学习完成！")

        # answerlst = redic_answer(get_answer(courseId=courseId, projectId=projectId,title=title))
        # commit_answer(examId=examId, courseId=courseId, projectId=projectId, examStartDate=get_time(), answerlst=answerlst, title=title)

    # with open("ids.json", "w", encoding='utf-8') as fp:
    #     fp.write(json.dumps(ids, ensure_ascii=False, indent=4))

def get_token(courseId, projectId):
    cookies = {
        'JSESSIONID': '5835DA0BEDB15322641F288F8E4777F4',
        '_ga': 'GA1.2.1896986469.1617799600',
        '_gid': 'GA1.2.1695136715.1617799600',
        'p_h5_u': 'D014C9B0-4727-4CE8-9C7E-79876E4CF1FC',
        'selectedStreamLevel': 'LD',
        'TOKEN': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Hm_lvt_3332a41b27280e2252d205a35b0f3b5b': '1617808453,1617808564,1617808651,1617872404',
        '_gat_gtag_UA_136948526_1': '1',
        'Hm_lpvt_3332a41b27280e2252d205a35b0f3b5b': '1617884261',
    }

    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'DNT': '1',
        'formData': 'undefined',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'ProvinceId': '50',
        'Origin': 'https://www.tcmjy.org',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.tcmjy.org/player?courseId=y30k6rZJ&projectId=QOZa6G3z',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {"courseInfo": {}, "projectId": projectId, "courseId": courseId}

    data = json.dumps(data, separators=(',', ':'))

    response = requests.post('https://www.tcmjy.org/api/security/detail/course', headers=headers, cookies=cookies,
                             data=data)

    # print(response.json())

    token = response.json()['data']['playerToken']
    # print(token)
    return token


def start(projectId, playerToken, playerTime, courseId):
    cookies = {
        'JSESSIONID': '5835DA0BEDB15322641F288F8E4777F4',
        '_ga': 'GA1.2.1896986469.1617799600',
        '_gid': 'GA1.2.1695136715.1617799600',
        'p_h5_u': 'D014C9B0-4727-4CE8-9C7E-79876E4CF1FC',
        'selectedStreamLevel': 'LD',
        'TOKEN': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Hm_lvt_3332a41b27280e2252d205a35b0f3b5b': '1617808453,1617808564,1617808651,1617872404',
        'Hm_lpvt_3332a41b27280e2252d205a35b0f3b5b': '1617883546',
    }
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'DNT': '1',
        'formData': 'undefined',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'ProvinceId': '50',
        'Origin': 'https://www.tcmjy.org',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.tcmjy.org/player?courseId=l49Q6z4L&projectId=QOZa6G3z',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # data = '{"projectId":"QOZa6G3z","playerToken":"30c78c67349f6a6880f0f5aaa2d96ce7","playerTime":18,"courseId":"l49Q6z4L"}'
    data = {"projectId": projectId,
            "playerToken": playerToken,
            "playerTime": playerTime,
            "courseId": courseId}
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post('https://www.tcmjy.org/api/security/course/play', headers=headers, cookies=cookies,
                             data=data)
    return response.json()

if __name__ == '__main__':
    get_examid()


