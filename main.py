
from flask import Flask, render_template
import csv
app = Flask(__name__)

button_label = []
with open("FirstAndSecondSymptoms.txt",'rU') as f: button_label.extend(f.read().replace('\n',' ').split('FIRST SYMPTOMS:'))
button_dict1 = dict(); 
for i in range(1,len(button_label)):
	button_label[i] = button_label[i].split('SECOND SYMPTOMS:')
	key = button_label[i].pop(0)
	button_dict1.update({key:button_label[i]})
button_label1 = button_dict1.keys()

<<<<<<< HEAD
=======
button_label5 = []
with open("SecondSymptomsToDiseases.txt",'rU') as f: button_label.extend(f.read().replace('\n',' ').split('SECOND SYMPTOMS:'))
button_dict2 = dict(); 
for i in range(1,len(button_label5)):
	button_label5[i] = button_label5[i].split('DISEASE:')
	if len(button_label5[i]) == 0 :
		continue
	key = button_label5[i].pop(0)
	print key
	button_dict2.update({key:button_label5[i]})
button_label6 = button_dict1.keys()

#print button_label1
>>>>>>> a6b672c90dd8e96af4d64b7224644248069e904f
color_list = []
for i in range(len(button_label1)-1):
	temp_id = i % 3
	temp_color = ''
	if temp_id is 0: temp_color = 'yellow'
	elif temp_id is 1: temp_color = 'green'
	else: temp_color = 'red'
	color_list.append(temp_color) 
button_list1 = zip(button_label1, color_list) 


def readsymptomLine(line):
	if 'FIRST' in line: return line[15:]
	else: return line[16:]


SYMPTOM_MAP = { }
with open("FirstAndSecondSymptoms.txt",'rU') as f:
	curr_symptom = ''

	for line in f.read().splitlines():
		if 'FIRST' in line:
			curr_symptom = readsymptomLine(line)
			SYMPTOM_MAP[readsymptomLine(line)] = []
		else: 
			SYMPTOM_MAP[curr_symptom].append(readsymptomLine(line))

# SYMPTOM_MAP.append(readsymptomLine(line))


@app.route("/")
def template_test():
	return render_template('sampleindex.html', button_list=button_label1)

@app.route("/symptoms2/<string:symptID>")
def symptoms2ndChoice(symptID):
<<<<<<< HEAD
	relevant_symptoms = SYMPTOM_MAP[str(symptID).strip(' ')]
	return render_template('sampleindex2.html',symptID=str(symptID), button_list=relevant_symptoms)
=======
	button_label2 = button_dict1.get(symptID.replace("%20"," ")+" ",["Nothing found"]);
	#print button_label2
	#print symptID.replace("%20"," ");
	color_list2 = []
	for i in range(len(button_label2)-1):
		temp_id = i % 3
		temp_color = ''
		if temp_id is 0: temp_color = 'yellow' 
		elif temp_id is 1: temp_color = 'green'
		else: temp_color = 'red'
		color_list2.append(temp_color)
	button_list1 = zip(button_label2, color_list2)
	return render_template('sampleindex2.html',symptID=symptID,button_list=button_list1)
>>>>>>> a6b672c90dd8e96af4d64b7224644248069e904f

@app.route("/symptoms3/<string:symptID>/<string:symptID2>")
def symptoms3ndChoice(symptID,symptID2):
	button_label10 = button_dict2.get(symptID2.replace("%20"," ")+' ',["Nothing found"]);
	#print button_label2
	#print symptID.replace("%20"," ");
	print button_label10
	color_list3 = []
	for i in range(len(button_label10)-1):
		temp_id = i % 3
		temp_color = ''
		if temp_id is 0: temp_color = 'yellow'
		elif temp_id is 1: temp_color = 'green'
		else: temp_color = 'red'
		color_list3.append(temp_color)
	button_list1 = zip(button_label10, color_list3)
	return render_template('sampleindex2.html',symptID=str(symptID.replace("%20"," ")+" "),button_list=button_list1)
	# #i want rates only for the diseases that we're dealing with for the symptoms -- depends on csv
	# rates = []
	# with open("fatality_rates.csv","rU") as k: rates.extend(k.read().split(','))
	# highest_rate = 0
	# for r in rates:
	# 	if highest_rate < rates[r]:
	# 		highest_rate = rates[r]

	arr = [] 
	with open('DiseaseandRate.csv') as f:
		arr = [_.split(',') for _ in f.read().splitlines()]

	for item in arr:
#		print item[0]
#		print item[1]
		if item[1]:
		    item[1] = float(item[1])

	max_item_probability = max(arr, key=lambda x: x[1]) 


	print(max_item_probability)
	# max_item_probability[0] = max_item_probability[0] / 100000

	return render_template('sampleindex3.html',rate=max_item_probability ) 

 
if __name__ == '__main__':
    app.run(debug=True)
