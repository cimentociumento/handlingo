# ⚙️ Como Configurar Vídeos Locais no HandLingo

## 📋 Passo a Passo

### 1. Criar Estrutura de Pastas

```bash
cd backend
mkdir -p static/videos
```

### 2. Baixar Vídeos

Veja `DOWNLOAD_VIDEOS.md` para saber onde baixar.

Coloque os vídeos na pasta `backend/static/videos/` com estes nomes:

- `ola.mp4`
- `obrigado.mp4`
- `por_favor.mp4`
- `bom_dia.mp4`
- `boa_tarde.mp4`
- `boa_noite.mp4`
- `familia.mp4`
- `amigo.mp4`
- `mae.mp4`
- `pai.mp4`
- `agua.mp4`
- `comida.mp4`
- `casa.mp4`
- `escola.mp4`
- `trabalho.mp4`
- `sim.mp4`
- `nao.mp4`
- `amor.mp4`
- `feliz.mp4`
- `entristecer.mp4`

### 3. Atualizar app.py

No arquivo `backend/app.py`, localize a seção `SIGNS_DATA` e atualize:

```python
SIGNS_DATA = [
    {
        "id": 1,
        "word": "Olá",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/ola.mp4",  # ← Altere aqui
        "description": "Saudação comum em LIBRAS"
    },
    # ... repita para todos os sinais
]
```

### 4. Configurar Flask para Servir Arquivos Estáticos

No `app.py`, adicione (se ainda não estiver):

```python
from flask import send_from_directory

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)
```

### 5. Testar

1. Inicie o backend: `python app.py`
2. Acesse: `http://localhost:5000/static/videos/ola.mp4`
3. O vídeo deve abrir no navegador

## 🔄 Alternativa: Usar URLs do YouTube

Se preferir usar vídeos do YouTube (sem baixar):

1. Encontre o vídeo no YouTube
2. Copie o ID do vídeo (da URL: `youtube.com/watch?v=ID_AQUI`)
3. Use no formato: `https://www.youtube.com/embed/ID_AQUI`

Exemplo:
```python
"video_url": "https://www.youtube.com/embed/7n2jYS1YJFE"
```

## 📝 Script de Atualização Automática

Veja `update_videos.py` para um script que ajuda a atualizar automaticamente.

