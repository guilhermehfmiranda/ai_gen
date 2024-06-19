import requests
from typing import (
    Any
    ,List
    ,Mapping
    ,Optional
)
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from ..ai_configs import (
    rest_api_type
    ,rest_api_host
    ,rest_api_url
    ,rest_api_header
    ,rest_api_prompt
)

class Rest_API(LLM):
    llm_host = rest_api_host
    llm_url = rest_api_url

    @property
    def _llm_type(self) -> str:
        return rest_api_type
    
    @property
    def identifying_params(self) -> Mapping[str, Any]:
        return {'llm_url' : self.llm_url}
    
    def _call(
        self
        ,prompt: str
        ,stop: Optional[List[str]] = None
        ,run_manager: Optional[CallbackManagerForLLMRun] = None
        ,**kwargs: Any
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        request = requests.post(
            self.llm_url
            ,headers = rest_api_header
            ,json = {
                rest_api_prompt : prompt
            }
        )
        request.raise_for_status()
        return request.content

def llm():
    return Rest_API()
