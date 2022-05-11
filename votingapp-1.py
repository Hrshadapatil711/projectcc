import requests
 from datetime import datetime
 import pytz

 IST = pytz.timezone('Asia/Kolkata')  
 raw_TS = datetime.now(IST)

 curr_date = raw_TS.strftime("%d-%m-%Y") 
 curr_time = raw_TS.strftime("%H-%M-%S")  

 tele_auth_token = "5375407084:AAGhXxiDARX0DRByUD7Z0H9VmWKHnjKZAKI" # Authentication token provided by Telegram bot
 tel_group_id = "voting_notifier"  

 msg = f" Message received on {curr_date} at {curr_time}"

 def send_msg_on_telegram (message):

     telegram_api_url = f"https://core.telegram.org/bots/api{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
     tel_resp = requests.get(telegram_api_url)

     if tel_resp.status_code == 200:
     print (" INFO: Notification has been sent on Telegram") 
else:
     print ("ERROR:Could not send Message")

     send_msg_on_telegram(msg)

