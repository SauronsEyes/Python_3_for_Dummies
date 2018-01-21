import numpy
import matplotlib.pyplot as plt


    

data_x=[2,4,3,6,8,8,10] #Change Data as per Requirement
data_y=[10,9,6,6,6,3,2]

meanx = numpy.mean(data_x)
meany = numpy.mean(data_y)

plt.xlabel('x')
plt.ylabel('y')
plt.scatter(data_x,data_y)

xsub=[]
ysub=[]

for x in data_x:
    subs = x-meanx
    xsub.append(subs)
    
for y in data_y:
    subs = y-meany
    ysub.append(subs)
    


xmult = []
xsqr = []
index=0

for x2 in xsub:
    mult = x2*ysub[index]
    xmult.append(mult)
    index = index+1
    
for x3 in xsub:
    sqrs=x3**2
    xsqr.append(sqrs)
    
    
sumx=numpy.sum(xmult)
sumy=numpy.sum(xsqr)

slope = sumx/sumy
y_intercept = meany-(slope*meanx)

plots = plt.gca()
xvalues = numpy.array(plots.get_xlim())
yvalues = y_intercept + slope * xvalues
plt.plot(xvalues, yvalues)


plt.show()
