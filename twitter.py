import twitter
import json

twitter_config_file = "twitter_api.config"

txt = open(twitter_config_file)
api_config = json.load(txt)

api = twitter.Api(consumer_key = api_config['CONSUMER_KEY'], consumer_secret = api_config['CONSUMER_SECRET'], access_token_key = api_config['ACCESS_TOKEN'], access_token_secret = api_config['ACCESS_TOKEN_SECRET'])
#users = api.GetFriends()
#print([u.name for u in users])
status = api.PostUpdate("A car was going to fast", "/home/pi/car-speed-detector/car_at_20160924_152731.jpg")
print(status.text)
