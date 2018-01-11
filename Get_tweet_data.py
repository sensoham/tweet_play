from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "947163831012225024-a1yXbFjeuoDWrjxv8qpEPu0IOHTLhOe"
access_token_secret = "Wetn5MRQesZu0Erfyfuf4hJcWWjuvrliIy6LQfb4XDbQN"
consumer_key = "F54kZcGDpBR7BGDLQoRAgsrvc"
consumer_secret = "2o5X9glmicLd8xSeqb5kdgKY5pAEkaXYMIaJxQz9UnKhGMwSpn"
    


class StdOutListener(StreamListener):
    def on_data(self, data):
        savefile = open('C:/Users/soham.s/Desktop/Code/tweets/stream_tweets','a')
        savefile.write(data)
        savefile.write('\n')
        savefile.close()
        print data
        return True
    
    def on_error(self, status):
        print status


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth,l)
stream.filter(track=["Missile"])


#boilerplate
