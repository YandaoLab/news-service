import requests
import json
import time
API='https://www.toptal.com/developers/feed2json/convert?url=https%3A%2F%2Fwww.daoblog.top%2Fatom.xml'
headers={
    'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Headers':'Content-Type',
    'Access-Control-Allow-Methods':'*',
    'Content-Type':'application/json;charset=utf-8'
}

def get_topic():
    try:
        dataList=[]
        data=requests.get(API,headers=headers,timeout=100)
        data=json.loads(data.text)
        data_json=data['items']#['list']
        for i in range(0,len(data_json)):
            dic = {
                'title': data_json[i].get('title',''),
                #'keyword': data_json[i].get('keyword',''),
                'url': '' + data_json[i].get('url',''),
                #'icon': data_json[i].get('icon','')
            }
            dataList.append(dic)
        return dataList
    except Exception as e:
        print(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),e)
        return None