import tweepy
import paralleldots
import collections
from collections import Counter
from tweepy import Stream
from tweepy.streaming import StreamListener
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


#Authentication Consumer_Key
Consumer_Key = 'SgtBBDtPnxGbc20G0OAvFvM9T'
Consumer_Secret = 'mPsn8C1gBIFIQP1sg5cov6NLLKve2DsGrmqalPyjSleEWlz5oQ'

#Authentication Access_Token

Access_Token = '811896074516328448-3qcZ4eM9jbiyCQoO46OGgmglTNXcBTa'
Access_Token_Secret = 'n81a8UqXosFrBXen1kwXngCGMx3tjuZsaQLnNvL6Qn6vC'

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

api = tweepy.API(auth)

####Retrieve_Tweets

class retrieve_tweets(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)


twitterStream = Stream(auth, retrieve_tweets())

#Default_Retreving_Tweet

twitterStream.filter(track=["akshay"])

#User_Input_Retreving_Tweet

twitterStream.filter(track=[input("Enter The Retreving Tweet\Alphabet:")])

####Count_No._of_Follwers

follower_count = api.get_user(input("Search Number of followers By Account Name:")).followers_count
print("Followers:"+ str(follower_count))

####Sentiments_Analysis

def sent_analysis():
    positive=0;
    negative=0;
    neutral=0;
    query()
    from paralleldots import set_api_key,sentiment

    set_api_key("ZLgGeYFRGNz2MjqNvVZOHk2ZyjTiKZ7JJNU8ebxHs44")
    
    paralleldots.get_api_key()
    for tweet in tweets:
        tweet_text=tweet.text
        sentiment_type=sentiment(tweet_text)
        sentiment_values=sentiment_type['sentiment']
        if sentiment_values=="positive":
            positive=positive+1;
        elif sentiment_values=="negative":
            negative=negative+1;
        else:
            neutral=negative+1;
    if positive>negative and positive>neutral:
        print("POSITIVE SENTIMENT with count"+ " "+str(positive))
    elif negative>positive and negative>neutral:
        print("NEGATIVE SENTIMENT with count" + " " +str(negative))
    else:
        print("NEUTRAL SENTIMNET with count" + " " +str(neutral))

sent_analysis()

####Location_language_and_time zone

def extract_info():
    tweet= retrieve_tweets()
    location =[]
    for data in tweet:
        tb = TextBlob(data.text)
        print("language of Tweet :"+tb.detect_language()+"\t timezone :" +str(data.user.time_zone))
        loc = data.user.location
        location.append(loc)
    word_counts = Counter(location)
    print("location \t No of occurences ")

extract_info()

####Tweet_A_Message_From_Your_Account

#Default

api.update_status(status ="Test Message #Python#Learning#TwitterBot, Welcome to the PYTHON_CLUB!!!")

#user_Input_Tweet

api.update_status(status =(input("Enter the message to Tweet from your Account:")))

####Top_usage

def top_usage():
    global count
    stop_words = set(stopwords.words('english'))
    a = [a.upper() for a in stop_words]
    tweets = api.user_timeline(screen_name="narendramodi", count=200, tweet_mode="extended")
    for tweet_compare in tweets:
        fulltext = tweet_compare.full_text
        temp = []
        temp.append(fulltext)
        tempp = temp
        import re
        cur_tweet = re.sub(r"http\S+", "", str(tempp))
        cur_tweet1 = re.split(r"\s", cur_tweet)
        cur_tweet = [w for w in cur_tweet1 if not w in stop_words]
        cur_tweet=[]
        for w in cur_tweet1:
            if w not in stop_words:
                cur_tweet.append(w)
                count = Counter(cur_tweet).most_common(10)
        print(count)

top_usage()
