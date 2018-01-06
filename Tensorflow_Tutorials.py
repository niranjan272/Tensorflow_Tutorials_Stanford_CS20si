
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[5]:


source_folder = "D:\\Study\\OneDrive - The University of Texas at Dallas\\02 Study\\22 Tensorflow\\"


# In[3]:


hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


# In[4]:


a = tf.add(3,5)
sess = tf.Session()
sess.run(a)


# In[7]:


a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)
with tf.Session() as sess:
    writer = tf.summary.FileWriter("./graphs",sess.graph)
    print(sess.run(x))
    
writer.close()
    

