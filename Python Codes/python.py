import pandas as pd

df=pd.read_json(r'C:\Machine Learning\Hackthon\data (2).json')

df_g2=df.unread.value_counts().reset_index()


import seaborn as sns

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

def clean(k):
    html_string = k
    soup = BeautifulSoup(html_string, 'html.parser')
    plain_text = soup.get_text().replace('"', "'")
    return plain_text

df["clean_content"]=df.body.apply(clean)

df["replied_to"]=df.reply_to.apply(lambda x:x[0]["email"] if x else "NO REPLY SENT")

df["file_type"]=df.files.apply(lambda x: x[0]["content_type"] if x else "NO ATTACHMENTS")


import matplotlib.pyplot as plt
import seaborn as sns



df["recived_day"]=df.received_at.dt.day

df["recived_hour"]=df.received_at.dt.hour

df["from_email"]=df["from"].apply(lambda x: x[0]["email"])

df["from_name"]=df["from"].apply(lambda x: x[0]["name"])

df["email_from"]=df["from"].apply(lambda x: x[0]["email"])

df_g=df.groupby("recived_hour",as_index=False).count()[["recived_hour","received_at"]]

plt.bar(df_g.recived_hour,df_g.received_at)
plt.xticks(range(0,24),range(0,24))
plt.show()

import pdfplumber

# Open the PDF file
with pdfplumber.open(r'C:\Users\ssrin\OneDrive\Desktop\C7 Input Files\res.pdf') as pdf:
    # Initialize an empty string to store extracted text
    text = ''

    # Iterate through each page and extract text
    for page in pdf.pages:
        text += page.extract_text()

# Print or use the extracted text
print(text)

# Specify the path to your text file
file_path = 'Metadata.txt'  # Replace with the path to your text file

# Open and read the text file
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Print the text from the file
    print("Text from the file:")
    print(file_contents)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

df1=pd.read_csv(r"C:\Users\ssrin\OneDrive\Desktop\C7 Input Files\dataset\fact_TS_iPASS.csv")

print(df1.describe().T)

# Tokenize the text into words
words = text.split()

# Create a dictionary to store word frequencies
word_frequency = {}

# Define a list of common words to ignore (customize as needed)
common_words_to_ignore = ["the", "of", "is", "a", "it", "for", "and", "to", "in", "this"]

# Calculate word frequencies
for word in words:
    word = word.lower()
    if word not in common_words_to_ignore:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

# Extract keywords based on word frequency
top_n_keywords = 5  # You can adjust this to get more or fewer keywords
keywords = [word for word, freq in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:top_n_keywords]]

# Print the extracted keywords
print("Keywords:", keywords)

df2=df.from_email.value_counts().reset_index()[:5]
sns.barplot(data=df2,x="from_email",y="count")
plt.xticks(rotation=90)
plt.show()

df3=df.file_type.value_counts().reset_index()[:5]
sns.barplot(data=df3,x="file_type",y="count")
plt.show()
