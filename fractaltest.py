import random as r
import os
import time
import sys

max = 32 # number of iterations
states = [""]
rules = [i[2:].zfill(8) for i in map(bin,range(2**8))]
states = [i[2:].zfill(3) for i in map(bin,range(2**3))]
punct = """!"#$%&'*+,-./:;<=>?@\^_`|~"""
speed = 0.005

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)

randints= r.randint(0,columns) # number of random inital 1s

def rint():
    return r.randint(0,255)
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
def ca(steprule=90):
   def rulecheck(l):
       bits = ''.join([str(ca[l-1]),str(ca[l]),str(ca[l+1])])
       k = states.index(bits)
       result = str(rules[steprule][k])
      #print(str(rules[rule][k]))
       return(result)
   ''' Celluar automata with Python - K. Hong'''
   # 64 Boolean - True(1) : '*'
   #            - False(0): '-'
   # Rule - the status of current cell value is True
   # if only one of the two neighbors at the previous step is True('*')
   # otherwise, the current cell status is False('-')
   # list representing the current status of 64 cells
   ca = [0] * columns
   for i in [r.randrange(columns) for i in range(randints)]:
       ca[i] = 1

   # new Cellular values
   ca_new = map(str,ca[:])

   # dictionary maps the cell value to a symbol
   dic = {'0':' ', '1':'*'}

   # initial draw - step 0
   delay_print(''.join( [dic[e] for e in ca_new]))
   # additional 31 steps
   step = 1
   while(True):
      ca_new = []
      # loop through 0 to 63 and store the current cell status in ca_new list
      for i in range(0,columns):
         # inside cells - check the neighbor cell state
         if i > 0 and i < (columns - 1):
            ca_new.append(rulecheck(i))

         # left-most cell : check the second cell
         elif(i == 0):
            if ca[1] == 1:
               ca_new.append(1)
            else:
               ca_new.append(0)

         # right-most cell : check the second to the last cell
         elif(i == (columns - 1)):
            if ca[(columns - 2)] == 1:
               ca_new.append(1)
            else:
               ca_new.append(0)
      ca_new = map(str,ca_new)
      # draw current cell state
     # print(''.join(map(str,ca_new)))
      delay_print(''.join( [dic[e] for e in ca_new]))
      if(step % 30 == 0):
          steprule = rint()
          dic['1'] = r.choice(punct)
          delay_print(str(steprule) + "~"*(columns-len(str(steprule))))
      # update cell list
      ca = ca_new[:]

      # step count
      step += 1

if __name__ == '__main__':
   ca(steprule=r.randint(0,255))
