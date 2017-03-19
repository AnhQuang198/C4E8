from flask import *

app = Flask(__name__)


@app.route('/')
def helloworld():
    return redirect(url_for("infor"))

number_of_visistor = 0

@app.route('/infor')
def infor():
    global number_of_visistor
    number_of_visistor += 1
    return render_template("infor.html", number_of_visistor = number_of_visistor * 10)

if __name__ == '__main__':
    app.run()
