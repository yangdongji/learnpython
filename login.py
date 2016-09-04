import urllib
import urllib2
import lxml.html as HTML
import re

class Login(object):

    def __init__(self,username,password,login_ur,post_url_prefix):
        self.username = username
        self.password = password
        self.login_url = login_ur
        self.post_url_prefix = post_url_prefix

    def login(self):
        post_url , post_data = self.getPostData()
        post_url = self.post_url_prefix + post_url
        req = urllib2.Request(url = post_url, data=post_data)
        resp = urllib2.urlopen(req)
        return  True

    def getPostData(self):
        url = self.login_url.strip()
        if not re.match(r'^http://',url):
            return None
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)
        login_page = resp.read()
        doc = HTML.fromstring(login_page)
        post_url = doc.xpath("//form[@method='post' and @id='lsform']/@action")[0]
        cookietime = doc.xpath("//input[@name='cookietime' and @id='ls_cookietime']/@value")[0]
        username = self.username
        password = self.password
        post_data = urllib.urlencode({
            'fastloginfield': 'username',
            'username': username,
            'password': password,
            'quickforward': 'no',
            'handlekey': 'ls',
            'cookietime': cookietime,
        })
        return  post_url,post_data





