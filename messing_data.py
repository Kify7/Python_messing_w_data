#using mailbox format
#Data in txt format
#Before we can read the contents of the file, we must tell Python which file we are going to work with
#and what we will be doing with it.
#This is done with the open() function
#open() returns a "file handle" - a variable used yo perom operations on the file
#Similar to "File ->Open" in a word procesor.

# handle = open(filename,mode)
#returns a handle used to manipulate the .txt file
#filename is a string
#mode is optional and should be 'r' if we are planning to read the file, and 'w' if we are going to
#write on the file.

fhand = open('mbox-short.txt','r')
print(fhand)

#The Newline Character
#We use a special character claled "newline" to indicate when a line ends
#We represent it as \n in strings
#Newline is still one character NOT TWO

stuff = 'Hello\nworld!'
print(stuff)

cosa = 'X\nY'
print(len(cosa))
  
#FILE PROCESING
#A text file has newlines at the end of each line



