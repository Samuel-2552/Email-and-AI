from flask import Flask, session, request, redirect, render_template, jsonify
import os
from nylas import APIClient
from dotenv import load_dotenv
import pdfplumber
import torch
import easyocr
from transformers import BartForConditionalGeneration, BartTokenizer
import pandas as pd
import matplotlib.pyplot as plt
from docx import Document
import json
import seaborn as sns


# Load environment variables from the .env file in the current directory
load_dotenv()

# Now you can access the environment variables just like before
import os

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
API_URL = os.getenv("API_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

nylas = APIClient(
    CLIENT_ID,
    CLIENT_SECRET,
    ACCESS_TOKEN
)  


file_data = ''

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")  # Set a secret key for session management

@app.route('/')
def index():
    
    return render_template('land.html')

@app.route('/load')
def load():

    return render_template('load.html')

@app.route('/download')
def download():
    global file_data
    message = nylas.messages
    file = []
    for mess in message:
        file.append(mess.files)
    
    filenames = []
    ids = []

    for item in file:
        if type(item) is list:
            for sub_item in item:
                if type(sub_item) is dict:
                    filename = sub_item.get("filename")
                    id_value = sub_item.get("id")
                    # print(filename, id_value)
                    if filename is not None:
                        filenames.append(filename)
                        if id_value is not None:
                            ids.append(id_value)

    file_data = zip(filenames, ids)

    file_data_with_icons = [(filename, id, get_file_icon(filename)) for filename, id in file_data]

    # print(file_data_with_icons)

    # for i in range(len(ids)):
    #     file = nylas.files.get(ids[i])
    #     downloaded_file = file.download()

    #     # Create a subdirectory for each file
    #     file_directory = os.path.join("downloaded_files", str(i))
    #     os.makedirs(file_directory, exist_ok=True)

    #     # Get the filename
    #     filename = filenames[i]

    #     # Save the downloaded file inside the subdirectory
    #     file_path = os.path.join(file_directory, filename)

    #     with open(file_path, 'wb') as f:
    #         f.write(downloaded_file)
        
    return render_template('files.html', file_data=file_data_with_icons)

@app.route('/process_file', methods=['GET'])
def process_file():
    # Get the file ID and filename from the request
    file_id = request.args.get('id')
    filename = request.args.get('filename')

    print(filename, file_id)

    file = nylas.files.get(file_id)
    downloaded_file = file.download()

    file_directory = os.path.join("files")

    file_path = os.path.join(file_directory, filename)

    with open(file_path, 'wb') as f:
        f.write(downloaded_file)

    extension = filename.split('.')[-1].lower()

    if extension == 'pdf':
        text=pdf(filename)
        print(text)
        summary = summarization(text)
        print(summary)
        return jsonify(f'Summary of the {filename}:\n {summary}')
    
    elif extension in ('jpg', 'jpeg', 'png'):
        text=image(filename)
        print(text)
        summary = summarization(text)
        print(summary)
        return jsonify(f'Summary of the {filename}:\n {summary}')
    
    elif extension == 'xlsx':
        filename = "files/" + filename
        df_excel = pd.read_excel(filename)
        summary_stats = df_excel.describe()
        # Create a bar plot
        summary_stats.plot(kind='bar', figsize=(10, 6))
        plt.title('Summary Statistics')
        plt.xlabel('Statistics')
        plt.ylabel('Values')
        plt.legend(loc='upper right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        # Save the plot as an image (e.g., PNG)
        plt.savefig('static/summary_statistics.png')

        # Close the plot to release resources (optional)
        plt.close()
        return f"Summary of your {filename}:\n 'static/summary_statistics.png'"
    
    elif extension == 'docx':
        filename = "files/" + filename
        doc = Document(filename)
        text = ''

        for paragraph in doc.paragraphs:
            text += paragraph.text
        
        print(text)

        # summary = summarization(text)
        # print(summary)

        return jsonify(f'Summary of the {filename}:\n {text}')
    


    # Assume you have some processing logic here
    # For demonstration, we'll just store the filename as content

    # Return the processed content as a response with the filename inserted
    return jsonify(f'Summary of the file: {summary}')


@app.route('/process_all', methods=['GET'])
def process_all():
    message = nylas.messages
    # Serialize the complex data
    serialized_data = serialize_complex_data(message)

    # Specify the file name and open it in write mode ('w')
    file_name = "files/data.json"
    with open(file_name, 'w', encoding='utf-8') as json_file:
        # Write the serialized data to the file
        json.dump(serialized_data, json_file, indent=4)

    df=pd.read_json('files/data.json')
    df["recived_day"]=df.received_at.dt.day
    df["recived_hour"]=df.received_at.dt.hour
    df["from_email"]=df["from"].apply(lambda x: x[0]["email"])
    df["from_name"]=df["from"].apply(lambda x: x[0]["name"])
    df["email_from"]=df["from"].apply(lambda x: x[0]["email"])
    df_g=df.groupby("recived_hour",as_index=False).count()[["recived_hour","received_at"]]
    plt.bar(df_g.recived_hour,df_g.received_at)
    plt.xticks(range(0,24),range(0,24))
    # Save the plot as an image (e.g., PNG)
    plt.savefig('static/summary_statistics1.png')
    plt.figure(figsize=(4,4))
    sns.jointplot(data=df,x="recived_day",y="recived_hour",kind="scatter")
    plt.yticks(range(0,24),range(0,24))
    plt.savefig('static/summary_statistics2.png')

    return jsonify('static/summary_statistics1.png','static/summary_statistics2.png')

def image(filename):
    filename = "files/" + filename
    reader = easyocr.Reader(['en'])  # Replace 'en' with the language you need
    result = reader.readtext(filename)
    text=''
    for detection in result:
        print(detection[1])
        text = text + detection[1]

    # print(result)
    return text

def pdf(filename):
    
    filename = "files/" + filename
    # Open the PDF file
    with pdfplumber.open(filename) as pdf:
        # Initialize an empty string to store extracted text
        text = ''

        # Iterate through each page and extract text
        for page in pdf.pages:
            text += page.extract_text()

   
    return text

def summarization(text):
     # Load the pre-trained BART model and tokenizer
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    # Tokenize and encode the input text
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding=True)

    # Generate the summary
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, min_length=30, max_length=200, early_stopping=True)

    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Print the summary
    print(summary)
    return summary


