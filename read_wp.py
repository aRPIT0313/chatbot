import re
import json

# Read the WhatsApp conversation file
with open('conversation3.txt', 'r', encoding='utf-8') as file:
    chat_data = file.readlines()

chat_entries = []

# Define a list to store the chat data
chat_list = {
    "questions": []
}

current_question = None

for line in chat_data:
    # Use regular expressions to extract sender and message content
    match = re.match(r'(\w+): (.*)', line)
    if match:
        sender, message = match.groups()

        # If the current message is a question, create a new question entry
        if current_question is None:
            current_question = {"question": message, "answer": None}
        else:
            # If the current message is an answer, add it to the current question
            current_question["answer"] = message
            chat_list["questions"].append(current_question)
            current_question = None

# Save the data to chat.json
with open('chat.json', 'w') as json_file:
    json.dump(chat_list, json_file, indent=2)
