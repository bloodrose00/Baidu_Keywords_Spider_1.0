# -*- coding: utf-8 -*-


from datetime import datetime
import requests
import json
# from fake_useragent import UserAgent
# import random
import zhconv



class Ballgametime_Spider(object):
    def __init__(self):
        self.url = 'http://www.ballgametime.com/api/index.php'


    def get_headers(self,cookie):
        # ua = UserAgent()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "19",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie":cookie,
            # "Cookie": "langflag00=zh-cn; _ga=GA1.2.1584426306.1576565793; _gid=GA1.2.570874221.1576565793; _gat=1; td_cookie=2193980219",
            "Host": "www.ballgametime.com",
            "Origin": "http://www.ballgametime.com",
            "Referer": "http://www.ballgametime.com/statistics",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",

        }
        return headers



    def form_params(self):
        params = {'fun': 'get_player_rank'}
        return params



    def get_page_json(self,headers,params):
        html = requests.post(url = self.url,headers=headers,data=params).text
        html_json = json.loads(html)
        # print(html_json)
        return html_json



    def parse_json(self,html_json):
        a = datetime.now()
        # print(a)
        # print(type(a))
        self.write_in(str(a) + '\n')


        base_data = html_json
        # 场均得分
        pts = base_data['pts']
        # pprint(pts)
        # print('场均得分:')
        self.write_in('****************************' + '\n')
        self.write_in('场均得分:')
        for i in pts:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name, position, score, teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')
        self.write_in('\n'+'\n'+'\n')



        # 场均篮板
        reb = base_data['reb']
        # pprint(reb)
        # print('场均篮板:')
        self.write_in('****************************' + '\n')
        self.write_in('场均篮板:')
        for i in reb:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name,position,score,teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')
        self.write_in('\n'+'\n'+'\n')



        # 助攻
        ast = base_data['ast']
        # pprint(ast)
        # print(type(ast))
        # print('助攻:')
        self.write_in('****************************' + '\n')
        self.write_in('助攻')
        for i in ast:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name,position,score,teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')
        self.write_in('\n'+'\n'+'\n')



        # 场均抢断
        stl = base_data['stl']
        # pprint(stl)
        # print('场均抢断：')
        self.write_in('****************************' + '\n')
        self.write_in('场均抢断:')
        for i in stl:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name,position,score,teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')
        self.write_in('\n'+'\n'+'\n')



        # 场均盖帽
        blk = base_data['blk']
        # pprint(blk)
        # print('场均盖帽:')
        self.write_in('****************************' + '\n')
        self.write_in('场均盖帽:')
        for i in blk:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name,position,score,teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')
        self.write_in('\n'+'\n'+'\n')



        # 场均失误
        turnover = base_data['turnover']
        # pprint(turnover)
        # print('场均失误:')
        self.write_in('****************************' + '\n')
        self.write_in('场均失误:')
        for i in turnover:
            # print(i)
            name = i['name']
            position = i['position']
            score = i['score']
            teamname = i['teamName']
            # print(name,position,score,teamname)
            name_ = '姓名:'+ name
            position_ = '位置:'+ position
            score_ = '分数:'+ score
            teamname_ = '球队:'+ teamname
            # print(type(teamname_))
            team = zhconv.convert(teamname_,'zh-cn')
            data = ['\n' + name_ + '\n' + position_ + '\n' + score_ + '\n' + team + '\n']
            self.write_in(data)
        self.write_in('****************************')




    def write_in(self,data):
        with open('ball_game'+'.txt','a') as f:
            try:
                f.writelines(data)
            except Exception as e:
                print('忽略错误...')



    def run(self):
        cookie = input('输入当前获取的cookie:')
        # 拼接请求头
        headers = self.get_headers(cookie)
        # 获取到的json格式内容
        params = self.form_params()
        html_json = self.get_page_json(headers,params)
        # 解析json格式,并打印测试
        data = self.parse_json(html_json)
        # 写入函数
        self.write_in(data)





if __name__ == '__main__':
    spider = Ballgametime_Spider()
    spider.run()



