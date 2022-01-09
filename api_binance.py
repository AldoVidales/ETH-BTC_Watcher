

  
 #This example uses Python 2.7 and the python-request library.

from os import close
import  os
from requests import Request, Session
import json
import requests
import pprint
from tkinter import  Button, Label, Tk,PhotoImage
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

#enviroment variables
from requests.sessions import session

url = os.getenv("url")

def priceBTC(url):
    API_KEY=os.getenv("API_KEY") 
    parameters = {
    'slug':'bitcoin',
    'convert':'USD'
    }
    headers={
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':f'{API_KEY}'
    }
    session=Session()
    session.headers.update(headers)

    response=session.get(url,params=parameters)
    #pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    BTC_price=str(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    return BTC_price

def priceETH(url):
    parameters = {
    'slug':'ethereum',
    'convert':'USD'
    }
    headers={
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'4bad95b8-4c48-43c2-b67b-13ab49d89276'
    }
    session=Session()
    session.headers.update(headers)

    response=session.get(url,params=parameters)
    #pprint.pprint(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
    ETH_price=str(json.loads(response.text)['data']['1027']['quote']['USD']['price'])
    return ETH_price


ETH_price=priceETH(url)
BTC_price=priceBTC(url)


    
class main:

    root=Tk()
    root.title("Lector de precio de crypto")
    root.geometry("500x700")
    root.resizable(0,0)
    imageneth = PhotoImage(file="giphy.gif")
    imagenbtc = PhotoImage(file="btc2.gif")


 


    precioeth=Label(root,text=f"El precio de ETH es " + "$" +ETH_price)
    precioeth.config(fg="black",bg="cyan",font=("Verdana",12))
    precioeth.pack()

    Label(root, image=imageneth, bd=1).pack(side="top")

    preciobtc=Label(root,text="El precio de BITCOIN BTC es "+ "$" + BTC_price )
    preciobtc.config(fg="black",bg="gold",font=("Verdana",12))
    preciobtc.pack()
    Label(root, image=imagenbtc, bd=1).pack(side="top")

    Button(text="EXIT",command=quit).pack()



    root.mainloop()

w=main()
