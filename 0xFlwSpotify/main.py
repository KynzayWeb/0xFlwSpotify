from follow_bot import spotify
import threading, os, time
from pystyle import * 

os.system('cls')
os.system('mode 60, 23')
os.system('Title Dev By Kynzay#6666 ^& Nity Web#0001')
print(Colors.purple + """
 _     __       __ _            _   
/ \   |_  |    (_ |_) _ _|_ o _|_ \/
\_/>< |   | \^/__)|  (_) |_ |  |  / 
""" + Colors.reset)

lock = threading.Lock()
counter = 0
proxies = []
proxy_counter = 0
spotify_profile = str(input(Colors.purple + "[" + Colors.blue + "+" + Colors.purple + "]" + Colors.gray + "Spotify Link Profile: "))
threads = int(input(Colors.purple + "\n[" + Colors.blue + "+" + Colors.purple + "]" + Colors.gray + "Threads: "))

def load_proxies():
    if not os.path.exists("proxies.txt"):
        print(Colors.purple + "[" + Colors.red + "ERROR" + Colors.purple + "]" + Colors.gray + "File proxies.txt not found")
        time.sleep(10)
        os._exit(0)
    with open("proxies.txt", "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
        if not len(proxies):
            print(Colors.purple + "[" + Colors.red + "ERROR" + Colors.purple + "]" + Colors.gray + "No proxies loaded in proxies.txt")
            time.sleep(10)
            os._exit(0)

print(Colors.purple + "[" + Colors.blue + "1" + Colors.purple + "]" + Colors.gray + " Proxies" + Colors.purple + "\n[" + Colors.blue + "2" + Colors.purple + "]" + Colors.gray + " Proxyless")
option = int(input(Colors.purple + "[" + Colors.blue + ">>>" + Colors.purple + "]" + Colors.gray + ""))
if option == 1:
    load_proxies()

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_starter():
    global counter
    if option == 1:
        obj = spotify(spotify_profile, proxies[proxy_counter])
    else:
        obj = spotify(spotify_profile)
    result, error = obj.follow()
    if result == True:
        counter += 1
        safe_print(Colors.purple + "[" + Colors.blue + "Logs" + Colors.purple + "]" + Colors.gray + "Followed {}".format(counter))
    else:
        safe_print(f"Error {error}")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_starter).start()
            proxy_counter += 1
        except:
            pass
        if len(proxies) <= proxy_counter: #Loops through proxy file
            proxy_counter = 0
