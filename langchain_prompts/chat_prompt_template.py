from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)


# this is used for creating dynamic system message
# we can also use this for creating dynamic human message
# we can also use this for creating dynamic ai message
# this comes under list of messages - dynamic messages



# prompt template is used for creating single turn messages
# and chat prompt template is used for creating multi turn messages