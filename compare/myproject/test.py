# fields = ['mileage', 'frontbrake', 'fuelcapacity', 'rearbrake', 'enginetype', 'displacement', 'bodytype', 'abs',
#           'headlamp', 'wheeltype', 'enginetype', 'displacement', 'maximumpower', 'maximumtorque', 'starting',
#           'coolingsystem', 'gearbox', 'clutch', 'no.ofcylinders', 'drivetype', 'supplysystem', 'transmissiontype',
#           'tyresize', 'tyretype', 'wheelsize', 'frontbrake', 'rearbrake', 'abs', 'ebs', 'tractioncontrol',
#           'cruisecontrol', 'navigation', 'quickshifter', 'launchcontrol', 'powermodes', 'adjustablewindscreen',
#           'mobileconnectivity', 'frontsuspension', 'rearsuspension', 'kerbweight', 'wheelbase', 'fuelcapacity',
#           'headlamp', 'taillamp', 'turnsignallamp', 'passswitch']
#
# for i in fields:
#     print(i, "text,")
# #
# # for i in fields:
# #     print("item['"+i+"'][index],")
# #
# # self.curr.execute(
# #                 """insert into retarkari_list(name,'mileage', 'frontbrake', 'fuelcapacity', 'rearbrake', 'enginetype', 'displacement', 'bodytype',
# #                       'abs', 'headlamp', 'wheeltype', 'enginetype', 'displacement', 'maximumpower', 'maximumtorque',
# #                       'starting', 'coolingsystem', 'gearbox', 'clutch', 'no.ofcylinders', 'drivetype', 'supplysystem',
# #                       'transmissiontype', 'tyresize', 'tyretype', 'wheelsize', 'frontbrake', 'rearbrake', 'abs', 'ebs',
# #                       'tractioncontrol', 'cruisecontrol', 'navigation', 'quickshifter', 'launchcontrol', 'powermodes',
# #                       'adjustablewindscreen', 'mobileconnectivity', 'frontsuspension', 'rearsuspension', 'kerbweight',
# #                       'wheelbase', 'fuelcapacity', 'headlamp', 'taillamp', 'turnsignallamp', 'passswitch') values (%s,'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
# #          '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
# #          '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""", (
#
#  def store_db(self, item):
#         print("Itemssssss")
#         # print('items:::',item)
#         self.curr.execute(
#             """insert into bike_list(name,mileage, frontbrake, fuelcapacity, rearbrake, enginetype, displacement, bodytype,
#                   abs, headlamp, wheeltype,  maximumpower, maximumtorque,
#                   starting, coolingsystem, gearbox, clutch, noofcylinders, drivetype, supplysystem,
#                   transmissiontype, tyresize, tyretype, wheelsize, ebs,
#                   tractioncontrol, cruisecontrol, navigation, quickshifter, launchcontrol, powermodes,
#                   adjustablewindscreen, mobileconnectivity, frontsuspension, rearsuspension, kerbweight,
#                   wheelbase, taillamp, turnsignallamp, passswitch) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
#      %s, %s, %s, %s, %s, %s, %s, %s)""", (
#                 item['mileage'],
#                 item['frontbrake'],
#                 item['fuelcapacity'],
#                 item['rearbrake'],
#                 item['enginetype'],
#                 item['displacement'],
#                 item['bodytype'],
#                 item['abs'],
#                 item['headlamp'],
#                 item['wheeltype'],
#                 item['maximumpower'],
#                 item['maximumtorque'],
#                 item['coolingsystem'],
#                 item['gearbox'],
#                 item['clutch'],
#                 item['noofcylinders'],
#                 item['drivetype'],
#                 item['supplysystem'],
#                 item['transmissiontype'],
#                 item['tyresize'],
#                 item['tyretype'],
#                 item['wheelsize'],
#                 item['ebs'],
#                 item['tractioncontrol'],
#                 item['cruisecontrol'],
#                 item['navigation'],
#                 item['quickshifter'],
#                 item['launchcontrol'],
#                 item['powermodes'],
#                 item['adjustablewindscreen'],
#                 item['mobileconnectivity'],
#                 item['frontsuspension'],
#                 item['rearsuspension'],
#                 item['kerbweight'],
#                 item['wheelbase'],
#                 item['taillamp'],
#                 item['turnsignallamp'],
#                 item['passswitch'],
#             ))
#         self.conn.commit()
from itertools import count

#
# l = ['mileage', 'frontbrake', 'rearbrake', 'fuelcapacity', 'enginetype', 'displacement', 'bodytype', 'abs', 'headlamp', 'wheeltype', 'maximumpower', 'maximumtorque', 'starting', 'coolingsystem', 'gearbox', 'clutch', 'noofcylinders', 'drivetype', 'supplysystem', 'transmissiontype', 'tyresize', 'tyretype', 'wheelsize', 'ebs', 'tractioncontrol', 'cruisecontrol', 'navigation', 'quickshifter', 'launchcontrol', 'powermodes', 'adjustablewindscreen', 'mobileconnectivity', 'frontsuspension', 'rearsuspension', 'kerbweight', 'wheelbase', 'taillamp', 'turnsignallamp', 'passswitch']
#
# for i in l:
#     print("item["+"'"+i+"']," )

