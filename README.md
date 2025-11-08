# 📝 TO-DO LIST Application

Application fullstack de gestion de tâches avec **Next.js + Redux** (frontend) et **FastAPI + SQLAlchemy** (backend).  
Permet de créer, mettre à jour, supprimer et gérer des tâches via un tableau de bord clair.

---

## 🛠 Technologies

**Frontend** : Next.js, Redux Toolkit, TypeScript, Tailwind CSS, Axios  
**Backend** : FastAPI, SQLAlchemy ORM, MySQL, Aerich, Python 3.8+

---

## 📋 Prérequis

- Python 3.8+  
- Node.js 18+  
- MySQL 8.0+  
- Git

---

## 🚀 Installation rapide

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/mdjenadbia/todo-list-app.git
cd todo-list-app
2️⃣ Base de données
sql
Copy code
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# ou importer
mysql -u root -p todo_db < todo_db.sql
3️⃣ Backend
bash
Copy code
cd backend
cp .env.example .env
# modifier .env avec vos paramètres MySQL
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
# créer les tables
python -c "from db.database import Base, engine; Base.metadata.create_all(bind=engine)"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Backend : http://127.0.0.1:8000
Docs API : http://127.0.0.1:8000/docs

4️⃣ Frontend
bash
Copy code
cd ../frontend
cp .env.example .env.local
npm install
npm run dev
Frontend : http://localhost:3000

📊 Endpoints API
Méthode	Endpoint	Description
GET	/api/v1/tasks	Toutes les tâches
POST	/api/v1/tasks	Créer une tâche
PUT	/api/v1/tasks/{id}	Mettre à jour une tâche
DELETE	/api/v1/tasks/{id}	Supprimer une tâche
GET	/api/v1/dashboard/stats	Statistiques du tableau de bord
GET	/health	Santé de l'API
GET	/health/database	Connexion à la base

🗄️ Base de données
Exporter :

bash
Copy code
mysqldump -u root -p todo_db > todo_db.sql
Importer :

bash
Copy code
mysql -u root -p todo_db < todo_db.sql
🏗️ Structure du projet
bash
Copy code
todo-list-app/
├── backend/    # FastAPI, SQLAlchemy, Aerich
├── frontend/   # Next.js, Redux, TypeScript
└── README.md
👤 Auteur
Messaoud DJENADBIA
📧 mdjenadbia@yahoo.fr