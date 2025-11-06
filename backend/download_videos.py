"""
Script para baixar vídeos de LIBRAS do YouTube
Requer: pip install yt-dlp
"""

import os
import subprocess
import sys

# Mapeamento de palavras para termos de busca
VIDEO_SEARCHES = {
    "ola": ["LIBRAS sinal olá", "LIBRAS sinal oi", "Aprenda LIBRAS olá"],
    "obrigado": ["LIBRAS sinal obrigado", "LIBRAS obrigado"],
    "por_favor": ["LIBRAS sinal por favor", "LIBRAS por favor"],
    "bom_dia": ["LIBRAS sinal bom dia", "LIBRAS bom dia"],
    "boa_tarde": ["LIBRAS sinal boa tarde", "LIBRAS boa tarde"],
    "boa_noite": ["LIBRAS sinal boa noite", "LIBRAS boa noite"],
    "familia": ["LIBRAS sinal família", "LIBRAS família"],
    "amigo": ["LIBRAS sinal amigo", "LIBRAS amigo"],
    "mae": ["LIBRAS sinal mãe", "LIBRAS mãe"],
    "pai": ["LIBRAS sinal pai", "LIBRAS pai"],
    "agua": ["LIBRAS sinal água", "LIBRAS água"],
    "comida": ["LIBRAS sinal comida", "LIBRAS comida"],
    "casa": ["LIBRAS sinal casa", "LIBRAS casa"],
    "escola": ["LIBRAS sinal escola", "LIBRAS escola"],
    "trabalho": ["LIBRAS sinal trabalho", "LIBRAS trabalho"],
    "sim": ["LIBRAS sinal sim", "LIBRAS sim"],
    "nao": ["LIBRAS sinal não", "LIBRAS não"],
    "amor": ["LIBRAS sinal amor", "LIBRAS amor", "LIBRAS sinal eu te amo"],
    "eu_te_amo": ["LIBRAS sinal eu te amo", "LIBRAS eu te amo"],  # Alias
    "feliz": ["LIBRAS sinal feliz", "LIBRAS feliz"],
    "entristecer": ["LIBRAS sinal entristecer", "LIBRAS entristecer", "LIBRAS sinal triste"],
    "triste": ["LIBRAS sinal triste", "LIBRAS triste"],  # Alias
}

def check_yt_dlp():
    """Verifica se yt-dlp está instalado"""
    try:
        subprocess.run(['yt-dlp', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_yt_dlp():
    """Instala yt-dlp"""
    print("Instalando yt-dlp...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp'])

def download_video(url, output_path):
    """Baixa um vídeo do YouTube"""
    cmd = [
        'yt-dlp',
        '-f', 'best[ext=mp4]/best',
        '--no-playlist',
        '-o', output_path,
        url
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar: {e}")
        return False

def search_youtube(query):
    """Busca vídeos no YouTube (retorna URL do primeiro resultado)"""
    cmd = [
        'yt-dlp',
        '--get-url',
        '--no-playlist',
        f'ytsearch1:{query}'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Para obter a URL do vídeo, precisamos de uma abordagem diferente
        # Por enquanto, retorna o termo de busca
        return query
    except:
        return None

def main():
    print("=" * 60)
    print("  Download de Vídeos de LIBRAS")
    print("=" * 60)
    print()
    
    # Verificar yt-dlp
    if not check_yt_dlp():
        print("yt-dlp não encontrado. Instalando...")
        install_yt_dlp()
        if not check_yt_dlp():
            print("ERRO: Não foi possível instalar yt-dlp")
            print("Instale manualmente: pip install yt-dlp")
            return
    
    # Criar pasta de vídeos
    video_dir = os.path.join('static', 'videos')
    os.makedirs(video_dir, exist_ok=True)
    
    print()
    print("IMPORTANTE: Este script requer URLs dos vídeos do YouTube.")
    print("Você precisa fornecer as URLs manualmente.")
    print()
    print("Instruções:")
    print("1. Acesse YouTube e encontre vídeos de LIBRAS")
    print("2. Para cada palavra, copie a URL do vídeo")
    print("3. Cole aqui quando solicitado")
    print()
    
    input("Pressione Enter para começar...")
    print()
    
    # Baixar cada vídeo
    for word, searches in VIDEO_SEARCHES.items():
        output_file = os.path.join(video_dir, f"{word}.mp4")
        
        # Verificar se já existe
        if os.path.exists(output_file):
            print(f"✓ {word}.mp4 já existe, pulando...")
            continue
        
        print(f"\nPalavra: {word}")
        print(f"Termos de busca sugeridos: {', '.join(searches)}")
        print(f"Exemplo: https://www.youtube.com/watch?v=VIDEO_ID")
        
        url = input("Cole a URL do vídeo (ou Enter para pular): ").strip()
        
        if not url:
            print(f"  Pulando {word}...")
            continue
        
        if not url.startswith('http'):
            print("  URL inválida, pulando...")
            continue
        
        print(f"  Baixando {word}...")
        if download_video(url, output_file):
            print(f"  ✓ {word}.mp4 baixado com sucesso!")
        else:
            print(f"  ✗ Erro ao baixar {word}")
    
    print()
    print("=" * 60)
    print("  Download concluído!")
    print("=" * 60)
    print()
    print("Próximos passos:")
    print("1. Verifique os vídeos em: backend/static/videos/")
    print("2. Atualize app.py para usar os vídeos locais")
    print("3. Veja CONFIGURE_VIDEOS.md para mais detalhes")

if __name__ == '__main__':
    main()

