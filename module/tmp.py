from nltk.corpus import stopwords
import io
import spacy
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup as bp


with open('t2.doc','r') as f:
    tt=f.read()
    t=bp(tt,'html.parser')
    print(t.text)