from configs.llms import (
    ollama
    ,openai
    ,rest_api_llm
)
from utils.ai import AI
from utils.data import format_converter

system_prompt = ''
user_input = ''

ai_output = format_converter(
    data = (
        AI(
            llm = rest_api_llm.llm()
        )
        .gen(
            system_prompt = system_prompt
            ,user_input = format_converter(
                data = user_input
                ,from_format = 'csv'
                ,to_format = 'json'
            )
        )
    )
    ,from_format = 'json'
    ,to_format = 'csv'
)

print(ai_output)