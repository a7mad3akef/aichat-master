
# coding: utf-8

# # Implementation of LDA and Text Cleaning to 20 News Group Dataset

# ---

# ### Import the required libraries

# In[1]:


import re
import string
import wordcloud
import numpy as np
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.datasets import fetch_20newsgroups
get_ipython().magic('matplotlib inline')


# ### Download and load the dataset

# In[2]:


data = fetch_20newsgroups(subset='test', shuffle=True)


# In[3]:


data.description


# In[4]:


data


# In[5]:


print len(data.target_names)
print data.target_names


# ## Natural Language Processing

# ---

# #### We will demonstrate this with a small pipeline of text processing including:
# 
# > Load the raw text.
# 1. Split into tokens.
# 2. Convert to lowercase.
# 3. Remove punctuation from each token.
# 4. Filter out remaining tokens that are not alphabetic.
# 5. Filter out tokens that are stop words.

# ### Convert all text to string

# In[6]:


data = str(data)


# ### Removal of Punctuation

# In[7]:


text = re.sub("[!@#$%\n^'*)\\(-=]"," ", data)


# ### Tokenize all text data

# In[8]:


tokens = word_tokenize(text)


# In[9]:


tokens = tokens[100:]


# In[10]:


tokens[:10]


# ### Convert to lower case

# In[11]:


tokens = [w.lower() for w in tokens]


# ### Remove remaining tokens that are not alphabetic

# In[12]:


words = [word for word in tokens if word.isalpha()]


# ### Filter out stop words

# In[13]:


stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:100])


# ### Apply Stemming

# In[14]:


from nltk.stem.porter import PorterStemmer
st = PorterStemmer()
words = [st.stem(word) for word in words]


# In[15]:


print words[:100]


# In[16]:


# Set the figure-size
plt.figure(figsize= (20,10))
wordcloud = WordCloud(
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=3000,
                      height=2000
                     ).generate(str(words))
plt.figure(1,figsize=(20, 20))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# In[17]:


from collections import Counter
counts = Counter(words).most_common(20)


# In[18]:


counts


# ## Now, we will apply LDA on the text data

# In[19]:


import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
from pyLDAvis.sklearn import prepare


# In[20]:


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


# In[21]:


vectorizer = TfidfVectorizer()
dtm_tfidf = vectorizer.fit_transform(words)
print(dtm_tfidf.shape)


# In[22]:


# for TFIDF DTM
lda_tfidf = LatentDirichletAllocation(n_components=10,learning_offset=50, max_iter=10)
lda_tfidf.fit(dtm_tfidf)


# In[ ]:


prepare(lda_tfidf, dtm_tfidf, vectorizer)


# #### Creating a Document Term Matrix to be used by LDA

# In[37]:


tf_vectorizer = .CountVectorizer(max_df=0.95, min_df=2, max_features=n_features, stop_words='english')
tf = tf_vectorizer.fit_transform(words)
vocab = tf_vectorizer.get_feature_names()


# ### Initialing and training the LDA model

# In[ ]:


model = lda.LDA(n_topics=20, n_iter=2000, random_state=1)
model.fit(tf)


# In[ ]:


topic_word = model.topic_word_
n = 5
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n+1):-1]
    print('*Topic {}\n- {}'.format(i, ', '.join(topic_words)))


# ### Prints each document along with the most likely topic.

# In[ ]:


doc_topic = model.doc_topic_
for n in range(40):
    topic_most_pr = doc_topic[n].argmax()
    print("\ndoc: {} topic: {}\n{}...".format(n,
                                            topic_most_pr,
                                            titles[n][:50]))

