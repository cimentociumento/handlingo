# Guia de Integração de Vídeos de LIBRAS

## Como Adicionar Vídeos Reais

### Opção 1: YouTube

1. Encontre vídeos de sinais de LIBRAS no YouTube
2. Use o ID do vídeo na URL do embed:
   - Se o vídeo é: `https://www.youtube.com/watch?v=ABC123`
   - Use no embed: `https://www.youtube.com/embed/ABC123`

3. Exemplo no código:
```python
{
    "id": 1,
    "word": "Olá",
    "video_url": "https://www.youtube.com/embed/ABC123",
    ...
}
```

### Opção 2: Repositório LIBRAS-Videos

1. Acesse o repositório: https://github.com/douglasliralima/LIBRAS-Videos
2. Baixe os vídeos dos sinais
3. Hospede em YouTube, Vimeo ou serviço de hospedagem
4. Use os IDs dos vídeos hospedados

### Opção 3: Hand Talk API

1. Acesse: https://api-docs.handtalk.me/
2. Integre a API para obter avatares 3D animados
3. Substitua os vídeos por chamadas da API

### Opção 4: Vimeo

1. Faça upload dos vídeos no Vimeo
2. Use o formato de embed:
   - `https://player.vimeo.com/video/VIDEO_ID`

## Exemplo de Vídeos de LIBRAS no YouTube

Procure por:
- "LIBRAS sinal [palavra]"
- "Aprenda LIBRAS [palavra]"
- Canais educacionais de LIBRAS

Canais recomendados:
- Hand Talk
- Libras em Ação
- Aprenda LIBRAS

## Atualização em Massa

Para atualizar todos os vídeos de uma vez, edite o arquivo `app.py` e substitua os `VIDEO_ID` pelos IDs reais dos vídeos do YouTube.

