# WhatsApp Reply Automation Bot
This documentation provides a description and usage instructions for the WhatsApp Response Automation Bot, which uses the Selenium library in Python. The bot allows you to send automatic messages to contacts on WhatsApp Web based on defined filters.

## Prerequisites

Make sure you have the following requirements before using WhatsApp Response Automation Bot:

- Python 3 installed on your system
- Selenium library installed (`pip install selenium`)
- Compatible Chrome browser driver installed. The bot is designed to work with Chrome, so Chrome is required to be installed on your system.
- Permissions to access WhatsApp Web and read messages from contacts.

## Installation

To install WhatsApp Response Automation Bot, follow the steps below:

1. Install the required dependencies by running the following command:

     ``` shell
     pip install -r requirements.txt
     ```

2. Set the variables in the `app.py` file:

     ```python
     contact_list = ['contact 1', 'contact 2']
     contact_filter = True # send messages only to contacts listed in the above array
     ```

3. Run the bot's Python file:

     ``` shell
     python app.py
     ```
