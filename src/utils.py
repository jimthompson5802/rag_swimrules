def preprocess_input(user_input):
    # Function to clean and prepare user input for the chatbot
    cleaned_input = user_input.strip().lower()
    return cleaned_input

def log_response(user_input, chatbot_response):
    # Function to log the user input and chatbot response
    with open('chatbot_log.txt', 'a') as log_file:
        log_file.write(f'User: {user_input}\nChatbot: {chatbot_response}\n\n')