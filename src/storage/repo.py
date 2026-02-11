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
        
HISTORY_LIMIT = 12

async def add_message(user_id: int, role: str, content: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO messages(user_id, role, content) VALUES(?, ?, ?)",
            (user_id, role, content),
        )
        await db.commit()

async def get_history(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT role, content FROM messages WHERE user_id=? ORDER BY id DESC LIMIT ?",
            (user_id, HISTORY_LIMIT),
        ) as cur:
            rows = await cur.fetchall()
    rows.reverse()
    return [{"role": r, "content": c} for (r, c) in rows]

async def reset_history(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM messages WHERE user_id=?", (user_id,))
        await db.commit()
