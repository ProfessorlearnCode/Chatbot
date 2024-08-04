# Chatbot GUI Application

## Overview

Welcome to the Chatbot GUI Application! This project features a simple yet interactive chatbot built using Python and Tkinter. It provides a user-friendly graphical interface for engaging with a virtual assistant that responds to a variety of predefined queries. Whether you want to greet the chatbot or learn more about its creators, this application offers a seamless and enjoyable chat experience.

## Features

- **Interactive GUI**: A sleek and intuitive interface for chatting with the bot.
- **Dynamic Responses**: The chatbot responds to a range of predefined intents.
- **Context Handling**: Simple yet effective response generation based on user input.
- **Easy Exit**: Type "bye" to end the conversation and close the application.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. **Clone the Repository**: 

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Prepare `intents.json`**:

   Ensure you have a file named `intents.json` in the same directory as `chatbot_gui.py`. This JSON file should contain your chatbot's intents and responses.

3. **Run the Application**:

   ```bash
   python chatbot_gui.py
   ```

### File Structure

- `chatbot_gui.py`: The main Python script for running the chatbot GUI.
- `intents.json`: JSON file containing predefined chatbot intents and responses.

### Example `intents.json`

Here is a sample `intents.json` file structure:

```json
{
    "intents": [
        {
            "intent": "greeting",
            "text": ["Hi", "Hello", "How are you?"],
            "responses": ["Hello!", "Good to see you!"],
            "extension": { "function": "", "entities": false, "responses": [] },
            "context": { "in": "", "out": "GreetingUserRequest", "clear": false },
            "entityType": "NA",
            "entities": []
        },
        {
            "intent": "goodbye",
            "text": ["bye", "goodbye"],
            "responses": ["Goodbye! Have a great day!"],
            "extension": { "function": "", "entities": false, "responses": [] },
            "context": { "in": "", "out": "LeavingUserRequest", "clear": false },
            "entityType": "NA",
            "entities": []
        }
    ]
}
```

## Usage

- **Run the script**: Execute the `chatbot_gui.py` script to open the chatbot application.
- **Interact**: Type your message in the input field and press "Send" to receive a response.
- **Exit**: Type "bye" to end the chat and close the application.

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes.


## Contact

For any questions or feedback, please reach out to farzam.professor@gmail.com
