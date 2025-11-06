# 📹 Guia Rápido: Vídeos de LIBRAS

## 🎯 Resumo Rápido

### Onde Baixar:
1. **GitHub LIBRAS-Videos** ⭐ (Mais fácil)
   - https://github.com/douglasliralima/LIBRAS-Videos
   - Clone ou baixe como ZIP

2. **YouTube** (Mais flexível)
   - Busque: "LIBRAS sinal [palavra]"
   - Use yt-dlp para baixar

### Como Configurar:

1. **Criar pasta:**
   ```bash
   cd backend
   mkdir -p static/videos
   ```

2. **Baixar vídeos** e colocar na pasta com estes nomes:
   - `ola.mp4`
   - `obrigado.mp4`
   - `por_favor.mp4`
   - `bom_dia.mp4`
   - `boa_tarde.mp4`
   - `boa_noite.mp4`
   - `familia.mp4`
   - `amigo.mp4`
   - `mae.mp4`
   - `pai.mp4`
   - `agua.mp4`
   - `comida.mp4`
   - `casa.mp4`
   - `escola.mp4`
   - `trabalho.mp4`
   - `sim.mp4`
   - `nao.mp4`
   - `amor.mp4`
   - `feliz.mp4`
   - `entristecer.mp4`

3. **Atualizar automaticamente:**
   ```bash
   python update_videos.py
   ```

Pronto! Os vídeos estarão configurados.

## 📚 Documentação Completa

- `DOWNLOAD_VIDEOS.md` - Onde baixar e como
- `CONFIGURE_VIDEOS.md` - Como configurar no sistema
- `download_videos.py` - Script para baixar do YouTube
- `update_videos.py` - Script para atualizar app.py automaticamente

