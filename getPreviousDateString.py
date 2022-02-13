def getPreviousDateString(interval, candles):
    if(interval == '1m'):
        return '{} minutes ago UTC'.format(candles + 2)
    if(interval == '5m'):
        return '{} hours ago UTC'.format(int((candles / 12) + 1))
    if(interval == '15m'):
        return '{} hours ago UTC'.format(int((candles / 4) + 1))
    if(interval == '1h'):
        return '{} days ago UTC'.format(int((candles / 24) + 1))
    if(interval == '4h'):
        return '{} days ago UTC'.format(int((candles / 6) + 1))
    if(interval == '6h'):
        return '{} days ago UTC'.format(int((candles / 4) + 1))
    if(interval == '12h'):
        return '{} days ago UTC'.format(int((candles / 2) + 1))    
    if(interval == '1d'):
        return '{} months ago UTC'.format(int((candles / 31) + 1))

# print(getPreviousDateString('12h', 40))