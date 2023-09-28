from nylas import APIClient

# Replace these with your actual credentials

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

# Replace '3ltkeutjntiqkbz8yxbzozxfx' with the actual file ID you want to download
file = nylas.files.get('3ltkeutjntiqkbz8yxbzozxfx')

# .download() returns the file itself.
# Most files will be returned as a binary object
downloaded_file = file.download()

# Now you can work with the downloaded file, for example, save it to disk
with open('downloaded_file.xlsx', 'wb') as f:
    f.write(downloaded_file)
