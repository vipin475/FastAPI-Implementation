# Synchronous Code

def get_user(user_id: int):
    user = database.query(user_id)  # Wait... wait... wait...
    return user

# Asynchronous Code
async def get_user(user_id: int):
    user = await database.query(user_id)  # Go do other stuff, come back when ready
    return user


# I/O-bound: mostly waiting

async def fetch_data():
    response = await http_client.get("https://api.example.com")  # 200ms wait
    return response.json()

# CPU-bound: actually computing

def calculate_report(data):
    result = 0
    for item in data:  # Millions of items
        result += complex_calculation(item)
    return result
# The CPU is busy the entire time. There's no waiting. Async provides zero benefit here — in fact, it adds overhead.




# Multiple Concurrent I/O Operations
# Slow: Sequential (3 seconds total)
def get_dashboard_sync():
    users = db.get_users()           # 1 sec
    orders = db.get_orders()         # 1 sec
    stats = api.get_stats()          # 1 sec
    return combine(users, orders, stats)

# Fast: Concurrent (1 second total)
async def get_dashboard_async():
    users, orders, stats = await asyncio.gather(
        db.get_users(),              # 1 sec ─┐
        db.get_orders(),             # 1 sec  ├─ All at once
        api.get_stats()              # 1 sec ─┘
    )
    return combine(users, orders, stats)



# Sync server:  1000 requests × 100ms each = needs many threads/processes

# Async server: 1000 requests × 100ms each = one process handles all




@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await async_db.fetch_user(user_id)
    return user




# Senario                           -           Recommendations
# Database with asyncpg, databases  -           async def
# Databases with psycogpy2, SsQLALchemy -       def
# HTTP calls with httpx, aiohttp    -           async def
# HTTP calls with requests          -           def
# File I/O with aiofiles            -           async def
# File I/O with built-in open()     -           def
# CPU Calculations                  -           def
# Multiple concurrent external calls -          asycn def + asyncio.gather() 