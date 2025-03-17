"""DICE FastAPI application.

Args:
    app: The FastAPI instance

Usage:
    run `fastapi dev` or `#` to start the server
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI(
    title="DICE",
)




