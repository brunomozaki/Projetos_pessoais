import pandas as pd
import slack 
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('amazon_webscraping/.env')        # Reads from .env file so that the token doesnt need to be written on the script
load_dotenv(dotenv_path= env_path)

client = slack.WebClient(token = os.environ['SLACK_TOKEN'])

df = pd.read_csv('amazon_webscraping/results.csv')


df['Price_Only'] = df['Price'].apply(lambda price: price.split('R$')[1]).str.strip().str.replace(',', '.').astype(float)        # Manipulation to transform price into string, removing spaces and then float
df_desc = df.describe()

max_price= df_desc['Price_Only'].max()
min_price = df_desc['Price_Only'].min()
mean_price = df_desc['Price_Only'].mean()

price_dic = {'Max Price' : max_price,
            'Min Price' : min_price,
            'Mean Price': mean_price
            }

df_price = pd.DataFrame(price_dic.items(),columns=['Metric', 'Value']) 
df_price

mkd_price = df_price.to_markdown()
mkd_price
client.chat_postMessage(channel = '#data-project', text= mkd_price)