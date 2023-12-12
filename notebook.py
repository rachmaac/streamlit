#!/usr/bin/env python
# coding: utf-8

# # Proyek Analisis Data: E-Commerce Public Dataset
# - Nama:Rachma Chrysanti
# - Email: r.chrysanti@gmail.com
# - Id Dicoding: rachmaac

# ## Menentukan Pertanyaan Bisnis

# - Bagaimana sentimen analisis dari review para pembeli?
# - Kata positif dan negatif apa yang sering muncul dari review?
# - Berapa tingkat akurasi model yang digunakan?

# ## Menyaipkan semua library yang dibuthkan

# In[151]:

from IPython import get_ipython
pip install matplotlib
get_ipython().system('pip install matplotlib')


# In[199]:


get_ipython().system('pip install statsmodels')


# In[200]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm


# ## Data Wrangling

# ### Gathering Data

# In[243]:


data="C:/Data Rachma/latihan/dicoding/archive/olist_order_reviews_dataset.csv"
df = pd.read_csv(data, encoding='latin1')
data="C:/Data Rachma/latihan/dicoding/archive/olist_order_payments_dataset.csv"
df_pay = pd.read_csv(data, encoding='latin1')


# ### Assessing Data

# In[3]:


print(df)


# ### Cleaning Data

# In[4]:


df.isna().sum()


# In[5]:


df[df.isna().any(axis=1)]


# In[8]:


df2 = df.dropna()


# In[9]:


df2


# In[ ]:


df = df.astype(str)


# ## Exploratory Data Analysis (EDA)

# ### Explore ...

# Average of review score

# In[108]:


df2['review_score'].count()


# In[109]:


bintang1 = df2[df2['review_score'] == 1]['review_score'].count()
bintang2 = df2[df2['review_score'] == 2]['review_score'].count()
bintang3 = df2[df2['review_score'] == 3]['review_score'].count()
bintang4 = df2[df2['review_score'] == 4]['review_score'].count()
bintang5 = df2[df2['review_score'] == 5]['review_score'].count()


# In[110]:


print('Skor bintang 1 - 5')
print('1 =', bintang1)
print('2 =', bintang2)
print('3 =', bintang3)
print('4 =', bintang4)
print('5 =', bintang5)
print ('total =', bintang1 + bintang2 + bintang3 + bintang4 + bintang5)


# In[181]:


mean = df2['review_score'].mean()
print(df2['review_score'].mean())


# In[192]:


# Filter komentar review dengan review_score = 1
komentar_score_1 = df2[df2['review_score'] == 1]['review_creation_date']

# Tampilkan komentar review dengan review_score = 1
for komentar in komentar_score_1:
    print(komentar)


# In[193]:


komentar_score_1


# Average of review answer time

# In[112]:


pd.to_datetime(df2['review_answer_timestamp'])
pd.to_datetime(df2['review_creation_date'])


# In[144]:


# Konversi kolom ke objek datetime
df2['review_creation_date'] = pd.to_datetime(df2['review_creation_date'])
df2['review_answer_timestamp'] = pd.to_datetime(df2['review_answer_timestamp'])

# Hitung selisih waktu dalam detik
df2['duration'] = (df2['review_answer_timestamp'] - df2['review_creation_date']).dt.total_seconds()


# In[145]:


df2['duration']


# In[147]:


df2['duration'] = df2['duration'] / 3600


# In[149]:


print(df2)


# In[ ]:


# Sebaran review score berdasarkan waktu
# data_sebaran = df2.groupby('review_creation_date')['review_score'].mean()
# plt.figure(figsize=(15, 5))
# data_sebaran.plot(kind='hist', color='blue')
# plt.title('Sebaran Review Score Berdasarkan Waktu')
# plt.xlabel('Tanggal Review')
# plt.ylabel('Review Score Rata-rata')
# plt.grid(axis='y')
# plt.show()

# Misalkan 'df' adalah DataFrame Anda
plt.figure(figsize=(12, 6))
plt.bar(df2['review_creation_date'], df2['review_score'], color='blue')
plt.title('Sebaran Review Score Berdasarkan Waktu')
plt.xlabel('Tanggal Review')
plt.ylabel('Review Score')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.show()


# ## Visualization & Explanatory Analysis

# ### Pertanyaan 1: 

# Berapa rata-rata skor dari review para pembeli dan skor apa yang paling sering diberikan?

# In[184]:


# Rata - rata skor review
mean = df2['review_score'].mean()
print(df2['review_score'].mean())


# In[158]:


# Skor yang paling sering diberikan pelanggan
# Data untuk diagram pie
sizes = [bintang1, bintang2, bintang3, bintang4, bintang5]
labels = ['1', '2', '3', '4', '5']
colors = ['red', 'orange', 'yellow', 'green', 'blue']

# Membuat diagram pie
plt.figure(figsize=(8, 8))  # Mengatur ukuran
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Memastikan diagram pie berbentuk lingkaran

# Menambahkan judul
plt.title('Diagram Pie Review Scores')

# Menampilkan diagram pie
plt.show()


# ### Pertanyaan 2: 

# Berapa rata - rata waktu respon penjual terhadap review dari pembeli dan durasi yang paling sering dilakukan?

# In[163]:


df2['duration']


# In[187]:


df2['duration'].mode().values[0]


# In[188]:


df2['duration'].mean()


# In[172]:


# Buat scatter plot
plt.figure(figsize=(10, 6))  # Atur ukuran gambar
plt.scatter(df2['duration'], df2['duration'].index, color='blue', alpha=0.5)  # Plot data
plt.xlabel('Durasi (jam)')  # Label sumbu x
plt.ylabel('Jumlah Data')  # Label sumbu y
plt.title('Scatter Plot Durasi Review')  # Judul scatter plot

# Tampilkan scatter plot
plt.show()


# ## Conclusion

# - Conclution pertanyaan 1
# Rata-rata skor dari review para pembeli dan skor apa yang paling sering diberikan adalah
# Rata - rata = 3.837585120439069
# Paling sering = 5
# Skor review termasuk ke dalam hal yang pertama kali dilihat oleh pembeli sebelum membeli suatu barang di toko sebuah e-commerce.
# - conclution pertanyaan 2
# Rata - rata waktu respon penjual terhadap review dari pembeli dan durasi respon terbanyak adalah:
# rata - rata = 85.9403776354869 jam,
# paling sering = 21.97388888888889 jam
# Respon termasuk ke dalam salah satu hal yang penting untuk dilakukan karena biasanya pembeli memberikan pertanyaan/ komplain ketidak sesuaian barang yang berkaitan dengan skor review. Biasanya, skor review dan review dapat diubah sebelum waktu tertentu. Untuk dapat meminimalisir skor kecil, maka perlu untuk memberikan respon terhadap review yang diberikan oleh pembeli.
 
