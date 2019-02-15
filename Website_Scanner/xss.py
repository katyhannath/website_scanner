
#!/usr/bin/env python3
import requests 
def get_target(url):
 command = 'xss' + url
 req = requests.post(command)
 results = str(req.read())
 return results 
 
#print("https://www.inthestyle.com/")



