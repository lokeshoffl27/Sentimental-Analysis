
import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r',encoding='iso-8859-15')
    line = f.readline()
    while line != '':
            tweets.append([line, t_type])
            line = f.readline()
    f.close()
    return tweets


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_tweet(tweet):
    return classifier.classify(extract_features(nltk.word_tokenize(tweet)))


pos_tweets = read_tweets('Training_Data/Social_Ranter.txt', 'positive')
neg_tweets = read_tweets('Training_Data/Negative.txt', 'negative')


    
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))


word_features = get_word_features(get_words_in_tweets(tweets))


training_set = nltk.classify.util.apply_features(extract_features, tweets)
classifier = NaiveBayesClassifier.train(training_set)
 


test_tweets = read_tweets('Test_Tweets/Tweets_Positive.txt', 'positive')
test_tweets.extend(read_tweets('Test_Tweets/Tweets_Negative.txt', 'negative'))  
total = accuracy = float(len(test_tweets))

for tweet in test_tweets:
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1
result=accuracy / total * 100

