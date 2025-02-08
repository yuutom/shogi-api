from fastapi import FastAPI
from pydantic import BaseModel
import shogi
import random

app = FastAPI()


class MoveRequest(BaseModel):
    sfen: str  # 将棋盤の状態を表すSFEN文字列


@app.post("/next-move")
async def get_ai_move(request: MoveRequest):
    board = shogi.Board()
    board.set_sfen(request.sfen)  # 受け取ったSFENをセット

    legal_moves = list(board.legal_moves)  # 合法手リスト
    if not legal_moves:
        return {"move": None}  # 合法手がない場合は終了

    ai_move = random.choice(legal_moves)  # ランダムな手を選択
    return {"move": str(ai_move)}
