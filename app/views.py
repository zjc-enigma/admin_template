# coding=utf8
import os
from flask import render_template, redirect
from flask import send_from_directory, request, Response
from jinja2 import Environment, FileSystemLoader, environment
from app import app


uber_data = [

                 {
    "date" : "2016-07-12",
    "bonus_cvt": 113,
    "total_cvt": 407,
    "bonus_cost": 7000000,
    "total_cost": 10000000,
    "bonus_imp" : 783800,
    "total_imp": 6040867
             },

                 {
    "date" : "2016-07-13",
    "bonus_cvt": 113,
    "total_cvt": 407,
    "bonus_cost": 2000000,
    "total_cost": 50000000,
    "bonus_imp" : 783800,
    "total_imp": 6040867

                 },

             {
    "date" : "2016-07-14",
    "bonus_cvt": 113,
    "total_cvt": 407,
    "bonus_cost": 7200000,
    "total_cost": 15000000,
    "bonus_imp" : 783800,
    "total_imp": 6040867
             },
    {
    "date" : "2016-07-15",
    "bonus_cvt": 1137,
    "total_cvt": 4007,
    "bonus_cost": 7900000,
    "total_cost": 10000001,
    "bonus_imp" : 7183800,
    "total_imp": 60340867
},
             {
    "date" : "2016-07-16",
    "bonus_cvt": 113,
    "total_cvt": 400,
    "bonus_cost": 2200000,
    "total_cost": 930000,
    "bonus_imp" : 713800,
    "total_imp": 600867
}
]

def get_series(key, den=None):
    template = "[gd({year}, {month}, {day}), {amount}]"
    series_list = []
    sum_amount = 0

    for item in uber_data:

        date_array = item['date'].split('-')
        year = date_array[0]
        month = date_array[1]
        day = date_array[2]
        amount = item[key]
        sum_amount += item[key]
        series_list.append(template.format(year=year,
                                           month=month,
                                           day=day,
                                           amount=amount))

    return {"sum":sum_amount, "string":"[" + ",".join(series_list) + "];"}


@app.route('/')
def index():
    return render_template('index.html',
                           data=uber_data,
                           bonus_cost_series=get_series("bonus_cost"),
                           total_cost_series=get_series("total_cost"),
                           bonus_cvt_series=get_series("bonus_cvt"),
                           total_cvt_series=get_series("total_cvt"),
                          bonus_imp_series=get_series("bonus_imp"),
                           total_imp_series=get_series("total_imp"),
     )


