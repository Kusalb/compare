# -*- coding: utf-8 -*-
import scrapy
from soupsieve.util import lower

from ..items import MyprojectItem


class CompareSpider(scrapy.Spider):
    name = 'compare'
    first_url = 'hero/splendor/specifications'
    start_urls = ['https://www.bikedekho.com/hero/splendor/specifications']

    def parse(self, response):
        a_selectors = response.xpath("//h3//a")
        links = []
        for selector in a_selectors:
            link = selector.xpath("@href").extract_first()
            links.append(link)

        print(links)

        fields = ['mileage', 'frontbrake', 'fuelcapacity', 'rearbrake', 'enginetype', 'displacement', 'bodytype', 'abs',
                  'headlamp', 'wheeltype', 'enginetype', 'displacement', 'maximumpower', 'maximumtorque',
                  'coolingsystem', 'gearbox', 'clutch', 'noofcylinders', 'drivetype', 'supplysystem',
                  'transmissiontype', 'tyresize', 'tyretype', 'wheelsize', 'frontbrake', 'rearbrake', 'abs', 'ebs',
                  'tractioncontrol', 'cruisecontrol', 'navigation', 'quickshifter', 'launchcontrol', 'powermodes',
                  'adjustablewindscreen', 'mobileconnectivity', 'frontsuspension', 'rearsuspension', 'kerbweight',
                  'wheelbase', 'fuelcapacity', 'headlamp', 'taillamp', 'turnsignallamp', 'passswitch']
        items = MyprojectItem()
        data = response.css('.right').css('::text').extract()
        spec = response.css('td:nth-child(1)').css('::text').extract()
        specs = []
        for i in spec:
            j = i.replace(" ", "")
            j = j.replace(".", "")
            k = lower(j)
            specs.append(k)
        # j=0
        # for i in data:
        #     items[spec[j]]=i
        #     j+=1
        #
        # print(items)
        # items['data'] = data
        # items['specs'] = specs

        final = []
        for l in data:
            # new=dictionary.get(i)
            if (l == None or l == "-"):
                l = "N/A"
            final.append(l)
        dictionary = dict(zip(specs, final))
        yield dictionary

        all_bikes = ['/hero/splendor/specifications', '/hero/super-splendor/specifications', '/hero/hf-deluxe/specifications',
         '/hero/xpulse-200/specifications', '/hero/passion-pro/specifications', '/hero/xtreme-200-s/specifications',
         '/hero/glamour-2017/specifications', '/hero/xpulse-200t/specifications', '/hero/splendor-pro/specifications',
         '/hero/pleasure/specifications', '/hero/passion-pro-110/specifications', '/hero/maestro-edge/specifications',
         '/hero/passion-xpro/specifications', '/hero/destini-125/specifications', '/hero/karizma-zmr/specifications',
         '/hero/duet/specifications', '/hero/xtreme-200s/specifications', '/hero/xtreme-sports/specifications',
         '/hero/splendor-ismart-110/specifications', '/hero/achiever/specifications', '/hero/hf-dawn/specifications',
         '/royal-enfield/classic-350/specifications', '/royal-enfield/bullet-350/specifications',
         '/royal-enfield/interceptor-650/specifications', '/royal-enfield/himalayan/specifications',
         '/royal-enfield/classic-500/specifications', '/royal-enfield/thunderbird-350x/specifications',
         '/royal-enfield/bullet-500/specifications', '/royal-enfield/thunderbird-350/specifications',
         '/royal-enfield/continental-gt-650/specifications', '/royal-enfield/thunderbird-500x/specifications',
         '/royal-enfield/thunderbird-500/specifications', '/honda/activa/specifications', '/honda/shine/specifications',
         '/honda/dio/specifications', '/honda/cb-hornet-160-r/specifications', '/honda/activa-125/specifications',
         '/honda/unicorn/specifications', '/honda/shine-sp/specifications', '/honda/activa-i/specifications',
         '/honda/livo/specifications', '/honda/cbr-250-r/specifications', '/honda/grazia/specifications',
         '/honda/unicorn-160/specifications', '/honda/xblade/specifications', '/honda/cd-110-dream/specifications',
         '/honda/dream-yuga/specifications', '/honda/navi/specifications', '/honda/cb300r/specifications',
         '/honda/aviator/specifications', '/honda/cbr650r/specifications', '/honda/gold-wing/specifications',
         '/honda/cbr-1000-rr/specifications', '/honda/cliq/specifications', '/honda/dream-neo/specifications',
         '/honda/crf-1000l-africa-twin/specifications', '/honda/cb1000r-plus/specifications',
         '/tvs/apache-160/specifications', '/tvs/apache/specifications', '/tvs/apache-rtr-200-4v/specifications',
         '/tvs/apache-rtr-180/specifications', '/tvs/akula-310/specifications', '/tvs/jupiter/specifications',
         '/tvs/ntorq-125/specifications', '/tvs/scooty/specifications', '/tvs/jupiter-grande/specifications',
         '/tvs/sport/specifications', '/tvs/xl-100/specifications', '/tvs/radeon/specifications',
         '/tvs/star-city-plus/specifications', '/tvs/scooty-zest/specifications', '/tvs/victor/specifications',
         '/tvs/wego/specifications', '/bajaj/bajaj-pulsar-200-ns/specifications', '/bajaj/pulsar-150/specifications',
         '/bajaj/pulsar-220/specifications', '/bajaj/pulsar-rs-200/specifications', '/bajaj/pulsar-180/specifications',
         '/bajaj/pulsar-150-ns/specifications', '/bajaj/pulsar-180f/specifications', '/bajaj/ct-100/specifications',
         '/bajaj/dominar-400/specifications', '/bajaj/avenger/specifications', '/bajaj/platina/specifications',
         '/bajaj/v/specifications', '/bajaj/avenger-cruise-220/specifications', '/bajaj/discover-125/specifications',
         '/bajaj/avenger-160/specifications', '/bajaj/discover-110/specifications',
         '/bajaj/avenger-street-180/specifications', '/bajaj/v12/specifications', '/yamaha/yzf-r15-v3/specifications',
         '/yamaha/mt-15/specifications', '/yamaha/fz-s/specifications', '/yamaha/fz-fi-version-3/specifications',
         '/yamaha/fz-250/specifications', '/yamaha/fz-fi/specifications', '/yamaha/fascino/specifications',
         '/yamaha/fz-s-fi-version-3/specifications', '/yamaha/sz-rr/specifications', '/yamaha/mt-09/specifications',
         '/yamaha/yzf-r3/specifications', '/yamaha/ray-zr/specifications', '/yamaha/fazer/specifications',
         '/yamaha/yzf-r15s/specifications', '/yamaha/fazer-250/specifications', '/yamaha/saluto/specifications',
         '/yamaha/ray/specifications', '/yamaha/saluto-rx/specifications',
         '/yamaha/yzf-r15-v3-moto-gp-edition/specifications', '/yamaha/yzf-r1/specifications',
         '/yamaha/alpha/specifications', '/suzuki/access-125/specifications', '/suzuki/hayabusa/specifications',
         '/suzuki/intruder-150/specifications', '/suzuki/gixxer/specifications',
         '/suzuki/burgman-street/specifications', '/suzuki/gixxer-sf/specifications', '/suzuki/gsx-s750/specifications',
         '/suzuki/v-strom-650/specifications', '/suzuki/dr-z50/specifications', '/suzuki/gsx-s1000/specifications',
         '/suzuki/gsx-r1000r/specifications', '/suzuki/v-storm/specifications', '/suzuki/rm-z250/specifications',
         '/suzuki/rm-z450/specifications']

        for i in all_bikes:
            next_url = 'https://www.bikedekho.com' + i
            yield response.follow(next_url, callback=self.parse)


