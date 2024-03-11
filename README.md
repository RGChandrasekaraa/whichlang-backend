WhichLang Backend
This is the backend component of the WhichLang project, a language detection application.

Overview
The WhichLang backend is built with Flask, a lightweight WSGI web application framework, and serves as the API endpoint for language detection.

Features
Language detection endpoint
Error handling for invalid requests
Logging of errors for debugging
Getting Started
To get started with the WhichLang backend, follow these steps:

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/RGChandrasekaraa/whichlang-backend.git
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Start the Flask server:

bash
Copy code
python run.py
The backend server should now be running locally at http://127.0.0.1:5000.

Usage
To use the language detection endpoint, send a POST request to /detect_language with a JSON payload containing the text to analyze. Here's an example using cURL:

bash
Copy code
curl -X POST http://127.0.0.1:5000/detect_language -H "Content-Type: application/json" -d '{"text": "Your text here"}'
The server will respond with a JSON object containing the detected language.

Error Handling
The backend includes error handling for invalid requests and unexpected errors. If a request is invalid or an unexpected error occurs, the server will respond with an appropriate error message.

Contributing
Contributions are welcome! If you'd like to contribute to the development of the WhichLang backend, please fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License.
