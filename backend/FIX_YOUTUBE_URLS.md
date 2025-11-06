# 🔧 Como Converter URLs do YouTube para Embed

## ⚠️ Problema

URLs do YouTube no formato `watch?v=` não funcionam em iframes.

## ✅ Solução

### Formato Errado:
```
https://www.youtube.com/watch?v=VIDEO_ID
```

### Formato Correto (para embed):
```
https://www.youtube.com/embed/VIDEO_ID
```

## 🔄 Como Converter

### Método 1: Manualmente

1. Pegue a URL: `https://www.youtube.com/watch?v=0Blw0JGc59I`
2. Extraia o ID: `0Blw0JGc59I`
3. Use no formato: `https://www.youtube.com/embed/0Blw0JGc59I`

### Método 2: Script Automático

Use o script `fix_youtube_urls.py` para converter automaticamente:

```bash
python fix_youtube_urls.py
```

## 📝 Exemplo

Você já atualizou:
- ✅ Bom dia: `https://www.youtube.com/embed/0Blw0JGc59I`
- ✅ Boa tarde: `https://www.youtube.com/embed/uREEiexMewk`
- ✅ Boa noite: `https://www.youtube.com/embed/rLe5gwZh9oM`

Essas URLs estão corretas agora!

## 🎯 Para Outros Vídeos

Quando adicionar mais vídeos do YouTube, sempre use o formato `embed`:

```python
"video_url": "https://www.youtube.com/embed/VIDEO_ID"
```

