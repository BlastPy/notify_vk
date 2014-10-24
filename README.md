notify_vk
=========

Show your message from vk.com in notify-osd

### Install vk api librarry

`sudo pip install vk`
 
[Author](https://github.com/dimka665/vk)
 
### Install supervisor to create demon
 
`sudo pip install supervisor` 
 
### Create config file for supervisor
 
`echo_supervisord_conf > supervisord.conf`
 
### Open config and add
```ini
[program:vk_notify]
command=python n_vk.py #address to file
stdout_logfile=./program.log  #address to log file
```

### Edit n_vk.py

`vkapi = vk.API('4597440', 'Your login', 'Your password', scope=2097151)`

### Start our demon

`supervisord -c supervisord.conf # start with our config`

### Other commands for supervisor

`supervisorctl status vk_notify # show status of our program` 

`supervisorctl stop vk_notify # stop program ` 

`supervisorctl start vk_notify # start program ` 

 
