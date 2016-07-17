#coding=utf-8
import requests
import MySQLdb
import datetime
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
api = "http://127.0.0.1:5666/update"
query_date = "2016-07-17"
conn = MySQLdb.connect(host='192.168.156.120', user='data',passwd='PIN239!@#$%^&8', charset='utf8')
conn.select_db('report');
cursor = conn.cursor()

sql = """select hl_clk_conv, clk_conv, round(hl_clk_conv*1.0/clk_conv,2) as '注册红包占 比', round(hl_cost,2), round(cost,2), hl_imp, imp from \
(select order_id, C.name, sum(click_conversion) as hl_clk_conv, sum(adv_cost) as hl_cost, sum(imp) as hl_imp from rpt_effect_day A \
join optimus.creative B on A.creative_id=B.id \
join optimus.ad_order C on A.order_id=C.id \
where theme like '%红利%' and day='{day1}' and order_id=27904 \
GROUP BY order_id \
) A \
join \
(select order_id, C.name, sum(click_conversion) as clk_conv, sum(adv_cost) as cost, sum(imp) as imp from rpt_effect_day A \
join optimus.creative B on A.creative_id=B.id \
join optimus.ad_order C on A.order_id=C.id \
where day='{day2}' and order_id=27904 \
GROUP BY order_id \
) B \
on A.order_id=B.order_id"""

#cursor.execute(sql, (query_date, query_date))
cursor.execute(sql.format(day1=query_date, day2=query_date))
all_data = cursor.fetchall()
cursor.close()
conn.close()

col = ["红包转化数", "总转化数", "红包转化占比", "红包消耗", "总消耗", "红包曝光", "总曝光"]

uber_data = {}

if all_data:
    for rec in all_data:
        uber_data =  {"date": query_date,
                      "bonus_cvt": int(rec[0]),
                      "total_cvt": int(rec[1]),
                      "bonus_cost": float(rec[3]),
                      "total_cost": float(rec[4]),
                      "bonus_imp": int(rec[5]),
                      "total_imp": int(rec[6]) }

        for i in range(len(rec)):
            print col[i], rec[i]

print json.dumps(uber_data)

requests.post(api, data=uber_data)
