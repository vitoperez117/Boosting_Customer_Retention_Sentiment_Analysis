import praw
from praw.models import MoreComments 
from pprint import pprint

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from wordcloud import WordCloud


'''DATA SCRAPING'''

#Initiate Reddit Instance
reddit = praw.Reddit(
    client_id="z3DgdGeM3hPFNuru2P3FGQ",
    client_secret=client_secret,
    user_agent="r/teacher scraper by u/carlschwabb",
)

#Build Scraper Function
def get_reviews (subreddit, keyword):

    pcr = []
    
    for submission in reddit.subreddit(subreddit).search(keyword, limit=None):
        entry = {'date': submission.created_utc,
                'author': submission.author,
                'title': submission.title,
                'text': submission.selftext,
                'url': submission.url}
        pcr.append(entry)
        for c in submission.comments:
            entry_c = {'date': c.created_utc,
                       'author': c.author,
                       'title': 'comment',
                       'text': c.body,
                       'url': c.permalink}
            pcr.append(entry_c)
            for r in c.replies:
                entry_r = {'date': r.created_utc,
                           'author': r.author,
                           'title': 'reply',
                           'text': r.body,
                           'url': r.permalink}
                pcr.append(entry_r)
                for rr in r.replies:
                    entry_rr = {'date': rr.created_utc,
                                'author': rr.author,
                                'title': 'sub1reply',
                                'text': rr.body,
                                'url': rr.permalink}
                    pcr.append(entry_rr)
                    for rrr in rr.replies:
                        entry_rrr = {'date': rrr.created_utc,
                                     'author': rrr.author,
                                     'title': 'sub2reply',
                                     'text': rrr.body,
                                     'url': rrr.permalink}
                        pcr.append(entry_rrr)
                        for rrrr in rrr.replies:
                            entry_rrrr = {'date': rrrr.created_utc,
                                        'author': rrrr.author,
                                        'title': 'sub3reply',
                                        'text': rrrr.body,
                                        'url': rrrr.permalink}
                            pcr.append(entry_rrrr)
                            for rrrrr in rrrr.replies:
                                entry_rrrrr = {'date': rr.created_utc,
                                            'author': rr.author,
                                            'title': 'sub4reply',
                                            'text': rr.body,
                                            'url': rr.permalink}
    return pcr

get_reviews('Teachers', 'eureka')

#Create DataFrame from Reddit Scrape results
df = pd.DataFrame.from_records(pcr)

#Convert Epoch time to DateTime
df['date'] = pd.to_datetime(df['date'], unit='s')


'''DATA CLEANING'''

#Create function to preprocess reviews
def preprocess_text(text):

    #convert all words to lower case
    tokens = word_tokenize(text.lower()) 
    
    #tokenize
    filtered_tokens = []
    for token in tokens: 
        if token not in stopwords.words('english'):
            filtered_tokens.append(token)
    
    #lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    for token in filtered_tokens:
        lemmatized_tokens.append(lemmatizer.lemmatize(token))
    
    #compile processed text
    processed_text = ' '.join(lemmatized_tokens)

    return processed_text

#Apply function to reviews text
df['reviewed text'] = df['text'].apply(preprocess_text)


#Identify which reviews explicitly or implicitly refer to Eureka    
def explicit(df):
    if 'eureka' in df:
        return ('yes')
    else:
        return ('no') 
    
df['explicit'] = df['reviewedText'].apply(explicit)


#Check explicit v. implicit
df['explicit'].value_counts()


'''SENTIMENT ANALYSIS'''

#Initiate Sentiment Analyzer instance
analyzer = SentimentIntensityAnalyzer()

def polarity_scores(text):
    scores = []
    
    for sentence in text :
        spread=analyzer.polarity_scores(sentence)
        scores.append(spread)

    return scores

#Convert scores into DataFrame
pscoresdf = pd.DataFrame(polarity_scores(df['reviewedText']))

#Merge into main DataFrame
df = df.join(pscoresdf)

#Gauge Sentiment
def sentiment(val):
    if val >= 0.05:
        return 'positive'
    elif val > -0.05 and val < 0.05:
        return 'neutral'
    elif val <= -0.05:
        return 'negative'
    
df['sentiment'] = df['compound'].apply(lambda val: sentiment(val))


'''DATA VISUALIZATION'''

#Plot Distribution of Sentiment
yaxis = df['sentiment'].value_counts().to_list()
xaxis = df['sentiment'].unique()

plt.bar(xaxis,yaxis)
plt.title('Total Sentiment Reviews')
plt.show()


##Plot Distribution of Pos, Neg, Neutral
for c in df.columns[7:11]:
    plt.hist(pscoresdf[c])
    plt.title(c)
    plt.tight_layout()
    plt.show()


#Isolate Rows where the text EXPLICITLY mentions 'Eureka'
expdf=df.loc[df['explicit'] == 'yes']

#Plot Distribution of Sentiment (explicit)
yexp = expdf['sentiment'].value_counts().to_list()
xexp = expdf['sentiment'].unique()

plt.bar(xexp,yexp)
plt.title('Total Sentiment Reviews (exp)')
plt.show()

#Plot Distribution of Pos, Neg, Neutral (explicit)
for c in expdf.columns[7:11]:
    plt.hist(expdf[c])
    plt.title(c)
    plt.tight_layout()
    plt.show()


'''KEYWORD EXTRACTOR'''

rake_nltk_var = Rake()
rake_nltk_var.extract_keywords_from_text(expdf['text'][1])
keywords_extracted = rake_nltk_var.get_ranked_phrases()


'''TOPIC MODELLING OF NEGATIVE REVIEWS'''

#Create DataFrame of only Negative entries
negdf = expdf.loc[expdf['sentiment'] == 'negative'].sort_values(by='compound', ascending=True)

#Create function using LSA Model on Preprocessed Text
def lsaModel (reviewedText):
    corpus = [i.split() for i in reviewedText]
    dictionary = corpora.Dictionary(corpus)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
    lsa = LsiModel(doc_term_matrix, num_topics=3, id2word=dictionary)
    return lsa

lsa = lsaModel(negdf['reviewedText'])

#LSA print topics
pprint(lsa.print_topics(num_topics=5, num_words=10))

#LSA show topics
pprint(lsa.show_topics(num_topics=-1, num_words=30, log=False, formatted=True))


#Create function using LDA Model on Preprocessed Text
def ldaModel (reviewedText):
    corpus = [i.split() for i in reviewedText]
    dictionary = corpora.Dictionary(corpus)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in corpus]
    lda = LdaModel(doc_term_matrix, num_topics=3, id2word=dictionary)
    return lda

lda = ldaModel(negdf['reviewedText'])

#LDA print topics
pprint(lda.print_topics(num_topics=-1, num_words=10))

#LDA show topics
pprint(lda.show_topics(num_topics=-1, num_words=30, log=False, formatted=True))
