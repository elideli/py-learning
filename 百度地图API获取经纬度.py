# coding:utf-8
import csv
import json

import requests


def get_geocode(address_temp):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    params = {
        "address": address_temp,
        "output": "json",
        "ak": "6AcEpBWpxUajiWVc2g8Cl4vSOVMLX7ng",
    }
    res = requests.get(url, params=params).content
    json_data = json.loads(res)
    if json_data['status'] == 0:
        return json_data['result']['location']


if __name__ == '__main__':
    all_data = []
    with open('新地产分析-0728.csv', 'r', encoding='utf-8') as lagou_file:
        reader = csv.reader(lagou_file)
        with open('address.csv', 'w+', encoding='utf-8') as address_file:
            writer = csv.writer(address_file)
            for line in reader:
                address = line[0]
                location = get_geocode(address)
                writer.writerow([address] + list(location.values()))
lagou_file.close()
address_file.close()
