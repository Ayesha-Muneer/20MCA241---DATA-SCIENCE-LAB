#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#ploting a simple graph
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])
plt.plot(x,y)
plt.show()


# In[3]:


#plot a dotted graph
plt.plot(x,y,'o')
plt.show()


# In[4]:


#plot graph with negative values
x=np.array([-1,-3,2,4])
y=np.array([1,3,-2,-4])
plt.plot(x,y)
plt.show()


# In[5]:


#plot graph with negative values
x=np.array([-1,-3,2,4])
y=np.array([1,3,-2,-4])
plt.plot(x,y,'*:y')
plt.show()


# In[6]:


#plot graph with label
x=np.array([1,2,3,4])
y=np.array([85,90,88,75])
plt.xlabel("Student")
plt.ylabel("Mark")
plt.plot(x,y)
plt.show()


# In[7]:


plt.scatter(x,y)


# In[8]:


#plot graph with marker
x=np.array([1,2,3,4])
y=np.array([85,90,88,75])
plt.xlabel("Student")
plt.ylabel("Mark")
plt.plot(x,y,marker='o')
plt.show()


# In[9]:


#plot graph with limit
x=np.array([1,2,3,4,5,6,7])
y=np.array([85,50,28,75,40,32,12])
plt.xlabel("Student")
plt.ylabel("Mark")
plt.ylim(0,100)
plt.plot(x,y)
plt.show()


# In[10]:


#plot graph with legend
x=np.array([1,2,3,4,5,6,7])
y=np.array([85,50,28,75,40,32,12])
plt.xlabel("Student")
plt.ylabel("Mark")
plt.ylim(0,100)
plt.plot(x,y)
plt.legend("Single line")
plt.show()


# In[11]:


#sin and cos value upto limit 7np
x=np.arange(0,5*np.pi,1) 
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s,label="sin")
plt.plot(x,c,label="cos")
plt.legend()


# In[12]:


#histogram using random
x=np.random.random((4,2))
plt.hist(x)


# In[13]:


#bar graph
x=np.array([1,2,3,4,5,6,7])
y=np.array([85,50,28,75,40,32,12])
plt.bar(x,y)


# In[14]:


#dictionary to graph
data={'Sree': 94,'Praveena': 96,'Ayesha':85,'Anusha':80,'Shilpa':100,'Ray':30}
name=list(data.keys())
mark=list(data.values())
plt.bar(range(len(data)), mark, tick_label=name)
plt.title("Student report")
plt.xlabel("Name")
plt.ylabel("Mark")
plt.show()


# In[15]:


#subplot in row
x1=np.array([1,2,3,4,5])
y1=np.array([25,50,28,32,12])
plt.subplot(1,2,1)
plt.plot(x1,y1)
x2=np.array([5,4,3,2,1])
y2=np.array([12,34,56,43,21])
plt.subplot(1,2,2)
plt.plot(x2,y2)


# In[16]:


#subplot in column
x1=np.array([1,2,3,4,5])
y1=np.array([25,50,28,32,12])
plt.subplot(2,1,1)
plt.plot(x1,y1)
x2=np.array([5,4,3,2,1])
y2=np.array([12,34,56,43,21])
plt.subplot(2,1,2)
plt.plot(x2,y2)


# In[17]:


#subplot 4
x1=np.array([1,2,3,4,5])
y1=np.array([25,50,28,32,12])
plt.subplot(2,2,1)
plt.plot(x1,y1)
x2=np.array([5,4,3,2,1])
y2=np.array([12,34,56,43,21])
plt.subplot(2,2,2)
plt.plot(x2,y2)
x3=np.array([5,4,3,2,1])
y3=np.array([12,34,56,43,21])
plt.subplot(2,2,3)
plt.plot(x3,y3)
x4=np.array([1,2,3,4,5])
y4=np.array([25,50,28,32,12])
plt.subplot(2,2,4)
plt.plot(x4,y4)


# In[20]:


import csv
with open('C:/Users/admin/Downloads/marks.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)

