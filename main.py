
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('sampleindex.html',my_string="HIIIIII",my_color="round yellow",my_list=[ [0,1,2],[3,4,5],[6,7]])


if __name__ == '__main__':
    app.run(debug=True)