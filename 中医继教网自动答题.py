import requests
import csv
import json
import time

"""
自动作答https://www.tcmjy.org/的考试！
食用方法：
通过地址“https://curl.trillworks.com/”取到cookies、headers
各个类的header需要单独提取，在network里面查看
其中在get_examin中的data为需要回答课程的data，在network里面提取
其他地方不需要修改，运行即可。

"""


def get_time():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return now

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

    data = '{projectId: "QOZa6G3z", courseId: "y30k6rZJ"}'
    response = requests.post('https://www.tcmjy.org/api/portal/detail', headers=headers, cookies=cookies, data=data)
    dic = response.json()
    ids = dic['data']['courseList']
    for item in ids:
        # print(item)
        examId = item['examId']
        title = item['title']
        courseId = item['userCourse']['courseId']
        projectId = item['userCourse']['projectId']
        answerlst = redic_answer(get_answer(courseId=courseId, projectId=projectId,title=title))
        commit_answer(examId=examId, courseId=courseId, projectId=projectId, examStartDate=get_time(), answerlst=answerlst, title=title)

    with open("ids.json", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(ids, ensure_ascii=False, indent=4))


def get_answer(courseId, projectId, title):
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

    data = '{"courseId":"' + courseId + '","projectId":"' + projectId + '"}'
    # print(data)
    response = requests.post('https://www.tcmjy.org/api/security/exam', headers=headers, cookies=cookies, data=data)
    answer = response.json()['data']['answers']
    with open("./answer/"+title + courseId + ".json", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(answer, ensure_ascii=False, indent=4))
    print(redic_answer(answer))
    return answer


def redic_answer(answer):
    answer_lst = []
    for item in answer:
        write_dic = {}
        write_dic["questionId"] = item["id"]
        write_dic["value"] = item["answer"]
        answer_lst.append(write_dic)
    return answer_lst


def commit_answer(examId, courseId, projectId, examStartDate,answerlst,title):
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
    examStartDate = "2021-04-08 18:52:14"
    data = {"examId": examId,
            "courseId": courseId,
            "projectId": projectId,
            "examStartDate": examStartDate,
            "answers": answerlst
            }
    data_ = json.dumps(data,separators=(',', ':'))
    print(data_,type(data_))
    # print(type(data_))
    print(f"准备作答：{title}")
    # print(f"参考答案：{answerlst}")
    # data_ = '{"examId":"74r2jB4Q","courseId":"6DWMbvZG","projectId":"JM3l2G4P","examStartDate":"2021-04-08 18:36:44","answers":[{"questionId":"Q3YpJAZ9","value":["C"]},{"questionId":"AD5ljX3r","value":["D"]},{"questionId":"64EE9249","value":["D"]}]}'
    # data_ = '{"examId":"5yDd9w4r","courseId":"7ZX5Gb3b","projectId":"JM3l2G4P","examStartDate":"2021-04-08 18:52:14","answers":[{"questionId":"AD59wdDr","value":["A"]}]}'
    # print(data_)
    time.sleep(3)
    response = requests.post('https://www.tcmjy.org/api/security/exam/submit', headers=headers, cookies=cookies,
                             data=data_)
    print(response.json())



if __name__ == '__main__':
    # get_time()
    # get_answer("6DWMbvZG", "JM3l2G4P")
    # commit_answer(1, 2, 3, 4)
    get_examid()
# {"examId":"5yDd9w4r","courseId":"7ZX5Gb3b","projectId":"JM3l2G4P","examStartDate":"2021-04-08 18:58:05","answers":[{"questionId":"AD59wdDr","value":["A"]}]}
# {"examId":"5yDd9w4r","courseId":"7ZX5Gb3b","projectId":"JM3l2G4P","examStartDate":"2021-04-08 18:52:14","answers":[{"questionId":"AD59wdDr","value":["A"]}]}