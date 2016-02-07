
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

 
if __name__ == '__main__':
    app.run(debug=True)
