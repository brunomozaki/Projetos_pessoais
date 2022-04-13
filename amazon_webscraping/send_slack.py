import pandas as pd
import slack 
import os
from pathlib import Path
from dotenv import load_dotenv
import json

env_path = Path('amazon_webscraping/.env')        # Reads from .env file so that the token doesnt need to be written on the script
load_dotenv(dotenv_path= env_path)

client = slack.WebClient(token = os.environ['SLACK_TOKEN'])

df = pd.read_csv('amazon_webscraping/results.csv')


df['Price_Only'] = df['Price'].apply(lambda price: price.split('R$')[1]).str.strip().str.replace(',', '.').astype(float)        # Manipulation to transform price into string, removing spaces and then float


max_price= df['Price_Only'].max()
min_price = df['Price_Only'].min()
mean_price = df['Price_Only'].mean()


block= [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Today's Price Descriptions"
			}
		},
		{
			"type": "divider"
		},
        {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Maximum Price:* ' + json.dumps(max_price)
				}
            ]
        },
        {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Minimum Price:* ' + json.dumps(min_price)
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Average Price:* ' + json.dumps(round(mean_price,2))
				}
            ]
        }

]


client.chat_postMessage(channel = '#data-project', blocks = block)