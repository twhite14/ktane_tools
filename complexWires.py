#complexWires.py
#Display a truth table for the complex wires in the game Keep Talking and Nobody Explodes

#Check whether colorama is installed, set variabeles appropriately
try:
  from colorama import init, Back
  init()
  cutNo  = Back.RED   + ' No  ' + Back.RESET
  cutYes = Back.GREEN + ' Cut ' + Back.RESET
except ImportError:
  cutNo  = ' No  '
  cutYes = ' Cut '
  print 'You should seriously consider installing colorama.'

#[led/star][red/blue]
truthTable  = [[1,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]

#Prompt the user for information about the bomb (Parallel ports, Serial number, Batteries)
invalidInput = True
while(invalidInput):
  parallel = raw_input('Parallel Port? (y/n) ')
  if(parallel.lower() == 'y'):
    truthTable[1][3] = 1
    truthTable[2][2] = 1
    truthTable[3][2] = 1
    invalidInput = False
  elif(parallel.lower() == 'n'):
    invalidInput = False
  else:
    print 'Invalid input, retry.'

invalidInput = True
while(invalidInput):
  evenSerial  = raw_input('Even Serial No.? (y/n) ')
  if(evenSerial.lower() == 'y'):
    truthTable[0][1] = 1
    truthTable[0][2] = 1
    truthTable[0][3] = 1
    truthTable[2][3] = 1
    invalidInput = False
  elif(evenSerial.lower() == 'n'):
    invalidInput = False
  else:
    print 'Invalid input, retry.'

invalidInput = True
while(invalidInput):
  twoPlusBatt = raw_input('2 or more batteries? (y/n) ')
  if(twoPlusBatt.lower() == 'y'):
    truthTable[2][1] = 1
    truthTable[3][0] = 1
    truthTable[3][1] = 1
    invalidInput = False
  elif(twoPlusBatt.lower() == 'n'):
    invalidInput = False
  else:
    print 'Invalid input, retry.'

#Print a header
print '\r\n             White Red  Blue R/B '

for x in xrange(0,4):
  if(x == 0):
    printThis = 'No LED, No * '
  elif(x == 1):
    printThis = 'No LED,    * '
  elif(x == 2):
    printThis = '   LED, No * '
  else:
    printThis = '   LED,    * '
  for y in xrange(0,4): 
    if(truthTable[x][y] == 1):
      printThis += cutYes
    else:
      printThis += cutNo
    
  print printThis
  