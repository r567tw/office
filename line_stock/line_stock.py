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

stock = get_setting()
print('結果： ',stock)
