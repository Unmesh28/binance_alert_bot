from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return


schedule.every().day.at("01:00").do(job,'4h', 'bba')
schedule.every().day.at("05:00").do(job,'4h', 'bba')
schedule.every().day.at("09:00").do(job,'4h', 'bba')
schedule.every().day.at("13:00").do(job,'4h', 'bba')
schedule.every().day.at("17:00").do(job,'4h', 'bba')
schedule.every().day.at("21:00").do(job,'4h', 'bba')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
