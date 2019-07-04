from itertools import groupby

def read(file):
    openFile = open(file,"r")
    return openFile.read().split("\n")
    openFile.close()

class Seg:
  def __init__(self,num,char):
    self.num = int(num)
    self.char = char

  def decode(self):
    return self.char*self.num

  def __str__(self):
    return str(self.num).zfill(2)+self.char

def decode(lines):

    codeLines=[]
    for x in lines:
      temp=[]

      for y in range(0,len(x),3):
        temp.append(Seg(x[y:y+2],x[y+2]))
      codeLines.append(temp)

    toReturn=""

    for i in codeLines:
      temp=""
      for x in i:
        temp=temp+ x.decode()
      toReturn=toReturn+temp+"\n"
    return toReturn

def encode(lines):
    
    pelist =[]

    for i in lines:
      pelist.append([''.join(g) for _, g in groupby(i)])
    elist = ""

    for i in pelist:
      temp = ""

      for x in i:
        temp=temp+str(Seg(len(x),x[0]))
      elist=elist+temp+"\n"
      
    return elist
