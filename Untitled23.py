#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests, bs4, graphviz


# In[2]:


url = "https://peps.python.org/#numerical-index"


# In[3]:


res = requests.get(url)


# In[4]:


res.status_code


# In[5]:


res.apparent_encoding


# In[6]:


res.encoding


# In[7]:


dom = bs4.BeautifulSoup(res.text)


# In[8]:


len(dom.find_all("table"))


# In[13]:


table = dom.find("table", attrs={"class": "pep-zero-table docutils align-default"})


# In[16]:


class PEPEntry:
    def __init__(self, status, ID, title, authors, versions):
        self.status = status
        self.ID = ID
        self.title = title
        self.authors = self.split_authors(authors)
        self.versions = versions

    def split_authors(self, string):
        if string == "":
            return []
        else:
            # replace ', Jr.' with ' Jr.'
            # split with ', '
            string = string.replace(', Jr.', ' Jr.')
            return string.split(', ')


# In[17]:


peps = []
for tr in table.find("tbody").find_all("tr"):
    tds = tr.find_all("td")
    if len(tds) < 5:
        continue
    status = tds[0].get_text()
    ID = tds[1].get_text()
    title = tds[2].get_text()
    authors = tds[3].get_text()
    versions = tds[4].get_text()
    entry = PEPEntry(status, ID, title, authors, versions)
    peps.append(entry)




# In[18]:


peps

