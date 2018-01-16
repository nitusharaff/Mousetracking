import pythoncom, pyHook
from flask import render_template
from flask import Flask
from flask import request
from flask import redirect
import os
import subprocess
from flask import  *
app = Flask(__name__)
app.secret_key = 'something simple for now'

#subprocess.Popen(['python', 'keym.py'])


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['t1']
    matric = request.form['t2']
    path = os.path.dirname(os.path.abspath(__file__)) + "/subjects/{}".format(matric)
    if not os.path.exists(path):
        os.makedirs(path)
    return redirect(url_for('ques1'))



@app.route('/ques1')
def ques1():
    return render_template('/text/QuesAboutNTU/option-type/AboutNtu1.html')


@app.route('/ques1', methods=['POST'])
def post_ques1():
    ans1 = request.form['test']
    return redirect(url_for('ques2'))



@app.route('/ques2')
def ques2():
    return render_template('/text/QuesAboutNTU/rating-type/ntuCanteen.html')


@app.route('/ques2', methods=['POST'])
def post_ques2():
    ans2 = request.form['rangeInput']
    return redirect(url_for('ques3'))




@app.route('/ques3')
def ques3():
    return render_template('/image/QuesAboutNTU/Image-NTU1.html')

@app.route('/ques3', methods=['POST'])
def post_ques3():
    ans3 = request.form['test2']
    print (ans3)
    return redirect(url_for('ques4'))


@app.route('/ques4')
def ques4():
    return render_template('/audio/QuesAboutSpeaker/QuesAboutSpeaker.html')



@app.route('/ques4', methods=['POST'])
def post_ques4():
    ans4 = request.form['test4']
    print (ans4)
    return redirect(url_for('ques5'))



@app.route('/ques5')
def ques5():
    return render_template('/video/nature-based/nature1.html')



@app.route('/ques5', methods=['POST'])
def post_ques5():
    ans5 = request.form['test5']
    return redirect(url_for('ques6'))


@app.route('/ques6')
def ques6():
    return render_template('/text/QuesAboutNTU/option-type/ntuHalls.html')



@app.route('/ques6', methods=['POST'])
def post_ques6():
    ans5 = request.form['test6']
    return redirect(url_for('ques7'))


@app.route('/ques7')
def ques7():
    return render_template('/text/generalQues/option-type/musicQues.html')



@app.route('/ques7', methods=['POST'])
def post_ques7():
    ans5 = request.form['test7']
    return redirect(url_for('ques1'))

if __name__ == '__main__':
    app.run()