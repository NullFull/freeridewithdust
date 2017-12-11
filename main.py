# coding=utf-8
import json
import webapp2
import datetime
from urllib import urlopen
from config import OPEN_AIR_KEY


'''
GCS = /usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/dev_appserver.py .
PATH = $PATH;$GCS/bin;
PYTHONPATH = 
'''

class MainPage(webapp2.RequestHandler):
    def get_time(self):
        # 'yyyy-mm-dd'
        return str(datetime.datetime.now()).split(' ')[0]
    def get_average(self):
        f = urlopen(
            'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM25&dataGubun=HOUR&searchCondition=WEEK&pageNo=1&numOfRows=30&_returnType=json&ServiceKey={key}'.format(
                key=OPEN_AIR_KEY
            ))
        data = json.load(f)
        values = [int(row['seoul']) for row in data['list'] if '16:00' > row['dataTime'].split()[1] > '00:00' and row['seoul'] != '']
        average = sum(values) / len(values)
        return average

    def get_forecast(self):
        f = urlopen(
            'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate={today}&_returnType=json&ServiceKey={key}'.format(
                today=self.get_time(), key=OPEN_AIR_KEY
            ))
        data = json.load(f)
        s = data['list'][0]['informGrade']
        grade = s.split(',')[0].split(':')[1].strip()
        return grade

    def get(self):
        average = self.get_average()
        forecast = self.get_forecast()

        if average > 50 and forecast == u'나쁨':
            data = {
                'message': '예 그렇습니다.',
                'icon': 'icon-on',
                'state': 'free'
            }
        else:
            data = {
                'message': '아니오 유료입니다',
                'icon': 'icon-off',
                'state': 'pay'
            }

        self.response.out.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"  lang="ko" xml:lang="ko">
<head>
<title>먼지먹고 무임승차</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8"/>
<meta name="viewport" content="width=device-width, user-scalable=no">
<link rel="icon" href="/static/favicon.ico">
<link rel="stylesheet" href="/static/style.css">
</head>

<body>
  <div class="{state}">
  <h1>오늘/지금/내일 서울시 대중교통은 무료인가요?</h1>
    <div class="ride_icon">
      <img src="/static/{icon}.svg">
      <p class="ride_nob">
        {message}
      </p>
    </div>
    <div class="info">
      <p>
        정보제공 : <a href="https://www.keco.or.kr/kr/main/index.do">한국환경정보</a>
      </p>
      <p>
        제작 : <a href="https://www.facebook.com/groupnullfull/">널채움(Nullfull)</a>
      </p>
    </div>
  </div>
</body>
</html>
'''.format(**data))

app = webapp2.WSGIApplication([
    ('/', MainPage),
])