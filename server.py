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
            from_ = item["message"]["from"]["id"]
            from_username = item["message"]["from"]["username"]
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
                        from_ = item["message"]["from"]["id"]
                        reply = make_comms(message)
                        bot.send_message(reply, from_)