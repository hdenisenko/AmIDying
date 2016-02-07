from lxml import html
import requests

BASE_URL = "http://www.webmd.com/"

root = 'http://symptomchecker.webmd.com/'
page1 = requests.get(root + 'symptoms-a-z')
tree1 = html.fromstring(page1.content)
links1 = tree1.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_1\');"]/@href')
symptoms1 = tree1.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_1\');"]/text()')
# print symptoms1


# page2 = requests.get(root + links1[i])
# tree2 = html.fromstring(page2.content)
# links2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/@href')
# symptoms2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/text()')


# page3 = requests.get(root + links1[i])
# tree3 = html.fromstring(page3.content)
# links3 = tree3.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-cmb_1\');"]/@href')
# symptoms3 = tree3.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-cmb_1\');"]/text()')
# displaySymptoms3.append(symptoms2)

# symptoms1.split(",")
# print symptoms1

# displaySymptoms2 = []
# for i in range(len(symptoms1)):
# 	page = requests.get(root + links1[i])
#  	tree2 = html.fromstring(page.content)
#  	links2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/@href')
#  	symptoms2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/text()')
#  	displaySymptoms2.append(symptoms2)

displaySymptom2Disease = []
for i in range (len(symptoms1)):
	print ("FIRST SYMPTOMS: "  + symptoms1[i])

	page2 = requests.get(root + links1[i])
	tree2 = html.fromstring(page2.content)
	links2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/@href')
	symptoms2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/text()')

	for i in range (len(symptoms2)):
		print ("SECOND SYMPTOMS: " + symptoms2[i] )
		if (i == len(symptoms2) - 1):
			print ("")
			print ("")
			print ("")
			print ("")


		page3 = requests.get(root + links2[i])
		tree3 = html.fromstring(page3.content)
		links3 = tree3.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-cmb_1\');"]/@href')
		diseases = tree3.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-cmb_1\');"]/text()')

		for i in range (len (diseases)):
			print ("DISEASES: " + diseases[i] )



	# break





# root2 = "http://symptomchecker.webmd.com/single-symptom?symptom=pain-or-discomfort&symid=1&loc=22"
# page2 = requests.get(root2)
# tree2 = html.fromstring(page2.content)
# links2 = tree2.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-sind_1\');"]/@href')


# print links1

 	
 	# print diseases 

 	# for i in range (len(links2)):
 	# 	page = requests.get(root +links2[i])
 	# 	tree3 = html.fromstring(page.content)
 	# 	links3 = tree3.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-cmb_1\');"]/text()')
 	# 	# diseases.append(links3)

# print displaySymptoms2 

# print diseases

# #This will create a list of symptoms:
# symptoms = tree.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_2\');"]/text()')
# #buyers2 = tree.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_2\');"]')






