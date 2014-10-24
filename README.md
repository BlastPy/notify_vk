notify_vk
=========

Show your message from vk.com in notify-osd

#Install vk api librarry

`sudo pip install vk`
 
[Author](https://github.com/dimka665/vk)
 
#Install supervisor for create demon
 
`sudo pip install supervisor` 
 
#Create config file for supervisor
 
`echo_supervisord_conf > supervisord.conf`
 
#Open config and add

`[program:vk_notify]
command=python n_vk.py #address to file
stdout_logfile=./program.log  #address to log file `

#Edit n_vk.py

`vkapi = vk.API('4597440', 'Your login','Your password',scope=2097151)`

#Start our demon

`supervisord -c supervisord.conf # start with our config`

#Other command for supervisor

`supervisorctl status program # show status our program
supervisorctl status # show all status 
supervisorctl stop program # stop program
supervisorctl start program # start program`
 
