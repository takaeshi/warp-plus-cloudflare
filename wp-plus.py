import urllib.request, socket
import json
import datetime
import random
import string
import time
import os
import sys
import threading
import requests
import math

# get proxy
print("Getting proxy list, please wait...")
proxiesapi= "https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
r = requests.get(proxiesapi)
with open("proxies.txt",'wb') as f: 
    f.write(r.content)
proxiesfile = open('proxies.txt', 'r')
proxiess = proxiesfile.readlines()
proxiess = [x.strip() for x in proxiess]
# print(proxies)
good_proxies = list()
socket.setdefaulttimeout(30)

#proxies counter
good = 0
bad = 0


work_threadss = 200

referrer = "c9e7cc44-3c31-441e-8e17-ce51f7214465" #wrap id

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

def run(proxyy):
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		#req         = requests.get(url, data, headers, proxies = {"http": proxyy, "https": proxyy})
		proxy = urllib.request.ProxyHandler({'http': proxyy, 'https': proxyy})
		opener = urllib.request.build_opener(proxy)
		urllib.request.install_opener(opener)
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)

g = 0
b = 0

working_p = list()

#check all proxies
def wp_plus(proxyy):
	sema.acquire()
	result = run(proxyy)
	global g
	global b
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
		print("")
		animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n[-] WORK ON ID: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		print("[*] After 18 seconds, a new request will be sent.")
		working_p.append(proxyy)
		time.sleep(18)
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("")
		print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
		print("")
		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")
	sema.release()	


# keep running with working proxies
def wp_plus_w(proxyy):
	while True:
		sema.acquire()
		result = run(proxyy)
		global g
		global b
		if result == 200:
			g = g + 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print("")
			print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
			print("")
			animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
			for i in range(len(animation)):
				time.sleep(0.5)
				sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
				sys.stdout.flush()
			print(f"\n[-] WORK ON ID: {referrer}")    
			print(f"[:)] {g} GB has been successfully added to your account.")
			print(f"[#] Total: {g} Good {b} Bad")
			print("[*] After 18 seconds, a new request will be sent.")
			time.sleep(18)
		else:
			b = b + 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print("")
			print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
			print("")
			print("[:(] Error when connecting to server.")
			print(f"[#] Total: {g} Good {b} Bad")
		sema.release()


#set thread limit
sema = threading.Semaphore(value=work_threadss)

# fist run on all proxies
thread_list = []
for p in proxiess:
	thread = threading.Thread(target=wp_plus, args=(p, ))
	thread_list.append(thread)

for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()


print('Working with', work_threadss, 'threads and', len(working_p), 'proxies')

#run on only working proxies now
thread_w_list = []
for p in working_p:
	thread = threading.Thread(target=wp_plus_w, args=(p, ))
	thread_w_list.append(thread)

for thread in thread_w_list:
	thread.start()

for thread in thread_w_list:
	thread.join()
