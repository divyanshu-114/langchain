from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)

# we can use this chat_history to maintain the context of the conversation
# we have to use dictonary for storing the chat history
# we have to use list for storing the chat history
# so that the chatbot have the context of the conversation
# model 
# two parts of  model invoke 
# single message - static message and dynamic message (single turn stand alone queries)
# list of messages - multiple messages (multi turn conversation)
# in this static messages but with system message, ai message and human message
# context windew and dynamic message using chat prompt template
# example - You are a {domain} expert
# in this we have a dynamic system message which is {domain} and static message which is You are a expert