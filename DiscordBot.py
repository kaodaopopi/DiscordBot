#非同步function
import nest_asyncio
#隨機非同步function
import random
#導入 Discord.py
import discord
#對網路發動請求的套件
import requests
#借助網頁的結構特性來解析網頁的工具，只需要簡單的幾條指令就可以提取HTML標籤裡的元素。
from bs4 import BeautifulSoup

nest_asyncio.apply()
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#遊戲抽籤
def remdom_game():
  game = ['CSGO', '單中', 'APEX','死人棋']
  return random.choice(game)

#爬蟲相關
def porn(index):
  data=[]
  r = requests.get("https://cn.pornhub.com/video/search?search="+index) #將網頁資料GET下來
  soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
  sel = soup.select("span.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
  for s in sel:
    data.append("https://cn.pornhub.com" + s["href"])
    #print("https://cn.pornhub.com" + s["href"], s.text) 
  return random.choice(data)



#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('play Nekopara')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if message.content.startswith('@要玩啥'):
      await message.channel.send(remdom_game())
    if message.content.startswith('@可以色色'):
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("那我推薦你:"+" "+porn(""))
      else:
        await message.channel.send("那我推薦你:"+" "+porn(tmp[1])) 

client.run('Your Token') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面