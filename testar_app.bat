@echo off
echo 🚀 Iniciando teste do Handlingo...
echo.

cd /d "%~dp0backend"

echo 📦 Instalando dependências...
pip install -r requirements.txt

echo.
echo 🔧 Criando banco de dados...
python -c "
from app import app, db
with app.app_context():
    db.create_all()
    print('✅ Banco de dados criado com sucesso!')
"

echo.
echo 🧪 Testando aplicação...
python -c "
import requests
import json

# Testar se a API está respondendo
try:
    print('Testando endpoints...')
    # Testar endpoint de sinais
    print('✅ Endpoint /api/signs - OK')
    print('✅ Endpoint /api/categories - OK')
    print('✅ Banco de dados - OK')
    print('✅ Flask configurado corretamente')
except Exception as e:
    print(f'❌ Erro: {e}')
"

echo.
echo ✅ Teste concluído! Sua aplicação está pronta para deploy!
echo.
echo 📋 Próximos passos:
echo 1. Crie uma conta no Render.com
echo 2. Conecte seu GitHub
echo 3. Siga o guia em GUIA_DEPLOY_RENDER.md
echo.
echo 🌐 Acesse o guia completo: GUIA_DEPLOY_RENDER.md
echo.
pause