def getPreviousDateString(interval):
    if(interval == '1m'):
        return '1 minute ago UTC'
    if(interval == '5m'):
        return '4 hours ago UTC'
    if(interval == '15m'):
        return '12 hours ago UTC'
    if(interval == '1h'):
        return '2 days ago UTC'
    if(interval == '4h'):
        return '8 days ago UTC' 
    if(interval == '1d'):
        return '2 months ago UTC'