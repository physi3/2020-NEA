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

#print(decode(encode(read("LogoArt.txt")).split("\n")))
while True:
  while True:
    try:
      inp = int(input("\nEnter RLE [0]\nDisplay ASCII art [1]\nConvert to ASCII art [2]\nConvert to RLE [3]\nQuit [4]\n>>> "))

      if inp > 4:
        print("That is not an option, enter a new number")
      else:
        break
    except:
      print("That is not an option, enter a new number")     
  if inp == 0: #Enter RLE
    while True:
      try:
        a = int(input("\nHow many lines of RLE would you like to enter? (Must be more than 2)\n>>> "))

        if a <= 2:
          print("\nThat is not an option, enter a new number\n")
          continue
        else:
          break
      except:
        print("\nThat is not an option, enter a new number\n") 
    RLE = []    
    while True:
      try:
        for i in range(a):
          RLE.append(input("\nEnter your line of RLE\n>>> "))
        input("Here is your art: \n\n"+decode(RLE)+"\nPress enter to return to the main menu.")
        break
      except:
        print("\nThat is not valid, please try again\n")
  if inp == 1: #Display ASCII art
    while True:
      try:
        inp = input("\nEnter ASCII art text file\n>>> ")
        openFile = open(inp,"r")
        print("\nHere's your ASCII art:\n\n"+openFile.read())
        openFile.close()
        input("Press enter to continue")
        break
      except:
       print("That is not an option, enter a new file") 
  if inp == 2: #Convert to ASCII art
    while True:
      try:
        inp = input("\nEnter RLE text file\n>>> ")
        print("\nHere's your ASCII art:\n\n"+decode(read(inp)))
        input("Press enter to continue")
        break
      except:
       print("That is not an option, enter a new file") 
  if inp == 3: #Convert to RLE
    while True:
      try:
        inp = input("\nEnter ASCII art text file\n>>> ")
        openFile = open("NewRLE.txt","w+")
        openFile.write(encode(read(inp)))
        openFile.close()

        openFile = open(inp,"r")
        leng=len(openFile.read())
        openFile.close()

        print("\nYour RLE was stored in NewRLE.txt and "+str(leng-len(encode(read(inp))))+" characters were dropped in compression.\n")
        input("Press enter to continue\n")
        break
      except:
       print("That is not an option, enter a new file")
  if inp == 4: #Quit
    print("Okay, bye then.")  
    break
