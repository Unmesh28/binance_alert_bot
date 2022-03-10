import pandas as pd

def getIndexPreviousVal(interval, ticker, previous_msg_file_name) :
    print('inside get index value')
    df = pd.read_csv(previous_msg_file_name)
    #print(fib_df['tickerName'])
    exists = ticker in df['tickerName'].values
    dfb = 0
    #print(exists)
    if (exists == True):
        print('Inside If.....')
        dfb = next(iter(df[df['tickerName']==ticker].index), 'no match')
        #print(dfb[interval][dfb])
        #print(fib_df[interval][dfb])
        return (dfb, df[interval][dfb])
    else : 
        # data = {
        #     'tickerName' : [ticker],
        #     '1m' : [0.0],
        #     '5m' : [0.0],
        #     '15m' : [0.0],
        #     '1h' : [0.0],
        #     '4h' : [0.0],
        #     '6h' : [0.0],
        #     '12h' : [0.0],
        #     '1d' : [0.0],
        #     '1w' : [0.0],
        #     '1month' : [0.0]
        # }
        data = ticker+'\n'
        with open(previous_msg_file_name, 'a') as fp :
            fp.write(data)
        fp.close()
        # df = pd.DataFrame(data)
        # df.to_csv(previous_msg_file_name, mode = 'a')
        # dfb = next(iter(df[df['tickerName']==ticker].index), 'no match')
        return (dfb, 0)



def add_cuurent_to_previous(value, index, interval, previous_msg_file_name) :
    print('inside add value')
    #print(type(interval))
    fib_df = pd.read_csv(previous_msg_file_name)
    #fib_df[interval][index] = value
    fib_df.loc[index, interval] = value
    fib_df.to_csv(previous_msg_file_name, index=False, float_format='%.16g')
    # fib_df.to_csv(previous_msg_file_name, mode='a', index=False, header=False)
