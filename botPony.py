import requests, datetime 
import sys, re
import lxml.html, cssselect 
import authRequests as auTh
import myTools as mT

def printf(format, *args):
    sys.stdout.write(format % args)

class BotHandler:

    def __init__(self):
        self.token = '465043467:AAFKMMkS7BZ5GF8x1-D0AZUCiUubqegGeRk'
        self.api_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.req = auTh.AuthRequests()
        self.myTool = mT.myHelp()
        self.myF = mT.myFunctions()
        

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = False

        return last_update

    def search_command(self, comm):
        if comm == 'состав' or comm == 'team':
            res = self.req.getSostav()
        elif comm == 'help':
            res = self.myTool.mText
        elif re.match('anagram', comm) or re.match('анаграм', comm) :
            resT = re.match('anagram', comm)
            if resT == None:
              resT = re.match('анаграм', comm)  
            word = comm[resT.end()+1:]
            res = self.myF.anagramizer(word)
        else:
            res = 'Command not search'
        return res

greet_bot = BotHandler()



def main ():
    new_offset=None
    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()
        if last_update:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']
            printf ('%s: %s\n', last_chat_name,last_chat_text)
            if last_chat_text == 'ПриветБот':
                greet_bot.send_message(last_chat_id, 'Привет '+last_chat_name+'. Я БотПони')
            elif last_chat_text == 'Hi' :
                greet_bot.send_message(last_chat_id, 'Hellow,'+last_chat_name+'. I am Bot Pony!')
            elif re.match("\/",last_chat_text):
                res = greet_bot.search_command(last_chat_text[1:])
                greet_bot.send_message(last_chat_id, res)
            else:
                pass
            new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

