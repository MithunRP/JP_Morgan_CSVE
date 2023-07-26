
# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_0(file):
    pass

def exercise_1(df):
    pass

def exercise_2(df, k):
    pass

def exercise_3(df, k):
    pass

def exercise_4(df):
    pass

def exercise_5(df):
    pass

def exercise_6(df):
    pass

def exercise_7(df):
    pass

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass


# In[2]:


df = pd.read_csv("transactions.csv")


# In[3]:


df.columns


# In[4]:


df.head()


# In[5]:


df.sample(5)


# In[6]:


df.type.unique()


# In[7]:


df.nameDest.value_counts().head(10)


# In[8]:


df[df.isFraud == 1]


# In[9]:


df.groupby("nameDest")["newbalanceDest"].agg("mean").sort_values(ascending=False)


# In[10]:


sns.countplot(x=df.type)
plt.title("Transaction types bar chart")
plt.show()


# In[11]:


sns.countplot(x=df.type, hue=df.isFraud)
plt.title("Transaction types bar chart")
plt.show()


# In[12]:


# def visual_1(df):
#     def transaction_counts(df):
#         # TODO
#         pass
#     def transaction_counts_split_by_fraud(df):
#         # TODO
#         pass

#     fig, axs = plt.subplots(2, figsize=(6,10))
#     transaction_counts(df).plot(ax=axs[0], kind='bar')
#     axs[0].set_title('TODO')
#     axs[0].set_xlabel('TODO')
#     axs[0].set_ylabel('TODO')
#     transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
#     axs[1].set_title('TODO')
#     axs[1].set_xlabel('TODO')
#     axs[1].set_ylabel('TODO')
#     fig.suptitle('TODO')
#     fig.tight_layout(rect=[0, 0.03, 1, 0.95])
#     for ax in axs:
#       for p in ax.patches:
#           ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
#     return 'TODO'

# visual_1(df)


# In[13]:


# def visual_2(df):
#     def query(df):
#         # TODO
#         pass
#     plot = query(df).plot.scatter(x='TODO',y='TODO')
#     plot.set_title('TODO')
#     plot.set_xlim(left=-1e3, right=1e3)
#     plot.set_ylim(bottom=-1e3, top=1e3)
#     return 'TODO'

# visual_2(df)

# In[14]:


def exercise_custom(df):
    # TODO
    pass
    
def visual_custom(df):
    # TODO
    pass

