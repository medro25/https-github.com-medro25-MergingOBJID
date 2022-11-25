file1 = open('CopyFailedFile.txt', 'r',encoding="utf8")
file2= open('NewCopyFailedFile1.txt', 'r',encoding="utf8")
Lines_Copyfailedfile = file1.readlines()
new_line = '\n'


#Reading CopyFailedFile
for line in Lines_Copyfailedfile:
    #print(line)
    #extract the OBJID
    x= line.split("*")
   # print(x)
    for i in x :
        #print(i)
# Catogorize the elements
     d=i.split("\t")
   # print(d)
# Object Id is the last index of the string
    objid=d[-1]
    #print(objid)
#create 
    #with open('objid.txt','a') as f:
     # if objid.startswith('%'):
       ## print(objid,file=f,end="")
      #if not objid.startswith('%'):
        # print((new_line),file=f,end="")
        # f.close()
# reading the NewCopyfailed file
Lines_NewCopyFailedFile=file2.readlines()
#for l in Lines_NewCopyFailedFile:
 #    with open('lines.txt', 'a') as file:
  #     print(l,end="",file=file)
   #    file.close()
 
print(len(Lines_Copyfailedfile))  

# Merging the OBJID with Newcopy faile file lines
file3= open('objid.txt', 'r',encoding="utf8")
Lines_obj = file3.readlines()
with open("z.txt","w") as zh:
 for i in range(len(Lines_Copyfailedfile)):
        line = Lines_NewCopyFailedFile[i].strip() + ' ' + Lines_obj[i]
        zh.write(line)
        print(line)
         