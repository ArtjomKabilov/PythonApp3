import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fail=open("dannie.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()
title = "Данные о ИТ безопасности"
plt.grid(True)
color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)
plt.show()

x1 = np.arange(-12,13)
y1 =(-1/18)*(x1**2)+12
plt.plot(x1,y1,color='black',linestyle='-',marker='')
x2 = np.arange(-4,5)
y2=(-1/8)*(x2**2)+6
plt.plot(x2,y2,color='black',linestyle='-',marker='')
x3 = np.arange(-12,-3)
y3=(-1/8)*(x3+8)**2+6
plt.plot(x3,y3,color='black',linestyle='-',marker='')
x4 = np.arange(4,13)
y4=(-1/8)*(x4-8)**2+6
plt.plot(x4,y4,color='black',linestyle='-',marker='')
x5 = np.arange(-4,-0.2,0.1)
y5=2*(x5+3)**2-9
plt.plot(x5,y5,color='black',linestyle='-',marker='')
x6 = np.arange(-4,0.1,0.2)
y6=1.5*(x6+3)**2-10
plt.title("Зонтик")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(axis="y",c="black",alpha=.4,lw=5,ls="-")
plt.xticks(np.arange(-15,16,5))
plt.yticks(np.arange(-15,16,5))
plt.grid(True)


plt.savefig("my_image.png") 
plt.show()


x1 = np.arange(-9,0)
y1 =(-1/8)*(x1+9)**2+8
plt.plot(x1,y1,color='black',linestyle='-',marker='')
x2 = np.arange(1,10)
y2=(-1/8)*(x2-9)**2+8
plt.plot(x2,y2,color='black',linestyle='-',marker='')
x3 = np.arange(-9,-7)
y3=7*(x3+8)**2+1
plt.plot(x3,y3,color='black',linestyle='-',marker='')
x4 = np.arange(8,10)
y4=7*(x4-8)**2+1
plt.plot(x4,y4,color='black',linestyle='-',marker='')
x5 = np.arange(-8,0)
y5=(1/49)*(x5+1)**2
plt.plot(x5,y5,color='black',linestyle='-',marker='')
x6 = np.arange(1,9)
y6=(1/49)*(x6-1)**2
plt.plot(x6,y6,color='black',linestyle='-',marker='')
x7 = np.arange(-8,0)
y7=(-4/49)*(x7+1)**2
plt.plot(x7,y7,color='black',linestyle='-',marker='')
x8 = np.arange(1,9)
y8=(-4/49)*(x8-1)**2
plt.plot(x8,y8,color='black',linestyle='-',marker='')
x9 = np.arange(-8,-1)
y9=(1/3)*(x9+5)**2-7
plt.plot(x9,y9,color='black',linestyle='-',marker='')
x10 = np.arange(2,9)
y10 =(1/3)*(x10-5)**2-7
plt.plot(x10,y10,color='black',linestyle='-',marker='')
x11 = np.arange(-2,0)
y11=-2*(x11+1)**2-2
plt.plot(x11,y11,color='black',linestyle='-',marker='')
x12 = np.arange(1,2)
y12 =-2*(x12-1)**2-2
plt.plot(x12,y12,color='black',linestyle='-',marker='')
x13 = np.arange(-1,1)
y13=-4*(x13**2)+2
plt.plot(x13,y13,color='black',linestyle='-',marker='')
x14 = np.arange(-1,1)
y14 =4*(x14**2)-6
plt.plot(x14,y14,color='black',linestyle='-',marker='')
x15 = np.arange(-2,1)
y15=-1.5*x15+2
plt.plot(x15,y15,color='black',linestyle='-',marker='')
x16 = np.arange(0,3)
y16 =1.5*x16+2
plt.plot(x16,y16,color='black',linestyle='-',marker='')


plt.title("Бабочка")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(axis="y",c="black",alpha=.4,lw=5,ls="-")
plt.xticks(np.arange(-15,16,5))
plt.yticks(np.arange(-15,16,5))
plt.grid(True)


plt.savefig("my_image2.png") 
plt.show()  
