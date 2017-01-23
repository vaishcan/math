#!/usr/bin/python
from random import randint
from datetime import datetime, timedelta
import time
import sys
(correct, wrong, tottime)=(0,0,0)
MAXQUESTIONS=30
FILENAME=".reports/subtractionsreport.txt"
##if (len(sys.argv) > 1):
#  MAXQUESTIONS=int(sys.argv[0])
#print MAXQUESTIONS
#exit()
def genReport():
   d = datetime(1,1,1) + timedelta(seconds=tottime)
   timestring="%d Min %d Sec" % (d.minute, d.second)
   msg  = "\n\n\n    ******Report*******\n"
   msg += "You took [%s] to answer [%s] questions\n" % (timestring,x+1)
   msg += "  Correct Answers %d\n" % correct
   msg += "  Wrong Answers   %d\n" % wrong
   msg += "      Report generated at {0}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
   msg += "\n    *******************\n"
   print msg
   reportsFile=open(FILENAME, 'a')
   reportsFile.write(msg)
   reportsFile.close()

for x in range(0, MAXQUESTIONS):
  num1=randint(1001, 9999)
  num2=randint(1001, 9999)
  if (num2 > num1):
    num1, num2 = num2, num1
  print ("Question %d" % (x+1))
  print ("--------------------")
  print ("             : %04d" % num1)
  print ("           - : %04d" % num2)
  print ("--------------------")
  print ("Difference   :"),
  t1=time.time()
  try:
    ans=raw_input()
    timetaken = time.time()-t1
    if ((num1-num2) == int(ans)):
      print ("*** Correct! ***  You took %d seconds\n" % timetaken)
      correct+=1
    else:
      print ("### Wrong! Expecting %d ###  You took %d seconds\n" % ((num1-num2),timetaken))
      wrong+=1

    if ((x+1==MAXQUESTIONS) or ((ans == 'Q') or (ans == 'q'))):
      genReport()
      exit()
    tottime += timetaken
  except KeyboardInterrupt:
      genReport()
      exit()
  except ValueError:
    print "Oops!  That was no valid number.  Try again..."


