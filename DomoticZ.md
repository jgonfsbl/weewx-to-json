# DomoticZ and WeeWX

In order to feed data coming from WeeWX into DomoticZ you need three things:
   1) A script generating or gathering data in the correct format 
   2) A set of calls to the DomoticZ API
   2) A cron job
   
## Feeding data into DomoticZ
In the root of this site there's a script called weewx2json.py. In order to feed data into DomoticZ you need to add the following lines at the end of that file:

```

#
# Load data to DomoticZ TEMP+HUM+BARO
# /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&svalue=TEMP;HUM;HUM_STAT;BAR;BAR_FOR
#
url = 'http://127.0.0.1/json.htm?type=command&param=udevice&idx=12&nvalue=0&svalue='+ temperature_out +';'+ humidity +';0;'+pressure+';0'
RESPONSE = HTTP.request('GET', url)

#
# Load data to DomoticZ UV
# /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&svalue=UV;TEMP
#
url = 'http://127.0.0.1/json.htm?type=command&param=udevice&idx=13&nvalue=0&svalue='+uv+';'+temperature_out
RESPONSE = HTTP.request('GET', url)

```

## Crontab job
```

*/10 * * * * /opt/weewx2json/venv/bin/python /opt/weewx2json/weewx2json.py > /dev/null 2>&1

``` 
