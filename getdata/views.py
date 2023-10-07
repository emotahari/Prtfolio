import json
import requests
import threading, time
from bs4 import BeautifulSoup
from django.http import HttpResponse
from timeloop import Timeloop
from datetime import timedelta
from getdata.models import Stocks, Price
from celery.schedules import crontab

tl = Timeloop()


def GetContent(request):
    data = []
    url = 'https://www.shakhesban.com/stocks/list-data?limit=1000&page=1&order_col=info.last_date&order_dir=desc&market=stock'
    content = requests.get(url)
    json1 = json.loads(content.text)
    message = json1['tbody']
    print(message)
    # data = content['tbody']
    soup = BeautifulSoup(message, "html.parser")
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        sahmName = tds[0]['data-val']
        content ={}
        objecti = {'sahmName': sahmName, 'content': content}
        for i in tds:
            dataVal = i['data-val']
            dataCol = i['data-col']
            content[dataCol]= dataVal

        data.append(objecti)
        row = Stocks.objects.create(source = url
        ,infoSymbol = objecti['content']['info.symbol']
        ,infoTitle = objecti['content']['info.title']
        ,infoMarket_fa = objecti['content']['info.market_fa']
        ,infoFlowTitle = objecti['content']['info.flow.title']
        ,infoLastTradePDrCotVal = objecti['content']['info.last_trade.PDrCotVal']
        ,infoLastTradeLastChange = objecti['content']['info.last_trade.last_change']
        ,infoLastTradeLastChangePercentage = objecti['content']['info.last_trade.last_change_percentage']
        ,infoLastPricePClosing = objecti['content']['info.last_price.PClosing']
        ,infoLastPriceClosingChange = objecti['content']['info.last_price.closing_change']
        ,infoLastPriceClosingChangePercentage = objecti['content']['info.last_price.closing_change_percentage']
        ,lastDate = objecti['content']['last_date']
        ,tradesZTotTran = objecti['content']['trades.ZTotTran']
        ,tradesQTotTran5J = objecti['content']['trades.QTotTran5J']
        ,tradesQTotCap = objecti['content']['trades.QTotCap']
        ,etcMotevasetHajmHarMoamele = objecti['content']['etc.motevaset_hajm_har_moamele']
        ,infoPriceYesterday = objecti['content']['info.PriceYesterday']
        ,infoPriceFirst = objecti['content']['info.PriceFirst']
        ,infoDayRangePriceMin = objecti['content']['info.day_range.PriceMin']
        ,infoDayRangePriceMax = objecti['content']['info.day_range.PriceMax']
        ,demands1_1 = objecti['content']['demands.1_1']
        ,demands1_0 = objecti['content']['demands.1_0']
        ,demands1_2 = objecti['content']['demands.1_2']
        ,demands1_4 = objecti['content']['demands.1_4']
        ,demands1_5 = objecti['content']['demands.1_5']
        ,demands1_3 = objecti['content']['demands.1_3']
        ,tradesArzeshBazar = objecti['content']['trades.arzesh_bazar']
        ,etcArzeshRoozDarayi = objecti['content']['etc.arzesh_rooz_darayi']
        ,etcArzeshDaftariDarayi = objecti['content']['etc.akharin_sarmaye']
        ,etcAkharinSarmaye = objecti['content']['etc.arzesh_daftari_darayi']
        ,etcBedehi = objecti['content']['etc.bedehi']
        ,etcHoghoghSahebanSaham = objecti['content']['etc.hoghogh_saheban_saham']
        ,etcPishbiniDaramad = objecti['content']['etc.pishbini_daramad']
        ,etcSoodKhalesTtm = objecti['content']['etc.sood_khales_ttm']
        ,infoPe = objecti['content']['info.pe']
        ,infoPb = objecti['content']['info.pb']
        ,infoPs = objecti['content']['info.ps']
        ,tradesBuyAndSellBuyIVolume = objecti['content']['trades.buy_and_sell.Buy_I_Volume']
        ,tradesBuyAndsellBuy_NVolume = objecti['content']['trades.buy_and_sell.Buy_N_Volume']
        ,tradesBuyAndSellSellIVolume = objecti['content']['trades.buy_and_sell.Sell_I_Volume']
        ,tradesBuyAndSellSellNVolume = objecti['content']['trades.buy_and_sell.Sell_N_Volume'])
    return HttpResponse(message)

# ticker = threading.Event()
# while not ticker.wait(wait_time):
#     GetContent()

#
# while True:
#   GetContent()
#   time.sleep(60)

def GetGold(request):
    url = 'https://call2.tgju.org/ajax.json?rev=fgO31kgQ8Wzfn4cj8u0XV1aU4Vw6hXY1oexDqeJrzcD58XNLCNKwfiqBndJ3'
    content = requests.get(url)
    json1 = json.loads(content.text)
    data = json1['current']
    for i in data:
        row = data[i]
        object = Price.objects.create(name = i
                                    ,d = row['d']
                                    ,dp = row['dp']
                                    ,dt = row['dt']
                                    ,h = row['h']
                                    ,l = row['l']
                                    ,p = row['p']
                                    ,t = row['t']
                                    ,tg = row['t-g']
                                    ,ten = row['t_en']
                                    ,ts = row['ts'])
        # print(object)
    return HttpResponse(data)


