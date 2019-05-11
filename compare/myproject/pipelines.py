# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector


class MyprojectPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        print('connected')
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='compare'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS bike_list""")
        self.curr.execute(
            """create table bike_list(mileage text,
frontbrake text,
fuelcapacity text,
rearbrake text,
enginetype text,
displacement text,
bodytype text,
abs text,
headlamp text,
wheeltype text,
maximumpower text,
maximumtorque text,
`starting` text,
coolingsystem text,
gearbox text,
clutch text,
noofcylinders text,
drivetype text,
supplysystem text,
transmissiontype text,
tyresize text,
tyretype text,
wheelsize text,
ebs text,
tractioncontrol text,
cruisecontrol text,
navigation text,
quickshifter text,
launchcontrol text,
powermodes text,
adjustablewindscreen text,
mobileconnectivity text,
frontsuspension text,
rearsuspension text,
kerbweight text,
wheelbase text,
taillamp text,
turnsignallamp text,
passswitch text)""")



    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into bike_list(mileage ,
frontbrake ,
rearbrake ,
fuelcapacity ,
enginetype ,
displacement ,
bodytype ,
abs ,
headlamp ,
wheeltype ,
maximumpower ,
maximumtorque ,
`starting` ,
coolingsystem ,
gearbox ,
clutch ,
noofcylinders ,
drivetype ,
supplysystem ,
transmissiontype ,
tyresize ,
tyretype ,
wheelsize ,
ebs ,
tractioncontrol ,
cruisecontrol ,
navigation ,
quickshifter ,
launchcontrol ,
powermodes ,
adjustablewindscreen ,
mobileconnectivity ,
frontsuspension ,
rearsuspension ,
kerbweight ,
wheelbase ,
taillamp ,
turnsignallamp ,
passswitch) values (
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,%s,%s)""", (
            item['mileage'],
            item['frontbrake'],
            item['rearbrake'],
            item['fuelcapacity'],
            item['enginetype'],
            item['displacement'],
            item['bodytype'],
            item['abs'],
            item['headlamp'],
            item['wheeltype'],
            item['maximumpower'],
            item['maximumtorque'],
            item['starting'],
            item['coolingsystem'],
            item['gearbox'],
            item['clutch'],
            item['noofcylinders'],
            item['drivetype'],
            item['supplysystem'],
            item['transmissiontype'],
            item['tyresize'],
            item['tyretype'],
            item['wheelsize'],
            item['ebs'],
            item['tractioncontrol'],
            item['cruisecontrol'],
            item['navigation'],
            item['quickshifter'],
            item['launchcontrol'],
            item['powermodes'],
            item['adjustablewindscreen'],
            item['mobileconnectivity'],
            item['frontsuspension'],
            item['rearsuspension'],
            item['kerbweight'],
            item['wheelbase'],
            item['taillamp'],
            item['turnsignallamp'],
            item['passswitch']
        ))
        self.conn.commit()
