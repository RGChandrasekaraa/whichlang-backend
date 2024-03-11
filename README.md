# WhichLang Backend

## Overview

This repository contains the backend component of the WhichLang project, an application for language detection. The backend is built using Flask, a Python web framework.

## Features

- Provides an API endpoint for language detection
- Handles invalid requests and unexpected errors
- Logs errors for debugging purposes

## Getting Started

Follow these instructions to set up and run the WhichLang backend on your local machine.

### Prerequisites

- Python 3.x installed on your system
- pip package manager

### Installation

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/RGChandrasekaraa/whichlang-backend.git
   \`\`\`

2. Navigate to the project directory:

   \`\`\`bash
   cd whichlang-backend
   \`\`\`

3. Install dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### Usage

1. Start the Flask server:

   \`\`\`bash
   python run.py
   \`\`\`

2. The backend server will now be running locally at \`http://127.0.0.1:5000\`.

3. To use the language detection endpoint, send a POST request to \`/detect_language\` with a JSON payload containing the text to analyze.

### Example Request

\`\`\`bash
curl -X POST http://127.0.0.1:5000/detect_language \\
-H "Content-Type: application/json" \\
-d '{"text": "Your text here"}'
\`\`\`

### Response

The server will respond with a JSON object containing the detected language.

## Contributing

Contributions to the WhichLang backend are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create your feature branch:

   \`\`\`bash
   git checkout -b feature/my-feature
   \`\`\`

3. Commit your changes:

   \`\`\`bash
   git commit -am 'Add some feature'
   \`\`\`

4. Push to the branch:

   \`\`\`bash
   git push origin feature/my-feature
   \`\`\`

5. Submit a pull request.

## License

This project is licensed under the MIT License
