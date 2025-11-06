# 🌐 Como Iniciar o Servidor Frontend

## Opção 1: Script Automático (Recomendado)

### Windows:
```bash
cd frontend
start.bat
```

### Linux/Mac:
```bash
cd frontend
chmod +x start.sh
./start.sh
```

## Opção 2: Python (Manual)

### Windows:
```bash
cd frontend
python -m http.server 8000
```

### Linux/Mac:
```bash
cd frontend
python3 -m http.server 8000
```

Depois acesse: **http://localhost:8000**

## Opção 3: Node.js (se tiver instalado)

```bash
cd frontend
npx http-server -p 8000
```

Ou se tiver http-server instalado globalmente:
```bash
cd frontend
http-server -p 8000
```

## Opção 4: Abrir Direto no Navegador

1. Abra o arquivo `frontend/index.html` diretamente no navegador
2. ⚠️ **Nota**: Algumas funcionalidades podem não funcionar devido a políticas CORS
3. Para uso completo, use um servidor (Opções 1-3)

## Opção 5: VS Code Live Server

Se você usa VS Code:
1. Instale a extensão "Live Server"
2. Clique com botão direito em `index.html`
3. Selecione "Open with Live Server"

## Verificar se está funcionando

1. O servidor deve mostrar mensagens no terminal
2. Acesse http://localhost:8000 no navegador
3. Você deve ver a tela de login do HandLingo

## Problemas?

**Porta 8000 já em uso:**
- Use outra porta: `python -m http.server 8080`
- Ou feche o programa que está usando a porta 8000

**Python não encontrado:**
- Instale Python: https://www.python.org/downloads/
- Ou use Node.js: `npx http-server`

**Erro de CORS:**
- Certifique-se de usar um servidor (não abra o arquivo diretamente)
- Verifique se o backend está rodando na porta 5000

