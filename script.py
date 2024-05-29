file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

file1_content = file1.read()
file2_content = file2.read()

file1_words = file1_content.split()
file2_words = file2_content.split()


file3_content = ''
for word in file1_words:
    if word in file2_words:
        file3_content += "[samecode" + str(file2_words.index(word)) +" " +"] "
    else:
        file3_content += word + " "
print(file3_content)
x=str(file3_content)
file3 = open('file3.txt', 'w')
file3.write(x)
file3.close()



file3_again=open('file3.txt', 'r')
file3_content = file3_again.read()
file3_words = file3_content.split()
# print(file3_words)
for i in range(0,len(file3_words)):
    if 'samecode' in file3_words[i]:
        # print(i)
        index=int(file3_words[i][9:])
        index=file3_words[index]
        








