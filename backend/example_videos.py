"""
Exemplo de como adicionar vídeos reais de LIBRAS ao HandLingo

Este arquivo mostra como você pode atualizar os vídeos no app.py
"""

# Exemplo de estrutura de vídeo usando diferentes fontes

EXAMPLE_VIDEOS = {
    # YouTube - substitua VIDEO_ID pelo ID real do vídeo
    "youtube": "https://www.youtube.com/embed/VIDEO_ID",
    
    # Vimeo - substitua VIDEO_ID pelo ID real do vídeo
    "vimeo": "https://player.vimeo.com/video/VIDEO_ID",
    
    # Hand Talk - usando avatares 3D (requer API key)
    "handtalk": "https://api.handtalk.me/avatar/translate?text=Olá",
    
    # Vídeo local/hospedado
    "local": "/static/videos/ola.mp4",
}

# Como encontrar vídeos de LIBRAS no YouTube:
"""
1. Acesse: https://www.youtube.com
2. Pesquise por: "LIBRAS sinal [palavra]" ou "Aprenda LIBRAS [palavra]"
3. Exemplos de buscas:
   - "LIBRAS sinal olá"
   - "LIBRAS sinal obrigado"
   - "Aprenda LIBRAS família"
4. Copie o ID do vídeo da URL
   - Se a URL é: https://www.youtube.com/watch?v=ABC123XYZ
   - O ID é: ABC123XYZ
5. Use no formato embed: https://www.youtube.com/embed/ABC123XYZ
"""

# Canais recomendados no YouTube:
RECOMMENDED_CHANNELS = [
    "Hand Talk",
    "Libras em Ação",
    "Aprenda LIBRAS",
    "Instituto Nacional de Educação de Surdos",
]

# Repositórios GitHub com datasets:
GITHUB_REPOS = [
    "douglasliralima/LIBRAS-Videos",
    # Adicione outros repositórios que encontrar
]

