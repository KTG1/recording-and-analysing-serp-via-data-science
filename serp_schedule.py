import shcedule
import datetime
from datetime import datetime

cse_id = "YOUR CUSTOM SEARCH ENGINE ID" # Custom Search Engine ID
api_key = "YOUR CUSTOM SEARCH API KEY" # API Key for Custom Search API of Google


"""
Calls the function with the determined frequency, for the determined queries.
Creates a CSV Output with the name of the actual date which the function called.
"""

def record_serp():
    date = datetime.now()
    date = date.strftime("%d%m%Y%H_%M_%S")
    df = adv.serp_goog(
        q=['Calories in Pizza', "Calories in BigMac"], key=api_key, cx=cse_id)
    df.to_csv(f'serp{date}' + '_' + 'scheduled_serp.csv')


schedule.every(10).seconds.do(record_serp)




#For making the Schedule work.
n = 5
while True:
    schedule.run_pending()
    time.sleep(1)
    n += 1