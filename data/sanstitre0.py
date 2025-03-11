# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:04:45 2025

@author: adrie
"""

from faker import Faker
import pandas as pd
import sqlite3
conn = sqlite3.connect('data/patients.db')
c = conn.cursor()
df=pd.read_csv("data/insurance.csv")
c.execute('''CREATE TABLE Sex(
   Id_Sex COUNTER,
   nom VARCHAR(50),
   PRIMARY KEY(Id_Sex)
);''')

c.execute('''
CREATE TABLE region(
   Id_region COUNTER,
   nom VARCHAR(50),
   PRIMARY KEY(Id_region)
);''')
c.execute('''

CREATE TABLE Smoker(
   Id_Smoker COUNTER,
   nom VARCHAR(50),
   PRIMARY KEY(Id_Smoker)
);''')
c.execute('''

CREATE TABLE Patient(
   Id_Patient COUNTER,
   bmi DECIMAL(15,2),
   age BYTE,
   prenom VARCHAR(50),
   charges DECIMAL(15,2),
   children BYTE,
   nom VARCHAR(50),
   Id_Smoker INT NOT NULL,
   Id_region INT NOT NULL,
   Id_Sex INT NOT NULL,
   PRIMARY KEY(Id_Patient),
   FOREIGN KEY(Id_Smoker) REFERENCES Smoker(Id_Smoker),
   FOREIGN KEY(Id_region) REFERENCES region(Id_region),
   FOREIGN KEY(Id_Sex) REFERENCES Sex(Id_Sex)
);
''')

# Insert a row of data
map_sex={}
for i,j in enumerate(df.sex.unique()):
    map_sex[j]=i
    c.execute("INSERT INTO Sex (Id_Sex, nom) VALUES (?, ?)", (i, j))
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
map_smoker={}
for i,j in enumerate(df.smoker.unique()):
    map_smoker[j]=i
    c.execute("INSERT INTO Smoker (Id_Smoker , nom) VALUES (?, ?)",(i,j))
    
map_region={}
for i,j in enumerate(df.region.unique()):
    map_region[j]=i
    c.execute("INSERT INTO region (Id_region , nom) VALUES (?, ?)",(i,j))
# Save (commit) the changes

fake_prenom=[]
for i in range(df.shape[0]):
    fake = Faker()
    nom=fake.name()
    c.execute("""INSERT INTO Patient (Id_Patient , bmi,age,prenom,nom,
              charges,children,
              Id_Smoker,Id_Sex,ID_region) VALUES (?, ?, ?, ?, ?, ?, ?, ? , ?,  ?)""",(i,df.loc[i,"bmi"]
    ,int(df.loc[i,"age"]),nom.split()[1],nom.split()[0]
    ,int(df.loc[i,"children"])
    ,map_sex[df.loc[i,"sex"]]
    ,map_smoker[df.loc[i,"smoker"]]
    ,map_region[df.loc[i,"region"]]
    ))

conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
    