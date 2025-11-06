"""
Versão simplificada do VLibras - alternativa quando o VLibras completo não está disponível.
Usa uma abordagem baseada em dicionário de palavras comuns.
"""

# Dicionário básico de glosses em LIBRAS para palavras comuns
# Baseado em sinais básicos de LIBRAS
LIBRAS_GLOSS_DICT = {
    "olá": "OLÁ",
    "oi": "OI",
    "obrigado": "OBRIGADO",
    "obrigada": "OBRIGADA",
    "por favor": "POR-FAVOR",
    "bom dia": "BOM-DIA",
    "boa tarde": "BOA-TARDE",
    "boa noite": "BOA-NOITE",
    "família": "FAMÍLIA",
    "amigo": "AMIGO",
    "amiga": "AMIGA",
    "mãe": "MÃE",
    "pai": "PAI",
    "água": "ÁGUA",
    "comida": "COMIDA",
    "casa": "CASA",
    "escola": "ESCOLA",
    "trabalho": "TRABALHO",
    "sim": "SIM",
    "não": "NÃO",
    "amor": "AMOR",
    "eu te amo": "AMOR",  # Alias para compatibilidade
    "feliz": "FELIZ",
    "entristecer": "ENTRISTECER",
    "triste": "ENTRISTECER",  # Alias para compatibilidade
    "bom": "BOM",
    "ruim": "RUIM",
    "certo": "CERTO",
    "errado": "ERRADO",
    "ok": "OK",
    "tchau": "TCHAU",
    "até logo": "ATÉ-LOGO",
    "desculpa": "DESCULPA",
    "de nada": "DE-NADA",
    "por favor": "POR-FAVOR",
    "com licença": "COM-LICENÇA",
    "me ajuda": "ME-AJUDA",
    "ajuda": "AJUDA",
    "favor": "FAVOR",
    "por favor": "POR-FAVOR",
}

def get_gloss(text: str) -> Optional[str]:
    """
    Retorna o gloss em LIBRAS para um texto (versão simplificada)
    
    Args:
        text: Texto em português (minúsculas)
        
    Returns:
        Gloss em LIBRAS ou None
    """
    text_lower = text.lower().strip()
    
    # Tentar match exato primeiro
    if text_lower in LIBRAS_GLOSS_DICT:
        return LIBRAS_GLOSS_DICT[text_lower]
    
    # Tentar match parcial para frases
    for key, value in LIBRAS_GLOSS_DICT.items():
        if key in text_lower or text_lower in key:
            return value
    
    return None

def translate_text_simple(text: str) -> Dict[str, Any]:
    """
    Traduz texto usando o dicionário simplificado
    
    Args:
        text: Texto em português
        
    Returns:
        Dicionário com resultado da tradução
    """
    gloss = get_gloss(text)
    
    if gloss:
        return {
            'original_text': text,
            'translation': gloss,
            'success': True,
            'method': 'simple_dict'
        }
    else:
        return {
            'original_text': text,
            'translation': None,
            'success': False,
            'error': 'Palavra não encontrada no dicionário',
            'method': 'simple_dict'
        }

