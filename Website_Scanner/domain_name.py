#!/usr/bin/env python3
from tld import get_fld

def get_domain_name(url):
    domain_name = get_fld(url)
    return domain_name

#print(get_domain_name('https://www.coventry.ac.uk/'))