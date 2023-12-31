import pandas as pd
df=pd.read_json(r'C:\Machine Learning\Hackthon\data (2).json')
import seaborn as sns
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
df["recived_day"]=df.received_at.dt.day
df["recived_hour"]=df.received_at.dt.hour
df["from_email"]=df["from"].apply(lambda x: x[0]["email"])
df["from_name"]=df["from"].apply(lambda x: x[0]["name"])
df["email_from"]=df["from"].apply(lambda x: x[0]["email"])



def clean(k):
    html_string = k
    soup = BeautifulSoup(html_string, 'html.parser')
    plain_text = soup.get_text().replace('"', "'")
    return plain_text

df["clean_content"]=df.body.apply(clean)

df["replied_to"]=df.reply_to.apply(lambda x:x[0]["email"] if x else "NO REPLY SENT")
df["file_type"]=df.files.apply(lambda x: x[0]["content_type"] if x else "NO ATTACHMENTS")



#new variable for pie-chart for knowing the percentage contribution

df5=pd.DataFrame(df.file_type.value_counts().reset_index())
#pie-chart

plt.pie(df5["count"], labels=df5["file_type"],autopct="%.2f")
plt.ylabel("")
plt.savefig("plt_pie.png")
plt.show()
#display content

'''This pie chart visually 
represents file types in emails, showing the proportion of each type, aiding quick comprehension of email content diversity'''


#df2 for bar plot
plt.figure(figsize=(8,5))
df2=df.from_email.value_counts().reset_index()[:5]
sns.barplot(data=df2,x="from_email",y="count")
plt.xticks(fontsize=8,rotation=8)
plt.savefig("plt_bar1.png")
plt.show()
""" This bar chart shows the top 5 email which has sent high number of mails"""


#for word cloud get all keywords in to form of list with variable name keywords

df_g=df.groupby("recived_hour",as_index=False).count()[["recived_hour","received_at"]]
plt.bar(df_g.recived_hour,df_g.received_at)
plt.savefig("plt_bar2.png")
plt.xticks(range(0,24),range(0,24))

"""This plot shows the number of mails recived per hour"""

#dummy keywords
keywords=['districts', 'fy', 'revenue', 'top', '5', 'any', 'growth', 'registration', 'that', 'there', 'list', 'down', 'between', 'what',
        'or', 'are', 'have', '•', 'these', 'document', '2022?', 'during', 'vehicle', 'sales', 'investments', 'telangana', 'stamp', 'how', 'does', 'generated']

plt.figure(figsize=(4,4))
sns.jointplot(data=df,x="recived_day",y="recived_hour",kind="scatter")
plt.yticks(range(0,24),range(0,24))
plt.savefig("plt_jp.png")
"""This code generates a scatterplot with 
custom y-axis labels, illustrating the relationship between the day and hour of email receipt for data analysis"""

from wordcloud import WordCloud

text_data = " ".join(keywords)

wordcloud = WordCloud(width=800, height=400,background_color="cyan").generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove axis
plt.savefig("plt_wc.png")
plt.show()

#display content

'''This word cloud visually 
highlights keywords extracted from email summaries, providing a quick and eye-catching way to identify key themes and topics'''

#new column creation

df["content_length"]=df.clean_content.apply(len)

#hist plot for knowing the distribution of the recived emails

sns.histplot(df.content_length,bins=30)
plt.xlim(0,18000)
plt.savefig("plt_hist.png")

#display content

'''This histplot visually displays the 
distribution of email content lengths in your received emails, helping you identify common lengths and outliers efficiently.'''



