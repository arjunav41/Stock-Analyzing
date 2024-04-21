#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install yfinance==0.2.4')
#!pip install pandas==1.3.3


# In[41]:


import pandas as pd
import yfinance as yf


# In[4]:


Tesla = yf.Ticker('TSLA')


# In[69]:


tesla_data = Tesla.history(period="max")


# In[70]:


tesla_data.reset_index(inplace=True)


# In[71]:


tesla_data.plot(x='Date', y="Close")


# In[72]:


tesla_data.head()


# In[65]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from plotly.subplots import make_subplots


# In[34]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"


# In[77]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[35]:


t_data = requests.get(url).text


# In[36]:


t_data


# In[37]:


soup = BeautifulSoup(t_data, 'html5lib')


# In[38]:


soup


# In[57]:


# Assuming `tesla_revenue` is a DataFrame and you want to append rows from the loop
tesla_revenue = pd.DataFrame()

# For demonstration, let's assume you have defined `Date` and `Revenue` variables in the loop
for row in soup.find("tbody").find_all("tr"):
    cols = row.find_all("td")
    if len(cols) >= 2:
        Date = cols[0].text
        Revenue = cols[1].text
        
        # Create a DataFrame from the row data
        row_data = {'Date': Date, 'Revenue': Revenue}
        row_df = pd.DataFrame([row_data])
        
        # Append the row DataFrame to the tesla_revenue DataFrame
        tesla_revenue = tesla_revenue.append(row_df, ignore_index=True)

# `tesla_revenue` now contains all the appended rows


# In[59]:


tesla_revenue.tail()


# In[85]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[87]:


def make_graph(stock_data, revenue_data, stock):
    # Import necessary libraries
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Create the subplots
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)
    
    # Filter data based on the dates specified
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']

    # Convert date columns to datetime format
    stock_data_specific['Date'] = pd.to_datetime(stock_data_specific['Date'])
    revenue_data_specific['Date'] = pd.to_datetime(revenue_data_specific['Date'])
    
    # Add the Share Price scatter plot
    fig.add_trace(go.Scatter(
        x=stock_data_specific['Date'],
        y=stock_data_specific['Close'].astype(float),
        name="Share Price"
    ), row=1, col=1)
    
    # Clean and convert the Revenue column
    revenue_data_specific['Revenue'] = revenue_data_specific['Revenue'].str.replace(',', '').str.replace('$', '').astype(float)
    
    # Add the Revenue scatter plot
    fig.add_trace(go.Scatter(
        x=revenue_data_specific['Date'],
        y=revenue_data_specific['Revenue'],
        name="Revenue"
    ), row=2, col=1)
    
    # Update x-axis titles
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    
    # Update layout and display the figure
    fig.update_layout(title=f"{stock} Historical Data")
    fig.show()


# In[88]:


make_graph(tesla_data, tesla_revenue, 'Tesla')


# In[99]:


gme = yf.Ticker('GME')


# In[108]:


gme_data = gme.history(period = "Max")


# In[109]:


gme_data.reset_index(inplace =True)


# In[111]:


gme_data.head()


# In[112]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"


# In[113]:


g_data = requests.get(url).text


# In[114]:


g_data


# In[115]:


soup = BeautifulSoup(t_data, 'html5lib')


# In[116]:


soup


# In[117]:


# Assuming `tesla_revenue` is a DataFrame and you want to append rows from the loop
gme_revenue = pd.DataFrame()

# For demonstration, let's assume you have defined `Date` and `Revenue` variables in the loop
for row in soup.find("tbody").find_all("tr"):
    cols = row.find_all("td")
    if len(cols) >= 2:
        Date = cols[0].text
        Revenue = cols[1].text
        
        # Create a DataFrame from the row data
        row_data = {'Date': Date, 'Revenue': Revenue}
        row_df = pd.DataFrame([row_data])
        
        # Append the row DataFrame to the tesla_revenue DataFrame
        gme_revenue = gme_revenue.append(row_df, ignore_index=True)

# `tesla_revenue` now contains all the appended rows


# In[119]:


gme_revenue.tail()


# In[120]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




