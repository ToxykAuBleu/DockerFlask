# OS / Image
FROM python:3.11-slim
LABEL version="1.0" maintainer="Foissac Mathieu <mfoissac002@iutbayonne.univ-pau.fr>"
WORKDIR /app

# Installation de Flask et de PostgreSQL pour Python
RUN pip3 install flask psycopg2-binary

# Lancement de l'application
ENTRYPOINT python3 index.py