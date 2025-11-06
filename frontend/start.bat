@echo off
echo ========================================
echo   HandLingo - Servidor Frontend
echo ========================================
echo.
echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo.
    echo Opcoes alternativas:
    echo 1. Instale Python: https://www.python.org/downloads/
    echo 2. Use Node.js: npx http-server
    echo 3. Abra index.html diretamente no navegador
    pause
    exit
)
echo.
echo Iniciando servidor na porta 8000...
echo.
echo Acesse: http://localhost:8000
echo.
echo Pressione CTRL+C para parar o servidor
echo.
python -m http.server 8000

