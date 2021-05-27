
import pandas as pd
import numpy as np
import os

os.chdir('D:/python programs/Projects/resume_parser')
data=pd.read_csv("dataset/resume_data.csv")

import io




from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)



    fp.close()
    device.close()
    text = retstr.getvalue()
    retstr.close()
    return text

def nextLine(txt):
	return " ".join(txt.split('\n'))

def remove_special(txt):
	r=""
	for i in txt:
		if i in "1234567890qwertyuiopasdfghjklzxcvbnm@#QWERTYUIOPASDFGHJKLZXCVBNM .":
			r+=i
		else:
			r+=' '
	return r

def extra_space(text):
	return " ".join(text.split())