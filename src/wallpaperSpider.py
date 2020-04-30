# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
import re
class wallpaper:
    def __init__(self,web_url):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        self.rootPath = r'./wallpaper'
        self.codeFormate = 'utf-8'

    def begin(self,starturl):
        r = requests.get(starturl, headers=self.headers)
        r.encoding = 'utf-8'
        bs = BeautifulSoup(r.text, 'lxml')                
        all_a = bs.find_all(lambda tag: tag.has_attr('href'))
        len_a = len(all_a)
        index = 0
        if os.path.exists(self.rootPath) is False:
            os.makedirs(self.rootPath)
        for a in all_a:
            index += 1
            if a['href'].startswith('https://yys.res.netease.com/pc/zt/20170731172708/data/'):
                if a['href'].endswith('.jpg'):
                    img = requests.get(a['href'], headers = self.headers)
                    file_name = str(a['href']).replace('https://yys.res.netease.com/pc/zt/20170731172708/data/', '').replace('/', ('_'))
                    path_file_name = self.rootPath + '/' + file_name
                    if img is not None:
                        if os.path.exists(path_file_name) is False:
                            f = open(path_file_name, 'wb+')
                            f.writelines(img)
                            f.close()
                            print('图像 %s 保存成功！当前进度为 %d/%d' %(file_name, index, len_a))
                        else:
                            print('图像 %s 已存在！当前进度为 %d/%d' %(file_name, index, len_a))
        print('全部壁纸下载成功！地址为 ./wallpaper')
starturl = 'https://yys.163.com/media/picture.html'
yySpider = wallpaper(starturl)
yySpider.begin(starturl)