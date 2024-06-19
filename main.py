from configs.llm import llm
from utils.ai import AI
from utils.data import format_converter

system_prompt = "You're a math teacher that only answers exactly what is asked."
user_input = "Answer: 2 + 2 is?"

ai_output = format_converter(
    data = (
        AI(
            llm = llm['ollama']()
        )
        .gen(
            system_prompt = system_prompt
            ,user_input = format_converter(
                data = user_input
                # ,from_format = 'csv'
                # ,to_format = 'json'
            )
        )
    )
    # ,from_format = 'json'
    # ,to_format = 'csv'
)

print(ai_output)