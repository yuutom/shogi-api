from fastapi import FastAPI
from pydantic import BaseModel
import shogi
import random

app = FastAPI()


class MoveRequest(BaseModel):
    sfen: str


@app.post("/next-move")
async def get_ai_move(request: MoveRequest):
    board = shogi.Board()
    board.set_sfen(request.sfen)

    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return {"move": None}

    ai_move = random.choice(legal_moves)
    return {"move": str(ai_move)}
