import requests
import json

# Testar as principais rotas do Handlingo
base_url = "http://localhost:5000"

print("🧪 Testando rotas do Handlingo...")
print("=" * 50)

# Rotas para testar
routes = [
    "/api/signs",
    "/api/categories", 
    "/api/lessons",
    "/api/users",
    "/static/videos",
    "/"
]

for route in routes:
    try:
        response = requests.get(base_url + route)
        print(f"📍 {route}: {response.status_code}")
        if response.status_code == 404:
            print(f"   ❌ Rota não encontrada!")
        elif response.status_code == 200:
            print(f"   ✅ OK!")
        else:
            print(f"   ⚠️  Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar {route}: {e}")

print("\n" + "=" * 50)
print("Teste concluído!")
print("\n📝 Verificando se há rota raiz...")

# Testar se tem rota raiz
try:
    response = requests.get(base_url)
    print(f"Rota raiz (/): {response.status_code}")
    if response.status_code == 404:
        print("ℹ️  A rota raiz não existe - isso é normal!")
        print("   O Flask está servindo apenas as rotas da API")
except Exception as e:
    print(f"Erro: {e}")