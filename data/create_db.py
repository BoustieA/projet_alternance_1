from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey, Date, DateTime, Enum
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

from sqlalchemy.orm import Session 
Base = declarative_base()

class Abonnement(Base):
    __tablename__ = 'abonnement'
    id_abonnement = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    tarif = Column(DECIMAL(15,2), nullable=False)
    duree_mois = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    type_salle = Column(String(50), nullable=False)

class Medecin(Base):
    __tablename__ = 'medecin'
    id_medecin = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    adresse = Column(String(255), nullable=False)
    telephone = Column(String(20), nullable=False)
    email = Column(String(50))

class Assurance(Base):
    __tablename__ = 'assurance'
    id_assurance = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    adresse = Column(String(255), nullable=False)
    telephone = Column(String(50), nullable=False)

class Club(Base):
    __tablename__ = 'club'
    id_club = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(33), nullable=False)
    adresse = Column(String(255), nullable=False)
    nb_salles = Column(Integer, nullable=False)
    nombre_machine = Column(Integer, nullable=False)
    surface_totale = Column(DECIMAL(15,2), nullable=False)
    nb_casiers = Column(Integer, nullable=False)
    nb_toilettes = Column(Integer, nullable=False)
    nb_douches = Column(Integer, nullable=False)
    nb_saunas = Column(Integer, nullable=False)
    nb_places_parking = Column(Integer, nullable=False)
    pays = Column(String(50), nullable=False)
    id_assurance = Column(Integer, ForeignKey('assurance.id_assurance'))
    assurance = relationship("Assurance")

class Salle(Base):
    __tablename__ = 'salle'
    id_salle = Column(Integer, primary_key=True, autoincrement=True)
    surface = Column(DECIMAL(15,2), nullable=False)
    nom = Column(String(50), nullable=False)
    consommation_eau = Column(DECIMAL(15,2), nullable=False)
    consommation_electricite = Column(DECIMAL(15,2), nullable=False)
    id_club = Column(Integer, ForeignKey('club.id_club'))
    club = relationship("Club")

class Machine(Base):
    __tablename__ = 'machine'
    id_machine = Column(Integer, primary_key=True, autoincrement=True)
    type_machine = Column(String(50), nullable=False)
    etat = Column(String(50), nullable=False)
    num_serie = Column(String(50), nullable=False)
    id_salle = Column(Integer, ForeignKey('salle.id_salle'))
    salle = relationship("Salle")

class Membre(Base):
    __tablename__ = 'membre'
    id_membre = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(33), nullable=False)
    prenom = Column(String(33), nullable=False)
    date_naissance = Column(Date, nullable=False)
    adresse = Column(String(50))
    telephone = Column(String(20))
    email = Column(String(100))
    num_licence = Column(String(50), nullable=False)
    rib = Column(String(50), nullable=False)
    type_membre = Column(String(50), nullable=False)
    date_inscription = Column(Date, nullable=False)
    id_abonnement = Column(Integer, ForeignKey('abonnement.id_abonnement'))
    id_medecin = Column(Integer, ForeignKey('medecin.id_medecin'))
    abonnement = relationship("Abonnement")
    medecin = relationship("Medecin")

class UtilisationMachine(Base):
    __tablename__ = 'utilisation_machine'
    id_membre = Column(Integer, ForeignKey('membre.id_membre'), primary_key=True)
    id_club = Column(Integer, ForeignKey('club.id_club'), primary_key=True)
    id_machine = Column(Integer, ForeignKey('machine.id_machine'), primary_key=True)
    energie_genere = Column(DECIMAL(15,2), nullable=False)
    heure_debut = Column(DateTime, nullable=False)
    heure_fin = Column(DateTime, nullable=False)

# Configuration de la base de données
DATABASE_URL = "sqlite:///test.sqlite"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
session = Session(bind=engine)
import datetime
print("Base de données créée avec succès !")
if __name__=="__main__":
    from faker import Faker
    fake = Faker()
    for i in range(10):
        
        S=Assurance()
        S.nom="i"
        S.adresse="de"
        S.telephone="10"
        session.add(S)
        
        A=fake.name().split()
        nom,prenom=A[0],A[1]
        """
        M=Membre()
        M.nom=nom
        M.prenom=prenom
        M.date_naissance=datetime.strptime("11/11/2020", "%d/%m/%Y").date()
        M.adresse="test"
        M.id_medecin=i
        M.rib="flme;f"
        M.id_abonnement=i
        M.telephone="efe"
        M.email=" fr"
        M.type_membre="VIP"
        M.num_licence="1"
        M.date_inscription=datetime.strptime("11/11/2020", "%d/%m/%Y").date()
        session.add(M)
        """
        CP=fake.address().split()[-1]
        
        rue=" ".join(fake.address().split()[:-1])
    session.commit()
    session.close()