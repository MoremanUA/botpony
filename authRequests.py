import requests
import lxml.html
import cssselect

class AuthRequests:
    def __init__(self):
        self.url = "http://quest.ua/Login.aspx?return=%2fDefault.aspx"
        self.login = "Alexey_bot2"
        self.passw = "kiev3225"
        
    def urlRequests (self,url=None):
        req = requests.Session()
        data = {"Login":self.login, "Password":self.passw}
        resp = req.post(self.url, data=data)
        if url != None:
            resp = req.get(url)
        return resp.text

    def getUrl(self):
        parsed = lxml.html.fromstring(self.urlRequests())
        pr = parsed.cssselect('#tblUserBox tr a')
        for i in pr:
            if i.text == 'Моя команда':
                urli = 'http://quest.ua'+i.get('href')
        return urli

    def getSostav (self):
        urli =  self.getUrl()
        parS =  lxml.html.fromstring(self.urlRequests(urli))
        parSs = parS.cssselect('#aspnetForm table')
        arr = parSs[1].cssselect('tr td a#lnkLogin')
        k=0
        res_text=''
        for i in arr:
            k += 1
            res_text += str(k)+". "+i.text+"\n"
        return res_text

    def getNextGames(self):
        pars = lxml.html.fromstring(self.urlRequests())
        parSs = pars.cssselect('table.gameInfo a#lnkGameTitle')
        for i in parSs:
            #parsN = i.cssselect('a#lnkGameTitle')
            print(i.text)
            #parsT = i.cssselect('td span.title')
            #print(parsT.text)
        return 'closr'
            
if __name__ == '__main__':
    req = AuthRequests()
    p = req.getNextGames()
    print(p)
