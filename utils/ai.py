from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

output_parser = StrOutputParser()

class AI():
    def __init__(
        self
        ,llm
    ):
        self.llm = llm

    def gen(
        self
        ,system_prompt
        ,user_input
    ):
        prompt = ChatPromptTemplate.from_messages([
            ('system', system_prompt)
            ,('user', "{input}")
        ])
        chain = prompt | self.llm | output_parser
        ai_output = chain.invoke({'input': user_input})
        return ai_output