# coding=utf8

from settings import *
import requests
import time
from requests.auth import HTTPBasicAuth

global NAME
global PASSWORD
global GITNAME
global GITPASSWORD


class Gitstar():
    def __init__(self, name, password, git_name, git_password):
        self.NAME = name
        self.PASSWORD = password
        self.GITNAME = git_name
        self.GITPASSWORD = git_password

        self.cookie = None

    def login_gitstar(self):
        r = requests.post("http://gitstar.top:88/api/user/login",
                          params={'username': self.NAME, 'password': self.PASSWORD})
        self.cookie = r.headers['Set-Cookie']
        return r.headers['Set-Cookie']

    def get_gitstar_recommend(self):
        cookie = self.login_gitstar()
        url = "http://gitstar.top:88/api/users/{}/status/recommend".format(self.NAME)
        response = requests.get(url, headers={'Accept': 'application/json', 'Cookie': cookie})
        jsn = response.json()
        list = []
        for obj in jsn:
            list.append(obj['Repo'])
        return list

    def star(self, url):
        global AUTH
        AUTH = HTTPBasicAuth(self.GITNAME, self.GITPASSWORD)
        res = requests.put("https://api.github.com/user/starred/" + url
                           , headers={'Content-Length': '0'}
                           , auth=AUTH)

    def update_gitstar(self):
        while True:
            url = "http://gitstar.top:88/star_update"
            res = requests.get(url, headers={'Accept': 'application/json', 'Cookie': self.cookie})
            print "update: " + str(res.status_code == 200)
            if res.status_code == 200:
                break

    def run_star(self):
        urls = self.get_gitstar_recommend()
        print "get total github repo for [%s]: %d" % (self.NAME, len(urls))
        i = 1
        try:
            for url in urls:
                self.star(url)
                print "[%d]Stared! -->%s" % (i, url)
                time.sleep(5.0)
                i = i + 1        
        finally:  
        	print "Please wait to update the data..."
        	if len(urls) > 0:
				self.update_gitstar()


if 'NAME' in dir():
    Gitstar(NAME, PASSWORD, GITNAME, GITPASSWORD).run_star()
else:
    for i in range(0, len(NAMES)):
        Gitstar(NAMES[i], PASSWORDS[i], GITNAMES[i], GITPASSWORDS[i]).run_star()
