import pandas as pd
from datetime import datetime


def support(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l-n1+1, l+1):
        if(df1.Low[i]>df1.Low[i-1]):
            return 0
    for i in range(l+1,l+n2+1):
        if(df1.Low[i]<df1.Low[i-1]):
            return 0
    return 1

#support(df,46,3,2)

def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l-n1+1, l+1):
        if(df1.High[i]<df1.High[i-1]):
            return 0
    for i in range(l+1,l+n2+1):
        if(df1.High[i]>df1.High[i-1]):
            return 0
    return 1
#resistance(df, 30, 3, 5)

def support_resistance(df, ticker, candles):
    print(ticker)
    sr = []
    rs = []
    n1=2
    n2=2
    for row in range(3, len(df) - n2): #len(df)-n2
        if support(df, row, n1, n2):
            sr.append([row,df.Low[row]])
        if resistance(df, row, n1, n2):
            rs.append([row,df.High[row]])
    print(sr)
    print(rs)
    temp = df["Close"].astype(float)

    for suppor in sr :
        print(suppor)
    # if temp.iloc[-1] 
