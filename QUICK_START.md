# 🚀 Guia Rápido de Início - HandLingo

## Início Rápido (5 minutos)

### 1. Backend (Terminal 1)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Você verá:
```
🤟 HandLingo Backend iniciado!
Servidor rodando em: http://localhost:5000
```

### 2. Frontend (Terminal 2)

**Opção A - Script Automático (Mais Fácil):**
- Windows: `cd frontend` e depois `start.bat`
- Linux/Mac: `cd frontend` e depois `./start.sh`

**Opção B - Python Manual:**
```bash
cd frontend
python -m http.server 8000
```

**Opção C - Abrir direto no navegador:**
- Abra `frontend/index.html` no seu navegador
- ⚠️ Algumas funcionalidades podem não funcionar sem servidor

Depois acesse: **http://localhost:8000**

> 💡 Veja `frontend/SERVIDOR.md` para mais opções e detalhes

### 3. Começar a Usar

1. Digite seu nome na tela inicial
2. Clique em "Começar a Aprender"
3. Escolha uma lição
4. Pratique os sinais de LIBRAS!

## ⚠️ Importante

**Você NÃO precisa instalar VLibras completo!** O sistema funciona perfeitamente sem ele.

Os vídeos estão usando placeholders. Para usar vídeos reais:

1. Abra `backend/app.py`
2. Procure por `SIGNS_DATA`
3. Substitua `VIDEO_ID` pelos IDs reais dos vídeos do YouTube
4. Veja `backend/VIDEO_INTEGRATION.md` para mais detalhes

## 🐛 Problemas Comuns

**Backend não inicia:**
- Verifique se Python está instalado: `python --version`
- Instale as dependências: `pip install -r requirements.txt`

**Frontend não carrega:**
- Certifique-se de que o backend está rodando na porta 5000
- Verifique o console do navegador (F12) para erros

**Vídeos não aparecem:**
- Isso é normal, os vídeos precisam ser substituídos por IDs reais
- Veja a seção "Importante" acima

## 📚 Próximos Passos

- [ ] Adicionar vídeos reais de LIBRAS
- [ ] Personalizar cores e design
- [ ] Adicionar mais sinais e lições
- [ ] Integrar com Hand Talk API

---

**Divirta-se aprendendo LIBRAS! 🤟**

