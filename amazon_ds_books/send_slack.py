import pandas as pd
import slack 
import os
from pathlib import Path
from dotenv import load_dotenv
import json
import psycopg2

env_path = Path('amazon_ds_books/.env')        # Reads from .env file so that the token doesnt need to be written on the script
load_dotenv(dotenv_path= env_path)



client = slack.WebClient(token = os.environ['SLACK_TOKEN'])

conn = psycopg2.connect(database="amazon_ds",
                        user= os.environ['POST_USER'], password=  os.environ['POST_PASS'],
                        host='localhost', port='5432'
)

query_max = '''
SELECT MAX(PRICE_NUM) FROM DS_BOOKS_MODEL
'''

query_min = '''
SELECT MIN(PRICE_NUM) FROM DS_BOOKS_MODEL
'''

query_avg = '''
SELECT ROUND(AVG(PRICE_NUM),2) FROM DS_BOOKS_MODEL
'''

query_popular = '''
SELECT * FROM DS_BOOKS_MODEL
WHERE REVIEW_COUNT = (SELECT MAX(REVIEW_COUNT) FROM DS_BOOKS_MODEL)
LIMIT 1
'''

df_max = pd.read_sql(query_max, conn)
max_value= df_max.values[0][0]

df_min = pd.read_sql(query_min, conn)
min_value = df_min.values[0][0]

df_avg = pd.read_sql(query_avg, conn)
avg_value = df_avg.values[0][0]


df_popular = pd.read_sql(query_popular, conn)

title_popular = str(df_popular['description'][0])
price_popular = df_popular['price_num'][0]
review_popular = int(df_popular['review_count'][0])
rating_popular = df_popular['rating_num'][0]
url_popular = df_popular['url'][0]


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
					"text": '*Maximum Price:* ' + 'R$ '+json.dumps(max_value)
				}
            ]
        },
        {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Minimum Price:* ' + 'R$ '+ json.dumps(min_value)
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Average Price:* ' + 'R$ '+ json.dumps(avg_value)
				}
            ]
        },
		{
			"type": "divider"
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Most Popular book"
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
					"text": '*Title:* ' + json.dumps(title_popular, ensure_ascii=False) 
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Price:* ' + 'R$'+ json.dumps(price_popular) 
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Number of reviews:* ' + json.dumps(review_popular) 
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Rating out of 5:* ' + json.dumps(rating_popular) 
				}
            ]
        },
          {
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": '*Link to buy:* ' + json.dumps(url_popular) 
				}
            ]
        }

]


client.chat_postMessage(channel = '#data-project', blocks = block)