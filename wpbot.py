import json
from difflib import get_close_matches

def load_chat(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"questions": []}
        save_chat(file_path, data)
    return data

def save_chat(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, chat: dict) -> str | None:
    for q in chat["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    chat: dict = load_chat('chat.json')
    while True:
        user_input: str = input('ME : ')
        if user_input.lower() == 'bye':
            break
        best_match: str | None = find_best(user_input, [q["question"] for q in chat["questions"]])

        if best_match:
            answer: str = get_answer(best_match, chat)
            print(f'bot: {answer}')
        else:
            print("Please teach me")
            new_answer: str = input("Type the answer or 'skip': ")

            if new_answer.lower() != "skip":
                chat["questions"].append({"question": user_input, "answer": new_answer})
                save_chat('chat.json', chat)
                print("Bot: Thank you")

if __name__ == '__main__':
    chat_bot()