from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return


schedule.every().day.at("01:00").do(job,'6h', 'bba')
schedule.every().day.at("07:00").do(job,'6h', 'bba')
schedule.every().day.at("13:00").do(job,'6h', 'bba')
schedule.every().day.at("19:00").do(job,'6h', 'bba')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
