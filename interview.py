import subprocess
from model import User
from Quiz import quiz
from dbase import db
from Admin import admin_user
from flask import *
import datetime
import time

app = Flask(__name__)
app.secret_key = 'something simple for now'
db_user = db(app)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')

    elif request.method == 'POST':
        adm=admin_user()

        session['quiz_id'] = request.form.get('quiznum')
        session['username'] = request.form['username']
        session['user_matric'] = request.form['userid']

        if request.form['adminname'] != adm.getUsername() or request.form['adminpwd'] != adm.getPwd() :
            flash("wrong username or password", "error")
            return render_template("admin.html")

        if request.form['submit'] == 'record':


            if (not request.form.get('quiznum') or not request.form.get('userid') or not request.form.get('username')):
                flash("enter quiz and user details to record","error")
                return render_template("admin.html")

            else:
                session["record"]= True

        elif request.form['submit'] == 'playback':
            session["record"] = False
            session['date'] = request.form.get('date', None)
            session['startq'] = request.form.get('startq', None)
            session['endq'] = request.form.get('endq', None)

    return redirect(url_for('index'))



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        if(session["record"]==False):
            return render_template("start.html",value=session['username'])
        else:
            return render_template('main.html',value=session['username'])

    elif request.method == 'POST':
        quiz_user=quiz()
        session['ques']= quiz_user.getQuestions( session['quiz_id'])
        session['quesid'] = quiz_user.getQuestionId(session['quiz_id'])
        user = User(session['username'], session['user_matric'])
        session["current_question"] = "0"
        if(session["record"]==True):
            session["dir"]=user.createDir(session['quiz_id'])
            session["logfile"] = user.setLogfile(session['quiz_id'])
            file= session["dir"]+"/"+session["logfile"]
            db_user.database_insert(user, session['quiz_id'],file)
            user.record(session['quiz_id'])
        elif (session["record"]==False):
            session["current_question"] = str(int(session['startq'])-1)
            log = db_user.getFilepath(session['user_matric'], session['quiz_id'], session['date'])
            firstime = db_user.getQuesStartTime(session['user_matric'], session['quiz_id'], 1)
            start = db_user.getQuesStartTime(session['user_matric'], session['quiz_id'], session['startq'])
            end = db_user.getQuesEndTime(session['user_matric'], session['quiz_id'], session['endq'])
            starttime = str(int(start) - int(firstime))
            endtime = str(int(end) - int(firstime))
            user.playback(log,starttime,endtime)

        return redirect(url_for('question'))



@app.route('/question', methods=['POST', 'GET'])
def question():

    if request.method== 'GET':

        session["start_ques"] = str(int(round(time.time() * 1000))  )
        #if "current_question" not in session:

        if int(session["current_question"]) >= len(session['ques']):
          if(session['record']==True):
            db_user.setCompleted(session['user_matric'],session['quiz_id'])
          return render_template("success.html")

        elif (session['record']==False and (int(session["current_question"]))>(int(session['endq'])-1)):
             return render_template("success.html")

        return render_template(session['ques'][int(session["current_question"])])


    elif request.method == 'POST':
        ans= str(request.form['test'])
        session["end_ques"] = str(int(round(time.time() * 1000)))
        if(session['record'])==True:
          db_user.insert_ans(session['user_matric'],session["quesid"][int(session["current_question"])],ans,session["start_ques"],session["end_ques"],(session['quiz_id']))
        session["current_question"]=  str(int(session["current_question"])+1)
        return redirect(url_for('question'))




@app.route('/coord', methods=['POST', 'GET'])
def trial():
    id = request.form['id']
    typ= request.form['type']
    ques = request.form['ques']
    yes = request.form['yes']
    no = request.form['no']
    maybe = request.form['maybe']
    audio = request.form['audio']

    video = request.form['video']

    image = request.form['image']
    rate = request.form['rate']
    text = request.form['text']
    sub = request.form['sub']
    viddur= request.form['viddur']
    auddur = request.form['auddur']

    if(session['record'])==True:
        if(not db_user.quesExist(id,typ)):
            db_user.insert_text_option(id,typ,ques,yes,no,maybe,rate,text,image,audio,video,sub,auddur,viddur)
        else:
            db_user.updateQues(id,typ,ques,yes,no,maybe,rate,text,image,audio,video,sub,auddur,viddur)

    return render_template("trial.html")


if __name__ == '__main__':
    app.run()