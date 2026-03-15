from langchain_openai import ChatOpenAI
# LLMs inherit from BaseLLM
# ChatModels inherit from BaseChatModel

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)
# temperature determines the randomness and creativity of the output
# max_completion_tokens determines the maximum number of tokens to generate

result = model.invoke("Write a 5 line poem on cricket")

# only result will give extra data, so we used result.content
print(result.content)