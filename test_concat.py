#coding: utf-8

import os,sys
import re
import time
from datetime import datetime


import requests
import json
from PIL import Image,ImageChops
import cPickle
from test_getdata import *

ss ="""<div class="gt_cut_fullbg gt_show"><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -157px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -145px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -265px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -277px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -181px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -169px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -241px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -253px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -109px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -97px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -289px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -301px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -85px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -73px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -25px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -37px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -13px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -1px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -121px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -133px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -61px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -49px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -217px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -229px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -205px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -193px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -145px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -157px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -277px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -265px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -169px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -181px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -253px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -241px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -97px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -109px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -301px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -289px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -73px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -85px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -37px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -25px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -1px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -13px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -133px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -121px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -49px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -61px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -229px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -217px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -193px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;http://static.geetest.com/pictures/gt/895656306/895656306.webp&quot;); background-position: -205px 0px;"></div></div>"""

image_save_path = '/home/moma/captcha_images/'
static_servers = "http://static.geetest.com/"
if not os.path.exists(image_save_path):
    os.system('mkdir %s'%image_save_path)

def download_img(url,name):
    res = requests.get(url)
    image_path = image_save_path+name
    try:
        with open(image_path,'wb') as f:
            f.write(res.content)
            print "image_save success!"
            return Image.open(image_path)
    except Exception as e:
        print e
        print "--------------download image: %s failed,url is: %s--------------"%(name,url)

def get_pos(ss):
    res = re.findall(r'-\w+?px\s-*\w+?px;\"',ss)
    # print res
    result = []
    for item in res:
        result.append(re.findall(r'\d+',item))
    return result


def recover(img,pos):
    size = img.size
    #先生成一块一样大小的空图片
    im = Image.new('RGBA',size)
    cols = len(pos)/2
    print "cols:",cols
    for count,item in enumerate(pos):
        # print count
        col = round(count/cols)
        # print count,col
        posx = int(item[0])
        posy = int(item[1])
        box = (posx,posy,posx+10,posy+58)
        region = img.crop(box)
        # origin_box = ((count%cols)*12,int(col)*58,(count%cols)*12+12,(int(col)*58)+58)
        origin_box = ((count%cols)*10,int(col)*58)
        # print origin_box
        im.paste(region,origin_box)
    return im

def get_dist(image1_url,image2_url):
    # location_list
    ################################
    image1 = download_img(image1_url,'fullbg.jpg')
    image2 = download_img(image2_url,'bg.jpg')
    pos = get_pos(ss)
    im1 = recover(image1,pos)
    print "im1.size--------------------------->",im1.size
    # im1.show()
    im2 = recover(image2,pos)
    # im2.show()
    ################################
    im = ImageChops.difference(im1,im2)
    width,height = im.size
    count = 0
    for i in range(width):
        color_count = 0
        for j in range(height):
            count += 1
            # print "count,width,height =",count,i,j
            # print im.getpixel((i,j))
            if color_count >30:
                return im,i
            if sum(im.getpixel((i,j))) > 120:
                color_count += 1
            elif sum(im.getpixel((i,j))) <=120:
                color_count = 0
    return im,-1


headers = {'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-US,en;q=0.8',
'Connection':'keep-alive',
'Cookie':'GeeTestUser=a3e643b51de0e88532b5f0e3e7e0e3d4; GeeTestAjaxUser=da53de5a02bd8f51ee602446622f9244; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215df9c149461be-00ab768a82dd6d-3977065e-2073600-15df9c14948f1%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; Hm_lvt_25b04a5e7a64668b9b88e2711fb5f0c4=1503133782; Hm_lpvt_25b04a5e7a64668b9b88e2711fb5f0c4=1503134226',
'Host':'api.geetest.com',
'Referer':'http://www.gsxt.gov.cn/corp-query-search-1.html',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}


headers1 = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'}


headers2 = {'cache-control': 'no-cache, no-store, must-revalidate','connection': 'keep-alive','content-length': 729,'content-type': 'text/javascript;charset=UTF-8'}

