"""
Módulo de integração com VLibras Translator
Baseado em: https://github.com/spbgovbr-vlibras/vlibras-translator-text-core

NOTA: O VLibras completo requer muitas dependências pesadas (torch, JPype1, etc).
Este módulo tenta usar o VLibras, mas funciona com fallback se não estiver disponível.
"""

import os
import sys
from typing import Optional, Dict, Any

VLIBRAS_AVAILABLE = False
VLIBRAS_ERROR = None

# Tentar importar VLibras - pode falhar devido a dependências
try:
    from vlibras_translate import Translator
    VLIBRAS_AVAILABLE = True
except ImportError as e:
    VLIBRAS_AVAILABLE = False
    VLIBRAS_ERROR = str(e)
except Exception as e:
    VLIBRAS_AVAILABLE = False
    VLIBRAS_ERROR = f"Erro ao inicializar: {str(e)}"


class VLibrasService:
    """Serviço para tradução de texto para LIBRAS usando VLibras"""
    
    def __init__(self):
        self.translator = None
        self.is_available = False
        self.error_message = None
        
        if VLIBRAS_AVAILABLE:
            try:
                self.translator = Translator()
                self.is_available = True
                print("✅ VLibras Translator inicializado com sucesso!")
            except Exception as e:
                self.is_available = False
                self.error_message = str(e)
                print(f"⚠️ Erro ao inicializar VLibras: {e}")
        else:
            self.error_message = VLIBRAS_ERROR or "Biblioteca não instalada"
            print(f"⚠️ VLibras não disponível: {self.error_message}")
            print("   O sistema continuará funcionando com vídeos estáticos.")
    
    def translate_text(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Traduz texto em português para LIBRAS usando VLibras
        Se VLibras não estiver disponível, usa fallback simplificado
        
        Args:
            text: Texto em português para traduzir
            
        Returns:
            Dicionário com informações da tradução ou None se houver erro
        """
        # Se VLibras estiver disponível, usar
        if self.is_available and self.translator:
            try:
                # Traduzir texto para LIBRAS
                result = self.translator.translate(text)
                
                return {
                    'original_text': text,
                    'translation': result,
                    'success': True,
                    'method': 'vlibras'
                }
            except Exception as e:
                print(f"Erro ao traduzir '{text}' com VLibras: {e}")
                # Fallback para método simples
                return self._translate_simple(text)
        
        # Se VLibras não estiver disponível, usar método simples
        return self._translate_simple(text)
    
    def _translate_simple(self, text: str) -> Dict[str, Any]:
        """Usa tradução simplificada como fallback"""
        try:
            from vlibras_simple import translate_text_simple
            return translate_text_simple(text)
        except ImportError:
            return {
                'original_text': text,
                'translation': None,
                'success': False,
                'error': 'Nenhum método de tradução disponível',
                'method': 'none'
            }
    
    def get_sign_gloss(self, text: str) -> Optional[str]:
        """
        Obtém o gloss (representação textual do sinal) para um texto
        
        Args:
            text: Texto em português
            
        Returns:
            Gloss em LIBRAS ou None
        """
        result = self.translate_text(text)
        if result and result.get('success'):
            # O resultado pode conter o gloss
            return result.get('translation')
        return None
    
    def generate_sign_url(self, text: str) -> Optional[str]:
        """
        Gera URL para visualização do sinal (se disponível)
        
        Args:
            text: Texto em português
            
        Returns:
            URL do sinal ou None
        """
        # Por enquanto retorna None, mas pode ser expandido
        # para integrar com serviços de vídeo ou avatares
        return None
    
    def is_service_ready(self) -> bool:
        """Verifica se o serviço VLibras está disponível"""
        return self.is_available


# Instância global do serviço
_vlibras_service = None

def get_vlibras_service() -> VLibrasService:
    """Obtém instância singleton do serviço VLibras"""
    global _vlibras_service
    if _vlibras_service is None:
        _vlibras_service = VLibrasService()
    return _vlibras_service

