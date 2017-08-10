import requests
from lxml import etree
from datetime import datetime
import csv


def get_title_data(url,page):
    for i in range(1,page+1):
        newurl = url + str(i)
        html = requests.get(newurl, headers=headers).content
        selector = etree.HTML(html)
        infos = selector.xpath("//ul[@class='sellListContent']/li")
        if len(infos) == 0:
               pass
        else:
            for info in infos:
                totalprice = info.xpath('div[1]/div[6]/div[1]/span/text()')
                unitprice = info.xpath('div[1]/div[6]/div[2]/span/text()')
                xiaoqu = info.xpath('div[1]/div[2]/div/a/text()')
                houseinfo = info.xpath('div[1]/div[2]/div/text()')
                time = info.xpath('div[1]/div[3]/div/text()')
                print (totalprice, unitprice, xiaoqu, houseinfo, time)
                info1.append([totalprice, unitprice, xiaoqu, houseinfo, time])


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    base_url = 'https://gz.lianjia.com/ershoufang/tianhe/pg'
    info1 = []
    get_title_data(base_url,2)
    with open('lianjia.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['总价', '单价', '小区', '房屋信息', '年代'])
        for row in info1:
            writer.writerow(row)