def fake_ax():
    #时间戳
    url1 = 'http://www.gsxt.gov.cn/SearchItemCaptcha?v=[__time__]'
    url2 = 'http://api.geetest.com/get.php?gt=[__gt__]&challenge=[__challenge__]&product=popup&offline=false&protocol=&path=/static/js/geetest.5.10.10.js&type=slide&callback=geetest_[__callback__]'
    url3 = 'http://api.geetest.com/ajax.php?gt=1d2c042096e050f07cb35ff3df5afd92&challenge=3a1502d5b2886923bc933d1ada15959ecj&userresponse=60606606060b3&passtime=1694&imgload=72&a=B%2C..1%2F%2F.00%2F-%2F.%2F--(!!Essty!)!)z!)!)!)(!*!)((((t(((z(ttu(!!(%24)%2F%24)%3A9%3A%3A9%3A9%3A%3A9%3F99%3A%40B39%3F%3A999%24%2FOD%2447&callback=geetest_1503304071186'
    t = time.time()
    t = int(round(1000*t))
    t = str(t)
    url1 = url1.replace('[__time__]',t)
    print "url1-->",url1
    res = requests.get(url1,headers = headers1)
    json_res = json.loads(res.content)
    challenge = json_res['challenge']
    gt = json_res['gt']
    print "1111chanllenge:",challenge
    print "1111gt:",gt
    url2 = url2.replace('[__gt__]',gt)
    url2 = url2.replace('[__challenge__]',challenge)
    t = time.time()
    ###callback参数最后为毫秒级的时间戳
    callback = int(round(1000*t))
    callback = str(callback)
    print callback
    url2 = url2.replace('[__callback__]',callback)
    print url2
    res2 = requests.get(url2)
    print res2
    print "res2 ------>\n",res2.content
    # tmp = res2.content
    # my_challenge = re.findall(r'\"challenge\"\:\s\"[\w\W]+?\"',tmp)
    # my_challenge = my_challenge[0].split(' ')[-1]
    # print "my_challenge----->",my_challenge
    dict2 = re.findall(r'\{[\s\S]+\}',res2.content)
    res3 = json.loads(dict2[0])
    print "!!!!!!res3!!!!!!!!!\n",res3
    fullbg_url = static_servers + res3['fullbg']
    print "fullbg_url----->",fullbg_url
    bg_url = static_servers + res3['bg']
    # download_img(fullbg_url,'fullbg.jpg')
    # download_img(bg_url,'bg.jpg')
    # pos = get_pos(ss)
    # img1_path = image_save_path+'fullbg.jpg'
    # img2_path = image_save_path+'bg.jpg'
    # img1 = Image.open(img1_path)
    # img2 = Image.open(img2_path)
    ###下面返回的dist就是要滑动的距离
    im,dist = get_dist(fullbg_url,bg_url)
    print "dist---->",dist
    # im.show()

    challenge = res3['challenge']
    # print "12345",my_challenge
    # print type(my_challenge)
    return gt,challenge,dist-6
    # challenge,validate = get_validate(gt,challenge)
    # print "validate---->",validate
    # print "challenge--->",challenge




    # url3 = url3.replace('[__gt__]',gt)
    # url3 = url3.replace('[__challenge]',challenge)
    # t = time.time()
    # ###callback参数最后为毫秒级的时间戳
    # callback = int(round(1000*t))
    # callback = str(callback)
    # url3 = url3.replace('[__callback__]',callback)
    # print url3
    # res3 = requests.get(url1,headers = headers)
    # json_res3 = json.loads(res3.content)
    # print 'res3:------------',json_res3

