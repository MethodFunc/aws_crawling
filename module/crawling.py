import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

from ..setting import datadict


def get_result(url, date):
    data_dict = datadict()
    response = requests.get(url)
    contents = bs(response.content, 'html.parser', from_encoding='cp949')
    date_object = datetime.strptime(date, "%Y%m%d%H%M")
    value = contents.find_all("tr", "text")
    for n, v in enumerate(value):
        tmp = v.find_all('td')
        for t, k in zip(tmp, data_dict.keys()):
            if k == 'dt':
                if (date_object.hour == 0) and (t.text != '00:00'):
                    date = date_object - timedelta(days=1)
                    date = date.strftime("%Y%m%d")
                    data_dict[k].append(date + ' ' + t.text)
                else:
                    date = date_object.strftime("%Y%m%d")
                    data_dict[k].append(date + ' ' + t.text)
            else:
                data_dict[k].append(t.text)

    # 필요한 부분만 뽑기 위해 필요없는 부분은 모두 제외 시킴
    data_dict.pop('rain')
    data_dict.pop('rain15')
    data_dict.pop('rain60')
    data_dict.pop('rain3h')
    data_dict.pop('rain6h')
    data_dict.pop('rain12h')
    data_dict.pop('rainday')
    data_dict.pop('temp')
    data_dict.pop('wd1s')
    data_dict.pop('wd10s')
    data_dict.pop('hum')
    data_dict.pop('pha')

    return data_dict
