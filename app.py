import urllib3
import json
from datetime import datetime, timezone
from bs4 import BeautifulSoup


urllib3.disable_warnings()
HTTP = urllib3.PoolManager()
URL = 'http://localhost:8000/'

RESPONSE = HTTP.request('GET', URL)
SOUP = BeautifulSoup(RESPONSE.data, features="html.parser")
TAG = SOUP.find_all("td", class_="stats_data")

exitformat = {
    'timestamp':
        datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SUTC"),
    'weather-data': {
        'temperature_in': TAG[9].text.strip(),
        'temperature_out': TAG[0].text.strip(),
        'humidity': TAG[4].text.strip(),
        'pressure': TAG[5].text.strip(),
        'wind': TAG[7].text.strip(),
        'rain': TAG[8].text.strip(),
        'uv': TAG[10].text.strip(),
        'et': TAG[11].text.strip(),
        'solar_radiation': TAG[12].text.strip()
    }
}

print(json.dumps(exitformat))
