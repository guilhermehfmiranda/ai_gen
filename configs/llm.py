from configs.llms import (
    ollama
    ,openai
    ,rest_api
)

llm = {
    'ollama' : ollama.llm
    ,'openai' : openai.llm
    ,'rest_api' : rest_api.llm
}