import twstock
import requests
import time


def get_setting():
    res = []
    try:
        with open("stock.txt") as f:
            data = f.readlines()
            # print('讀入: ',data)
            data.remove("股票代號, 期望買進價格 , 期望賣出價格\n")
            for line in data:
                stock = line.split(",")
                res.append([stock[0].strip(), float(stock[1]), float(stock[2])])
    except:
        print("stock.txt 讀取錯誤")
    return res


# 讀取股票的名稱和股價
def get_price(stockid):
    stock = twstock.realtime.get(stockid)
    if stock["success"]:
        return (stock["info"]["name"], float(stock["realtime"]["latest_trade_price"]))
    else:
        return (False, False)


# 是否符合四大買賣點
def get_four_best(stockid):
    stock = twstock.Stock(stockid)
    best = twstock.BestFourPoint(stock).best_four_point()
    if best:
        if best[0]:
            info = "買進"
        else:
            info = "賣出"
        return (info, best[1])
    else:
        return (False, False)


def send_ifttt(v1, v2, v3):
    url = (
        "https://maker.ifttt.com/trigger/toline/with/key/b2QX3cOUM5Mre5xpxE7R3-?value1="
        + str(v1)
        + "&value2="
        + str(v2)
        + "&value3="
        + str(v3)
    )
    res = requests.get(url)
    if res.text[:5] == "Congr":
        print("股票" + str(v1) + "判斷已傳送資料給line")
    return res.text


stocks = get_setting()
# print('結果： ',stock)

for stock in stocks:
    id, low, high = stock
    name, price = get_price(id)
    message = ""
    if price <= low:
        message += "買進(股票低於自己設定的" + str(low) + "元)\n"
    elif price >= high:
        message += "賣出(股票高於自己設定的" + str(high) + "元)\n"

    act, why = get_four_best(id)
    message += "[四大買賣點判斷]" + act + why

    send_ifttt(name, price, message)
    print("請等個10秒鐘，不然這支程式會被證交所ban掉嗚嗚嗚！")
    time.sleep(10)
