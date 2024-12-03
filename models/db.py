from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://usuarioo:kageyama27@localhost:5432/reportes'
# estructura postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_base_de_datos>

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
