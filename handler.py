import requests
import os
from pprint import pprint
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv())

def get_all_indicators(api_key, domain, page=1, all_indicators=[]):
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/url_list?limit=50&page={page}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        has_next = data.get("has_next")
        page_number = data.get("page_num")
        url_list = data.get("url_list")
        all_indicators.extend(url_list)
        

        if has_next:
            page_number += 1
            get_all_indicators(api_key, domain, page_number, all_indicators)
    else:
        print(f"{response.status_code}")
        print(response.json())

    return all_indicators

all_indicators = get_all_indicators(api_key=None, domain="XXXXXX")

for x in all_indicators:
    pprint(x)


    