TO-DO LIST Application
Application fullstack de gestion de tâches développée avec Next.js + Redux (frontend) et FastAPI + SQLAlchemy (backend).
Elle permet aux utilisateurs de créer, mettre à jour, supprimer et gérer les tâches efficacement via une interface de tableau de bord claire.

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
Extensions VS Code Recommandées
json
{
  "recommendations": [
    "ms-python.python",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-typescript-next",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-json",
    "formulahendry.auto-rename-tag"
  ]
}
Prérequis Système
Python 3.8+

Node.js 18+

MySQL 8.0+ (recommandé)

Git

🚀 Installation et Lancement
1️⃣ Cloner le Repository
bash
git clone https://github.com/mdjenadbia/todo-list-app.git
cd todo-list-app
code .  # Ouvrir dans VS Code
2️⃣ Configuration de la Base de Données
sql
-- Dans MySQL, exécuter :
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
3️⃣ Backend (FastAPI)
📁 Ouvrir le terminal dans VS Code (Ctrl+`)
Étape 1 : Configuration de l'environnement
bash
cd backend
cp .env.example .env
Éditer le fichier .env :
env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/todo_db
SECRET_KEY=your-secret-key
DEBUG=True
Étape 2 : Environnement virtuel
bash
# Créer et activer l'environnement virtuel
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
Étape 3 : Installation des dépendances
bash
pip install -r requirements.txt
Étape 4 : Configuration de la base
bash
# Création des tables
python -c "from db.database import Base, engine; Base.metadata.create_all(bind=engine)"
Étape 5 : Lancer le serveur
bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
✅ Backend disponible sur : http://127.0.0.1:8000
📚 Documentation API : http://127.0.0.1:8000/docs

4️⃣ Frontend (Next.js + TypeScript)
📁 Ouvrir un nouveau terminal dans VS Code (Ctrl+Shift+`)
Étape 1 : Navigation
bash
cd frontend
Étape 2 : Configuration
bash
cp .env.example .env.local
Vérifier le fichier .env.local :
env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
Étape 3 : Installation
bash
npm install
Étape 4 : Lancement
bash
npm run dev
✅ Frontend disponible sur : http://localhost:3000

📊 Endpoints API
Méthode	Endpoint	Description
GET	/api/v1/tasks	Récupérer toutes les tâches
POST	/api/v1/tasks	Créer une nouvelle tâche
PUT	/api/v1/tasks/{id}	Mettre à jour une tâche
DELETE	/api/v1/tasks/{id}	Supprimer une tâche
GET	/api/v1/dashboard/stats	Statistiques du tableau de bord
GET	/health	Santé de l'API
GET	/health/database	Connexion base de données
🗄️ Gestion Base de Données
Exportation
bash
mysqldump -u root -p todo_db > todo_db.sql
Importation
bash
mysql -u root -p todo_db < todo_db.sql
Structure de la table
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
🛠️ Commandes Utiles dans VS Code
Installation complète
bash
# Dans le terminal VS Code
npm run install:all
Lancement simultané
bash
# Backend + Frontend
npm run dev:full

# Windows
npm run dev:full:win
Développement
bash
# Vérification TypeScript
npm run type-check

# Linting
npm run lint

# Tests
npm run test
Débogage dans VS Code
Ajouter dans .vscode/launch.json :

json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Frontend Dev",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/frontend/node_modules/.bin/next",
      "args": ["dev"],
      "cwd": "${workspaceFolder}/frontend"
    }
  ]
}
🏗️ Structure du Projet dans VS Code
text
todo-list-app/
├── 📁 backend/
│   ├── models/          # Modèles SQLAlchemy
│   ├── schemas/         # Schémas Pydantic
│   ├── services/        # Logique métier
│   ├── routes/          # Endpoints API
│   ├── db/              # Configuration DB
│   └── main.py          # App FastAPI
├── 📁 frontend/
│   ├── components/      # Composants React
│   ├── pages/           # Pages Next.js
│   ├── store/           # Redux Store
│   ├── services/        # Services API
│   └── types/           # Types TypeScript
└── 📄 README.md
🚀 Déploiement
Backend
Render, Railway, ou Heroku

Frontend
Vercel (recommandé pour Next.js)

Netlify

🐛 Dépannage VS Code
Problèmes courants
IntelliSense ne fonctionne pas

Recharger VS Code : Ctrl+Shift+P → "Developer: Reload Window"

Import errors TypeScript

bash
npm run type-check
Environnement virtuel non détecté

Sélectionner l'interpréteur : Ctrl+Shift+P → "Python: Select Interpreter"

Dépendances manquantes

bash
# Réinstallation
cd frontend && rm -rf node_modules package-lock.json && npm install
cd ../backend && pip install -r requirements.txt
Raccourcis VS Code utiles
`Ctrl+`` : Ouvrir le terminal

Ctrl+Shift+P : Palette de commandes

F5 : Débogage

Ctrl+Shift+E : Explorateur de fichiers

👤 Auteur
Messaoud DJENADBIA
📧 Email : mdjenadbia@yahoo.fr
🌐 GitHub : mdjenadbia

📄 Licence
Ce projet est sous licence MIT.

<div align="center">
⭐ N'oubliez pas de mettre une star au repository !

</div>
Prochaines étapes dans VS Code :
Ouvrez le dossier dans VS Code

Installez les extensions recommandées

Utilisez les terminaux intégrés

Profitez du développement avec IntelliSense