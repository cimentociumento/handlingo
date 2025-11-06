# Como Instalar JPype1 no Windows

## Problema
JPype1 requer compilação C++, que não está disponível por padrão no Windows.

## Soluções (em ordem de preferência)

### Solução 1: Usar Binário Pré-compilado (MAIS FÁCIL) ✅

Use conda ou pip com binários pré-compilados:

```bash
# Opção A: Usar conda (recomendado)
conda install -c conda-forge jpype1

# Opção B: Instalar versão específica que tem wheel pré-compilado
pip install JPype1==1.4.1
```

### Solução 2: Instalar Visual Studio Build Tools

1. **Baixe o Visual Studio Build Tools:**
   - Acesse: https://visualstudio.microsoft.com/downloads/
   - Baixe "Build Tools for Visual Studio 2022"

2. **Instale com os componentes C++:**
   - Execute o instalador
   - Selecione "Desktop development with C++"
   - Instale

3. **Reinicie o terminal** e tente novamente:
   ```bash
   pip install JPype1
   ```

### Solução 3: Usar Python via Conda (RECOMENDADO)

Conda geralmente tem binários pré-compilados:

```bash
# Instalar Miniconda se não tiver
# https://docs.conda.io/en/latest/miniconda.html

# Criar ambiente
conda create -n handlingo python=3.10
conda activate handlingo

# Instalar JPype1
conda install -c conda-forge jpype1

# Depois instalar o resto
pip install -r requirements.txt
```

### Solução 4: Usar Versão Alternativa

Se nada funcionar, tente instalar uma versão específica que pode ter wheel:

```bash
pip install JPype1==1.4.1
# ou
pip install JPype1==1.3.0
```

## ⚠️ IMPORTANTE

**Você NÃO precisa instalar JPype1 para usar o HandLingo!**

O sistema HandLingo funciona perfeitamente sem o VLibras completo. Ele usa:
- ✅ Método simplificado (sempre disponível)
- ✅ Vídeos estáticos

**Recomendação**: Use o sistema sem instalar JPype1/VLibras completo.

## Verificar se Funcionou

```bash
python -c "import jpype; print('JPype1 instalado!')"
```

Se não der erro, está funcionando!

