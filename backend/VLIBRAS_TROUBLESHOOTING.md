# 🔧 Solução de Problemas - VLibras

## Erros Comuns

### Erro: "Failed to build JPype1"

**Causa**: JPype1 requer compilador C++ (Visual Studio Build Tools no Windows)

**Solução**: 
- O sistema funciona SEM o VLibras completo instalado
- Use o método simplificado que já está integrado
- Se quiser instalar JPype1, instale Visual Studio Build Tools primeiro

### Erro: "torch==2.0.0 not found"

**Causa**: PyTorch 2.0.0 não está mais disponível nas versões mais recentes

**Solução**:
- O sistema funciona perfeitamente SEM o VLibras completo
- O método simplificado já está funcionando
- Não é necessário instalar o VLibras completo para usar o HandLingo

## Como Funciona Agora

O sistema HandLingo tem **3 modos de operação**:

1. **Modo VLibras Completo** (se instalado com sucesso)
   - Usa tradução neural completa
   - Requer muitas dependências pesadas

2. **Modo Simplificado** (sempre disponível)
   - Usa dicionário de palavras comuns
   - Funciona imediatamente, sem instalação extra
   - Suporta palavras básicas de LIBRAS

3. **Modo Fallback** (vídeos estáticos)
   - Usa vídeos do YouTube se disponíveis
   - Funciona sempre como última opção

## O Sistema Funciona Sem Instalação Extra!

Você **NÃO precisa** instalar o VLibras completo. O sistema já funciona com:
- ✅ Dicionário simplificado de LIBRAS
- ✅ Vídeos estáticos do YouTube
- ✅ Interface completa funcionando

## Se Quiser Tentar Instalar o VLibras Completo

**Requisitos**:
- Python 3.10+
- Compilador C++ (Visual Studio Build Tools no Windows)
- ~5GB de espaço em disco para dependências
- Paciência (instalação pode levar 30+ minutos)

**Comandos**:
```bash
# Windows - instale Visual Studio Build Tools primeiro
# https://visualstudio.microsoft.com/downloads/

# Depois tente:
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple vlibras-translate==1.3.4rc1
```

**Mas NÃO é necessário!** O sistema já funciona perfeitamente sem isso.

## Verificar Status

Execute o backend e veja a mensagem:
- ✅ "VLibras Translator: ATIVO" - VLibras completo funcionando
- ⚠️ "VLibras Translator: NÃO DISPONÍVEL" - Usando método simplificado (normal!)
- ✅ Sistema continua funcionando normalmente em ambos os casos

