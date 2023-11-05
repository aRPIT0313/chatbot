import re
import json

# Read your WhatsApp chat from a text file
with open('wp2.txt', 'r', encoding='utf-8') as file:
    chat_data = file.read()

# Define regular expressions to extract messages and participants
message_pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2} - (.*?): (.*))')
participants = list(set(match.group(2) for match in re.finditer(message_pattern, chat_data)))

# Extract messages and participants
messages = [(match.group(2), match.group(3)) for match in re.finditer(message_pattern, chat_data)]

# Function to generate questions and answers
def generate_qa(messages, participant):
    qa_pairs = []
    for i in range(len(messages) - 1):
        if messages[i][0] == participant:
            qa_pairs.append({"question": messages[i][1], "answer": messages[i + 1][1]})
    return qa_pairs

# Choose a participant to generate questions and answers for
selected_participant = participants[0]

# Generate questions and answers for the selected participant
qa_pairs = generate_qa(messages, selected_participant)

# Create a dictionary to store the data
data = {"questions": qa_pairs}

# Save the data as JSON
with open('chat.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data saved to whatsapp_qa.json")
