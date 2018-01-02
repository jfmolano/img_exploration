
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[13]:


img_amelie = cv2.imread('./imgs/klimt_1.png')


# In[14]:


# In[15]:


# In[18]:


# In[19]:


# In[20]:


img_reshaped = np.reshape(img_amelie, (img_amelie.size//3,3))
img_reshaped = np.array([img_reshaped])


# In[21]:


# In[22]:


resized_image = cv2.resize(img_reshaped, (200, 50)) 


# In[23]:


plt.figure(figsize=(15,5))
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()

