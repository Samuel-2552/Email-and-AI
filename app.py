from flask import Flask, session, request, redirect, render_template
import os
from nylas import APIClient
from dotenv import load_dotenv

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
    message = nylas.messages
    file = []
    for mess in message:
        file.append(mess.files)
    
    filenames = []
    ids = []
    flag=0

    for item in file:
        if type(item) is list:
            for sub_item in item:
                if type(sub_item) is dict:
                    filename = sub_item.get("filename")
                    id_value = sub_item.get("id")
                    print(filename, id_value)
                    if filename is not None:
                        filenames.append(filename)
                        if id_value is not None:
                            ids.append(id_value)

    for i in range(len(ids)):
        file = nylas.files.get(ids[i])
        downloaded_file = file.download()

        # Create a subdirectory for each file
        file_directory = os.path.join("downloaded_files", str(i))
        os.makedirs(file_directory, exist_ok=True)

        # Get the filename
        filename = filenames[i]

        # Save the downloaded file inside the subdirectory
        file_path = os.path.join(file_directory, filename)

        with open(file_path, 'wb') as f:
            f.write(downloaded_file)
        
    return "Successfull!"




if __name__ == "__main__":
    app.run()
