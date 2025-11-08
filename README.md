# TO-DO LIST Application

Application fullstack de gestion de tâches développée avec Next.js + Redux (frontend) et FastAPI + SQLAlchemy (backend).
Elle permet aux utilisateurs de créer, mettre à jour, supprimer et gérer les tâches efficacement via une interface de tableau de bord claire.

Prérequis

Avant de lancer le projet, assurez-vous d’avoir installé :

- [Python 3.12+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [MySQL](https://dev.mysql.com/downloads/)
- [Git](https://git-scm.com/)


## 🛠 Technologies Utilisées

### Frontend
- Next.js 14
- Redux Toolkit
- Material-UI (MUI)
- TypeScript

### Backend  
- FastAPI
- SQLAlchemy ORM
- MySQL
- Aerich (migrations)
- Python 3.8+

## 🚀 Installation et Lancement

### Pré-requis
- Node.js 18+
- Python 3.8+
- MySQL

### Installation
```bash
# Cloner le repository
git clone [votre-repo-url]
cd todo-app

cloner todo_db depuis GitHub
1️⃣ Cloner le dépôt GitHub

Ouvrez un terminal et exécutez :

git clone https://github.com/<username>/<repository>.git
cd <repository>

Importer le fichier SQL

Toujours dans le terminal :

mysql -u root -p todo_db < todo_db.sql

# Installer toutes les dépendances
npm run install:all

# Configurer les variables d'environnement
cp backend/.env.example backend/.env

# Éditer le fichier .env avec vos paramètres MySQL

Instructions d’Installation
1️⃣ Backend (FastAPI)
Étape 1 : Créer et activer un environnement virtuel
cd backend
python -m venv venv
venv\Scripts\activate  # Sur Windows
# ou
source venv/bin/activate  # Sur Mac/Linux

Étape 2 : Installer les dépendances
pip install -r requirements.txt

Étape 3 : Configurer la base de données

Assurez-vous que MySQL fonctionne, puis créez une base de données :

CREATE DATABASE todo_db;

Étape 4 : Générer les tables de la base
python create_tables.py

Étape 5 : Démarrer le serveur backend
uvicorn main:app --reload


Le backend sera disponible à :
👉 http://127.0.0.1:8000

2️⃣ Frontend (Next.js + TypeScript)
Étape 1 : Aller dans le dossier frontend
cd ../frontend

Étape 2 : Installer les dépendances
npm install

Étape 3 : Lancer le serveur de développement
npm run dev


Ouvrez ensuite votre navigateur à :
👉 http://localhost:3000

📊 Endpoints API
Méthode	Endpoint	Description
GET	/api/v1/tasks	Récupérer toutes les tâches
POST	/api/v1/tasks	Créer une nouvelle tâche
PUT	/api/v1/tasks/{id}	Mettre à jour une tâche
DELETE	/api/v1/tasks/{id}	Supprimer une tâche
GET	/api/v1/dashboard/stats	Récupérer les statistiques du tableau de bord
🗄️ Sauvegarde de la Base de Données

Pour exporter ou importer votre base MySQL :

Exporter :

mysqldump -u root -p todo_db > todo_db.sql


Importer :

mysql -u root -p todo_db < todo_db.sql

🚀 Déploiement (optionnel)

Vous pouvez déployer :

Backend sur Render ou Railway

Frontend sur Vercel

💡 Auteur

👤 Messaoud DJENADBIA
📧 Email : mdjenadbia@yahoo.fr

🌐 GitHub : mdjenadbia

🧾 Licence

Ce projet est sous licence MIT — libre à utiliser et modifier.

✅ Résumé

Une fois l’installation terminée :

Lancer le backend : uvicorn main:app --reload

Lancer le frontend : npm run dev

Ouvrir le navigateur : http://localhost:3000
