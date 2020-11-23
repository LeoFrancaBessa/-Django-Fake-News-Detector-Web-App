import re
import nltk
from nltk.stem import WordNetLemmatizer
import pickle


def clean_train_data(x):
    text = x
    text = text.lower()
    text = re.sub('\[.*?\]', '', text) # remove square brackets
    text = re.sub(r'[^\w\s]','',text) # remove punctuation
    text = re.sub('\w*\d\w*', '', text) # remove numbers
    text = re.sub(r'http\S+', '', text)
    text = re.sub('\n', '', text)
    return text

stop_en = nltk.corpus.stopwords.words("english")
def remove_stopwords(text):
    token_text = nltk.word_tokenize(text)
    remove_stop = [word for word in token_text if word not in stop_en]
    join_text = ' '.join(remove_stop)
    return join_text

def remove_reuter(text):
    re.sub(r'^.*?reuters', '', text)
    

model = pickle.load(open("fake_news_LR.sav", "rb"))
cv = pickle.load(open("countvectorizer.sav", "rb"))


text = 'It seemed like such a sweet story — Donald Trump sending his personal plane down to Camp Lejeune, N.C., when 200 Marines were stranded after fighting in the 1991 Persian Gulf War. At least that is the story that Sean Hannity of Fox News has touted on his website for several months. But a reader, Lazer Cohen of Brooklyn, was suspicious and asked The Fact Checker to check it out.'

text = [text]

text = [clean_train_data(x) for x in text]

text = [remove_stopwords(x) for x in text]


bag = cv.transform(text)

label = model.predict(bag)
