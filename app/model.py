from config import OLLAMA_SERVE_PORT, OLLAMA_CHAT_LLM
from langchain.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

SYS_PROMPT_TEMPLATE = """You are an AI programming assistant. Follow the user's requirements carefully andto the letter. 
First, think step-by-step and describe your plan for what to build in pseudocode, written out in great detail. 
Then, output the code in a single code block. Minimize any other prose.
"""

USER_PROMPT_TEMPLATE = """
{question}
"""


class LLModel:
    def __init__(
        self, *, model=OLLAMA_CHAT_LLM, temperature=1.0, top_p=0.7, num_ctx=2048
    ):
        self.llm = Ollama(
            base_url=f"http://ollama:{OLLAMA_SERVE_PORT}",
            model=model,
            temperature=temperature,
            top_p=top_p,
            num_ctx=num_ctx,
            verbose=True,
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate.from_template(SYS_PROMPT_TEMPLATE),
                # TODO: Implement conversation history
                HumanMessagePromptTemplate.from_template(USER_PROMPT_TEMPLATE),
            ]
        )

    @property
    def runnable(self):
        return self.prompt | self.llm | StrOutputParser()
