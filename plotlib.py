import matplotlib.pyplot as plt
#plt.plot([1,2,3,4],[4,8,6,1],'-o') #adding dot and line
#plt.plot([5,6,7,8],'-go') #addind red and dot line
#plt.plot([9,10,11,12],'-ro')
#plt.title("Design by amogh")
#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.plot([1,2,3,44,5,])
##x=[1,2,3,4,]
##y=[9,7,8,11
##plt.plot(x,y)
##plt.xlabel("Roll")
##plt.ylabel("Mark")
x=["sci","m1","sst"]
y=[100,95,88]
plt.plot(x,y,label="vedant")

y1=[13,55,89]
plt.plot(x,y1,label="shruti")

y2=[40,45,88]
plt.plot(x,y2,label="pranav")

plt.legend()

plt.show()