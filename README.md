

##  Comment utiliser ce projet

### 1. Créer et activer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate  # Sous Windows
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Initialiser la base de données

```bash
python init_db.py
```

Cela crée les tables nécessaires et insère quelques produits dans la base de données.

### 4. Lancer l'application

```bash
python run.py
```

Ouvrir ensuite [http://localhost:5000](http://localhost:5000) dans votre navigateur pour accéder à la boutique.

---



