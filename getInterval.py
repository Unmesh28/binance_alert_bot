from binance import Client

def getInterval(interval):
    if(interval == '1m'):
        return Client.KLINE_INTERVAL_1MINUTE
    if(interval == '5m'):
        return Client.KLINE_INTERVAL_5MINUTE
    if(interval == '15m'):
        return Client.KLINE_INTERVAL_15MINUTE
    if(interval == '1h'):
        return Client.KLINE_INTERVAL_1HOUR
    if(interval == '4h'):
        return Client.KLINE_INTERVAL_4HOUR
    if(interval == '1d'):
        return Client.KLINE_INTERVAL_1DAY