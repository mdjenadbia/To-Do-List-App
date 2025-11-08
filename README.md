📝 TO-DO LIST Application
Application fullstack de gestion de tâches développée avec Next.js + Redux (frontend) et FastAPI + SQLAlchemy (backend). Elle permet aux utilisateurs de créer, mettre à jour, supprimer et gérer les tâches efficacement via une interface de tableau de bord claire.

🛠 Technologies Utilisées
Frontend
Next.js 14 - Framework React

Redux Toolkit - Gestion d'état

TypeScript - Langage de programmation

Tailwind CSS - Styles et design

Axios - Requêtes HTTP

Backend
FastAPI - Framework Python moderne

SQLAlchemy ORM - Mapping objet-relationnel

MySQL - Base de données relationnelle

Aerich - Gestion des migrations

Python 3.8+ - Langage backend

📋 Prérequis
Avant de lancer le projet, assurez-vous d'avoir installé :

Python 3.8+

Node.js 18+

MySQL (8.0+ recommandé)

Git

🚀 Installation et Lancement
1️⃣ Cloner le Repository
bash
# Cloner le dépôt GitHub
git clone https://github.com/mdjenadbia/todo-list-app.git
cd todo-list-app
2️⃣ Configuration de la Base de Données
sql
-- Se connecter à MySQL et créer la base de données
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Ou importer depuis un fichier SQL (si disponible)
mysql -u root -p todo_db < todo_db.sql
3️⃣ Backend (FastAPI)
Étape 1 : Configuration de l'environnement
bash
cd backend

# Copier le fichier d'environnement
cp .env.example .env

# Éditer le fichier .env avec vos paramètres MySQL
# DATABASE_URL=mysql+pymysql://username:password@localhost:3306/todo_db
Étape 2 : Environnement virtuel
bash
# Créer et activer un environnement virtuel
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur Mac/Linux
source venv/bin/activate
Étape 3 : Installation des dépendances
bash
pip install -r requirements.txt
Étape 4 : Migrations de la base de données
bash
# Initialiser Aerich pour les migrations
aerich init -t db.database.TORTOISE_ORM
aerich init-db

# Ou créer les tables directement
python -c "from db.database import Base, engine; Base.metadata.create_all(bind=engine)"
Étape 5 : Démarrer le serveur backend
bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
✅ Backend disponible sur : http://127.0.0.1:8000
📚 Documentation API : http://127.0.0.1:8000/docs

4️⃣ Frontend (Next.js + TypeScript)
Étape 1 : Navigation vers le dossier frontend
bash
cd ../frontend
Étape 2 : Configuration de l'environnement
bash
# Créer le fichier d'environnement
cp .env.example .env.local

# Vérifier que l'URL de l'API est correcte
# NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
Étape 3 : Installation des dépendances
bash
npm install
Étape 4 : Lancement du serveur de développement
bash
npm run dev
✅ Frontend disponible sur : http://localhost:3000

📊 Endpoints API
Méthode	Endpoint	Description
GET	/api/v1/tasks	Récupérer toutes les tâches
POST	/api/v1/tasks	Créer une nouvelle tâche
PUT	/api/v1/tasks/{id}	Mettre à jour une tâche
DELETE	/api/v1/tasks/{id}	Supprimer une tâche
GET	/api/v1/dashboard/stats	Récupérer les statistiques du tableau de bord
GET	/health	Vérifier la santé de l'API
GET	/health/database	Vérifier la connexion à la base de données
🗄️ Gestion de la Base de Données
Exportation de la base
bash
mysqldump -u root -p todo_db > todo_db.sql
Importation de la base
bash
mysql -u root -p todo_db < todo_db.sql
Structure de la table tasks
sql
CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    is_completed BOOLEAN DEFAULT FALSE,
    is_deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
🚀 Commandes Utiles
Installation complète
bash
# Installer toutes les dépendances (frontend + backend)
npm run install:all
Lancement complet
bash
# Lancer backend et frontend simultanément
npm run dev:full

# Sur Windows
npm run dev:full:win
Développement
bash
# Vérification TypeScript
npm run type-check

# Linting
npm run lint

# Tests
npm run test
🏗️ Structure du Projet
text
todo-list-app/
├── 📁 backend/
│   ├── models/          # Modèles de données SQLAlchemy
│   ├── schemas/         # Schémas Pydantic
│   ├── services/        # Logique métier
│   ├── routes/          # Points d'terminaison API
│   ├── db/              # Configuration base de données
│   └── main.py          # Application FastAPI principale
├── 📁 frontend/
│   ├── components/      # Composants React
│   ├── pages/           # Pages Next.js
│   ├── store/           # Configuration Redux
│   ├── services/        # Services API
│   └── types/           # Types TypeScript
└── 📄 README.md
🚀 Déploiement (Optionnel)
Backend
Render, Railway, ou Heroku

Configuration des variables d'environnement de production

Frontend
Vercel (recommandé pour Next.js)

Netlify ou Railway

🐛 Dépannage
Problèmes courants
Erreur de connexion à la base de données

Vérifier que MySQL est démarré

Confirmer les identifiants dans .env

Erreur CORS

Vérifier que le backend écoute sur le port 8000

Contrôler les configurations CORS dans main.py

Problèmes de dépendances

Réinstaller les dépendances :

bash
cd frontend && rm -rf node_modules package-lock.json && npm install
cd ../backend && pip install -r requirements.txt
👤 Auteur
👤 Messaoud DJENADBIA
📧 Email : mdjenadbia@yahoo.fr
🌐 GitHub : mdjenadbia

📄 Licence
Ce projet est sous licence MIT — libre à utiliser et modifier.