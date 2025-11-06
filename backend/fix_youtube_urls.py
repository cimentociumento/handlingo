"""
Script para converter URLs do YouTube de watch?v= para embed
"""

import re
import os

def convert_youtube_url(url):
    """Converte URL do YouTube para formato embed"""
    if not url:
        return url
    
    # Verificar se já está no formato embed
    if '/embed/' in url:
        return url
    
    # Extrair ID do vídeo
    patterns = [
        r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)',
        r'youtu\.be/([a-zA-Z0-9_-]+)',
        r'youtube\.com/embed/([a-zA-Z0-9_-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            return f"https://www.youtube.com/embed/{video_id}"
    
    return url

def fix_app_py():
    """Corrige URLs do YouTube no app.py"""
    
    app_py_path = 'app.py'
    
    if not os.path.exists(app_py_path):
        print(f"ERRO: {app_py_path} não encontrado!")
        return False
    
    # Ler arquivo
    with open(app_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Padrão para encontrar URLs do YouTube
    pattern = r'("video_url":\s*")(https?://[^"]*youtube[^"]*)(")'
    
    def replace_url(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        
        new_url = convert_youtube_url(url)
        
        if new_url != url:
            print(f"  Convertido: {url} -> {new_url}")
        
        return f"{prefix}{new_url}{suffix}"
    
    # Substituir todas as URLs
    new_content = re.sub(pattern, replace_url, content)
    
    # Salvar se houver mudanças
    if new_content != content:
        with open(app_py_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print()
        print("✓ URLs corrigidas!")
        return True
    else:
        print("Nenhuma URL precisa ser corrigida.")
        return False

def main():
    print("=" * 60)
    print("  Corrigir URLs do YouTube no app.py")
    print("=" * 60)
    print()
    print("Convertendo URLs de watch?v= para embed...")
    print()
    
    if fix_app_py():
        print()
        print("Próximo passo: Reinicie o servidor Flask")
    else:
        print("Nenhuma alteração necessária.")

if __name__ == '__main__':
    main()

