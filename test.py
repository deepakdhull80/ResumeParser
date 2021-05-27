from main import Parser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import sys
from module.ListFiles import files

main_file=files()[0]
secondary_file=files(False)
per1=""

try:
	


	f1=Parser("primary_file/"+main_file).get_json()
	


	for i in f1['skills']:
		per1+=i + " "

	# for i in f1['education']:
	# 	per1+=i+" "



except:
	print("Oops!", sys.exc_info()[0], "occurred in primary section.")

# ------------------------------------------------------------------------------

def calculatePercentage(filename):
	f2=Parser("secondaryFile/"+filename).get_json()
	per2=""
	

	for i in f2['skills']:
		per2+=i + " "

	# for i in f2['education']:
	# 	per2+=i+" "


	txt=[per1,per2]
	# print(txt)

	lo=CountVectorizer()
	tmp=lo.fit_transform(txt)

	result=cosine_similarity(tmp)[0][1]*100

	return {"name":filename.split('.')[0],"email":f2["email"],"phone":f2["phone"],"score":result}


for file in secondary_file:
	print(calculatePercentage(file))



# try:
# 	for file in secondary_file:
# 		try:
# 			print(calculatePercentage(file))	
# 		except:
# 			print("Oops!", sys.exc_info()[0], "file error with "+file)		

# except:
# 	print("Oops!", sys.exc_info()[0], "occurred in secondary section.")	






