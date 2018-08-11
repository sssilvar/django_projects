from django.http import HttpResponse
from django.shortcuts import render

import operator

def home(request):
    data = {
        'site': 'Home'
    }
    return render(request, 'home.html', data)

def count(request):
    text = request.GET['textToCount']
    n_words = len(text.split())

    # COunt words
    wordlist = text.split()
    word_counts = {w: wordlist.count(w) for w in wordlist}
    word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))

    data = {
        'site': 'Counter',
        'text': text,
        'count': n_words,
        'words': list(word_counts.keys()),
        'counts': list(word_counts.values())
    }

    return render(request, 'count.html', data)