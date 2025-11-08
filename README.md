TO-DO LIST Application

Application fullstack de gestion de tâches développée avec Next.js + Redux (frontend) et FastAPI + SQLAlchemy (backend).
Elle permet de créer, mettre à jour, supprimer et gérer efficacement les tâches via un tableau de bord clair.

📦 Prérequis

Avant de lancer le projet, assurez-vous d’avoir installé :

Python 3.12+

Node.js 18+

MySQL

Git

🛠 Technologies Utilisées
Frontend

Next.js 14

Redux Toolkit

Material-UI (MUI)

TypeScript

Backend

FastAPI

SQLAlchemy ORM

MySQL

Aerich (migrations)

Python 3.8+

🚀 Installation et Lancement
1️⃣ Cloner le projet
git clone [votre-repo-url]
cd todo-app

2️⃣ Configurer la base de données MySQL

Créer la base de données :

CREATE DATABASE todo_db;


Importer les données initiales si nécessaire :

mysql -u root -p todo_db < todo_db.sql

3️⃣ Backend (FastAPI)

Aller dans le dossier backend et créer un environnement virtuel :

cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


Installer les dépendances :

pip install -r requirements.txt


Configurer les variables d’environnement :

cp .env.example .env
# puis éditer .env avec vos paramètres MySQL


Générer les tables de la base :

python create_tables.py


Démarrer le serveur :

uvicorn main:app --reload


URL backend : http://127.0.0.1:8000

4️⃣ Frontend (Next.js)

Aller dans le dossier frontend :

cd ../frontend


Installer les dépendances :

npm install


Lancer le serveur de développement :

npm run dev


URL frontend : http://localhost:3000

📊 Endpoints API
Méthode	Endpoint	Description
GET	/api/v1/tasks	Récupérer toutes les tâches
POST	/api/v1/tasks	Créer une nouvelle tâche
PUT	/api/v1/tasks/{id}	Mettre à jour une tâche
DELETE	/api/v1/tasks/{id}	Supprimer une tâche
GET	/api/v1/dashboard/stats	Récupérer les statistiques du tableau de bord
🗄 Sauvegarde de la base de données

Exporter :

mysqldump -u root -p todo_db > todo_db.sql


Importer :

mysql -u root -p todo_db < todo_db.sql

🚀 Déploiement (optionnel)

Backend : Render, Railway

Frontend : Vercel

💡 Auteur

Mdjenad Bia
📧 your-email@example.com

🌐 GitHub

🧾 Licence

Ce projet est sous licence MIT — libre à utiliser et modifier.

✅ Résumé d’utilisation

Lancer le backend :

uvicorn main:app --reload


Lancer le frontend :

npm run dev


Ouvrir le navigateur :

http://localhost:3000