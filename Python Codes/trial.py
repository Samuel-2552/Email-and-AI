from nylas import APIClient
import json

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
 

message = nylas.messages
# message = ""
# print(message)



# Specify the file name and open it in append mode ('a')
# file_name = "output.txt"
# with open(file_name, 'w', encoding='utf-8') as file:
#     # Write the content to the file
#     file.write(str(nylas.messages.all(limit=1000)))




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

# Serialize the complex data
serialized_data = serialize_complex_data(message)

# Specify the file name and open it in write mode ('w')
file_name = "data.json"
with open(file_name, 'w', encoding='utf-8') as json_file:
    # Write the serialized data to the file
    json.dump(serialized_data, json_file, indent=4)

# File is automatically closed when the 'with' block is exited
# print("Subject: {} | unread: {} | from: {} | Date: {} | Labels: {} | Object: {} | | Reply_To: {} | Starred: {} | To: {} | Snippet: {}".format(
#     message.subject, message.unread, message.from_, message.date, message.labels, message.object, message.reply_to, message.starred, message.to, message.snippet
# ))


# threads = nylas.threads.all(limit=10)
# for thread in threads:
#     print("Subject: {} | Participants: {} | Date: {}".format(
#         thread.subject, thread.participants, thread.date
#         )
#     )

# for thread in nylas.threads.where(unread=True, limit=5):
#     print(thread.subject)