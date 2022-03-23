from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return


schedule.every(1).minutes.do(job,'1m', 'bba')
schedule.every(1).minutes.do(job,'5m', 'bba')
schedule.every(1).minutes.do(job,'15m', 'bba')
schedule.every(1).minutes.do(job,'1h', 'bba')
schedule.every(1).minutes.do(job,'4h', 'bba')
schedule.every(1).minutes.do(job,'6h', 'bba')
schedule.every(1).minutes.do(job,'12h', 'bba')
schedule.every(1).minutes.do(job,'1d', 'bba')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
