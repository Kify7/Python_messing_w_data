
#READING THE *WHOLE* TXT
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

#SEARCHING THROUGH A FILE
fhand = open('mbox-short.txt')
for line in fhand :
    if line.startswith('From') :
        print(line) #running this program will also print the \n character of the newlines in between:
                    #that is: the print statement generates one more newline(\n) than the txt has
                    #we deal with this with the function for white spaces: rstrip()

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('From') :
        print(line)


#SKIPPING WITH CONTINUE: the same blck of code, using the inverse of startswith:

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)

#USING in TO SELECT LINES
#We can look for a string, anywhere on a line , as our selection criteria:
fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not '@utc.ac.za' in line :
        continue
    print(line)