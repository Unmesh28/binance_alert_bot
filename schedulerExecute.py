from execute import execute
import schedule
import time
import datetime 

def job(t):
    #print("I'm working...", t)
    execute(t)
    print(datetime.datetime.now())
    return


schedule.every().day.at("10:35").do(job,'1h')
schedule.every().day.at("11:00").do(job,'1h')
schedule.every().day.at("11:30").do(job,'1h')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
