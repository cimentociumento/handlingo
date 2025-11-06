# 🤟 HandLingo - Aprenda LIBRAS de Forma Gamificada

Um site educacional moderno e gamificado para aprender LIBRAS (Língua Brasileira de Sinais), inspirado no Duolingo.

## 🚀 Características

- **Gamificação Completa**: Sistema de XP, níveis, streaks e pontuação
- **Interface Moderna**: Design bonito e intuitivo estilo Duolingo
- **Lições Interativas**: Questões com vídeos de sinais de LIBRAS
- **Progresso Personalizado**: Acompanhe seu aprendizado
- **Múltiplas Categorias**: Saudações, Pessoas, Objetos, Lugares, Sentimentos

## 📋 Pré-requisitos

- Python 3.8+ (recomendado 3.10+)
- Navegador web moderno

**Nota**: O VLibras completo é opcional. O sistema funciona perfeitamente sem ele!

## 🛠️ Instalação

### Backend

1. Navegue até a pasta backend:
```bash
cd backend
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências básicas:
```bash
pip install -r requirements.txt
```

**Nota**: Se quiser instalar o VLibras completo (opcional):
- Windows: `cd backend && install_complete.bat`
- Linux/Mac: `cd backend && chmod +x install_complete.sh && ./install_complete.sh`
- Veja `backend/INSTALL_JPYPE1_WINDOWS.md` se tiver problemas

5. Execute o servidor:
```bash
python app.py
```

O backend estará rodando em `http://localhost:5000`

### Frontend

1. Abra o arquivo `frontend/index.html` em um navegador web moderno
2. Ou use um servidor local simples:
```bash
# Python
cd frontend
python -m http.server 8000

# Node.js
npx http-server frontend
```

3. Acesse `http://localhost:8000` no navegador

## 📚 Como Usar

1. **Inicie o backend** (porta 5000)
2. **Abra o frontend** no navegador
3. **Digite seu nome** e comece a aprender!
4. **Escolha uma lição** e pratique os sinais
5. **Acompanhe seu progresso** com XP, níveis e streaks

## 🎯 Estrutura do Projeto

```
handlingo/
├── backend/
│   ├── app.py              # API Flask
│   ├── requirements.txt    # Dependências Python
│   └── handlingo.db        # Banco de dados SQLite (criado automaticamente)
├── frontend/
│   ├── index.html          # Interface principal
│   ├── styles.css          # Estilos
│   └── app.js              # Lógica do frontend
└── README.md
```

## 🔌 API Endpoints

- `GET /api/signs` - Lista todos os sinais
- `GET /api/signs/<id>` - Obtém um sinal específico
- `GET /api/lessons` - Lista todas as lições
- `GET /api/lessons/<id>` - Obtém uma lição específica
- `POST /api/users` - Cria um novo usuário
- `GET /api/users/<id>` - Obtém dados do usuário
- `GET /api/users/<id>/progress` - Obtém progresso do usuário
- `POST /api/users/<id>/complete-lesson` - Completa uma lição

## 📹 Integração com Vídeos

Os vídeos de sinais podem ser integrados de várias formas:

1. **YouTube**: Use vídeos públicos de sinais de LIBRAS
   - Pesquise por "LIBRAS sinal [palavra]" no YouTube
   - Copie o ID do vídeo e use no formato: `https://www.youtube.com/embed/VIDEO_ID`

2. **Vimeo**: Hospede vídeos próprios
   - Formato: `https://player.vimeo.com/video/VIDEO_ID`

3. **Repositórios GitHub**: Use datasets como LIBRAS-Videos
   - Acesse: https://github.com/douglasliralima/LIBRAS-Videos
   - Baixe os vídeos e hospede no YouTube ou Vimeo

4. **Hand Talk API**: Integre com a API brasileira Hand Talk
   - Documentação: https://api-docs.handtalk.me/

**Para adicionar vídeos reais:**
1. Edite o arquivo `backend/app.py`
2. No array `SIGNS_DATA`, substitua `VIDEO_ID` pelos IDs reais dos vídeos
3. Veja `backend/VIDEO_INTEGRATION.md` para mais detalhes

## 🎨 Personalização

- **Cores**: Edite as variáveis CSS em `frontend/styles.css`
- **Sinais**: Adicione mais sinais em `SIGNS_DATA` no `backend/app.py`
- **Lições**: Crie novas lições editando o array `LESSONS`

## 🚧 Melhorias Futuras

- [ ] Integração com Hand Talk API
- [ ] Mais sinais e lições
- [ ] Sistema de revisão espaçada
- [ ] Modo de prática livre
- [ ] Competições e rankings
- [ ] Certificados de conclusão

## 📝 Licença

Este projeto é open source e está disponível para uso educacional.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para adicionar mais sinais, melhorar a interface ou adicionar novas funcionalidades.

---

**Desenvolvido com ❤️ para promover o aprendizado de LIBRAS**

