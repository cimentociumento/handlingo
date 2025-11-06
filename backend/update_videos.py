"""
Script para atualizar automaticamente as URLs de vídeo no app.py
"""

import re
import os

# Mapeamento de palavras para nomes de arquivo
WORD_TO_FILE = {
    "Olá": "ola.mp4",
    "Obrigado": "obrigado.mp4",
    "Por favor": "por_favor.mp4",
    "Bom dia": "bom_dia.mp4",
    "Boa tarde": "boa_tarde.mp4",
    "Boa noite": "boa_noite.mp4",
    "Família": "familia.mp4",
    "Amigo": "amigo.mp4",
    "Mãe": "mae.mp4",
    "Pai": "pai.mp4",
    "Água": "agua.mp4",
    "Comida": "comida.mp4",
    "Casa": "casa.mp4",
    "Escola": "escola.mp4",
    "Trabalho": "trabalho.mp4",
    "Sim": "sim.mp4",
    "Não": "nao.mp4",
    "Amor": "amor.mp4",
    "Eu te amo": "amor.mp4",  # Alias
    "Feliz": "feliz.mp4",
    "Entristecer": "entristecer.mp4",
    "Triste": "entristecer.mp4",  # Alias
}

def update_app_py():
    """Atualiza app.py com URLs de vídeos locais"""
    
    app_py_path = 'app.py'
    
    if not os.path.exists(app_py_path):
        print(f"ERRO: {app_py_path} não encontrado!")
        return False
    
    # Ler arquivo
    with open(app_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Atualizar cada vídeo
    for word, filename in WORD_TO_FILE.items():
        # Verificar se arquivo existe
        video_path = f'static/videos/{filename}'
        if os.path.exists(video_path):
            # Buscar e substituir a URL do vídeo
            pattern = rf'("word":\s*"{re.escape(word)}"[^}}]*?"video_url":\s*")[^"]*(")'
            replacement = rf'\1/static/videos/{filename}\2'
            content = re.sub(pattern, replacement, content)
            print(f"✓ Atualizado: {word} -> /static/videos/{filename}")
        else:
            print(f"⚠ Não encontrado: {video_path} (mantendo URL original)")
    
    # Salvar arquivo
    with open(app_py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()
    print("Atualização concluída!")
    return True

def main():
    print("=" * 60)
    print("  Atualizar URLs de Vídeo no app.py")
    print("=" * 60)
    print()
    
    if update_app_py():
        print()
        print("Próximo passo: Reinicie o servidor Flask")
    else:
        print("Erro ao atualizar arquivo")

if __name__ == '__main__':
    main()

