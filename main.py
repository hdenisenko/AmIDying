from flask import Flask, render_template
from jinja2 import Template
from lxml import html
import requests
app = Flask(__name__)
@app.route("/")


def template_test():
    root = 'http://symptomchecker.webmd.com/'
    page = requests.get(root + 'symptoms-a-z')
    tree = html.fromstring(page.content)
    links1 = tree.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_1\');"]/@href')
    symptoms1 = tree.xpath('//a[@onclick="return sl(this, \'\', \'sc-symindex-az_1\');"]/text()')
    mylist = []
    for i in range(len(symptoms1)//10):
        temp = []
        for j in range(10):
            temp.append(symptoms1[i+j])
        mylist.append(temp)

    return render_template('sampleindex.html', my_string="Wheeeee!", my_list = mylist)


if __name__ == '__main__':
    app.run(debug=True)
