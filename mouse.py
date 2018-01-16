import pythoncom, pyHook
import datetime
import simplejson
from flask import Flask
from flask import  session

app = Flask(__name__)
a=[]
pos=[]


def OnMouseEvent(event):
    # called when mouse events are received
    #k= datetime.datetime.now()
    #l= "%s:%s." % (k.minute, k.second)
    #if ( l== m):
     #   print "start"
    #if (l == n):
     #   print "equal"
    #print datetime.datetime.now()
    fo = open('log1.txt', 'a')

    fo.write(event.MessageName)
    fo.write(";")
    fo.write(str(event.Position))
    fo.write("\n")
    #pos=str(event.Position)
    #msg=event.MessageName
    #seq=(msg,pos)
    #s=";"
    #joining= s.join(seq)
    #print joining
    #fo.write(joining)

    a.append(event.MessageName)
    pos.append(event.Position)
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    #print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    x,y= event.Position
    print 'x:',x
    print 'y:',y
    print '---'
    # print 'Wheel:',event.Wheel
  #  print 'Injected:',event.Injected

   # print ("messages array:", a)
    #print ("positions array:", pos)


    # Close opend file

# return True to pass the event to other handlers
    return True




# create a hook manager
hm = pyHook.HookManager()

#x= datetime.datetime.now()+datetime.timedelta(0,10)
#y=  x + datetime.timedelta(0,1)
#print x
#print y
# watch for all mouse events
#m= "%s:%s." % (x.minute, x.second)
#print m
#n= "%s:%s." % (y.minute, y.second)
hm.MouseAll = OnMouseEvent
# set the hook
hm.HookMouse()
# wait forever
pythoncom.PumpMessages()

