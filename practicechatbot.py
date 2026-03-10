print("Namaste! Welcome to our ChatBot")
print("You can ask me some basic question, and I will try to answer you")
response = {
    "hello": "Hi, welcome, How i can help you!",
    "how are you": "I am very fine, Thank you ",
    "who are you": "I am smart AI Chatbot",
    "motivate me": "The way do anything is the way you do everthing",
    "happy": "Great to hear that",
    "discipline": "complete your today task",
    "free time": "playing guitar",
}
def getresponseofbot(userQuestion):
    userQuestion = userQuestion.lower()
    for i in response:
        if i ==userQuestion:
            return response[i]
while True:
    userInput = input("Please ask your question :")
    if userInput.lower() == "exit":
        break
    reply = getresponseofbot(userInput) 
    print("Bot Response :",reply)