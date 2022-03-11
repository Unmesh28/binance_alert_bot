from execute import execute
import schedule
import time
import datetime 

def job(t, strategy):
    #print("I'm working...", t)
    execute(t, strategy)
    print(datetime.datetime.now())
    return


# schedule.every(1).minutes.do(job,'1m', 'fib')
# schedule.every(1).minutes.do(job,'5m', 'fib')
# schedule.every(1).minutes.do(job,'15m', 'fib')
# schedule.every(1).minutes.do(job,'1h', 'fib')
# schedule.every(1).minutes.do(job,'4h', 'fib')
# schedule.every(1).minutes.do(job,'6h', 'fib')
# schedule.every(1).minutes.do(job,'12h', 'fib')
# schedule.every(1).minutes.do(job,'1d', 'fib')

#schedule.every(1).minutes.do(job,'1m', 'sup_res')
schedule.every(1).minutes.do(job,'5m', 'sup_res')
schedule.every(1).minutes.do(job,'15m', 'sup_res')
schedule.every(1).minutes.do(job,'1h', 'sup_res')
schedule.every(1).minutes.do(job,'4h', 'sup_res')
schedule.every(1).minutes.do(job,'6h', 'sup_res')
schedule.every(1).minutes.do(job,'12h', 'sup_res')
schedule.every(1).minutes.do(job,'1d', 'sup_res')

# schedule.every().day.at("11:31").do(job,'1h', 'fib')
# schedule.every().day.at("01:00").do(job,'1h')
# schedule.every().day.at("02:00").do(job,'1h')
# schedule.every().day.at("03:00").do(job,'1h')
# schedule.every().day.at("04:00").do(job,'1h')
# schedule.every().day.at("05:00").do(job,'1h')
# schedule.every().day.at("06:00").do(job,'1h')
# schedule.every().day.at("07:00").do(job,'1h')
# schedule.every().day.at("08:00").do(job,'1h')
# schedule.every().day.at("09:00").do(job,'1h')
# schedule.every().day.at("10:00").do(job,'1h')
# schedule.every().day.at("11:00").do(job,'1h')
# schedule.every().day.at("12:00").do(job,'1h')
# schedule.every().day.at("13:00").do(job,'1h')
# schedule.every().day.at("14:00").do(job,'1h')
# schedule.every().day.at("15:00").do(job,'1h')
# schedule.every().day.at("16:00").do(job,'1h')
# schedule.every().day.at("17:00").do(job,'1h')
# schedule.every().day.at("18:00").do(job,'1h')
# schedule.every().day.at("19:00").do(job,'1h')
# schedule.every().day.at("20:00").do(job,'1h')
# schedule.every().day.at("21:00").do(job,'1h')
# schedule.every().day.at("22:00").do(job,'1h')
# schedule.every().day.at("23:00").do(job,'1h')
# schedule.every().day.at("00:00").do(job,'1h')


# schedule.every().day.at("01:00").do(job,'4h')
# schedule.every().day.at("05:00").do(job,'4h')
# schedule.every().day.at("09:00").do(job,'4h')
# schedule.every().day.at("13:00").do(job,'4h')
# schedule.every().day.at("17:00").do(job,'4h')
# schedule.every().day.at("21:00").do(job,'4h')



while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
