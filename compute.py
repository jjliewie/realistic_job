import pandas as pd
from math import sqrt
import xlrd
import numpy as np

def euclidean_distance(x,y):
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def cosine_similarity(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/sqrt(sumxx*sumyy)

data = pd.read_excel(r'/Users/julierhee/Desktop/demo.xlsx') 
jobs = []
for row in data:    
    jobs.append(row)
jobs.pop(0)

print('________')

book = xlrd.open_workbook('/Users/julierhee/Desktop/demo.xlsx') 
sheet = book.sheet_by_name('Sheet1')
bayes = book.sheet_by_name('Sheet2')
da = [[sheet.cell_value(c, r) for c in range(1, sheet.nrows)] for r in range(1, sheet.ncols)]
la = [[bayes.cell_value(c, r) for c in range(1, bayes.nrows)] for r in range(1, bayes.ncols)]

print(da)
print(la)

s = 0
for t in la:
  s += t[0]
print(s)

realistic = []
for h in la:
  realistic.append(h[0]/s)

d = []
for i in range(len(jobs)):
  d.append((jobs[i], da[i]))
print(d)

k = [1, 0, 0, 0, 1, 1, 1, 0, 1, 0]

compare = {}
for i in d:
  compare[i[0]] = cosine_similarity(i[1], k)

maximum = [0, 0]
for j, t in compare.items():
  if t > maximum[1]:
    maximum[1] = t
    maximum[0] = j
  print(str(j)+ " : " + str(t))

print("the job that fits your personality best is: " + str(maximum[0]))

realistic_maximum = [0,0]
cnt = 0
for j, t in compare.items():
  if (t * realistic[cnt]) > realistic_maximum[1]:
    realistic_maximum[1] = (t * realistic[cnt])
    realistic_maximum[0] = j
  cnt += 1

print("the job that you can most realistically attain is: " + str(realistic_maximum[0]))

# can i just say that writing this much code took me like 2 hours :(
