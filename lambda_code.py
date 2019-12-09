import json
import time
from discord_webhook import DiscordWebhook


def lambda_handler(event, context):
    records = event["Records"][0]
    datafile_name = records["s3"]["object"]["key"]
    datafile_size = records["s3"]["object"]["size"]
    bucket_name = records["s3"]["bucket"]["name"]
    
    polite_message = "You have uploaded " + datafile_name + ". It's size is " + str(datafile_size) + ".\nIt has been placed into: " + bucket_name
    print(polite_message)
    #My Discords Webhook
    #webhook = DiscordWebhook(url='[Secret Redacted]', 
    #content=polite_message)
    #webhook.execute()
    
    #Sobek Webhook
    webhook = DiscordWebhook(url='[Secret Redacted]', 
    content=polite_message)
    webhook.execute()

