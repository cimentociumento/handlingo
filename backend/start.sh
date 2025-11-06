#!/bin/bash
echo "Iniciando servidor HandLingo..."
echo ""
echo "Instalando dependências..."
pip install -r requirements.txt
echo ""
echo "Criando banco de dados..."
python app.py

