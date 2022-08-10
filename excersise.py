import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,'o:r',mec='g',mfc='g')
plt.show()




x = np.array([12,14,16,18,20,22,24])
y = np.array([100,200,250,400,300,450,500])

plt.plot(x, y)

plt.xlabel("Temperature (celsius)")
plt.ylabel("Sales")

plt.show()




x1 = [10,20,30]
y1 = [10,20,30]
plt.plot(x1, y1, label = "line 1")

x2 = [30,40,50]
y2 = [30,40,50]
plt.plot(x2, y2, label = "line 2")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('Two Line plot')

plt.legend()
plt.show()




# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

# Get the angles from 0 to 2 pie (360 degree) in narray object
X = np.arange(0, math.pi*2, 0.05)

# Using built-in trigonometric function we can directly plot
# the given cosine wave for the given angles
Y1 = np.sin(X)
Y2 = np.cos(X)
Y3 = np.tan(X)
Y4 = np.tanh(X)

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2)

# For Sine Function
axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Sine Function")

# For Cosine Function
axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Cosine Function")

# For Tangent Function
axis[1, 0].plot(X, Y3)
axis[1, 0].set_title("Tangent Function")

# For Tanh Function
axis[1, 1].plot(X, Y4)
axis[1, 1].set_title("Tanh Function")

# Combine all the operations and display
plt.show()






import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='blue',width = 0.4)

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()




import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}

courses = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.barh(courses, values, color ='red')

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()




import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}
color=("red","yellow","maroon","green","black","cyan")
courses = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color =color)

plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()




import numpy as np
import matplotlib.pyplot as plt

y1 = [22,30,35,35,26]
y2 = [25,32,30,35,29]
x_labels = ['G1','G2','G3','G4','G5']
x1 = np.arange(5)
width = 0.40

plt.bar(x1-0.2,y1,color="green",width=width,label='Men')
plt.bar(x1+0.2,y2,color="red",width=width,label='Women')
plt.xticks(x1,x_labels)



plt.xlabel("Person")
plt.ylabel("Scores")
plt.legend()

plt.title("scores by group and gender")
plt.show()






import matplotlib.pyplot as plt
import numpy as np

y = np.array([22.2,17.6,8.8,8,7.7,6.7])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]

plt.pie(y, labels = mylabels)
plt.show()






import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('9_data.csv')
country_data = df["country"]
medal_data = df["gold_medal"]


plt.pie(medal_data, labels=country_data)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show() 






import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
s = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

plt.scatter(x, m,label="maths marks")
plt.scatter(x, s,label="science marks")
plt.legend(loc='upper right')

plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter plot")
plt.show() 
