#隨機非同步function
import random
#對網路發動請求的套件
import requests
#借助網頁的結構特性來解析網頁的工具，只需要簡單的幾條指令就可以提取HTML標籤裡的元素。
from bs4 import BeautifulSoup
#導入 Discord.py
import discord

#遊戲抽籤
def remdom_game():
  game = ['CSGO', '單中', 'APEX','死人棋']
  return random.choice(game)

#爬蟲(PornHub)
def porn(index):
  data=[]
  r = requests.get("https://cn.pornhub.com/video/search?search="+index) #將網頁資料GET下來
  soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
  sel = soup.select("span.title a") #取HTML標中的 <span class="title"></span> 中的<a>標籤存入sel
  for s in sel:
    data.append("https://cn.pornhub.com" + s["href"])
    #print("https://cn.pornhub.com" + s["href"], s.text) 
  return random.choice(data)

#骰子遊戲(18拉)
def dice():
  my_files = ['pic/0.png','pic/1.png','pic/2.png','pic/3.png','pic/4.png','pic/5.png']

  Threedice = [
    discord.File(random.choice(my_files)),
    discord.File(random.choice(my_files)),
    discord.File(random.choice(my_files)),
  ]
  return Threedice


