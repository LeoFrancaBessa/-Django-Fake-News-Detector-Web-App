from django.shortcuts import render
import re
import nltk
import pickle
import os

nltk.download('punkt')
nltk.download('stopwords')

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


# our home page view
def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(text):

    text = [text]
    text = [clean_train_data(x) for x in text]
    text = [remove_stopwords(x) for x in text]

    BASE = os.path.dirname(os.path.abspath(__file__))
    model = pickle.load(open(os.path.join(BASE, "fake_news_LR.sav"), "rb"))
    vectorized = pickle.load(open(os.path.join(BASE, "countvectorizer.sav"), "rb"))
    prediction = model.predict(vectorized.transform(text))

    if prediction[0] == 0:
        return "Fake"
    elif prediction[0] == 1:
        return "True"
    else:
        return "error"


# our result page view
def result(request):
    news = str(request.GET['news'])
    result = getPredictions(news)

    return render(request, 'result.html', {'result': result})
