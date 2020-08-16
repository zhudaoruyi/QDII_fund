# -*- coding: utf-8 -*-
# @Author  : Randy Pen
# @Email   : randy86@gmail.com


import codecs
import logging
from finance import daychange4
from flask import Flask, jsonify, render_template

logging.basicConfig(format='%(asctime)s %(levelname)s [%(module)s] %(message)s', level=logging.INFO)
log = logging.getLogger()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/books", methods=["GET"])
def books():
    return jsonify([{"author": "Eason", "id": "01", "price": 39, "title": "Hoe"},
                    {"author": "Trump", "id": "02", "price": 99, "title": "County"},
                    {"author": "Aositing", "id": "03", "price": 129, "title": "aabd"},
                    {"author": "Jasan", "id": "04", "price": 39, "title": "should"}])


@app.route("/date", methods=["GET"])
def dt():
    # return jsonify([{"day01": "2020-08-11", "day02": "2020-08-12", "day03": "2020-08-13", "day04": "2020-08-14"}])
    return jsonify(["2020-08-11", "2020-08-12", "2020-08-13", "2020-08-14"])


@app.route("/fund_code/160416", methods=["GET"])
def fetch_data():
    data = []
    total_percent = 0
    with codecs.open("160416.txt", "r", encoding="utf-8") as fr:
        cons = fr.read()
        cons = cons.splitlines()
    for i, line in enumerate(cons):
        li = line.split(",")
        lin = {"id": i+1, "code": li[0], "name": li[1], "percent": li[2], "weights": 0}
        data.append(lin)
        total_percent += float(li[2])
    data1 = []
    for da in data:
        lin = da
        lin["weights"] = "%.3f" % (float(da["percent"]) * 100 / total_percent)
        try:
            # cls = daychange4(da["code"], "2020-08-14")
            cls = ["0", "0", "0", "0"]
        except Exception as e:
            cls = ["0", "0", "0", "0"]
            pass
        lin["day01"] = "%.3f" % (float(cls[0]) * 100)
        lin["day02"] = "%.3f" % (float(cls[1]) * 100)
        lin["day03"] = "%.3f" % (float(cls[2]) * 100)
        lin["day04"] = "%.3f" % (float(cls[3]) * 100)
        data1.append(lin)
    return jsonify(data1)


@app.route("/fund_code/164906", methods=["GET"])
def fetch_data1():
    data = []
    total_percent = 0
    with codecs.open("164906.txt", "r", encoding="utf-8") as fr:
        cons = fr.read()
        cons = cons.splitlines()
    for i, line in enumerate(cons):
        li = line.split(",")
        lin = {"id": i+1, "code": li[0], "name": li[1], "percent": li[2], "weights": 0}
        data.append(lin)
        total_percent += float(li[2])
    data1 = []
    for da in data:
        lin = da
        lin["weights"] = "%.3f" % (float(da["percent"]) * 100 / total_percent)
        try:
            cls = daychange4(da["code"], "2020-08-14")
            # cls = ["0", "0", "0", "0"]
        except Exception as e:
            cls = ["0", "0", "0", "0"]
            pass
        lin["day01"] = "%.3f" % (float(cls[0]) * 100)
        lin["day02"] = "%.3f" % (float(cls[1]) * 100)
        lin["day03"] = "%.3f" % (float(cls[2]) * 100)
        lin["day04"] = "%.3f" % (float(cls[3]) * 100)
        data1.append(lin)
    return jsonify(data1)


@app.route("/fund_code/513050", methods=["GET"])
def fetch_data2():
    data = []
    total_percent = 0
    with codecs.open("513050.txt", "r", encoding="utf-8") as fr:
        cons = fr.read()
        cons = cons.splitlines()
    for i, line in enumerate(cons):
        li = line.split(",")
        lin = {"id": i+1, "code": li[0], "name": li[1], "percent": li[2], "weights": 0}
        data.append(lin)
        total_percent += float(li[2])
    data1 = []
    for da in data:
        lin = da
        lin["weights"] = "%.3f" % (float(da["percent"]) * 100 / total_percent)
        try:
            cls = daychange4(da["code"], "2020-08-14")
            # cls = ["0", "0", "0", "0"]
        except Exception as e:
            cls = ["0", "0", "0", "0"]
            pass
        lin["day01"] = "%.3f" % (float(cls[0]) * 100)
        lin["day02"] = "%.3f" % (float(cls[1]) * 100)
        lin["day03"] = "%.3f" % (float(cls[2]) * 100)
        lin["day04"] = "%.3f" % (float(cls[3]) * 100)
        data1.append(lin)
    return jsonify(data1)


if __name__ == '__main__':
    app.run("0.0.0.0", "5000")
