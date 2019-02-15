#!/usr/bin/env python3
import os

def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()

#print(get_ip_address('rgu.ac.uk'))