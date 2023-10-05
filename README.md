# AI Infused Inbox

![GitHub license](https://img.shields.io/github/license/Samuel-2552/Email-and-AI)
![GitHub release (latest by date)](https://github.com/Samuel-2552/Email-and-AI.git)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

#### Description

AI Infused Inbox is a Flask web application developed for the Nylas and AI Hackathon. This application integrates with the **Nylas API** to fetch emails that contain attachments. It then uses **AI-powered algorithms** to analyze the type of attachment and extract its content, providing a summary to the user.

#### Features

- *Fetch emails with attachments from your inbox.*
- *Automatically classify attachment types (e.g., documents, images, PDFs).*
- *Extract and summarize the content of attachments.*
- *User-friendly web interface for easy interaction.*
- *Real-time updates and notifications.*

#### Installation

1. Clone this repository:

   shell
   git clone https://github.com/Samuel-2552/Email-and-AI.git
   

2. Install the required dependencies for backend:

   shell
   pip install -r requirements.txt
   

3. Set up your Nylas API credentials in `.env`:

    NYLAS_CLIENT_ID='YOUR_CLIENT_ID'
    NYLAS_CLIENT_SECRET='YOUR_CLIENT_SECRET'
    NYLAS_API_SERVER='YOUR_API_SERVER'


4. Set up environment:

   shell
   cd backend
   $env:FLASK_APP="./server.py"


5. Run the Backend Application:

    shell
    python -m flask run --port=9000
    
6. Install node.js:
    
    https://nodejs.org/en/download

7. Frontend Installations:
    
    shell
    cd frontend
    npm install vite
    npm install vite-config
    npm install jquery
    npm i --save @fortawesome/fontawesome-svg-core
    npm install --save @fortawesome/free-solid-svg-icons
    npm install --save @fortawesome/react-fontawesome

8. Run the Frontend Application:

    shell
    npm run start
    

   
   

#### Usage

1. Visit `http://localhost:5000` in your web browser.
2. Log in with your Nylas account.
3. Explore your AI-infused inbox with automated content summaries!

#### Contributing

Contributions are welcome! 
*Please see our [contributing guidelines](CONTRIBUTING.md) for more details.*

#### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
