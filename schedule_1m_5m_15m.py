from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return

schedule.every(1).minutes.do(job,'1m', 'fib')
schedule.every(1).minutes.do(job,'5m', 'fib')
schedule.every(1).minutes.do(job,'15m', 'fib')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
