#import modules
import time
from datetime import datetime as dt 

#add sites to block
sites_to_block = [

    'www.facebook.com', 
    'facebook.com',
    'www.youtube.com',
    'youtube.com',
    'www.gmail.com',
    'gmail.com'
]

#Windows hostfile
Windows_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Windows_host
redirect = "127.0.0.1"

#function to add & remove mapped website urls to the hostfile depending on working time

def block_websites():
    while True:
        if dt(dt.now().year, 
        dt.now().month, 
        dt.now().day, 9) < dt.now() < dt(dt.now().year,
        dt.now().month, 
        dt.now().day, 18):
            print("Do your work")

            with open(default_hoster, 'r+') as hostfile:
                host = hostfile.read()
                
                for site in sites_to_block:
                    if site not in hosts:

                        hostfile.write(redirect + '' + site + '\n')
                    else:
                            with open(default_hoster, + 'r+') as hostfile:
                                hosts = hostfile.readlines()

                                hostfile.seek(0)
                                
                                for host in hosts:
                                    if not any (site in host for site in sites_to_block):
                                        hostfile.write(host)

                                        hostfile.trucate()
                                        print('Good time')
                                        time.sleep(3)

if  __name__ == '__main__':
    block_websites()

