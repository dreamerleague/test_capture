# -*- coding: utf-8 -*-

from selenium import webdriver
from pyvirtualdisplay import Display
import socket
socket.setdefaulttimeout(20)
import threadpool
import time
import os

# import exsql

def capture(url):
    file_path = save_dir + os.sep + "%s.png"%str(url)
    if os.path.exists(file_path):
        print '== == == %s exist' %(url)
        return
    print url
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    try:
        browser = webdriver.Chrome()
    except Exception, e:
    	print 'e0'
        print e
        return
    wait_time = 1
    try:
        time.sleep(2)
        browser.get("http://"+url)
    except socket.timeout:
        print 'exit, socket, timeout'
    except Exception, e:
        print 'e1', e
    try:
        browser.save_screenshot(file_path)
    except Exception, e:
        print 'e2', e
    else:
        print "+++ +++ +++ %s" % (file_path)

    browser.quit()
    display.stop()

def manager_thread(url_list, num_thread):
    '''分配线程'''
    pool = threadpool.ThreadPool(num_thread)
    requestlist = threadpool.makeRequests(capture, url_list)
    [pool.putRequest(req) for req in requestlist]
    pool.wait()
    pool.dismissWorkers(num_thread)
    if pool.dismissWorkers:
        pool.joinAllDismissedWorkers()

if __name__ == "__main__":
    # con, cur = exsql.connect_db('13.56.111.204', 'emoma', 'bestmoma201&', 'coupon_site_temp')
    # import sys
    # if len(sys.argv) == 1:
    #     sql = "select max(flag_date) from tool_sc_view_summary ;"
    #     maxdate = exsql.execute_sql(cur, sql)
    #     execute_date = maxdate[0][0]
    # else:
    #     execute_date = sys.argv[1]
    # print execute_date
    # sql = "select slug from tool_sc_view_summary where flag_date = %s%s%s and uv>10 and flag_type = 'codes';" %("'", execute_date, "'")
    # domain_list = exsql.execute_sql(cur, sql)
    # domain_list = [item[0] for item in domain_list]

    # sql = "select website from home_reviewed_brandlist;"
    # reviewed_brand_list = exsql.execute_sql(cur, sql)
    # reviewed_brand_list = [item[0] for item in reviewed_brand_list]

    # url_list = []
    # for url in domain_list:
    #     if url not in reviewed_brand_list:
    #         url_list.append(url)
    # print execute_date
    # print len(domain_list)
    # print len(reviewed_brand_list)
    # print len(url_list)
    # if len(url_list) == 0:
    #     exit()
    # save_dir = "/usr/share/nginx/coupon_temp/webroot/screenshot"
    # thread_num = 1
    # manager_thread(url_list, thread_num)
    url = "www.baidu.com"
    save_dir = "/home/moma/captcha_images"
    capture(url)
