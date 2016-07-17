#coding=utf-8

import requests


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


requests.post("http://127.0.0.1:5666/update", data=uber_data[1])


