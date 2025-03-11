from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from data.ORM import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

# Initialisation de l'application FastAPI
app = FastAPI()

# Configuration de la base de données SQLite
DATABASE_URL = "sqlite:///./data/patients.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import inspect

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check-tables")
def check_tables(db: Session = Depends(get_db)):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return {"tables": tables}

@app.get("/debug-db")
def debug_db(db: Session = Depends(get_db)):
    try:
        return {"db_type": str(type(db))}
    except Exception as e:
        return {"error": str(e)}

# Route de test : Hello World
@app.get("/")
def read_root():
    return {"Use /docs for documentation"}

# Route pour récupérer toutes les données
@app.get("/Sex")
def get_sex(db: Session = Depends(get_db)):
    try:
        db_ = db.query(Sex).all()
        return {"sex": [s.nom for s in db_]}
    except Exception as e:
        return {"error": str(e)} 

@app.get("/Smoker")
def get_smoker(db: Session = Depends(get_db)):
    try:
        db_ = db.query(Smoker).all()
        return {"smokers": [s.nom for s in db_]}
    except Exception as e:
        return {"error": str(e)}  # Capture the exact error message

@app.get("/Patients")
def get_patient(db: Session = Depends(get_db)):
    db_ = db.query(Patient).all()  # Utilisation du modèle Marque
    return db_
"""
# Route pour créer une nouvelle marque
@app.post("/Sex")
def create_marque(marque: MarqueIn, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == marque.name).first()  # Utilisation du modèle Marque
    if db_marque:
        raise HTTPException(status_code=400, detail="Marque déjà existante")
    
    db.add(Marque(name=marque.name))  # Utilisation du modèle Marque
    db.commit()
    db.refresh(db_marque)
    
    return {"message": f"Marque '{marque.name}' créée avec succès"}

# Route pour mettre à jour une marque
@app.put("/marques/{name}")
def update_marque(name: str, marque: MarqueIn, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == name).first()  # Utilisation du modèle Marque
    if not db_marque:
        raise HTTPException(status_code=404, detail="Marque non trouvée")
    
    db_marque.name = marque.name
    db.commit()
    db.refresh(db_marque)
    
    return {"message": f"Marque '{name}' mise à jour avec succès vers '{marque.name}'"}

# Route pour supprimer une marque
@app.delete("/marques/{name}")
def delete_marque(name: str, db: Session = Depends(get_db)):
    db_marque = db.query(Marque).filter(Marque.name == name).first()  # Utilisation du modèle Marque
    if not db_marque:
        raise HTTPException(status_code=404, detail="Marque non trouvée")
    
    db.delete(db_marque)
    db.commit()
    
    return {"message": f"Marque '{name}' supprimée avec succès"}
"""