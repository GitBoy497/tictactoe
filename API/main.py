from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from routes.game_routes import router as game_router

load_dotenv()

app = FastAPI()

app.include_router(game_router, prefix="/tic_tac_toe")