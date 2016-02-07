
from flask import Flask, render_template
import csv
app = Flask(__name__)

button_label = []
with open("test.csv",'rU') as f: button_label.extend(f.read().split(','))



color_list = []
for i in range(len(button_label)-1):
	temp_id = i % 3
	temp_color = ''
	if temp_id is 0: temp_color = 'yellow'
	elif temp_id is 1: temp_color = 'green'
	else: temp_color = 'red'
	color_list.append(temp_color)
button_list = zip(button_label, color_list)

@app.route("/")
def template_test():
	return render_template('sampleindex.html', button_list=button_list)

@app.route("/symptoms2/<string:symptID>")
def symptoms2ndChoice(symptID):
	return render_template('sampleindex2.html',symptID=str(symptID),button_list=button_list)

@app.route("/symptoms3/<string:symptID>/<string:symptID2>")
def symptoms3ndChoice(symptID,symptID2):
	# #i want rates only for the diseases that we're dealing with for the symptoms -- depends on csv
	# rates = []
	# with open("fatality_rates.csv","rU") as k: rates.extend(k.read().split(','))
	# highest_rate = 0
	# for r in rates:
	# 	if highest_rate < rates[r]:
	# 		highest_rate = rates[r]

	#
	return render_template('sampleindex3.html',rate=[783706/100000])

 
if __name__ == '__main__':
    app.run(debug=True)
