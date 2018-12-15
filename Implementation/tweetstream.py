from tweepy import OAuthHandler
from tweepy import API
from textblob import TextBlob
import re
from tkinter import *

ckey= 'g7PQBR3Rb3W7TDhgpIXeV9NHx'
csecret= 'CK9qnyPkUqSae7bhQ7KxlxqZmCEoTwxKOcFOPiSKlBFgHQzwlS'
atoken='3252742549-jOKldJhe8WbtSJyyJLQFH7rrQKFnxlmFTFGhgrW'
asecret='nNnjwVArszV3CvPDX5TRNM9oGolemKpnxxSRRCLqS3HVg'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = API(auth)


def str_clean(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def show_entry_fields(sname):
        f=open('Username.txt','w+')
        f.write(sname)
        f.close()
        alltweets = []  
        new_tweets = []
        outtweets = []
        new_tweets = api.user_timeline(screen_name = sname,count=200)
        alltweets.extend(new_tweets)	
        oldest = alltweets[-1].id - 1    
        while len(new_tweets) > 0:
            print ("getting tweets before ",(oldest));        
            new_tweets = api.user_timeline(screen_name = sname,count=200,max_id=oldest)        
            alltweets.extend(new_tweets)        
            oldest = alltweets[-1].id - 1
            print ("...%s tweets downloaded so far",(len(alltweets)));    
        tweets = [[tweet.text] for tweet in alltweets]
        pos=0
        neg=0
        status.configure(text = "Tweets downloaded so far : " + str(len(tweets)))
        status2.configure(text = "Tweets Fetched successfully ")
        f1 = open('Test_Tweets/Tweets_Positive.txt', 'w+',encoding='UTF-8',errors='ignore')
        f2 = open('Test_Tweets/Tweets_Negative.txt', 'w+',encoding='UTF-8',errors='ignore')
        for i in tweets:
            clean=str_clean(str(i))            
            analysis = TextBlob(clean)
            #print(analysis.show_informative_features(5)) 
            if analysis.sentiment.polarity > 0:
                 pos+=1
                 f1.write(str(i)+'\n')
            else:
                 neg+=1
                 f2.write(str(i)+'\n')
        print(pos)
        print(neg)
        status2.configure(text = "Stored successfully ")
        status3.configure(text = "Predicting Personality Results......")
        f1.close()
        f2.close()




master = Tk()
#master.configure(background="#a1dbcd")
Label(master, text="Behavioral Studies through Social Media ", fg="#a1dbcd" ,bg="#383a39",font=("Helvetica",20)).pack()
Label(master, text="\nEnter Twitter Name : ").pack()
e1 = Entry(master)
e1.pack()

Button(master, text='Fetch', fg="#a1dbcd" ,bg="#383a39" ,command= lambda:show_entry_fields(e1.get())).pack(pady=15)
Label(master, text="Status : ").pack()
status = Label(master)
status.pack(pady=10)

status2 = Label(master)
status2.pack()
status2 = Label(master)
status2.pack()
status3 = Label(master)
status3.pack()
mainloop( )



