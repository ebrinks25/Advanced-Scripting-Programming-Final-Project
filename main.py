import tweepy
import time
import random

bearer_token = 'bearer_token'
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)


def create_tweet(quote_list, rand_int):
    quote = quote_list[rand_int] + "#theoffice"
    modified = quote.split(" — ")
    new_quote = modified[0] + "\n -" + modified[1]
    print("Just tweeted: ", new_quote, "\n at: ", time.ctime(), "\n----------")
    client.create_tweet(text=new_quote)


f = open("quotes.txt", "r")
quote_list = []
for x in f:
    x.rstrip()
    quote_list.append(x)


#On the hour, the loop will execute a quote post. It also will follow back all the users that follow the bot.
follower_list = []

while True:
    current_time = time.time()
    if (current_time % 3600 == 0):
        rand_int = random.randint(1, len(quote_list) - 1)
        create_tweet(quote_list, rand_int)
        quote_list.remove(quote_list[rand_int])
        follower_list.append(client.get_users_followers("1458923005028057095"))
        for i in follower_list:
            temp = getattr(i, "data")
            client.follow_user(temp[0].id)




#SOURCES
#https://stackoverflow.com/questions/70061685/can-a-tweeter-bot-post-tweets-or-quotes-via-v2-api-essential-access
#https://docs.tweepy.org/en/stable/
#https://www.programiz.com/python-programming/time
#https://quotecatalog.com/quotes/tv/the-office
#https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/
