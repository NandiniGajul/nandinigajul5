#writing in file 
with open("text.txt","w",encoding='utf-8')as f:
    f.write("hello")
    f.close()
    f = open("text.txt","r")
print(f.read())

#reading file
f = open('text.txt','r',encoding='utf-8')
print(f.read())

#closing opened file
f = open("text.txt","r",encoding='utf-8')
print(f.read())
f.close()




#reading file
f = open('text.txt','r')
print(f.read())

#writing in file 
f = open("text.txt","w")
f.write("fileoperation")
f.close()
f = open("text.txt","r")
print(f.read())

#closing opened file 
f = open("text.txt","r")
print(f.read())
f.close() 
