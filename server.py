from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = "ohh.."
    elif msg  == "Hello":
        reply = "hey"
    elif msg =="Hey":
        reply = "what's up?"
    elif msg =="Who are you":
        reply ="Navneet's bot"
    elif msg =="What can you do?":
        reply ="For now I am in development phase so idk fam."
    elif msg  == "hello":
        reply = "hey"
    elif msg =="hey":
        reply = "what's up?"
    elif msg =="who are you":
        reply ="Navneet's bot"
    elif msg =="what can you do for me?":
        reply ="For now I am in development phase so idk fam."
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
            reply = make_reply(message)
            bot.send_message(reply, from_)
