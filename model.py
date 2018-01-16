import os
import subprocess
import datetime

class User:

   def __init__(self,name,matric):
        self.name=name
        self.matric=matric
        self.logfile=""
        self.pathdir=""


   def getName(self):
       """Return user instance of id, return None if not exist"""
       try:
           return self.name
       except UserWarning:
           return None

   def getMatric(self):

       try:
           return self.matric
       except UserWarning:
           return None


   def createDir(self,quizid):
       self.pathdir = os.path.dirname(os.path.abspath(__file__)) + "/subjects/{0}${1}".format(self.matric,datetime.datetime.now().strftime("%Y-%m-%d"))
       if not os.path.exists(self.pathdir):
            os.makedirs(self.pathdir)
       return self.pathdir


   def setLogfile(self,quizid):
       self.logfile = self.matric + quizid + ".txt"
       return self.logfile


   def record(self,quizid):
      self.setLogfile(quizid)
      subprocess.Popen(['python', 'keym.py',self.pathdir,self.logfile])


   def playback(self, log,starttime,endtime):
     subprocess.Popen(['python', 'play.py',log, starttime,endtime])



