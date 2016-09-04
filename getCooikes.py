#用来爬取网页需要的COOIKES
import os
import hashlib
import cookielib

LOGIN_URL = 'http://登陆页面地址'
USER_NAME = '用户名'
PASSWORD = '密码'

HOST = '目标网页主域名'
REFERER = 'http://目标网页主域名/'
POST_URL_PREFIX = 'http://目标网页主域名/'
COOKIES_FILE = '/tmp/pyspider.%s.%s.cookies' % (HOST, hashlib.md5(USER_NAME).hexdigest())
COOKIES_DOMAIN = HOST

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
HTTP_HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection' : 'keep-alive',
    'DNT' : '1',
    'Host' : HOST,
    'Referer' : REFERER,
    'User-Agent' : USER_AGENT,
}

def getCookies():
    cookiesJar = cookielib.MozillaCookieJar(COOKIES_FILE)
    if not os.path.isfile(COOKIES_FILE):
        cookiesJar.save()
    cookiesJar.load (COOKIES_FILE)
    cookieProcessor = urllib2.HTTPCookieProcessor(cookiesJar)
    cookieOpener = urllib2.build_opener(cookieProcessor, urllib2.HTTPHandler)
    for item in HTTP_HEADERS:
        cookieOpener.addheaders.append ((item ,HTTP_HEADERS[item]))
    urllib2.install_opener(cookieOpener)
    if len(cookiesJar) == 0:
        login = Login(USER_NAME, PASSWORD, LOGIN_URL, POST_URL_PREFIX)
        if login.login():
            cookiesJar.save()
        else:
            return None
    cookiesDict = {}
    for cookie in cookiesJar:
        if COOKIES_DOMAIN in cookie.domain:
            cookiesDict[cookie.name] = cookie.value
    return cookiesDict

