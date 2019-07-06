import twstock

def get_setting():
    res = []
    try:
        with open('stock.txt') as f:
            data = f.readlines()
            print('讀入: ',data)
            data.remove('股票代號, 期望買進價格 , 期望賣出價格 ,股票名稱\n')
            for line in data:
                stock = line.split(',')
                res.append([stock[0].strip(), float(stock[1]), float(stock[2])])
    except:
        print('stock.txt 讀取錯誤')
    return res

#讀取股票的名稱和股價
def get_price(stockid):
    stock = twstock.realtime.get(stockid)
    if stock['success']:
        return (stock['info']['name'], float(stock['realtime']['latest_trade_price']))
    else:
        return (False, False)

#是否符合四大買賣點
def get_best(stockid):
    stock = twstock.Stock(stockid)
    best = twstock.BestFourPoint(stock).best_four_point()
    if(best):
        return ('買進' if best[0] else '賣出',best[1])
    else:
        return (False, False)

def send_ifttt(v1,v2,v3):
    url = ('https://maker.ifttt.com/trigger/toline/with/key/b2QX3cOUM5Mre5xpxE7R3-?value1='+str(v1)+'&value2='+str(v2)+'&value3='+str(v3))
    res = requests.get(url)
    if res[:5] == 'Congr':
        print('已傳送資料給line')
    return r.text

stocks = get_setting()
# print('結果： ',stock)

for stock in stocks:
    print(stock)
