
#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
 
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip().upper()
    print (line)


#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
a = 0
n = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    a = a + float(line.split(":")[1])
    n = n+1
avg = a/n
print("Average spam confidence:" , avg)


#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.split()
    for i in temp:
        if i in lst: 
            continue
        else: 
            lst.append(i)
lst.sort()            
print(lst)


#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From") : 
        continue
    if line.split()[0] == "From" :
        temp = line.split()[1]
        count = count + 1
        print(temp)

print("There were", count, "lines in the file with From as the first word")

#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
fh = open(fname)

sender = dict()

for line in fh:
    if not line.startswith("From") : 
        continue
    if line.split()[0] == "From" :
        temp = line.split()[1]
        sender[temp] = sender.get(temp,0) + 1

max_sender = None
max_sent = None
for person,count in sender.items():
    if max_sent is None or count > max_sent:
        max_sent = count
        max_sender = person
print(max_sender, max_sent)

#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
fh = open(fname)

lst = list()
counts =  dict()
for line in fh:
    if not line.startswith("From") :
        continue
    if line.split()[0] ==  "From" :
        temp = line.split()[5]
        hour = temp.split(':')[0]
        counts[hour] = counts.get(hour,0) + 1

for key, val in counts.items():
    new_tup = (key,val)
    lst.append(new_tup)

lst = sorted(lst)

for key,val in lst :
    print(key,val)
