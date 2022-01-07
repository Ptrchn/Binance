#binancecheak.py

from binance.client import Client
import time
from songline import Sendline



token = '----------your-token---------------'
messenger = Sendline(token)

line_condition = True

api_key = '----------------your-api-------------------------'
api_secret = '----------------your-api-----------------------'
client = Client(api_key, api_secret)
mycoin1 = ['BTCBUSD']
namecoin1 = ['BTC']
mycoin2 = ['ETHBUSD']
namecoin2 = ['ETH']
mycoin3 = ['BNBBUSD']
namecoin3 = ['BNB']
mycoin4 = ['SLPBUSD']
namecoin4 = ['SLP']


condition = {'BTCBUSD':{'buy':1,'sell':1000000},
             'ETHBUSD':{'buy':120000,'sell':130000},
             'SLPBUSD':{'buy':0.8,'sell':1},
             'BNBBUSD':{'buy':16000,'sell':18000},}

#print(condition['BTCBUSD'])

def CheckCondition(coin,price):

    text = ''
    check_buy = condition[coin]['buy']
    if price <= check_buy:
        txt = '\n{} ราคาลงแล้ว เหลือ: {:,.2f} บาท ระวังตกรถ!!!\n(ราคาที่อยากได้: {:,.2f} บาท)\n'.format(coin,price,check_buy)
        #print(txt)
        text += txt + '\n'
    check_sell = condition[coin]['sell']
    if price >= check_sell:
        txt = '\n{} ราคาขึ้นแล้ว ราคาล่าสุด: {:,.2f} บาท รีบขายด่วน!!!\n(ราคาที่อยากได้: {:,.2f}) บาท\n'.format(coin,price,check_sell)
        #print(txt)
        text += txt
        
    return text




current_text = ''



def CheckPrice():
        global current_text
        #while True:
        prices = client.get_all_tickers()

        alltext = ''
        text_line = ''
                
        for p in prices:
            for c in mycoin1:
                sym = c
                if p['symbol'] == sym:
                    pc = float(p['price'])
                    rate = 33.20
                    cal = pc * rate
                    for n in namecoin1:
                        #print('เหรียญ: {} ราคา: {:,.8f} บาท'.format(sym,cal))
                        #print('ราคา USD: {}'.format(pc))
                        text = '{} ราคา : {:,.2f} บาท'.format(n,cal)
                        alltext += text + '\n'
                        if line_condition == True:
                            if c in condition:
                                checktext = CheckCondition(c,cal)
                                if len(checktext) > 0:
                                    text_line += checktext


        for p in prices:
            for c in mycoin2:
                sym = c
                if p['symbol'] == sym:
                    pc = float(p['price'])
                    rate = 33.20
                    cal = pc * rate
                    for n in namecoin2:
                         #print('เหรียญ: {} ราคา: {:,.8f} บาท'.format(sym,cal))
                         #print('ราคา USD: {}'.format(pc))
                         text = '{} ราคา : {:,.2f} บาท'.format(n,cal)
                         alltext += text + '\n'
                         if line_condition == True:
                               if c in condition:
                                    checktext = CheckCondition(c,cal)
                                    if len(checktext) > 0:
                                          text_line += checktext

        for p in prices:
            for c in mycoin3:
                sym = c
                if p['symbol'] == sym:
                    pc = float(p['price'])
                    rate = 33.20
                    cal = pc * rate
                    for n in namecoin3:
                         #print('เหรียญ: {} ราคา: {:,.8f} บาท'.format(sym,cal))
                         #print('ราคา USD: {}'.format(pc))
                         text = '{} ราคา : {:,.2f} บาท'.format(n,cal)
                         alltext += text + '\n'
                         if line_condition == True:
                               if c in condition:
                                     checktext = CheckCondition(c,cal)
                                     if len(checktext) > 0:
                                          text_line += checktext

        for p in prices:
            for c in mycoin4:
                sym = c
                if p['symbol'] == sym:
                    pc = float(p['price'])
                    rate = 33.20
                    cal = pc * rate
                    for n in namecoin4:
                         #print('เหรียญ: {} ราคา: {:,.8f} บาท'.format(sym,cal))
                         #print('ราคา USD: {}'.format(pc))
                         text = '{} ราคา : {:,.2f} บาท'.format(n,cal)
                         alltext += text + '\n'
                         if line_condition == True:
                               if c in condition:
                                    checktext = CheckCondition(c,cal)
                                    if len(checktext) > 0:
                                          text_line += checktext


            
                                    
                                
                                
        if line_condition == True and current_text != text_line:
            print('Condition: ',text_line)
            current_text = text_line
            messenger.sendtext(text_line)
            


        v_result.set(alltext)
        print('-------------')
        R1.after(100000,CheckPrice)

def CheckCoin():

     coin = Box.get()
     COIN = coin.upper()
     COINUSDT = COIN + 'USDT'
     Tcoin = [COINUSDT]

#     Tcoin = COINUSDT.text

     prices = client.get_all_tickers()

     alltext2 = ''

     for p in prices:
          for c in Tcoin:
             sym = c
             if p['symbol'] == sym:
                 pc = float(p['price'])
                 rate = 33.20
                 cal = pc*rate
                 N = COIN
                 print('เหรียญ: {} ราคา: {:,.2f} บาท'.format(N,cal))
                 text2 = 'เหรียญ {} ราคา {:,.2f} บาท'.format(N,cal)
                
     v2_result.set(text2)
                
    

                  
                
##############################GUI####################################

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมเช็คราคาจาก Binance')

FONT1 = ('Angsana New' , 25)

L1 = ttk.Label(text='ราคา Binance ล่าสุด',font=FONT1)
L1.pack()

#B1 = ttk.Button(GUI,text='Check!',command=CheckaPrice)
#B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('------------------------')
R1 = ttk.Label(textvariable=v_result,font=FONT1)
R1.pack()

CheckPrice()

L1 = ttk.Label(text='ราคาเหรียญที่ต้องการ',font=FONT1)
L1.pack()

Box = ttk.Entry(GUI)
Box.pack(ipadx = 60,ipady = 10)

B2 = ttk.Button(GUI,text='Check!',command=CheckCoin)
B2.pack(ipadx=20,ipady=10)

v2_result = StringVar()
v2_result.set('------------------------')
R2 = ttk.Label(textvariable =v2_result,font=FONT1)
R2.pack()

GUI .mainloop()






























                
