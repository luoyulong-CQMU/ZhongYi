import requests
import csv
import json
import time
from classInfo import *

"""
自动作答https://www.tcmjy.org/的考试！
食用方法：
通过地址“https://curl.trillworks.com/”取到cookies、headers
各个类的header需要单独提取，在network里面查看
其中在get_examin中的data为需要回答课程的data，在network里面提取
其他地方不需要修改，运行即可。
注意：：：：：需要先完成学习，才能能答题！
"""


def get_time():
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return now


def get_examid():
    """
    通过向服务器发送请求，获得课程所有课堂的id、考试id
    并把获得的内容以json格式存入根目录，保存名为ids.json
    并循环id列表，调用获取答案函数及提交答案函数完成模拟考试
    :return:
    """
    data = class_data
    response = requests.post(get_class_url, headers=class_headers, cookies=class_cookies, data=data)
    dic = response.json()
    ids = dic['data']['courseList']
    for item in ids:
        examId = item['examId']
        title = item['title']
        courseId = item['userCourse']['courseId']
        projectId = item['userCourse']['projectId']
        answerlst = redic_answer(get_answer(courseId=courseId, projectId=projectId, title=title))
        commit_answer(examId=examId, courseId=courseId, projectId=projectId, examStartDate=get_time(),
                      answerlst=answerlst, title=title)

    with open("ids.json", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(ids, ensure_ascii=False, indent=4))


def get_answer(courseId, projectId, title):
    """
    通过传入课程ID向服务器发送请求获取答案
    :param courseId: 课程Id
    :param projectId: 课程Id
    :param title: 考试组题目
    :return: 答案，类型为json
    """
    data = '{"courseId":"' + courseId + '","projectId":"' + projectId + '"}'
    response = requests.post(get_answer_url, headers=class_headers, cookies=class_cookies, data=data)
    answer = response.json()['data']['answers']
    with open("./answer/" + title + courseId + ".json", "w", encoding='utf-8') as fp:
        fp.write(json.dumps(answer, ensure_ascii=False, indent=4))
    return answer


def redic_answer(answer):
    answer_lst = []
    for item in answer:
        write_dic = {}
        write_dic["questionId"] = item["id"]
        write_dic["value"] = item["answer"]
        answer_lst.append(write_dic)
    return answer_lst


def commit_answer(examId, courseId, projectId, examStartDate, answerlst, title):
    """
    通过传入的参数，配置POST_PARAM
    通过POST请求模拟提交答案
    :param examId: 考试的Id，为每一项考试的Id
    :param courseId:同为课程Id
    :param projectId: 课程Id，考试所对应课程Id
    :param examStartDate:考试开始时间，通过当前时间获取，延时2s后发送提交请求
    :param answerlst:考试答案列表{其中包含每一个试题的唯一id和正确选项}
    :param title:考试组的题目
    :return:无返回值
    """
    # 如果向服务器提交考试失败，尝试手动设置examStartData为当前时间前30分钟左右，或增加提交延时
    # examStartDate = "2021-04-08 18:52:14"
    data = {"examId": examId,
            "courseId": courseId,
            "projectId": projectId,
            "examStartDate": examStartDate,
            "answers": answerlst
            }
    data_str = json.dumps(data, separators=(',', ':'))

    print(f"准备作答：{title}")

    time.sleep(2)
    response = requests.post(exam_submit_url, headers=class_headers, cookies=class_cookies,
                             data=data_str)
    print("作答完毕！") if response.json()['code'] == 200 else print("作答错误！")


if __name__ == '__main__':
    get_examid()