def get_validate(gt,challenge,dist):
    try:
        # 获得bg和fullbg
        # challenge,bg,fullbg=get_bg_fullbg(gt,challenge)
        # print 'challenge:',challenge
        # print 'bg:',bg
        # print 'fullbg:',fullbg

        # # 缺口距离  供编写鼠标轨迹使用  距离边框6
        # dist=get_dist(bg,fullbg)-6  
        # print 'dist:',dist

        # 根据dist挑选一个路径
        # track来自文件 teg=1  否则 0
        track,tag=choice_track_list(dist)   # 来自训练路径 tag=1
        print "-------track---------%s\n"%track
        print "--------tag----------%s\n"%tag
        # 规范化轨迹数据  [[x,y,t],...]
        track_list=format_track(track)  # 路径列表
        print "track_list---------------->\n",track_list

        # 若tag==0,即轨迹数据不在已收集的轨迹文件中（来自候选轨迹列表）,
        # 则截取路径（从中截取需要的长度）
        if tag!=1:
            new_track_list=create_track(track_list,dist)
            print "if---------new_track_list---------%s\n"%new_track_list
        else:
            # tag==1 轨迹数据来自文件 直接赋值
            new_track_list=track_list
            print "else---------new_track_list---------%s\n"%new_track_list
        print "new_track_list------------->\n",new_track_list

        # 根据challenge和 new_track_list 
        # 计算 userresponse 和 a 参数
        userresponse,a=get_userresponse_a(challenge,new_track_list)
        print 'userresponse:------------------>',userresponse
        print 'a:----------------------------->',a

        url='http://api.geetest.com/ajax.php'
        # passtime parse_3所需的参数
        passtime=new_track_list[-1][-1]
        print 'passtime:',passtime

        # 防止太频繁 休眠时间可改短  
        time.sleep(2)

        # 获得 validate
        validate=parse_3(url,gt,challenge,userresponse,passtime,a)

        time.sleep(2)

        # if len(validate)>0:
        #   print challenge
        #   print validate

        return challenge,validate
    except Exception,e:
        print "error happens------------------------>"
        print e
        return '',''

    def get_uri(page):
        links=[]
        alist=page.xpath(u'//a[@class="search_list_item db"]')

        web_site='http://www.gsxt.gov.cn'
        for item in alist:
            # print item.attrib['href']
            links.append(web_site+item.attrib['href'])
        return links




if "__main__" == __name__:
    # img = Image.open('/home/moma/Downloads/fullbg.jpg')
    # img2 = Image.open('/home/moma/Downloads/bg.jpg')
    # print img.size
    # pos = get_pos(ss)
    # print pos
    # im = recover(img,pos)
    # im2 = recover(img2,pos)
    # im.show()
    # im2.show()
    # # im3 = ImageChops.invert(im2)
    # # Image.blend(im,im3,0.5).show()
    # # ImageChops.difference(im,im2).show()
    # image,distance = get_dist(im,im2)
    # print "distance is ",distance
    # box = (distance,0,distance+100,58)
    # image.crop(box).show()
    








    # searchword='百度'
    pageNo=1
    data_href='http://www.gsxt.gov.cn/corp-query-search-%s.html' %(pageNo)

    headers = {
        "Origin": "http://www.gsxt.gov.cn", 
        "Proxy-Connection": "keep-alive", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36", 
        "Host": "www.gsxt.gov.cn", 
        "Referer": "http://www.gsxt.gov.cn/index.html", 
        "Cache-Control": "max-age=0"
    }

    # searchwords = ['百度','新浪','网易','阿里巴巴','腾讯','滴滴','饿了么']




    #####要搜索的关键词
    searchwords = ['百度','网易']







    for searchword in searchwords:
        gt,challenge,dist = fake_ax()
        print gt
        print challenge
        print dist
        # print (get_pos(ss))
        challenge, validate = get_validate(gt,challenge,dist)
        print "\n######################validate########################",validate
        data = {
            "searchword": searchword, 
            "geetest_challenge": challenge, 
            "token": "41111854", 
            "tab": "", 
            "geetest_seccode": validate+"|jordan", 
            "geetest_validate": validate,
            'page':str(pageNo)
            }

        # 谨慎(请求必须加上headers) 稍不注意 就被短暂封ip
        if validate!=None:
            res=requests.post(data_href,headers=headers,data=data).content
            # print "\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$res$$$$$$$$$$$$$$$$$$$$$$\n",res

            page=etree.HTML(res)

            links=get_uri(page)

            print '查询结果如下:'
            result_path = '/home/moma/Documents/codes/capture_project/results/'+searchword+'.txt'
            # result_path = '/home/moma/Documents/codes/capture_project/results/'+searchword+'.txt'
            with open(result_path,'wb') as f:
                for link in links:
                    print link
                    f.write(link+'\n')
                # content = requests.get(link,headers=headers).content
                # print content.xpath()

