from bot import telegram_chatbot
# initialise bot
bot = telegram_chatbot("config.cfg")

def make_reply(msg, from_id):
    reply = None
    if type(msg) != type('abc'):
        reply = None
    else:
        if msg.lower() == "start":
            reply = '@'+from_id+' Who summon the START GOD!'        
    return reply

def make_comms(msg):
    reply = None
    if type(msg) != type('abc'):
        reply = None
    else:
        if msg != None:
            reply = msg + ' is the starter!'
    return reply

def reply_happy_birthday():
    reply = '''Happy Birthday to You
Happy Birthday to You
Happy Birthday to You
Happy Birthday to You

恭祝你福壽與天齊
慶賀你生辰快樂
年年都有今日 
歲歲都有今朝
恭喜你 恭喜你
'''
    return reply
update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["chat"]["id"]

            # check username exists or not
            if 'username' in item["message"]["from"].keys():
                from_username = item["message"]["from"]["username"]
            else:
                from_username = 'sender'
                
            # check if bot is added to group
            if 'new_chat_participant' in item["message"].keys():
                pass

            # Happy Birthday
            if isinstance(message, str) and 'happy birthday' in message.lower():
                bot.send_message(reply_happy_birthday(), from_)                
               
            reply = make_reply(message, from_username)
            bot.send_message(reply, from_)
            if reply != None:
                updates = bot.get_updates(offset=update_id)
                updates = updates["result"]
                if updates:
                    for item in updates:
                        update_id = item["update_id"]
                        try:
                            message = str(item["message"]["text"])
                        except:
                            message = None
                        from_ = item["message"]["chat"]["id"]
                        reply = make_comms(message)
                        bot.send_message(reply, from_)