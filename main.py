import string
import nltk

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.tokenize import word_tokenize

def proc_text():
    text = "Al principio tuve un par de problemas con el servicio de atención al cliente durante mi estancia. El gerente " \
        "del hotel se puso en contacto conmigo directamente y mi opinión sobre la atención al cliente cambió. Durante " \
        "mi estancia el hotel tenía muchos huéspedes. Reservé una noche y no estuve mucho en la habitación. Creo que " \
        "los problemas que tuve se habrían solucionado inmediatamente si me hubiese dado cuenta antes. Me alojaría en " \
        "el hotel de nuevo pero sólo me alojaría en una de las habitaciones grandes. "
    tokens = nltk.tokenize.word_tokenize(text)
    print(tokens)
    stop_words_es = set(stopwords.words('spanish'))

    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    print(tokens)

    tokens = list(filter(lambda stop_word: stop_word not in stop_words_es, tokens))
    print(tokens)
    word_frequencies = {}
    for word in tokens:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())
    print(word_frequencies)
    ##analisis de

    ##Analisis de sentimientos
    sid = SentimentIntensityAnalyzer()
    result = sid.polarity_scores(text)
    print(result)

def analyze_sentiment():
    x= "Al principio tuve un par de problemas con el servicio de atención al cliente durante mi estancia. El gerente " \
       "del hotel se puso en contacto conmigo directamente y mi opinión sobre la atención al cliente cambió. Durante " \
       "mi estancia el hotel tenía muchos huéspedes. Reservé una noche y no estuve mucho en la habitación. Creo que " \
       "los problemas que tuve se habrían solucionado inmediatamente si me hubiese dado cuenta antes. Me alojaría en " \
       "el hotel de nuevo pero sólo me alojaría en una de las habitaciones grandes. "
    #nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    result = sid.polarity_scores(x)
    print(result)
    ##compound es el resultado numerico que va de -1 a 1

def analyze_text():

    x = "Al principio tuve un par de problemas con el servicio de atención al cliente durante mi estancia. El gerente " \
        "del hotel se puso en contacto conmigo directamente y mi opinión sobre la atención al cliente cambió. Durante " \
        "mi estancia el hotel tenía muchos huéspedes. Reservé una noche y no estuve mucho en la habitación. Creo que " \
        "los problemas que tuve se habrían solucionado inmediatamente si me hubiese dado cuenta antes. Me alojaría en " \
        "el hotel de nuevo pero sólo me alojaría en una de las habitaciones grandes. "

    tokens = nltk.tokenize.word_tokenize(x)
    print(tokens)
    stop_words_es = set(stopwords.words('spanish'))

    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    print(tokens)

    print(len(tokens))
    fdist1 = nltk.FreqDist(tokens).values()
    print(fdist1)
    fdist2 = nltk.FreqDist(tokens).keys()
    print(fdist2)
    fdist3 = nltk.FreqDist.plot(tokens)



if __name__ == '__main__':
    proc_text()
    #analyze_sentiment()
    #analyze_text()