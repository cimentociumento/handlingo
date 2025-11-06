# 🚀 Deploy do Frontend HandLingo no Render

## 📋 **Passo a Passo Completo**

### **1. Criar novo serviço no Render**

1. Acesse: https://render.com
2. Clique em **"New +"** → **"Static Site"**
3. Conecte ao seu repositório GitHub
4. Configure conforme abaixo:

### **2. Configuração do Static Site**

**Nome do serviço:** `handlingo-frontend`

**Build Command:**
```bash
cd frontend && chmod +x build.sh && ./build.sh
```

**Publish Directory:**
```
frontend
```

**Environment Variables:**
```
API_BASE_URL=https://handlingo.onrender.com/api
```

### **3. Configurações Avançadas**

**Custom Domains:** (Opcional)
- Adicione seu domínio personalizado

**Headers:**
- `Access-Control-Allow-Origin`: `https://handlingo.onrender.com`
- `Access-Control-Allow-Methods`: `GET, POST, PUT, DELETE, OPTIONS`
- `Access-Control-Allow-Headers`: `Content-Type, Authorization`

### **4. Deploy e Teste**

1. Clique em **"Create Static Site"**
2. Aguarde 2-3 minutos pro deploy
3. Acesse a URL fornecida (ex: `https://handlingo-frontend.onrender.com`)
4. Teste o jogo completo!

## 🎯 **Resultado Final**

- **Frontend público:** `https://handlingo-frontend.onrender.com`
- **Backend API:** `https://handlingo.onrender.com`
- **Acesso global:** Disponível de qualquer dispositivo!

## 🎮 **Como Jogar**

1. Acesse a URL do frontend
2. Digite seu nome
3. Escolha uma lição
4. Aprenda LIBRAS com vídeos interativos!

## 🔧 **Arquivos de Configuração**

- `render-frontend.yaml` - Configuração do Render
- `frontend/build.sh` - Script de build Linux
- `frontend/build.bat` - Script de build Windows

## 📱 **Compatibilidade**

✅ Desktop (Windows, Mac, Linux)
✅ Mobile (Android, iOS)
✅ Tablets
✅ Smart TVs

---

**🤟 HandLingo - Aprenda LIBRAS de forma divertida!**