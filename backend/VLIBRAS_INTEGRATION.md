# Integração com VLibras Translator

Este projeto integra o [VLibras Translator Text Core](https://github.com/spbgovbr-vlibras/vlibras-translator-text-core) do governo brasileiro para gerar traduções dinâmicas de texto para LIBRAS.

## 📦 Instalação

### Windows:
```bash
cd backend
install_vlibras.bat
```

### Linux/Mac:
```bash
cd backend
chmod +x install_vlibras.sh
./install_vlibras.sh
```

### Manual:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple vlibras-translate==1.3.4rc1
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple vlibras-deeplearning==1.4.1rc1
```

## 🚀 Como Funciona

O VLibras Translator permite traduzir texto em português para representações em LIBRAS (gloss).

### Endpoints Disponíveis

1. **Traduzir Texto**:
   ```
   POST /api/translate
   Body: { "text": "Olá" }
   Response: { "original_text": "Olá", "translation": "...", "success": true }
   ```

2. **Obter Sinal com VLibras**:
   ```
   GET /api/signs/<id>
   Response: { ..., "vlibras_gloss": "...", "vlibras_enabled": true }
   ```

## 🔧 Uso no Código

```python
from vlibras_service import get_vlibras_service

vlibras = get_vlibras_service()
if vlibras.is_service_ready():
    result = vlibras.translate_text("Olá")
    if result and result.get('success'):
        print(result.get('translation'))
```

## ⚠️ Notas Importantes

- **O VLibras completo é OPCIONAL** - o sistema funciona perfeitamente sem ele!
- O sistema usa um método simplificado que já está integrado
- O VLibras completo requer Python 3.10+, compilador C++, e muitas dependências pesadas
- Se o VLibras completo não estiver disponível, o sistema usa:
  1. Método simplificado (dicionário de palavras comuns) - **SEMPRE DISPONÍVEL**
  2. Vídeos estáticos como fallback final
- **Recomendação**: Use o sistema sem instalar o VLibras completo - ele já funciona perfeitamente!

## 📚 Documentação

- [Repositório Oficial](https://github.com/spbgovbr-vlibras/vlibras-translator-text-core)
- [Documentação VLibras](https://www.gov.br/governodigital/pt-br/vlibras)

## 🐛 Problemas Comuns

**Erro ao instalar:**
- Certifique-se de usar Python 3.10+
- Tente instalar com `--no-cache-dir`

**VLibras não inicializa:**
- Verifique se todas as dependências foram instaladas
- Execute `python -c "from vlibras_translate import Translator"` para testar

**Tradução não funciona:**
- Verifique os logs do backend
- O sistema usa fallback para vídeos estáticos se VLibras falhar

