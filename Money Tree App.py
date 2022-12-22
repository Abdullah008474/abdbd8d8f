import requests as rq
import random
import threading

code=input ('》Enter Code : ')

def Mission():
	while True:
		strings='qwertyuioplkjhgfdsazxcvbnm'
		name=''.join (random.choice (strings)for i in range (5))
		
		url='https://moneytreerewards.app/api/v1/users'
		headers={
		'Accept': 'application/json',
		'Content-Type': 'application/json; charset=UTF-8',
		'Content-Length': '578',
		'Host': 'moneytreerewards.app',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.12.1'
		}
		json={
		  "first_name": f"{name}",
		  "gender": "male",
		  "birth_year": 2000,
		  "country_code": "EG",
		  "g_advertising_id": "2217ca5e-ef39-4c01-a6fd-c4ca5ed7e8c3",
		  "timezone": "Africa/Cairo",
		  "device": "Infinix-X559C",
		  "device_name": "Infinix X559C",
		  "os_platform": "android",
		  "os_version": "3.18.35+",
		  "user_agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20030723",
		  "device_language": "US",
		  "installation_id": "3256facc2a13413dbf4b370b4ecd98c1",
		  "referrer": "utm_source\u003dgoogle-play\u0026utm_medium\u003dorganic,0,0,false"
		}
		
		r=rq.post (url,headers=headers,json=json).json()
		access_token=(r['data']['access_token'])
		
		################################
		
		url1=f'https://moneytreerewards.app/api/v1/profile/join_team?access_token={access_token}&invite_code={code}'
		headers1={
		'Accept': 'application/json',
		'Content-Length': '0',
		'Host': 'moneytreerewards.app',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.12.1'
		}
		r1=rq.post (url1,headers=headers1).json()
		if (r1['status'])=='error':
		    print ('sorry , This Invite Code has used toomey!')
		else:
		    print ('Done Invited Successfully')
		    #print ('This Code reach limit,  Try again Later')
Mission()