import time
from collections import defaultdict, deque

WINDOW_SECONDS = 10
MAX_REQUESTS = 5

_hits = defaultdict(lambda: deque())

def is_rate_limited(user_id: int) -> bool:
    now = time.time()
    q = _hits[user_id]

    # eski requestlarni o‘chirish
    while q and (now - q[0] > WINDOW_SECONDS):
        q.popleft()

    if len(q) >= MAX_REQUESTS:
        return True

    q.append(now)
    return False
