#USING in TO SELECT LINES
#We can look for a string, anywhere on a line , as our selection criteria:
xfile = open('mbox-short.txt')
for line in xfile :
    line = line.strip()
    if not '@uct.ac.za' in line :
        continue
    print(line)

fname = input('Enter file name: ')
try :
    fhand = open(fname)
except :
    print('file: ',fname , 'cannot be oppened')
    quit()
    
count = 0
for line in fhand :
    if line.startswith ('Subject: ') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


