#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "http://www.mengchenghui.com/"
assign_url = "http://www.mengchenghui.com/plugin.php?id=qidou_assign:iframe&infloat=yes&handlekey=assign&inajax=1&ajaxtarget=fwin_content_assign"

cookies = dict(
    cookies_are='qqnews_closed=yes; _ga=GA1.2.1305238275.1484418073; mUyL_029b_saltkey=YqXryaoR; mUyL_029b_lastvisit=1484792110; mUyL_029b_ulastactivity=efe7hXmS4NiHC4EFJvwC5mbz4RFdO74c5KrdTS%2Bp0bzaRzFRUSdR; mUyL_029b_auth=4ff0%2BUrlGRgLN36VeJdHLs%2FnEBRqu7S1r84rtwTb%2BxD5f09mC3zAbUwnZ8M%2BrwK5cs4kEwne1XzcGtR%2Bkdti0rFz; mUyL_029b_lastcheckfeed=8088%7C1484795931; mUyL_029b_lip=70.53.154.177%2C1484794676; mUyL_029b_sid=LsaRDi; pgv_pvi=4267456960; pgv_info=ssi=s6918731068; CNZZDATA1254006440=1812046160-1484412934-%7C1484792129; mUyL_029b_lastact=1484795936%09misc.php%09patch; mUyL_029b_connect_is_bind=0'
)

cookies_joyce = dict(
    cookies_are='_ga=GA1.2.1305238275.1484418073; mUyL_029b_saltkey=ZRLR3rZr; mUyL_029b_lastvisit=1484884999; mUyL_029b_sendmail=1; mUyL_029b_ulastactivity=aa32rUK7JU0KKyYPxBnULxsV7PDEjkj4sLke8FiKFbpAAhv16fCC; mUyL_029b_auth=01a9mRnfVfjbBtMqOTuzEODzxzWntJVaht4zbGsWB2POzHXNadP0UdmEV588HXz1b%2BeSCRoFX4ttt96o9mTn1O5MEA; mUyL_029b_lastcheckfeed=28653%7C1484888696; mUyL_029b_checkfollow=1; mUyL_029b_lip=24.114.96.33%2C1484874122; mUyL_029b_checkpm=1; tjpctrl=1484890502484; mUyL_029b_sid=YhbbZY; pgv_pvi=4267456960; pgv_info=ssi=s6918731068; CNZZDATA1254006440=1812046160-1484412934-%7C1484887595; mUyL_029b_noticeTitle=1; mUyL_029b_lastact=1484888709%09misc.php%09patch; mUyL_029b_connect_is_bind=0; qqnews_closed=yes'
)

cookies_test = dict(
    cookies_are='_ga=GA1.2.1305238275.1484418073; qqnews_closed=yes; tjpctrl=1484890576970; mUyL_029b_saltkey=bRrrah30; mUyL_029b_lastvisit=1484885842; mUyL_029b_sendmail=1; mUyL_029b_ulastactivity=fc44k1%2Fni2v9HvB3vQ6k8xv6h0nPq2CdFjwFPyi5dfhdiJrfi%2FoY; mUyL_029b_auth=78632qN4AVyDwUQ%2B1aURNhvXCyzhgUUvsnn8AVO13khgZgdtX21ulZUn19dN866HqsjGGI5oVXubazCL4Z%2BixFkAgw; mUyL_029b_lastcheckfeed=60498%7C1484889449; mUyL_029b_checkfollow=1; mUyL_029b_lip=70.53.154.177%2C1484803003; mUyL_029b_sid=gK0uJe; mUyL_029b_checkpm=1; pgv_pvi=4267456960; pgv_info=ssi=s6918731068; CNZZDATA1254006440=1812046160-1484412934-%7C1484887595; mUyL_029b_lastact=1484889453%09misc.php%09patch; mUyL_029b_connect_is_bind=0'
)

s = requests.Session()
r = s.get(url, cookies=cookies_test)
r_assign = s.get(assign_url, cookies=cookies_test)

soup = BeautifulSoup(r.text, 'html.parser')
name_html = soup.find_all('a', title='访问我的空间')

if (r.status_code == 200):
    for name in name_html:
        print('\n' + name.string + ' 登录成功....\n')
else:
    print('\n登录失败....\n')

if (r_assign.status_code == 200):
    print('签到成功...\n')
else:
    print('签到失败...\n')
