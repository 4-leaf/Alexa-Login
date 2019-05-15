class login():
    def __init__(self):
        self.username = ""
        self.password = "" 
        self.ip = ""
        self.session = self._Alexa_Session()
    
    def _Alexa_Session(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        session = requests.Session()
        session.headers.update(headers)
        return session

    def _Alexa_CSRF_Token(self):
        raw_html = self.session.get("https://www.alexa.com/login")
        searchable_html  = BeautifulSoup(raw_html.text, "html.parser")
        return searchable_html.find('input', {'name':'csrf'})['value']
        
    def Alexa(self):
        data = {
            'csrf': self._Alexa_CSRF_Token(),
		        'resource':'https://www.alexa.com/pro/dashboard',
		        'ip_address':'172.93.53.132',
		        'email':self.username,
		        'password':self.password,
		}
        return self.session.post("https://www.alexa.com/login/ajaxex", data = data)

    def Alexa_Proof(self):
        return self.session.get("https://www.alexa.com/comparison?sites=google.com&display=json")

output = login()
Alexa = output.Alexa()
print(output._Alexa_CSRF_Token())
print(BeautifulSoup(Alexa.text, "html.parser"))
