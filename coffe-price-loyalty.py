import urllib.request
import time

price = 7
while price >= 4.74:
    site = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = site.read() .decode('utf-8')
    w = text.find('>$')
    begin = w + 2
    end = w + 6
    price = float(text[begin:end])
    if price < 4.74:
        time.sleep(10)
        print(price)


# Just to know
# print(len(text))
