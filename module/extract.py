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
# from docx import Document

stop_word=set(stopwords.words('english'))

skills=pd.read_csv("data/skills.csv")
skills=skills['skills']
skills=np.array(skills)

state=pd.read_csv('data/state.csv')
state=state['state']
state=np.array(state)

city=pd.read_csv('data/city.csv')
city=city['city']
city=np.array(city)

nlp=spacy.load('en_core_web_sm')


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
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
		if i in "1234567890qwertyuiopasdfghjklzxcvbnm@#+QWERTYUIOPASDFGHJKLZXCVBNM .":
			r+=i
		else:
			r+=' '
	return r

def extra_space(text):
	return " ".join(text.split())

#------JSON features-------------

#extract Skills
def extract_skills(tokens):
    
    skill=[]
    for token in tokens:
        if token.text in skills:
            skill.append(token.text)
    return list(set(skill))


def get_state(tokens):
	for token in tokens:
		if token.text in state:
			return token.text

def get_city(tokens):
	for token in tokens:
		if token.text in city:
			return token.text
#done
def getPhone(string):
    phone=re.findall(r"[0-9]+",string)
    
    res=[]
    for i in phone:
        if len(i)==10:
            res.append(i)
    return res


#done
def getEmail(string):
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",string)
    return email

def extract_name(email):
    try:
        return email[0].split("@")[0]
    except:
        return ""

def extract_url(string):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)

def extract_education(tokens):
    li=[]
    for ent in tokens.ents:
        if ent.label_=="ORG" and ("engineering and technology" in ent.text  or "engineering" in ent.text or "college" in ent.text or "university" in ent.text or "iit" in ent.text or "school" in ent.text or "institute" in ent.text or "bca" in ent.text):
            li.append(ent.text)
    return li
# stop_words

def tokenize(string):
	return nlp(string)

def non_stop_words(tokens):
    s=""
    for token in tokens:
        if token.text.strip().lower() not in stop_word:
            s=s+token.text.strip().lower()+" "
    return s.strip()


#supporting function
def convert_to_text(filename,format="pdf"):
	resume=""
	if format=='pdf':
		resume=convert_pdf_to_txt(filename)
	elif format=='docx':
		resume=getdata(filename)
	else:
		with open(filename,'r') as file:
			t=file.read()
			resume=bp(t,'html.parser').text
	
	resume=nextLine(resume)
	resume=extra_space(remove_special(resume))
	resume=nlp(resume)
	resume=non_stop_words(resume)
	return resume



def getExperience(string):
	pass

#docx file 
def getdata(filename):
    return  
    
    # d=Document(filename)
	# file=d.paragraphs[0].text
	# for i in d.paragraphs:
	# 	file+=" "+i.text
	# return file

# ------------dry run main panel-----------


# doc_text=convert_to_text('resume.pdf')


# token=nlp(doc_text)





# f1=convert('t3.pdf')
# f2=convert('t4.pdf')
# f3=convert('t1.pdf')
# # print(f2)

# txt=[f1,f2]

# lo=CountVectorizer()
# tmp=lo.fit_transform(txt)

# print(cosine_similarity(tmp)[0][1]*100)
