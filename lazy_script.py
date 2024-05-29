file1=open("file1.txt","r")
file2=open("file2.txt","r")
file3=open("file3.txt","w")


file1_content=file1.readline()
file1_words=file1_content.split()

file2_content=file2.read()
file2_words=file2_content.split()

for words in file1_words:
   if words in file2_words:
      value=words.replace(words,"samecode")   
      value=" "+ value+ str(file2_words.index(words)) +" "
      file3.write(value)
      
   else:
      words= " "+ words + " "
      file3.write(words)
# print(file3)      
file3.seek(0)
file3.close()
file3=open("file3.txt","r")
file3_content=file3.read() 
# print(file3_content)
file3_words=file3_content.split() 	
# print(file3_words)

for i in range(0,len(file3_words)):
   if "samecode" in file3_words[i]:
    index = int(file3_words[i][8:])
    #print(second[ind])
    file3_words[i] = file2_words[index]
print(file3_words)