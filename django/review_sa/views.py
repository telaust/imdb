from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
# from sklearn
# Create your views here.
from .models import Sentiment


def reviewSAView(request):
    
    # sentiment analysis here
    items = Sentiment.objects.all()
    # sentiment = "23"
    return render(request, "index.html", {"items": items})


def analyse(request):
    Sentiment.objects.all().delete()
    text: str = request.POST.get("Text1", False)
    if text == "" or text is None:
        res = Sentiment(sentiment="empty string")
    else:
        res: int = load_and_predict(text)
        res = Sentiment(sentiment="positive" if res == 1 else "negative")
    
    if res is not None:
        res.save()
    return HttpResponseRedirect('/review_sa/')
    
    
def load_and_predict(text: str) -> int:
    loaded_model = pickle.load(open("logreg1.pkl", 'rb'))
    loaded_tfidf_transformer = pickle.load(open("tfidf.pkl", 'rb'))
    loaded_cv_transformer = pickle.load(open("cv.pkl", 'rb'))

    result = loaded_model.predict(loaded_tfidf_transformer.transform(loaded_cv_transformer.transform([text])) )
    return result[0]