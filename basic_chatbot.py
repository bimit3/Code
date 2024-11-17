import nltk
import random
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "Happy to help!", "No problem!"],
    "weather": ["The weather today is sunny with a chance of rain in the evening.", 
                "It's a bit cloudy today, but no rain is expected.", 
                "It's a warm day today with a few scattered showers expected later."],
    "unknown": ["I'm not sure I understand. Could you rephrase?", "Sorry, I didn't catch that.", "Can you please clarify?"]
}

keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you", "exit"],
    "thanks": ["thanks", "thank you", "appreciate", "grateful"],
    "weather": ["weather", "forecast", "rain", "sunny", "cloudy"]
}

def preprocess_input(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens

def detect_intent(tokens):
    for token in tokens:
        for intent, words in keywords.items():
            if token in words:
                return intent
    return "unknown"

def chatbot_response(user_input):
    tokens = preprocess_input(user_input)
    intent = detect_intent(tokens)
    return random.choice(responses[intent])

def chat():
    print("Chatbot: Hello! I'm your assistant. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "bye", "goodbye"]:
            print(random.choice(responses["goodbye"]))
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()
