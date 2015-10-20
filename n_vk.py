# -*- coding: utf-8 -*- 
import sys
import vk
import time
import os
### Another commit ###
vkapi = vk.API('4597440', 'Your login','Your password',scope=2097151) #Takes token from vk.com
s = vkapi.access_token 
while True:
	messages = vkapi('messages.get', count=1) #Take last message
	"""
	Read status of message
	if read_state = 0 send notify
	else sleep 5 second 
	"""
	status = messages['items'][0]['read_state']
	if status !=1:
		frnds = vkapi('friends.get')	#Takes freinds list
		message =  messages['items'][0]['body'].encode('utf-8') #Takes body of message
		friend =  messages['items'][0]['user_id'] #Takes 'id' of sender
		frn= vkapi.users.get(user_id=friend) #Take name and surname of sender
		ret_status = messages['items'][0]['id'] #Takes 'id' of message
		friednd =  frn[0]['first_name'].encode('utf-8') + ' ' + frn[0]['last_name'].encode('utf-8') 
		x = ('"'+message+'"','"'+friednd+'"') #Formatting message for send notify
		ret_status = vkapi('messages.markAsRead',peer_id=friend) #Mark message as read
		time.sleep(1) 
		os.system('notify-send -i ~/32.png  %s %s ' % (x[1],x[0])) #Send our notify
		time.sleep(1)
		
	else:
		time.sleep(5) 
	### 
	So just have fun.
	###
