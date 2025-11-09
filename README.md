# TO-DO LIST Application

Application fullstack de gestion de tâches développée avec Next.js + Redux (frontend) et FastAPI + SQLAlchemy (backend).

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
git clone [https://github.com/mdjenadbia/To-Do-List-App]
cd To-Do-List-App

# Importer la base de donnee (todo_db)
mysql -u root -p todo_db < todo_db.sql
cd todo-app

# pour executer le programme (backend et frontend)
  lancer le lien:
 To-Do-List-App/start_project.bat

# Installer toutes les dépendances
npm run install:all

# Configurer les variables d'environnement
cp backend/.env.example backend/.env
# Éditer le fichier .env avec vos paramètres MySQL
