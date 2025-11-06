# HandLingo Backend

Backend Flask para o HandLingo - Sistema de aprendizado gamificado de LIBRAS.

## 🚀 Instalação Rápida

### Instalação Básica (Recomendada)

```bash
# 1. Instalar dependências básicas
pip install -r requirements.txt

# 2. Iniciar servidor
python app.py
```

**Pronto!** O sistema funciona perfeitamente assim.

### Instalação Completa (Opcional)

Se quiser instalar o VLibras completo (não é necessário):

```bash
# Windows
install_complete.bat

# Linux/Mac
chmod +x install_complete.sh
./install_complete.sh
```

## 📋 Requisitos

- Python 3.8+ (recomendado 3.10+)
- Dependências básicas (Flask, etc.)

### Opcional (para VLibras completo):
- Visual Studio Build Tools (Windows)
- Python 3.10+
- ~5GB de espaço em disco

## 🔧 Problemas Comuns

### Erro ao instalar JPype1?

**Solução**: Você NÃO precisa instalar JPype1! O sistema funciona sem ele.

Se mesmo assim quiser instalar:
- Veja `INSTALL_JPYPE1_WINDOWS.md`
- Ou use: `install_jpype1.bat`

### Erro ao instalar VLibras?

**Solução**: Normal! O sistema funciona sem VLibras completo.
- Veja `VLIBRAS_TROUBLESHOOTING.md`
- O método simplificado já está funcionando

## 📚 Documentação

- `VLIBRAS_INTEGRATION.md` - Integração com VLibras
- `VLIBRAS_TROUBLESHOOTING.md` - Solução de problemas
- `INSTALL_JPYPE1_WINDOWS.md` - Como instalar JPype1

## ✅ O Sistema Funciona Sem Instalação Extra!

O HandLingo tem 3 modos de operação:
1. **Método Simplificado** ✅ (sempre disponível)
2. **Vídeos Estáticos** ✅ (sempre disponível)  
3. **VLibras Completo** (opcional, requer instalação extra)

## 🎯 Endpoints da API

- `GET /api/signs` - Lista todos os sinais
- `GET /api/signs/<id>` - Obtém um sinal
- `POST /api/translate` - Traduz texto usando VLibras (simplificado ou completo)
- `GET /api/lessons` - Lista lições
- `POST /api/users` - Cria usuário

## 🚀 Iniciar Servidor

```bash
python app.py
```

Servidor rodará em: `http://localhost:5000`

