import time
from datetime import datetime as dt
import os

hosts_path =r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 20):
        print("Working Hours...")
    else :
        print("Fun hours...")
    time.sleep(5)