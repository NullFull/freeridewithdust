# coding=utf-8
import json
import webapp2
from urllib import urlopen



class MainPage(webapp2.RequestHandler):
    def get_average(self):
        f = urlopen(
            'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM25&dataGubun=HOUR&searchCondition=WEEK&pageNo=1&numOfRows=30&_returnType=json&ServiceKey=hFfytrBnh8rAAckaVVfx4io3JRk4hFurd5sM4SUf5Fhnea2dOVy8rUlJrHBxN%2BuZYe5vWIvd0g9NldVJu8Bd3g%3D%3D')
        data = json.load(f)
        values = [int(row['seoul']) for row in data['list'] if '16:00' > row['dataTime'].split()[1] > '00:00']
        average = sum(values) / len(values)
        return average

    def get_forecast(self):
        f = urlopen('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMinuDustFrcstDspth?searchDate=2017-11-26&InformCode=PM25&_returnType=json&ServiceKey=hFfytrBnh8rAAckaVVfx4io3JRk4hFurd5sM4SUf5Fhnea2dOVy8rUlJrHBxN%2BuZYe5vWIvd0g9NldVJu8Bd3g%3D%3D')
        data = json.load(f)
        s = data['list'][0]['informGrade']
        grade = s.split(',')[0].split(':')[1].strip()
        return grade

    def get(self):
        average = self.get_average()
        forecast = self.get_forecast()

        if average > 50 and forecast == u'나쁨':
            self.response.out.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"  lang="ko" xml:lang="ko">
<head>
<title>먼지먹고 무임승차</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>
<style>
 html { height: 100%; }
  body {
    margin: auto 0;
    text-align: center;
    color: #fff;
    height: 100%;
  }
  h1 {
    margin: 0;
  }
  
  .bg_Grad01 {
    padding-top: 40px;
    height: 100%;
    background: linear-gradient(to top, #15485d, #f29492);
  }
</style>
<body>
  <div class="bg_Grad01">
  <h1>먼지먹고 무임승차</h1>
    <div class="ride_icon">
      <img src="/static/icon_02.png">
      <p class="ride_nob">
          Yes
      </p>
    </div>
    <div class="info">
      <p>
        정보제공 : 한국환경정보
      </p>
      <p>
        제작 : 널채움(Nullfull)
      </p>
    </div>
  </div>
</body>

</html>

                    ''')
        else:
            self.response.out.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"  lang="ko" xml:lang="ko">
<head>
<title>먼지먹고 무임승차</title>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>
<style>
 html { height: 100%; }
  body {
    margin: auto 0;
    text-align: center;
    color: #fff;
    height: 100%;
  }
  h1 {
    margin: 0;
  }
  
  .bg_Grad01 {
    padding-top: 40px;
    height: 100%;
    background: linear-gradient(to top, #15485d, #f29492);
  }
</style>
<body>
  <div class="bg_Grad01">
  <h1>먼지먹고 무임승차</h1>
    <div class="ride_icon">
      <img src="/static/icon_02.png">
      <p class="ride_nob">
          Nope
      </p>
    </div>
    <div class="info">
      <p>
        정보제공 : 한국환경정보
      </p>
      <p>
        제작 : 널채움(Nullfull)
      </p>
    </div>
  </div>
</body>

</html>

                    ''')


app = webapp2.WSGIApplication([
    ('/', MainPage),
])