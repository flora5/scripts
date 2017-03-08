# -*- coding:utf-8 -*-
# flora.bai


import os
from shutil import rmtree
from calendar import monthrange
from datetime import datetime, timedelta


home = os.path.expanduser('~') + '/file_test'

client_info_path = home + '/info'
client_log_path = home + '/log'

template_path = home + '/template'
captcha_img_path = home + '/captcha'
id_img_path = home + '/id_img'


def create_once():
    if not os.path.exists(template_path):
        os.makedirs(template_path)
        print template_path
    if not os.path.exists(captcha_img_path):
        os.makedirs(captcha_img_path)
        print captcha_img_path
    if not os.path.exists(id_img_path):
        os.makedirs(id_img_path)
        print id_img_path


def create_month_client_info():
    now = datetime.now() + timedelta(days=1)
    days = monthrange(now.year, now.month)
    client_info = client_info_path + '/' + str(now.year) + '/' + str(now.month).rjust(2,"0")
    for d in range(now.day, days[1]+1):
        day_str = str(d).rjust(2,"0")
        client_info_name = client_info + '/' + day_str
        if not os.path.exists(client_info_name):
            os.makedirs(client_info_name)
            print client_info_name


def create_month_client_log():
    now = datetime.now() + timedelta(days=1)
    days = monthrange(now.year, now.month)
    client_log = client_log_path + '/' + str(now.year) + '/' + str(now.month).rjust(2,"0")
    for d in range(now.day, days[1]+1):
        day_str = str(d).rjust(2,"0")
        client_log_name = client_log + '/' + day_str
        if not os.path.exists(client_log_name):
            os.makedirs(client_log_name)
            print client_log_name


def clean_dirs():
    rmtree(home,ignore_errors=True)
    print 'clean...'


if __name__ == '__main__':
    #clean_dirs()
    create_once()
    create_month_client_info()
    create_month_client_log()
