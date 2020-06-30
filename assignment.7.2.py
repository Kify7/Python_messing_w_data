#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fname = open(fname)
count = 0
lista = [];
for line in fname :
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    count = count + 1
    xfile = float(line[20:])
    lista.append(xfile)

add= 0
for element in lista :
    add = add + element
    average = add / count
    rounded = round(average, 15)
print('Average spam confidence:', rounded)