print("Namaste! Welcome to your ChatBot" )
print("You can ask me some basic question, and I will try to answer you")

response = {  # this is use for store the question and answer

    "hello": "Hi, welcome, How i can help you!",
    "how are you": "I am very fine, Thank you ",
    "who are you": "I am smart AI Chatbot",
    "motivate me": "The way do anything is the way you do everthing",
    "happy": "Great to hear that",
    "discipline": "complete your today task",
    "free time": "playing guitar",

}
def getResponseOfBot(userQuestion):
     userQuestion= userQuestion.lower() # this is use for cnvert the user query into lower case, 
     for i in response:  # i tabtak chalega jabtak response me question h,
        if i == userQuestion:
            return response[i] # this is use for return the ans of the ques
while True:
     userInput= input("Please ask your question:" ) # firstly call the user input and store in userInput variable
     if "bye" in userInput.lower():
         break
     reply= getResponseOfBot(userInput)  # userInput ko getResponseOfBot function me pass karenge and uska reply ko reply variable me store karenge
     print("Bot Rsponse :", reply) # why show none because if user ask question which is not in stored in response variable then it will return none, so we can handle this by add else condition in getResponseofbot
