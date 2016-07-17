# coding=utf8
import os
from flask import render_template, redirect, flash
from flask import send_from_directory, request, Response
from jinja2 import Environment, FileSystemLoader, environment
from app import app
from utils import myutils
from forms import RegistrationForm
import json

def get_series(key, uber_data, den=None):
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


@app.route('/update',  methods=['GET', 'POST'])
def update():

    stat_data_path = "data/daily_stat_data"
    stat_data = myutils.parse_json_conf(stat_data_path)
    
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        form_data = {"date":form.date.data,
                    "bonus_cvt": form.bonus_cvt.data,
                    "total_cvt": form.total_cvt.data,
                    "bonus_cost": form.bonus_cost.data,
                    "total_cost": form.total_cost.data,
                    "bonus_imp": form.bonus_imp.data,
                    "total_imp": form.total_imp.data}

        if not stat_data or stat_data[-1]['date'] != form_data['date']:
            stat_data.append(form_data)

        else:
            stat_data[-1]["bonus_cvt"] = form_data['bonus_cvt']
            stat_data[-1]["total_cvt"] = form_data['total_cvt']
            stat_data[-1]["bonus_cost"] = form_data['bonus_cost']
            stat_data[-1]["total_cost"] = form_data['total_cost']
            stat_data[-1]["bonus_imp"] = form_data['bonus_imp']
            stat_data[-1]["total_imp"] = form_data['total_imp']


        myutils.update_conf(stat_data, stat_data_path)
        return json.dumps(form_data), 200

    return render_template('update.html', form=form)



@app.route('/')
def index():
    print "goto index route"
    uber_data = myutils.parse_json_conf("data/daily_stat_data")
    print "reloading uberdata"
    return render_template('index.html',
                           data=uber_data,
                           bonus_cost_series=get_series("bonus_cost", uber_data),
                           total_cost_series=get_series("total_cost", uber_data),
                           bonus_cvt_series=get_series("bonus_cvt", uber_data),
                           total_cvt_series=get_series("total_cvt", uber_data),
                           bonus_imp_series=get_series("bonus_imp", uber_data),
                           total_imp_series=get_series("total_imp", uber_data),
     )


