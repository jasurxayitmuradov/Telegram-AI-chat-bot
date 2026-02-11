import aiosqlite
from .db import DB_PATH

async def get_mode(user_id: int) -> str:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT mode FROM user_state WHERE user_id=?",
            (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else "chat"

async def set_mode(user_id: int, mode: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO user_state(user_id, mode)
            VALUES(?, ?)
            ON CONFLICT(user_id)
            DO UPDATE SET mode=excluded.mode
            """,
            (user_id, mode)
        )
        await db.commit()
