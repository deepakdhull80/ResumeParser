import os
import nltk
from module.extract import getdata,convert_to_text,extract_skills,get_state,get_city,getPhone,tokenize,getEmail,extract_education,extract_name


class Parser:
	def __init__(self,filename):
		self.directory=os.getcwd()
		self.file=__file__
		self.format=filename.split('.')[-1]
		self.filename=filename
		self.core=""
		self.name=""
		self.email=[]
		self.phone=[]
		self.skill=[]
		self.education=[]
		self.state=""
		self.city=""
		self.tokenize=None
		nltk.download('stopwords')


	def data(self):
		self.core=convert_to_text(self.filename,format=self.format)
		tokens=tokenize(self.core)
		self.tokenize=tokens
		self.skill=extract_skills(tokens)
		self.email=getEmail(self.core)
		self.phone=getPhone(self.core)
		self.education=extract_education(tokens)
		self.state=get_state(tokens)
		self.city=get_city(tokens)
		self.name=extract_name(self.email)

	def tokens(self):
		self.data()
		return self.tokenize

	def get_json(self):
		self.data()
		return {
		"name":self.name,
		"email":self.email,
		"phone":self.phone,
		"city":self.city,
		"state":self.state,
		"education":self.education,
		"skills":self.skill
		}


# print(Parser('t1.pdf').get_json())