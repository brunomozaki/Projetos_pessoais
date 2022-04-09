import pandas as pd
import slack 
import slack_sdk.web

client = slack.WebClient(token = 'fill in token')


client.chat_postMessage(channel = '#data-project', text= 'Hello')