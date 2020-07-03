# Import the Twython Class
#https://stackabuse.com/accessing-the-twitter-api-with-python/   " for the future and live streaming tweets to synca nd
# below code also "
from twython import Twython
import pandas as pd
import json

# generate credentials into json file.
# credentials = {}
# credentials['CONSUMER_KEY'] = "xaSyP6ErOdluosOSZja2keAX6"
# credentials['CONSUMER_SECRET'] = "RqRAryuFJa0M3BzNZPMpZcE9vX1eNlpSyElXzwQo5KoXx8s6c1"
# credentials['ACCESS_TOKEN'] = "2657275194-taGtsHYQUq5oDQT63O3AR6BrRRnPtYepDeGqP76"
# credentials['ACCESS_SECRET'] = "C44MQ09bbf3DLdeAVoh728RKb4Zn4PaafacZJ0vIsK1cU"

# with open("twitter_Credentials.json", "w") as file:
#     json.dump(credentials, file)

# Load credentials from json file
with open("twitter_Credentials.json", "r") as file:
    creds = json.load(file)
# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'],creds['CONSUMER_SECRET'] )

# search tweets
search_terms = ['salmankhan','karanjohar','aliabhat']

dict_ = {'screen_name': [], 'date': [],
         'text': [],}

for query_term in search_terms:

    # Create our query
    query = {'q': f"{query_term}+and -filter:retweets",
             'count': '100',
             'lang': 'en',
             'since' : '2018-11-01',
             }
    for status in python_tweets.search(**query, tweet_mode= 'extended')['statuses']:
        #dict_['id'].append(status['user']['id'])
        dict_['screen_name'].append(status['user']['screen_name'])
        dict_['date'].append(status['created_at'])
        #dict_['followers'].append(status['user']['followers_count'])
        #dict_['listed'].append(status['user']['listed_count'])
        #dict_['retweet'].append(status['retweet_count'])
        #dict_['inreplyto'].append(status['in_reply_to_screen_name'])
        #dict_['friends_count'].append(status['user']['friends_count'])
        dict_['text'].append(status['full_text'])
        #dict_['favorite_count'].append(status['favorite_count'])
        #dict_['location'].append(status['user']['location'])
        df1 = pd.DataFrame(dict_)
        df1.to_csv(f"{query_term}_tweets_csv.csv", index_label='index_numbers')

df = pd.DataFrame(dict_)
df.sort_values(by='date',inplace=True, ascending=False)
print(df)
print(df['screen_name'].unique())
print(df['text'].unique())
print(len(df['screen_name'].unique()))
print(len(df['text'].unique()))
df.to_csv("all_tweets_csv.csv",index_label='index_numbers')
