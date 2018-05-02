import pythoncom, pyHook
import sys
dir= sys.argv[1]
file = sys.argv[2]
filename= dir+"/"+file

def OnMouseEvent(event):
    # called when mouse events are received
    fo = open(filename, "a")


    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
   # print 'WindowName:',event.WindowName
    print 'Position:',event.Position
   # print 'Wheel:',event.Wheel
  #  print 'Injected:',event.Injected
    print '---'
    fo.write(event.MessageName)
    fo.write(";")
    fo.write(str(event.Time))
    fo.write(";")
    fo.write(str(event.Position))
    fo.write("\n")

   # return True to pass the event to other handlers
    return True


def OnKeyboardEvent(event):
    fo = open(filename, "a")

    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    #print 'Extended:', event.Extended
    #print 'Injected:', event.Injected
    #print 'Alt', event.Alt
    #print 'Transition', event.Transition
    print '---'

    fo.write(event.MessageName)
    fo.write(";")
    fo.write(str(event.Time))
    fo.write(";")
    fo.write(str(event.Key))
    fo.write("\n")
# return True to pass the event to other handlers
    return True


# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
hm.MouseAll = OnMouseEvent
# set the hook
hm.HookMouse()

pythoncom.PumpMessages();