def CalculatePrice(ind):
    if ind == 'p' :
        nimPrice = Price.objects.filter(name='nim')
        print(nimPrice)
        return  nimPrice

def ShowPrice(request):
    nim = CalculatePrice('p')
    return HttpResponse(nim)


def DoGetContent():
    data = []
    url = 'https://www.shakhesban.com/stocks/list-data?limit=1000&page=1&order_col=info.last_date&order_dir=desc&market=stock'
    content = requests.get(url)
    json1 = json.loads(content.text)
    message = json1['tbody']
    print(message)
    # data = content['tbody']
    soup = BeautifulSoup(message, "html.parser")
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        sahmName = tds[0]['data-val']
        content ={}
        objecti = {'sahmName': sahmName, 'content': content}
        for i in tds:
            dataVal = i['data-val']
            dataCol = i['data-col']
            content[dataCol]= dataVal

        data.append(objecti)
        row = Stocks.objects.create(source = url
        ,infoSymbol = objecti['content']['info.symbol']
        ,infoTitle = objecti['content']['info.title']
        ,infoMarket_fa = objecti['content']['info.market_fa']
        ,infoFlowTitle = objecti['content']['info.flow.title']
        ,infoLastTradePDrCotVal = objecti['content']['info.last_trade.PDrCotVal']
        ,infoLastTradeLastChange = objecti['content']['info.last_trade.last_change']
        ,infoLastTradeLastChangePercentage = objecti['content']['info.last_trade.last_change_percentage']
        ,infoLastPricePClosing = objecti['content']['info.last_price.PClosing']
        ,infoLastPriceClosingChange = objecti['content']['info.last_price.closing_change']
        ,infoLastPriceClosingChangePercentage = objecti['content']['info.last_price.closing_change_percentage']
        ,lastDate = objecti['content']['last_date']
        ,tradesZTotTran = objecti['content']['trades.ZTotTran']
        ,tradesQTotTran5J = objecti['content']['trades.QTotTran5J']
        ,tradesQTotCap = objecti['content']['trades.QTotCap']
        ,etcMotevasetHajmHarMoamele = objecti['content']['etc.motevaset_hajm_har_moamele']
        ,infoPriceYesterday = objecti['content']['info.PriceYesterday']
        ,infoPriceFirst = objecti['content']['info.PriceFirst']
        ,infoDayRangePriceMin = objecti['content']['info.day_range.PriceMin']
        ,infoDayRangePriceMax = objecti['content']['info.day_range.PriceMax']
        ,demands1_1 = objecti['content']['demands.1_1']
        ,demands1_0 = objecti['content']['demands.1_0']
        ,demands1_2 = objecti['content']['demands.1_2']
        ,demands1_4 = objecti['content']['demands.1_4']
        ,demands1_5 = objecti['content']['demands.1_5']
        ,demands1_3 = objecti['content']['demands.1_3']
        ,tradesArzeshBazar = objecti['content']['trades.arzesh_bazar']
        ,etcArzeshRoozDarayi = objecti['content']['etc.arzesh_rooz_darayi']
        ,etcArzeshDaftariDarayi = objecti['content']['etc.akharin_sarmaye']
        ,etcAkharinSarmaye = objecti['content']['etc.arzesh_daftari_darayi']
        ,etcBedehi = objecti['content']['etc.bedehi']
        ,etcHoghoghSahebanSaham = objecti['content']['etc.hoghogh_saheban_saham']
        ,etcPishbiniDaramad = objecti['content']['etc.pishbini_daramad']
        ,etcSoodKhalesTtm = objecti['content']['etc.sood_khales_ttm']
        ,infoPe = objecti['content']['info.pe']
        ,infoPb = objecti['content']['info.pb']
        ,infoPs = objecti['content']['info.ps']
        ,tradesBuyAndSellBuyIVolume = objecti['content']['trades.buy_and_sell.Buy_I_Volume']
        ,tradesBuyAndsellBuy_NVolume = objecti['content']['trades.buy_and_sell.Buy_N_Volume']
        ,tradesBuyAndSellSellIVolume = objecti['content']['trades.buy_and_sell.Sell_I_Volume']
        ,tradesBuyAndSellSellNVolume = objecti['content']['trades.buy_and_sell.Sell_N_Volume'])
    return message
def DoGetGold():
    url = 'https://call2.tgju.org/ajax.json?rev=fgO31kgQ8Wzfn4cj8u0XV1aU4Vw6hXY1oexDqeJrzcD58XNLCNKwfiqBndJ3'
    content = requests.get(url)
    json1 = json.loads(content.text)
    data = json1['current']
    for i in data:
        row = data[i]
        object = Price.objects.create(name = i
                                    ,d = row['d']
                                    ,dp = row['dp']
                                    ,dt = row['dt']
                                    ,h = row['h']
                                    ,l = row['l']
                                    ,p = row['p']
                                    ,t = row['t']
                                    ,tg = row['t-g']
                                    ,ten = row['t_en']
                                    ,ts = row['ts'])
        # print(object)
    return data
while True:
  DoGetContent()
  DoGetGold()
  time.sleep(43200)

