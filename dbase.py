import MySQLdb
import datetime


class db:

    def __init__(self, app=None):
        self.con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="root", db="interview")
        self.con.autocommit(True)

    def database_insert(self,user,quiznum,file):
        cur = self.con.cursor()
        cur.execute("INSERT INTO subject(name,matric,intw_num,intw_date,logfile) VALUES(%s,%s,%s,%s,%s);",
                (user.getName(), user.getMatric(), quiznum, datetime.datetime.now().strftime("%Y-%m-%d"), file ))



    def insert_ans(self,user_matric,question_id,ans,start_time,end_time,quizid):
        cur = self.con.cursor()
        cur.execute("INSERT INTO answers(matric,question_id,ans,ques_startTime,ques_endTime,quiz_id,date) VALUES(%s,%s,%s,%s,%s,%s,%s);",(user_matric, question_id,ans,start_time, end_time,  quizid ,str(datetime.datetime.now().strftime("%Y-%m-%d"))))

    def getFilepath(self,user_matric,quizid, date):
        cur = self.con.cursor()
        cur.execute("Select logfile from subject where matric=(%s) and intw_num=(%s) and intw_date=(%s);",( user_matric, quizid, date))
        return cur.fetchall()[0][0]

    def getQuesStartTime(self,user_matric,quizid, startques):
        cur = self.con.cursor()
        cur.execute("Select ques_startTime from answers where matric=(%s) and quiz_id=(%s) and question_id=(%s);",(user_matric, quizid,startques))
        return cur.fetchall()[0][0]

    def getQuesEndTime(self,user_matric,quizid, endques):
        cur = self.con.cursor()
        cur.execute("Select ques_endTime from answers where matric=(%s) and quiz_id=(%s) and question_id=(%s);",(user_matric, quizid,endques))
        return cur.fetchall()[0][0]

    def insert_text_option(self,id,typ,ques,yes,no,maybe,rate,text,image,audio,video,sub,auddur,viddur):
        cur = self.con.cursor()
        cur.execute("INSERT INTO question(id,typ,ques,yes,nop,maybe,rate,textt, image,audio,video,sub,audio_dur , video_dur) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,typ,ques,yes,no,maybe,rate,text, image,audio,video,sub,auddur,viddur))

    def quesExist(self,id,typ):
        cur = self.con.cursor()
        exist = cur.execute(  "Select * from question where id=(%s) and typ=(%s);",(id, typ))
        return exist

    def updateQues(self,id, typ, ques, yes, no, maybe, rate, text, image, audio, video, sub,auddur,viddur):
        cur = self.con.cursor()
        cur.execute("Update question set ques=(%s),yes=(%s),nop=(%s),maybe=(%s),rate=(%s),textt=(%s), image=(%s),audio=(%s),video=(%s),sub=(%s),audio_dur=(%s),video_dur=(%s) where id=(%s) and typ=(%s);",(ques, yes, no, maybe, rate, text, image, audio, video, sub,auddur,viddur, id, typ))

    def setCompleted(self,matric,quizid):
        cur = self.con.cursor()
        cur.execute("INSERT INTO completed(matric,quizid, date) VALUES(%s,%s,%s);",(matric,quizid,str(datetime.datetime.now().strftime("%Y-%m-%d"))))
