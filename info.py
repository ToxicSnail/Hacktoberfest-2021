import requests
import time
from bs4 import BeautifulSoup


price = 0
array_price = []


val = input('Введите монету для совета\n')
if val == 'hot':
    url = "https://www.binance.com/api/v1/depth?symbol=" + val.upper() + "ETH"
elif val == 'eth':
    url = "https://www.binance.com/api/v3/ticker/price?symbol=" + val.upper() + "USDT"
else:
    url = "https://www.binance.com/api/v3/ticker/price?symbol=" + val.upper() + "USDT"

price_old = 0
inc = 1

print("Подождите примерно 1 минуту, пока алгоритм высчитывает зависимость")

while True:
    while len(array_price) != 6:
        response = requests.get(url)
        soup = str(BeautifulSoup(response.text, "html.parser"))
        # print(soup[29:36])
        time.sleep(0.1)
        price = float(soup[29:36])
        array_price.append(price)
        if price > price_old:
            print(inc, '. ', price, '  ', '↑')
        elif price == price_old:
            print(inc, '. ', price, '  ', '→')
        else:
            print(inc, '. ', price, '  ', '↓')
        price_old = price
        time.sleep(5)
        inc += 1
    delta_price = array_price[-1] - (max(array_price) + min(array_price)) / 2
    if delta_price > 0:
        print('--------------------------')
        print('Aboba выросла на', str(delta_price) + "$")
        break
    elif (delta_price < 0):
        print('--------------------------')
        print('Aboba упала на', str(delta_price) + "$")
        break
    else:
        print('--------------------------')
        print('Aboba осталась той же Абобой')
        break
