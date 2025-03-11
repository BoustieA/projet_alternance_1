# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 13:36:24 2025

@author: adrie
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Sex(Base):
    __tablename__ = "Sex"
    
    Id_Sex = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    #patients = relationship("Patient", back_populates="Sex")

class Region(Base):
    __tablename__ = "region"
    
    Id_region = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    #atients = relationship("Patient", back_populates="region")

class Smoker(Base):
    __tablename__ = "Smoker"
    
    Id_Smoker = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    #patients = relationship("Patient", back_populates="smoker")

class Patient(Base):
    __tablename__ = "Patient"
    
    Id_Patient = Column(Integer, primary_key=True, autoincrement=True)
    bmi = Column(DECIMAL(15,2), nullable=False)
    age = Column(Integer, nullable=False)
    prenom = Column(String(50), nullable=False)
    nom = Column(String(50), nullable=False)
    charges = Column(DECIMAL(15,2), nullable=False)
    children = Column(Integer, nullable=False)
    
    Id_Smoker = Column(Integer, ForeignKey("Smoker.Id_Smoker"), nullable=False)
    Id_region = Column(Integer, ForeignKey("region.Id_region"), nullable=False)
    Id_Sex = Column(Integer, ForeignKey("Sex.Id_Sex"), nullable=False)
    
    #smoker = relationship("Smoker", back_populates="Patient")
    #region = relationship("Region", back_populates="Patient")
    #sex = relationship("Sex", back_populates="Patient")