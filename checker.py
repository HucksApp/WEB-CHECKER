import requests
login_email = "jakehunt@gmail.com"
login_password ="pussypie"

##res = requests.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=True)
##print(res.headers['Content-Type'],res.status_code)


with requests.Session() as session:
    res = session.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=False)

print(res.status_code, res.headers['content-type'], res.headers)



