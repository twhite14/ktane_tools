from colorama import init, Fore, Back

init()  #initialize coloramas

parallel    = raw_input('Parallel Port? (y/n) ')
evenSerial  = raw_input('Even Serial No.? (y/n) ')
twoPlusBatt = raw_input('2 or more batteries? (y/n) ')

colorNo  = Back.RED   + ' No  ' + Back.RESET
colorYes = Back.GREEN + ' Yes ' + Back.RESET


#[led/star][red/blue]
truthTable  = [[1,0,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]

if(parallel.lower() == 'y'):
  truthTable[1][3] = 1
  truthTable[2][2] = 1
  truthTable[3][2] = 1
else:
  if(parallel.lower() != 'n'):
    print 'RESULTS MAY BE INACCURATE'

if(evenSerial.lower() == 'y'):
  truthTable[0][1] = 1
  truthTable[0][2] = 1
  truthTable[0][3] = 1
  truthTable[2][3] = 1
else:
  if(evenSerial.lower() != 'n'):
    print 'RESULTS MAY BE INACCURATE'

if(twoPlusBatt.lower() == 'y'):
  truthTable[2][1] = 1
  truthTable[3][0] = 1
  truthTable[3][1] = 1
else:
  if(twoPlusBatt.lower() != 'n'):
    print 'RESULTS MAY BE INACCURATE'    

#Print a header
print '             White Red  Blue R/B '

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
      printThis += colorYes
    else:
      printThis += colorNo
    
  print printThis
  