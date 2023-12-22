from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory


class BOT:
    def __init__(self):
        pass


    def answer(self, query, content, page_no):
        llm = ChatOpenAI(
            temperature=0.5, model_name="gpt-3.5-turbo"
        )
        prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    "You are an AI document assistant, which greets users and answers question from a given "
                    "document."
                    f"Document: {content}."
                    "Do not engage in conversations or any activity unrelated to the given document."
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{question}")
            ]
        )
        memory = ConversationBufferWindowMemory(k=15, memory_key="chat_history", return_messages=True)
        conversation = LLMChain(
            llm=llm,
            prompt=prompt,
            # verbose=True,
            memory=memory
        )

        response = conversation({"question": f'{query}'})['text']
        return response, page_no
