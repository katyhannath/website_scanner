
#!/usr/bin/env python3
import requests 
def get_target(url):
 payload = "*script* alert('XSS'); /*script* " 
 req = requests.post(get_target + payload) 
 if payload in req.text: print("XSS Vulnerablity discovered! Refer to XSS payloads for further escalation") 
 else: print("secure")





