import requests
import json
import pyfiglet
from time import sleep
#========= Libraries ========#


W = '\x1b[38;5;231m'  # Dark white 
G = '\x1b[1;32m'  # Green
R = '\x1b[38;5;88m'  # Dark red 
B = '\x1b[38;5;18m'  # Dark Blue
b = '\x1b[38;5;153m'  # light blue 
Y = '\x1b[38;5;226m'  # Dark yellow
#========= Colors ========#


logo = pyfiglet.figlet_format("        RED-X")
print(R+logo+W)
print(f"     {Y}TELEGRAM CHANNEL➩ {G}@REDX_64")
print(f"      {Y}INSTAGRAM I'D ➩ {G}@N5I4X\n\n")
#========= Logo ========#


Description = input(f"{W}ENTER A DESCRIPTION FOR THE IMAGE {Y}➩{b} ")
while True:
	sleep(4)
	headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'origin': 'https://www.writecream.com',
	    'priority': 'u=1, i',
	    'referer': 'https://www.writecream.com/',
	    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
	}
	
	params = {
	    'prompt': Description,
	    'aspect_ratio': '16:9',
	    'link': 'writecream.com',
	    'description': Description,
	}
	
	response = requests.get(
	    'https://1yjs1yldj7.execute-api.us-east-1.amazonaws.com/default/ai_image',
	    params=params,
	    headers=headers,
	)
#========= communications ========#

	
	response_data = response.json()
	image = response_data.get('image_link', 'No image link Found ')
	attempt = response_data.get('second', 'No attempt Found ')
	status = response_data.get('status', 'No status Found ')
	base = response_data.get('base64', 'No base64 Found ')
	
	if 'image_link' or 'second' or 'status' or 'base64' in  response_data:
		print(f'''


   {R}♕  {B}################## {G}RED-X HACKER {B}##################  {R}♕{G}


👉 / {G}im = {W}{image}  ✅
👉 / {G}base = {W}{base}     ✅
👉 / {G}status = {W}{status}            ✅
👉 / {G}attempt = {W}{attempt} ✅


   {R}♕  {B}################## {G}RED-X HACKER {B}##################  {R}♕{G}
		
	''')
	else:
		print(f'''{R}
	
	
		
im = {image}  ❌
base = {base}     ❌
status = {status}            ❌
attempt = {attempt} ❌
	
		
	''')
#========= Design ========#