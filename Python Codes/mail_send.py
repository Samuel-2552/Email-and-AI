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
    ACCESS_TOKEN,
)

draft = nylas.drafts.create()
draft.subject = "Query and help regarding (Nylas and AI) hackathon"
draft.body = '''
Respected Nylas Team,

		I am Samuel Joseph, student from Rajalakshmi Engineering College, Chennai India, me and team are working extensively on this hackathon and would need your support and help.

We are developing AI tool that would analyse email attachments, extract its content and provide a summary and other necessary details using OPENAI API. Kindly provide us with OPENAI API key if possible that would help us to develop the product better.  

The personal email that we have contains very less data for analysis. It would be better if you could provide us with an email account that receives a lots of emails every hour so that data analysis can be performed better and predictions can be made such as whether user will read, what type of mail user will receive, etc. 

Kindly reply to this mail and provide your best support, we assure you that our project will be one of its kind.

Thanks and Regards,

Samuel Joseph 
Ph No: +91 8279598383
	
“This mail was sent using nylas API”

'''
draft.to = [{'name': 'My Nylas Friend', 'email': 'alvaro.t@nylas.com'}]

draft.send()  
 