# company_list = ['hero-bikes', 'honda-bikes', 'royal-enfield-bikes', 'tvs-bikes', 'bajaj-bikes', 'yamaha-bikes',
#                 'suzuki-bikes']
# bike_removed =[]
# for i in company_list:
#     print('www.bikedekho.com/'+i)

l = ['/hero/splendor', '/hero/super-splendor', '/hero/hf-deluxe', '/hero/xpulse-200', '/hero/passion-pro',
     '/hero/xtreme-200-s', '/hero/glamour-2017', '/hero/xpulse-200t', '/hero/splendor-pro', '/hero/pleasure'
    , '/hero/passion-pro-110', '/hero/maestro-edge', '/hero/passion-xpro', '/hero/destini-125', '/hero/karizma-zmr',
     '/hero/duet', '/hero/xtreme-200s', '/hero/xtreme-sports', '/hero/splendor-ismart-110', '/hero/achiever',
     '/hero/hf-dawn', '/royal-enfield/classic-350', '/royal-enfield/bullet-350', '/royal-enfield/interceptor-650',
     '/royal-enfield/himalayan', '/royal-enfield/classic-500', '/royal-enfield/thunderbird-350x',
     '/royal-enfield/bullet-500', '/royal-enfield/thunderbird-350', '/royal-enfield/continental-gt-650',
     '/royal-enfield/thunderbird-500x', '/royal-enfield/thunderbird-500', '/honda/activa', '/honda/shine', '/honda/dio',
     '/honda/cb-hornet-160-r', '/honda/activa-125', '/honda/unicorn', '/honda/shine-sp', '/honda/activa-i',
     '/honda/livo', '/honda/cbr-250-r', '/honda/grazia', '/honda/unicorn-160', '/honda/xblade', '/honda/cd-110-dream',
     '/honda/dream-yuga', '/honda/navi', '/honda/cb300r', '/honda/aviator', '/honda/cbr650r', '/honda/gold-wing',
     '/honda/cbr-1000-rr', '/honda/cliq', '/honda/dream-neo', '/honda/crf-1000l-africa-twin', '/honda/cb1000r-plus',
     '/tvs/apache-160', '/tvs/apache', '/tvs/apache-rtr-200-4v', '/tvs/apache-rtr-180', '/tvs/akula-310',
     '/tvs/jupiter', '/tvs/ntorq-125', '/tvs/scooty', '/tvs/jupiter-grande', '/tvs/sport', '/tvs/xl-100', '/tvs/radeon',
     '/tvs/star-city-plus', '/tvs/scooty-zest', '/tvs/victor', '/tvs/wego', '/bajaj/bajaj-pulsar-200-ns',
     '/bajaj/pulsar-150', '/bajaj/pulsar-220', '/bajaj/pulsar-rs-200', '/bajaj/pulsar-180', '/bajaj/pulsar-150-ns',
     '/bajaj/pulsar-180f', '/bajaj/ct-100', '/bajaj/dominar-400', '/bajaj/avenger', '/bajaj/platina', '/bajaj/v',
     '/bajaj/avenger-cruise-220', '/bajaj/discover-125', '/bajaj/avenger-160', '/bajaj/discover-110',
     '/bajaj/avenger-street-180', '/bajaj/v12', '/yamaha/yzf-r15-v3', '/yamaha/mt-15', '/yamaha/fz-s',
     '/yamaha/fz-fi-version-3', '/yamaha/fz-250', '/yamaha/fz-fi', '/yamaha/fascino', '/yamaha/fz-s-fi-version-3',
     '/yamaha/sz-rr', '/yamaha/mt-09', '/yamaha/yzf-r3', '/yamaha/ray-zr', '/yamaha/fazer', '/yamaha/yzf-r15s',
     '/yamaha/fazer-250', '/yamaha/saluto', '/yamaha/ray', '/yamaha/saluto-rx', '/yamaha/yzf-r15-v3-moto-gp-edition',
     '/yamaha/yzf-r1', '/yamaha/alpha', '/suzuki/access-125', '/suzuki/hayabusa', '/suzuki/intruder-150',
     '/suzuki/gixxer', '/suzuki/burgman-street', '/suzuki/gixxer-sf', '/suzuki/gsx-s750', '/suzuki/v-strom-650',
     '/suzuki/dr-z50', '/suzuki/gsx-s1000', '/suzuki/gsx-r1000r', '/suzuki/v-storm', '/suzuki/rm-z250',
     '/suzuki/rm-z450']

new = []
for i in l:
  j=(i+'/specifications')
  new.append(j)

print(new)
