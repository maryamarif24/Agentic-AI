from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool
from agents.run import RunConfig
import os
from dotenv import load_dotenv
from math import sqrt, log, sin, cos, tan

set_tracing_disabled(disabled=True)
load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
async def add(a: int, b: int) -> int:
    return a + b

@function_tool
async def sub(a: int, b: int) -> int:
    return a - b

@function_tool
async def mul(a: int, b: int) -> int:
    return a * b

@function_tool
async def div(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

@function_tool
async def underroot(a: float) -> float:
    return sqrt(a)

@function_tool
async def power(base: int, exponent: int) -> int:
    return pow(base, exponent)

@function_tool
async def logarithm(x: float) -> float:
    return log(x)

@function_tool
async def sine(angle: float) -> float:
    return sin(angle)

@function_tool
async def cosine(angle: float) -> float:
    return cos(angle)

@function_tool
async def tangent(angle: float) -> float:
    return tan(angle)

agent = Agent(
    name="Assistant",
    instructions="You are a naughty assistant. Giving wrong answers funny at first with emoji then the right answers.",  # Updated instructions
    tools=[add, sub, mul, div, underroot, power, logarithm, sine, cosine, tangent]
)

result = Runner.run_sync(agent, "What is 3*6?", run_config=config)

print(result.final_output)