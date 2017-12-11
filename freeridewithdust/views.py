# coding=utf-8
import json
from urllib import urlopen
from datetime import datetime
from django.conf import settings
from django.shortcuts import render


def get_time():
    # 'yyyy-mm-dd'
    return str(datetime.now()).split(' ')[0]


def get_average():
    f = urlopen(
        'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM25&dataGubun=HOUR&searchCondition=WEEK&pageNo=1&numOfRows=30&_returnType=json&ServiceKey={key}'.format(
            key=settings.OPEN_AIR_KEY
        ))
    data = json.load(f)
    values = [int(row['seoul']) for row in data['list'] if
              '16:00' > row['dataTime'].split()[1] > '00:00' and row['seoul'] != '']
    average = sum(values) / len(values)
    return average


def get_forecast():
    f = urlopen(
        'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate={today}&_returnType=json&ServiceKey={key}'.format(
            today=get_time(), key=settings.OPEN_AIR_KEY
        ))
    data = json.load(f)
    s = data['list'][0]['informGrade']
    grade = s.split(',')[0].split(':')[1].strip()
    return grade


def index(request):
    average = get_average()
    forecast = get_forecast()

    data = {}
    if average > 50 and forecast == u'나쁨':
        data['class'] = 'free'
        data['icon'] = 'icon-free.svg'
        data['message'] = u'예 그렇습니다.'
    else:
        data['class'] = 'nonfree'
        data['icon'] = 'icon-nonfree.svg'
        data['message'] = u'아니오 유료입니다'

    return render(request, 'index.html', data)
