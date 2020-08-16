# -*- coding: utf-8 -*-
# @Author  : Randy Pen
# @Email   : randy86@gmail.com

import logging
import yfinance as yf
from datetime import datetime, timedelta

logging.basicConfig(format='%(asctime)s %(levelname)s [%(module)s] %(message)s', level=logging.INFO)
log = logging.getLogger()


def stock(code="AAPL"):
    aapl = yf.Ticker(code)
    cominfo = aapl.history(period="1d",
                           interval="1d",
                           start="2020-08-11",
                           end="2020-08-15")
    print(cominfo)
    return 0


def daychange(code="AAPL", date="2020-08-14"):
    dt = datetime.strptime(date, "%Y-%m-%d")
    end = (dt + timedelta(days=1)).strftime("%Y-%m-%d")
    hist = yf.Ticker(code).history(period="1d", interval="1d", start=date, end=end)
    print(hist)
    print(hist["Close"])
    closes = hist["Close"].values.tolist()
    print(closes)
    assert len(closes) == 2
    assert closes[0] != 0
    return closes[1] / closes[0] - 1


def daychange4(code="AAPL", date="2020-08-14"):
    dt = datetime.strptime(date, "%Y-%m-%d")
    start = (dt - timedelta(days=3)).strftime("%Y-%m-%d")
    end = (dt + timedelta(days=1)).strftime("%Y-%m-%d")
    hist = yf.Ticker(code).history(period="1d", interval="1d", start=start, end=end)
    log.info("Till {} history of {} is \n{}".format(date, code, hist))
    # print(hist["Close"])
    closes = hist["Close"].values.tolist()
    # print(closes)
    assert len(closes) == 5
    # assert closes[0] != 0
    return [closes[i] / closes[i-1] - 1 for i, v in enumerate(closes) if i > 0]


def main():
    # stock()
    # code = "AAPL"
    # dt = "2020-08-14"
    # dc = daychange(code, dt)
    # print("%s %s 的涨跌是 %s" % (code, dt, dc))
    cls = daychange4()
    print(cls)
    return 0


if __name__ == '__main__':
    main()
