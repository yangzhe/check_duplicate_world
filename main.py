# _*_ coding: utf-8 _*_
#上面一行确保utf-8编码，汉字支持。

def test():
    global NAME;
    NAME = "test!";
    return NAME;

f = open("text.txt")
duplicated = 0;

line = f.readline()
while line:
    #print line+"\n",                 #, ignore line change symbol  #print(line, end= '')       # in python 3
    wordlist = line.split();
    tmplen = len(wordlist);
    if tmplen>0:
      prev = wordlist[0];
    if tmplen==0:
      prev='' 
    cur = '';
    for i in range(1,len(wordlist)):
        cur = wordlist[i]
        if prev == cur:
            print "Duplicated Happened AT: " + cur + " and " + prev;
            duplicated = 1;
            print line  
        prev = cur;
    line = f.readline()
f.close()
if duplicated!=1:
    print "Great! No duplicated words found!"


