@echo off
echo Iniciando servidor HandLingo...
echo.
echo Instalando dependencias...
pip install -r requirements.txt
echo.
echo Criando banco de dados...
python app.py
pause

