from db.database import Base, engine
from models.task_models import Task  # استدعاء الموديل Task

print("🔧 Creating tables in the database...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
