import requests 
import json 
import time
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO) 
bot = Bot("2034226986:AAG5q8l3FMxhfqS85zAMM5e8pSrwHlRP7NA") 
dp = Dispatcher(bot)

channel = #Канал
admin_id = #Админ! Строго Украинец!!!

@dp.message_handler(commands=['start'])
async def send_message(message):
  chat_id = message.chat.id
  mes_id = message.message_id
  try:
    await bot.send_message(chat_id, text = "СЛАВА УКРАИНЕ!")
          
    while True:
      url = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
      url2 = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"
   
      #первый запрос
      response = requests.get(url)
      response = json.loads(response.text)
      
      res = response["result"]["Ask"]
      price_btc = str(res).split(".")[0]
      time.sleep(8)
      #второй запрос
      response2 = requests.get(url2)
      response2 = json.loads(response2.text)
      
      res2 = response2["result"]["Ask"]
      price_btc2 = str(res2).split(".")[0]
        
      if price_btc > price_btc2:
        await bot.send_message(channel, text = f"*🔴 {price_btc2}$*", parse_mode="markdown")
        time.sleep(2)
          
      elif price_btc < price_btc2:
        await bot.send_message(channel, text = f"*🟢 {price_btc2}$*", parse_mode="markdown")
        time.sleep(2)
        
  except Exception as e:
    print(e)
    return send_message(message)
    await bot.send_message(chat_id, text = e)
      
executor.start_polling(dp, skip_updates=True)
















 