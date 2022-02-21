from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return

schedule.every(1).minutes.do(job,'12h', 'fib')
schedule.every(1).minutes.do(job,'1d', 'fib')
# schedule.every().day.at("01:00").do(job,'12h', 'fib')
# schedule.every().day.at("13:00").do(job,'12h', 'fib')

# schedule.every().day.at("01:00").do(job,'1d', 'fib')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
