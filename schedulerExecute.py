from execute import execute
import schedule
import time
import datetime 

def job(t):
    #print("I'm working...", t)
    execute(t)
    print(datetime.datetime.now())
    return


schedule.every().day.at("1:00").do(job,'1h')
schedule.every().day.at("2:00").do(job,'1h')
schedule.every().day.at("3:00").do(job,'1h')
schedule.every().day.at("4:00").do(job,'1h')
schedule.every().day.at("5:00").do(job,'1h')
schedule.every().day.at("6:00").do(job,'1h')
schedule.every().day.at("7:00").do(job,'1h')
schedule.every().day.at("8:00").do(job,'1h')
schedule.every().day.at("9:00").do(job,'1h')
schedule.every().day.at("10:00").do(job,'1h')
schedule.every().day.at("11:00").do(job,'1h')
schedule.every().day.at("12:00").do(job,'1h')
schedule.every().day.at("13:00").do(job,'1h')
schedule.every().day.at("14:00").do(job,'1h')
schedule.every().day.at("15:00").do(job,'1h')
schedule.every().day.at("16:00").do(job,'1h')
schedule.every().day.at("17:00").do(job,'1h')
schedule.every().day.at("18:00").do(job,'1h')
schedule.every().day.at("19:00").do(job,'1h')
schedule.every().day.at("20:00").do(job,'1h')
schedule.every().day.at("21:00").do(job,'1h')
schedule.every().day.at("22:00").do(job,'1h')
schedule.every().day.at("23:00").do(job,'1h')
schedule.every().day.at("00:00").do(job,'1h')


schedule.every().day.at("1:00").do(job,'4h')
schedule.every().day.at("5:00").do(job,'4h')
schedule.every().day.at("9:00").do(job,'4h')
schedule.every().day.at("13:00").do(job,'4h')
schedule.every().day.at("17:00").do(job,'4h')
schedule.every().day.at("21:00").do(job,'4h')



while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
