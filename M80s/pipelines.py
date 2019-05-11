# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class M80SPipeline(object):
    def __init__(self):
        print("sql 连接创建中。。。。。。。。。。。。。")
        # 建立数据库连接
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Android520@', db='python',
                                          charset='utf8')
        # 创建操作游标
        self.cursor = self.connection.cursor()
        print("sql 连接创建成功")
    def process_item(self, item, spider):
        sql='insert into python.java(company_name,job_name,address,salary,time) ' \
            'value (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")'.format(item['company_name'],item['job_name'],item['address'],item['salary'],item['time'])
        self.cursor.execute(sql)
        self.connection.commit()
        print("插入数据{}{}{}{}{}".format(item['company_name'],item['job_name'],item['address'],item['salary'],item['time']))

        return item
    def __del__(self):
        self.connection.close()
        self.cursor.close()