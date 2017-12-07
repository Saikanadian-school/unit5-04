from __future__ import division 
import ui

numlist = []

def averagearray(array_numbers = []):
    arraysum = 0
    for avalue in array_numbers:
      print avalue
      arraysum = arraysum + avalue
    averagenumbers = arraysum / len(array_numbers)
    return averagenumbers

def addbutton(sender):
    global numlist
    if (view['textfield1'].text == ''):
      view['errorlabel'].text = 'please enter a mark' 
      return
    if (int(view['textfield1'].text) > 100 or int(view['textfield1'].text) < 0):
      view['errorlabel'].text = 'please enter 0-100'
      return 
    numlist.append(int(view['textfield1'].text))
    view['markview'].text = view['markview'].text + view['textfield1'].text +'\n'
    view['textfield1'].text = str()
    view['errorlabel'].text = str()

def averagebutton(sender):
    global numlist
    view['averagelabel'].text = str(averagearray(numlist))

view = ui.load_view()
view.present('fullscreen')

#view['markview'].text = 'hello world'
#print view['markview'].text

