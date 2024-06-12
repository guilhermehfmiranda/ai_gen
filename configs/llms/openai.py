import httpx
from langchain_openai import ChatOpenAI
from ...configs.ai_configs import (
    openai_api_key
    ,openai_organization
)

llm = ChatOpenAI(
    api_key = openai_api_key
    ,organization = openai_organization
    ,http_client = httpx.Client(verify = False, follow_redirects = True)
)

# client: Any = Field(default=None, exclude=True)  #: :meta private:

# async_client: Any = Field(default=None, exclude=True)  #: :meta private:

# model_name: str = Field(default="gpt-3.5-turbo", alias="model")
"""Model name to use."""

# temperature: float = 0.7
"""What sampling temperature to use."""

# model_kwargs: Dict[str, Any] = Field(default_factory=dict)
"""Holds any model parameters valid for `create` call not explicitly specified."""

# openai_api_key: Optional[SecretStr] = Field(default=None, alias="api_key")
"""Automatically inferred from env var `OPENAI_API_KEY` if not provided."""

# openai_api_base: Optional[str] = Field(default=None, alias="base_url")
"""Base URL path for API requests, leave blank if not using a proxy or service 
    emulator."""

# openai_organization: Optional[str] = Field(default=None, alias="organization")
"""Automatically inferred from env var `OPENAI_ORG_ID` if not provided."""

# to support explicit proxy for OpenAI
# openai_proxy: Optional[str] = None

# request_timeout: Union[float, Tuple[float, float], Any, None] = Field(
#     default=None, alias="timeout"
# )
"""Timeout for requests to OpenAI completion API. Can be float, httpx.Timeout or 
    None."""

# max_retries: int = 2
"""Maximum number of retries to make when generating."""

# streaming: bool = False
"""Whether to stream the results or not."""

# n: int = 1
"""Number of chat completions to generate for each prompt."""

# max_tokens: Optional[int] = None
"""Maximum number of tokens to generate."""

# tiktoken_model_name: Optional[str] = None
"""The model name to pass to tiktoken when using this class. 
Tiktoken is used to count the number of tokens in documents to constrain 
them to be under a certain limit. By default, when set to None, this will 
be the same as the embedding model name. However, there are some cases 
where you may want to use this Embedding class with a model name not 
supported by tiktoken. This can include when using Azure embeddings or 
when using one of the many model providers that expose an OpenAI-like 
API but with different models. In those cases, in order to avoid erroring 
when tiktoken is called, you can specify a model name to use here."""

# default_headers: Union[Mapping[str, str], None] = None

# default_query: Union[Mapping[str, object], None] = None

# Configure a custom httpx client. See the
# [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
# http_client: Union[Any, None] = None
"""Optional httpx.Client. Only used for sync invocations. Must specify 
    http_async_client as well if you'd like a custom client for async invocations.
"""

# http_async_client: Union[Any, None] = None
"""Optional httpx.AsyncClient. Only used for async invocations. Must specify 
    http_client as well if you'd like a custom client for sync invocations."""
