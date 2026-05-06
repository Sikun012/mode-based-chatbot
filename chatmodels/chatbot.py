from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model = "mistral-small-2506", temperature=0.9)

print("choose your AI mode --")
print("Press 1 for Angry mode: ")
print("Press 2 for Funny mode: ")
print("Press 3 for Sad mode: ")

choice = int(input("Tell your response :--"))

if choice ==1:
    mode = "You are an Angry agent. You response aggressively and impatiently."
elif choice == 2:
    mode = "You are an Funny agent. You response humor and jokes."
elif choice == 3:
    mode = "You are an Sad agent. You response in a depressed and emotional tone."

message = [
    SystemMessage(content=mode)
]

print("------------------- Welcome to my chatbot -------------------")

while True:
    prompt = input("You: ")
    message.append(HumanMessage(content=prompt))
    if prompt ==0:
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ",response.content)

print(message)

