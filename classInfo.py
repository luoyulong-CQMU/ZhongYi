# -*- coding:utf-8 -*- 

"""
作者：luoyu
日期：2021年04月08日
"""

class_data = '{projectId: "JM3l2G4P"}'
projectId_parm = "JM3l2G4P"
exam_submit_url = 'https://www.tcmjy.org/api/security/exam/submit'
get_answer_url = 'https://www.tcmjy.org/api/security/exam'
get_class_url = 'https://www.tcmjy.org/api/portal/detail'
get_token_url = 'https://www.tcmjy.org/api/security/detail/course'
referer_url = f'https://www.tcmjy.org/player?projectId={projectId_parm}'
token_referer_url = 'https://www.tcmjy.org/player?courseId=y30k6rZJ&projectId=QOZa6G3z'
play_video_url = 'https://www.tcmjy.org/api/security/course/play'
class_cookies = {
        'JSESSIONID': 'DBD8EA7C0000F5EC4F93C87EA01D9AB2',
        '_ga': 'GA1.2.1896986469.1617799600',
        '_gid': 'GA1.2.1695136715.1617799600',
        'p_h5_u': 'D014C9B0-4727-4CE8-9C7E-79876E4CF1FC',
        'selectedStreamLevel': 'LD',
        'TOKEN': 'G32oWeLD_43f52adb7dd8454db678d25a03cf54be',
        'Hm_lvt_3332a41b27280e2252d205a35b0f3b5b': '1617808453,1617808564,1617808651,1617872404',
        'Hm_lpvt_3332a41b27280e2252d205a35b0f3b5b': '1617873336',
    }

class_headers = {
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
        'Referer': referer_url,
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

token_headers = {
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
        'Referer': token_referer_url,
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }


if __name__ == '__main__':
    pass