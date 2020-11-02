import requests
from bot import botmain

bot = botmain("config.cfg")

update_id = None
while True:
    print("OK")
    updates = bot.get_updates(offset=update_id)
    if(updates['ok'] == True):
        updates = updates['result']
        if updates:
            for item in updates:
                update_id = item['update_id']
                try:
                    msgobj = item["message"]
                except:
                    msgobj = None
                if msgobj is not None:
                    if(item['message']['chat']['type'] == 'group' or item['message']['chat']['type'] == 'supergroup' or item['message']['chat']['type'] == 'channel'):
                        chatfromid = item["message"]["from"]["id"]
                        chatid = item["message"]["chat"]["id"]
                        try:
                            message = str(item["message"]["text"])
                            print(message)
                        except:
                            message = None
                        bot.send(message, chatid)
    else:
        print("Not OK")
        url = "https://api.telegram.org/bot{}/deleteWebhook".format(bot.token)
        requests.get(url)