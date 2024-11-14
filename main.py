import logging
from typing import Text

import ollama
import uvicorn
from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger(__name__)
logging.basicConfig(level=2, format="%(asctime)-15s %(levelname)-8s %(message)s")


@app.post("/tell_joke")
async def tell_joke(topic: Text = "") -> Text:
    response = ollama.generate(
        model="llama3.1",
        prompt=f"""
    You are a good assistant
    Tell me a funny joke about {topic}
""",
    )
    logger.debug(response)
    return response["response"]


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
