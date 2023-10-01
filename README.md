# AI Infused Inbox

![GitHub license](https://img.shields.io/github/license/Samuel-2552/Email-and-AI)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Samuel-2552/Email-and-AI)
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
   git clone https://github.com/yourusername/ai-infused-inbox.git
   

2. Install the required dependencies:

   shell
   pip install -r requirements.txt
   

3. Set up your Nylas API credentials in `config.py`:

   python
   NYLAS_API_KEY = "YOUR_API_KEY_HERE"
   

4. Run the application:

   shell
   python app.py
   

#### Usage

1. Visit `http://localhost:5000` in your web browser.
2. Log in with your Nylas account.
3. Explore your AI-infused inbox with automated content summaries!

#### Contributing

Contributions are welcome! 
*Please see our [contributing guidelines](CONTRIBUTING.md) for more details.*

#### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
