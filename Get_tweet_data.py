from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
    


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
stream.filter(track=[TermToTrack])


#boilerplate
