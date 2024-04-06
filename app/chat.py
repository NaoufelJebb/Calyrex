import chainlit as cl
from chainlit.input_widget import Select, Slider

from config import OLLAMA_CHAT_LLM, OLLAMA_CODE_LLM
from model import LLModel

SETTINGS = [
    Select(
        id="model",
        label="Ollama - Chat Model",
        values=[OLLAMA_CHAT_LLM, OLLAMA_CODE_LLM],
        initial_index=0,
    ),
    Slider(
        id="temperature",
        label="Temperature",
        initial=1,
        min=0,
        max=2,
        step=0.1,
        description="Controls the randomness/determinism of the LLM's output.",
        tooltip="Higher temperature will result in more creative and imaginative output.",
    ),
    Slider(
        id="top_p",
        label="Top P",
        initial=0.7,
        min=0.0,
        max=1.0,
        step=0.01,
        description="Nucleus Sampling.",
        tooltip="Lower top-p values reduce diversity and focus on the most probable tokens.",
    ),
    Slider(
        id="context_length",
        label="Context Window",
        initial=8192,
        min=50,
        max=16000,
        step=128,
        description="Number of tokens the model can take as input when generating responses.",
    ),
]


@cl.on_chat_start
async def on_chat_start():
    settings = await cl.ChatSettings(SETTINGS).send()
    await setup_llm(settings)


@cl.on_settings_update
async def setup_llm(settings):
    llm = LLModel(
        model=settings["model"],
        temperature=settings["temperature"],
        top_p=settings["top_p"],
        num_ctx=settings["context_length"],
    )
    cl.user_session.set("runnable", llm.runnable)


@cl.on_message
async def main(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    if not runnable:
        runnable = LLModel().runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
    ):
        await msg.stream_token(chunk)

    await msg.send()
