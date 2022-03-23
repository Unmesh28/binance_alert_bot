from ctypes import resize
from genericpath import exists
import pandas as pd
from datetime import datetime
import numpy as np
from getIndex import add_cuurent_to_previous, getIndexPreviousVal
from previous_msg_file import createNewFile
from sendTelegramMessage import send_message
import settings



def isSupport(df,i):
  support = df['Low'][i] < df['Low'][i-1]  and df['Low'][i] < df['Low'][i+1] and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]
  return support

def isResistance(df,i):
  resistance = df['High'][i] > df['High'][i-1]  and df['High'][i] > df['High'][i+1] and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2]
  return resistance

def isFarFromLevel(l, s, levels):
   return np.sum([abs(l-x) < s  for x in levels]) == 0


def support_resistance(df, ticker, candles, interval):
    print(ticker)
    startIndex = df.shape[0] - candles + 2
    df = df.iloc[-candles::]
    temp = df["Close"].astype(float)
    s =  np.mean(df['High'].astype(float) - df['Low'].astype(float))
    #print(df.shape)
    levels = []
    support_levels = []
    resistance_levels = []
    
    for i in range(startIndex, df.shape[0]-2):
        #print(df['Low'])
        if isSupport(df,i):
            l = float(df['Low'][i])
            if isFarFromLevel(l,s, levels):
                levels.append(l)
                support_levels.append(l)
        elif isResistance(df,i):
            l = float(df['High'][i])
            if isFarFromLevel(l, s, resistance_levels):
                levels.append(l)
                resistance_levels.append(l)
    print(support_levels)
    print(resistance_levels)
    previous_msg_file_name_support = "previous_msg_support.csv"
    file_exists1 = exists(previous_msg_file_name_support)
    print(file_exists1)
    if (file_exists1 == False) :
        createNewFile(previous_msg_file_name_support)    
    previous_msg_file_name_resistance = "previous_msg_resistance.csv"
    file_exists2 = exists(previous_msg_file_name_resistance)
    print(file_exists2)
    if (file_exists2 == False) :
        createNewFile(previous_msg_file_name_resistance)  

    index1, prevous_support = getIndexPreviousVal(interval, ticker, previous_msg_file_name_support)
    index2, prevous_resistance = getIndexPreviousVal(interval, ticker, previous_msg_file_name_resistance)
    current_support = 0
    current_resistance = 0
    #print(len(support_levels))
    if support_levels :
        #current_support = np.float64("{:.16g}".format(support_levels[len(support_levels) - 1]))
        support_levels.sort()
        for i in range(len(support_levels) - 1, 0) :
            if(support_levels[i] <= temp.iloc[-1]):
                current_support = np.float64("{:.16g}".format(support_levels[i]))
            else :
                current_support = prevous_support
    if resistance_levels :
        #current_resistance = current_support = np.float64("{:.16g}".format(resistance_levels[len(resistance_levels) - 1]))
        resistance_levels.sort()
        for i in range(0, len(resistance_levels)) :
            if(resistance_levels[i] >= temp.iloc[-1]):
                current_resistance = np.float64("{:.16g}".format(resistance_levels[i]))
            else :
                current_resistance = prevous_resistance

    print(support_levels)
    print(resistance_levels)
    
    if (current_support != prevous_support) :
        add_cuurent_to_previous(current_support, index1, interval, previous_msg_file_name_support)
        if(temp.iloc[-1] < current_support) :
            message = "Alert: Support Hit " +str(temp.iloc[-1]) + "\nSymbol :"+ticker+"\nInterval : "+interval + "\nSupport Levels : " + str(support_levels)
            for chat_id in settings.token_chatID_dict:
                send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])

    if (current_resistance != prevous_resistance) :
        add_cuurent_to_previous(current_resistance, index2, interval, previous_msg_file_name_resistance)
        if(temp.iloc[-1] > current_resistance) :
            message = "Alert: Resistance Hit at " +str(temp.iloc[-1]) + "\nSymbol :"+ticker+"\nInterval : "+interval + "\nResistance Levels : " + str(resistance_levels)
            for chat_id in settings.token_chatID_dict:
                send_message(chat_id, "sendMessage", message, settings.token_chatID_dict[chat_id])


        
    
    




    
