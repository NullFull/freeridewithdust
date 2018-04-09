# coding=utf-8
import json
from urllib import urlopen
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render
from django.core.cache import caches
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'freeridewithdust.settings'


def get_time():
    # 'yyyy-mm-dd'
    return str(datetime.now() - timedelta(days=1)).split(' ')[0]


# def test():
#     yesterday = str(datetime.now() - timedelta(days=1)).split(' ')[0].replace('-', '')
#     print yesterday
#     seoul_values = []
#     for i in range(17):
#         time = str(i) if i > 9 else '0' + str(i)
#         f = urlopen(
#             'http://openapi.seoul.go.kr:8088/{key}/json/TimeAverageAirQuality/0/25/{yesterday}{time}'.format(
#                 key=settings.SEOUL_AIR_KEY, yesterday=yesterday, time=time
#             ))
#         data = json.load(f)
#         values = [d['PM25'] for d in data['TimeAverageAirQuality']['row'] if
#                   d['PM25'] != 0]
#         print(yesterday, time, 'hour: ', values)
#         avg = sum(values) / len(values)
#         print(yesterday, time, 'hour avg: ', avg)
#         seoul_values.append(avg)
#     return sum(seoul_values) / len(seoul_values)


def get_average():
    yesterday = get_time().replace('-', '')
    cacher = caches['default']
    cache_key = yesterday + '-values'
    if cache_key not in cacher:
        seoul_values = []
        for i in range(17):
            time = str(i) if i > 9 else '0' + str(i)
            f = urlopen('http://openapi.seoul.go.kr:8088/{key}/json/TimeAverageAirQuality/0/25/{yesterday}{time}'.format(
                key=settings.SEOUL_AIR_KEY ,yesterday=yesterday, time=time
            ))
            data = json.load(f)
            values = [d['PM25'] for d in data['TimeAverageAirQuality']['row'] if d['PM25'] != 0]
            avg = sum(values) / len(values)
            seoul_values.append(avg)
        cacher.set(cache_key, sum(seoul_values) / len(seoul_values))
    return cacher.get(cache_key)


# def get_average():
#     f = urlopen(
#         'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM25&dataGubun=HOUR&searchCondition=WEEK&pageNo=1&numOfRows=30&_returnType=json&ServiceKey={key}'.format(
#             key=settings.OPEN_AIR_KEY
#         ))
#     data = json.load(f)
#     values = [int(row['seoul']) for row in data['list'] if
#               '16:00' > row['dataTime'].split()[1] > '00:00' and row['seoul'] != '']
#     average = sum(values) / len(values)
#     return average


def get_forecast():
    f = urlopen(
        'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate={today}&_returnType=json&ServiceKey={key}'.format(
            today=get_time(), key=settings.OPEN_AIR_KEY
        ))
    data = json.load(f)
    forecasts = [d for d in data['list'] if d['informCode'] == 'PM25' and d['informData'] == str(datetime.now()).split(' ')[0]][:2]
    grades = [d['informGrade'].split(',')[0].split(':')[1].strip() for d in forecasts]
    result = u'나쁨' if (grades[0] == '나쁨' and grades[0] == grades[1]) else grades[0]
    return result


def index(request):

    # average = get_average()
    # forecast = get_forecast()
    #
    # data = {}
    # if average > 50 and forecast == u'나쁨':
    #     data['class'] = 'free'
    #     data['icon'] = 'icon-free.svg'
    #     data['message'] = u'예 그렇습니다.'
    # else:
    #     data['class'] = 'nonfree'
    #     data['icon'] = 'icon-nonfree.svg'
    #     data['message'] = u'아니오 유료입니다'

    return render(request, 'index.html')
