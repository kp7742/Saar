from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import nltk; nltk.download('punkt')

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words




LANGUAGE = "english"


list = []
def summary(SENTENCES_COUNT=10):
   string=""
   url = "http://www.feynmanlectures.caltech.edu/I_02.html"
   parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
   # or for plain text files
   #parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
   stemmer = Stemmer(LANGUAGE)

   summarizer = Summarizer(stemmer)
   summarizer.stop_words = get_stop_words(LANGUAGE)

   for sentence in summarizer(parser.document, SENTENCES_COUNT):
         string+=str(sentence)
   return string




