#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "http://www.mengchenghui.com/"
assign_url = "http://www.mengchenghui.com/plugin.php?id=qidou_assign:iframe&infloat=yes&handlekey=assign&inajax=1&ajaxtarget=fwin_content_assign"

cookies = dict(
    cookies_are='qqnews_closed=yes; _ga=GA1.2.1305238275.1484418073; mUyL_029b_saltkey=YqXryaoR; mUyL_029b_lastvisit=1484792110; mUyL_029b_ulastactivity=efe7hXmS4NiHC4EFJvwC5mbz4RFdO74c5KrdTS%2Bp0bzaRzFRUSdR; mUyL_029b_auth=4ff0%2BUrlGRgLN36VeJdHLs%2FnEBRqu7S1r84rtwTb%2BxD5f09mC3zAbUwnZ8M%2BrwK5cs4kEwne1XzcGtR%2Bkdti0rFz; mUyL_029b_lastcheckfeed=8088%7C1484795931; mUyL_029b_lip=70.53.154.177%2C1484794676; mUyL_029b_sid=LsaRDi; pgv_pvi=4267456960; pgv_info=ssi=s6918731068; CNZZDATA1254006440=1812046160-1484412934-%7C1484792129; mUyL_029b_lastact=1484795936%09misc.php%09patch; mUyL_029b_connect_is_bind=0'
)

cookies_test = dict(
    cookies_are='qqnews_closed=yes; _ga=GA1.2.1305238275.1484418073; mUyL_029b_saltkey=YqXryaoR; mUyL_029b_lastvisit=1484792110; mUyL_029b_ulastactivity=efe7hXmS4NiHC4EFJvwC5mbz4RFdO74c5KrdTS%2Bp0bzaRzFRUSdR; mUyL_029b_auth=4ff0%2BUrlGRgLN36VeJdHLs%2FnEBRqu7S1r84rtwTb%2BxD5f09mC3zAbUwnZ8M%2BrwK5cs4kEwne1XzcGtR%2Bkdti0rFz; mUyL_029b_lastcheckfeed=8088%7C1484795931; mUyL_029b_lip=70.53.154.177%2C1484794676; mUyL_029b_sid=LsaRDi; pgv_pvi=4267456960; pgv_info=ssi=s6918731068; CNZZDATA1254006440=1812046160-1484412934-%7C1484792129; mUyL_029b_lastact=1484795936%09misc.php%09patch; mUyL_029b_connect_is_bind=0'
)

s = requests.Session()
r = s.get(url, cookies=cookies)
r_assign = s.get(assign_url)

soup = BeautifulSoup(r.text, 'html.parser')
name = soup.find_all('a', title='访问我的空间')
print(name)
print(r_assign.status_code)
