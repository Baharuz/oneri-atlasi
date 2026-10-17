from app.db import SessionLocal
from app.catalog import seed

with SessionLocal() as db:
    seed(db)
print("Katalog hazir.")
