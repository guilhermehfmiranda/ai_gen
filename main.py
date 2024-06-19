# import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from configs.llms.rest_api_llm import llm

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ('system', "You're a coffee deprived data engineer.")
    ,('user', "{input}")
])

chain = prompt | llm | output_parser
response = chain.invoke({'input': "what do you need right now?"})
print(response)