def get_file_icon(filename):
    extension = filename.split('.')[-1].lower()
    if extension == 'pdf':
        return 'fa fa-file-pdf-o'
    elif extension == 'csv':
        return 'fa fa-file-excel-o'
    elif extension in ('jpg', 'jpeg', 'png'):
        return 'fa fa-file-image-o'
    elif extension == 'xlsx':
        return 'fa fa-file-excel-o'
    elif extension == 'docx':
        return 'fa fa-file-word-o'
    elif extension == 'pptx':
        return 'fa fa-file-powerpoint-o'
    else:
        return 'fa fa-file'  # Default icon

# Custom function to serialize complex data
def serialize_complex_data(data):
    serialized_data = []
    for item in data:
        # Serialize custom objects or handle other non-serializable data as needed
        received_at_str = item['received_at'].strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
        serialized_item = {
            'bcc': item['bcc'],
            'cc': item['cc'],
            'received_at': received_at_str,
            'events': item['events'],
            'files': item['files'],
            'from': item['from'],
            'to': item['to'],
            'reply_to': item['reply_to'],
            'object':item['object'],
            'unread': item['unread'],
            'starred':item['starred'],
            '_labels': item['_labels'],
            'snippet':item['snippet'],
            'subject':item['subject'],
            'body': item['body'],

            # Add other serializable fields as needed
        }
        serialized_data.append(serialized_item)
    return serialized_data


if __name__ == "__main__":
    app.run(debug=True)