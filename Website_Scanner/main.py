#!/usr/bin/env python3
from general import *
from domain_name import *
from ip_address import *
from nmap import *
from whois import * 
    
ROOT_DIR = 'companies'
create_dir(ROOT_DIR)
    
def gather_info(name1, url):
    domain_name = get_domain_name(url)
    ip_address  = get_ip_address(url)
    nmap        = get_nmap('-A', domain_name)
    whois       = get_whois(domain_name)
    create_report(name1, url, domain_name, nmap, whois)
   
def create_report(name1, full_url, domain_name, nmap, whois):
    project_dir = ROOT_DIR + '/' + name1
    create_dir(project_dir)
    write_file(project_dir + '/full_url', full_url)
    write_file(project_dir + '/domain_name', domain_name)
    write_file(project_dir + '/nmap', nmap)
    write_file(project_dir + '/whois', whois)

print(gather_info('Coventry', 'https://www.coventry.ac.uk/'))
  

