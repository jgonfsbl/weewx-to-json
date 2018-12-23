import urllib3
import json
import re
from datetime import datetime, timezone
from bs4 import BeautifulSoup


urllib3.disable_warnings()
HTTP = urllib3.PoolManager()
URL = 'http://localhost:8000/'

RESPONSE = HTTP.request('GET', URL)
SOUP = BeautifulSoup(RESPONSE.data, features="html.parser")
TAG = SOUP.find_all("td", class_="stats_data")

WIND_COURSE = re.sub('^.+from ','',TAG[7].text.strip())
WIND_COURSE = re.sub('\u00b0.+','',WIND_COURSE)

exitformat = {
    'timestamp':
        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SUTC"),
    'weather-data': {
        'temperature_in' : re.sub('\u00b0C','',TAG[9].text.strip()),
        'temperature_out': re.sub('\u00b0C','',TAG[0].text.strip()),
        'humidity'       : re.sub('%','',TAG[4].text.strip()),
        'pressure'       : re.sub(' mbar','',TAG[5].text.strip()),
        'wind_speed'     : re.sub(' m/s.+','',TAG[7].text.strip()),
        'wind_course'    : WIND_COURSE,
        'rain'           : re.sub(' mm/hr','',TAG[8].text.strip()),
        'uv'             : TAG[10].text.strip(),
        'et'             : re.sub(' mm','',TAG[11].text.strip()),
        'solar_radiation': re.sub(' W/m\u00b2','',TAG[12].text.strip())
    }
}

print(json.dumps(exitformat))