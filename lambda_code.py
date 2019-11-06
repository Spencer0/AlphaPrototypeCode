import json
import time
from discord_webhook import DiscordWebhook


def lambda_handler(event, context):
    records = event["Records"][0]
    datafile_name = records["s3"]["object"]["key"]
    datafile_size = records["s3"]["object"]["size"]
    print("You have uploaded " + datafile_name + ". It's size is " + str(datafile_size))
    polite_message = "You have uploaded " + datafile_name + ". It's size is " + str(datafile_size)
    
    #My Discords Webhook
    #webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/641531129161318410/zgSY79kg8CVZVUAH8WlaFtg91xWzAO9U_q6rjoaawBZQEIIhCu_BJ62b0jRCY0u5S6bV', 
    #content=polite_message)
    #webhook.execute()
    
    #Sobek Webhook
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/624644412605071386/vH2qW75Dwxw8eM3Km8nGfj7YdttY6pjmXVfo4oT9L49Lt3y-CfUeQd4GeTCukKUT8Uqe', 
    content=polite_message)
    webhook.execute()