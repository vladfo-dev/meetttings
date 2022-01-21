from backend.app.database import SessionLocal


async def get_db_func():
    with MySuperContextManager() as db:
        yield db


class MySuperContextManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()