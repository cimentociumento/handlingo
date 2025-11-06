from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

# Importar serviço VLibras
try:
    from vlibras_service import get_vlibras_service
    VLIBRAS_ENABLED = True
except ImportError:
    VLIBRAS_ENABLED = False
    print("⚠️ VLibras não disponível - usando vídeos estáticos")
    def get_vlibras_service():
        return None

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handlingo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Inicializar banco de dados mesmo quando rodando via Gunicorn
try:
    with app.app_context():
        db.create_all()
        print("✅ Banco de dados inicializado (SQLite)")
except Exception as e:
    # Evitar falha do servidor por erro de inicialização
    print(f"⚠️ Erro ao inicializar banco de dados: {e}")

# Modelos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LessonProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, default=0)
    completed_at = db.Column(db.DateTime)

# Dados de sinais de LIBRAS
# URLs de vídeos do YouTube com sinais de LIBRAS educativos
# Vídeos de canais educacionais de LIBRAS
SIGNS_DATA = [
    {
        "id": 1,
        "word": "Olá",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/ola.mp4",
        "description": "Saudação comum em LIBRAS"
    },
    {
        "id": 2,
        "word": "Obrigado",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/obrigado.mp4",
        "description": "Forma de agradecer em LIBRAS"
    },
    {
        "id": 3,
        "word": "Por favor",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/por_favor.mp4",
        "description": "Pedido educado em LIBRAS"
    },
    {
        "id": 4,
        "word": "Bom dia",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/Bom_Dia.mp4",
        "description": "Saudação matutina"
    },
    {
        "id": 5,
        "word": "Boa tarde",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/Boa_Tarde.mp4",
        "description": "Saudação vespertina"
    },
    {
        "id": 6,
        "word": "Boa noite",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/Boa_Noite.mp4",
        "description": "Saudação noturna"
    },
    {
        "id": 7,
        "word": "Família",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/familia.mp4",
        "description": "Grupo de pessoas relacionadas"
    },
    {
        "id": 8,
        "word": "Amigo",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/amigo.mp4",
        "description": "Pessoa com quem você tem amizade"
    },
    {
        "id": 9,
        "word": "Mãe",
        "category": "Pessoas",
        "difficulty": 1,
        "video_url": "/static/videos/mae.mp4",
        "description": "Mãe em LIBRAS"
    },
    {
        "id": 10,
        "word": "Pai",
        "category": "Pessoas",
        "difficulty": 1,
        "video_url": "/static/videos/pai.mp4",
        "description": "Pai em LIBRAS"
    },
    {
        "id": 11,
        "word": "Água",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/agua.mp4",
        "description": "Líquido essencial"
    },
    {
        "id": 12,
        "word": "Comida",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/comida.mp4",
        "description": "Alimento em geral"
    },
    {
        "id": 13,
        "word": "Casa",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/casa.mp4",
        "description": "Lugar onde você mora"
    },
    {
        "id": 14,
        "word": "Escola",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/escola.mp4",
        "description": "Local de ensino"
    },
    {
        "id": 15,
        "word": "Trabalho",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/trabalho.mp4",
        "description": "Local de trabalho"
    },
    {
        "id": 16,
        "word": "Sim",
        "category": "Respostas",
        "difficulty": 1,
        "video_url": "/static/videos/sim.mp4",
        "description": "Resposta afirmativa"
    },
    {
        "id": 17,
        "word": "Não",
        "category": "Respostas",
        "difficulty": 1,
        "video_url": "/static/videos/nao.mp4",
        "description": "Resposta negativa"
    },
    {
        "id": 18,
        "word": "Amor",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/amor.mp4",
        "description": "Expressão de amor"
    },
    {
        "id": 19,
        "word": "Feliz",
        "category": "Sentimentos",
        "difficulty": 2,
        "video_url": "/static/videos/feliz.mp4",
        "description": "Estado de alegria"
    },
    {
        "id": 20,
        "word": "Entristecer",
        "category": "Sentimentos",
        "difficulty": 2,
        "video_url": "/static/videos/entristecer.mp4",
        "description": "Estado de tristeza"
    },
    {
        "id": 21,
        "word": "Tchau",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/tchau.mp4",
        "description": "Despedida em LIBRAS"
    },
    {
        "id": 22,
        "word": "Tudo bem",
        "category": "Saudações",
        "difficulty": 1,
        "video_url": "/static/videos/Tudo_bem.mp4",
        "description": "Pergunta/resposta comum"
    },
    {
        "id": 23,
        "word": "Filho",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/filho.mp4",
        "description": "Filho em LIBRAS"
    },
    {
        "id": 24,
        "word": "Filha",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/filha.mp4",
        "description": "Filha em LIBRAS"
    },
    {
        "id": 25,
        "word": "Irmão",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/irmão.mp4",
        "description": "Irmão em LIBRAS"
    },
    {
        "id": 26,
        "word": "Irmã",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/irmã.mp4",
        "description": "Irmã em LIBRAS"
    },
    {
        "id": 27,
        "word": "Esposa",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/esposa.mp4",
        "description": "Esposa em LIBRAS"
    },
    {
        "id": 28,
        "word": "Marido",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/marido.mp4",
        "description": "Marido em LIBRAS"
    },
    {
        "id": 29,
        "word": "Criança",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/criança.mp4",
        "description": "Criança em LIBRAS"
    },
    {
        "id": 30,
        "word": "Bebê",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/Bebe.mp4",
        "description": "Bebê em LIBRAS"
    },
    {
        "id": 31,
        "word": "Adulto",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/adulto.mp4",
        "description": "Adulto em LIBRAS"
    },
    {
        "id": 32,
        "word": "Jovem",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/jovem.mp4",
        "description": "Jovem em LIBRAS"
    },
    {
        "id": 33,
        "word": "Homem",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/homem.mp4",
        "description": "Homem em LIBRAS"
    },
    {
        "id": 34,
        "word": "Bisavó",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/bisavó.mp4",
        "description": "Bisavó em LIBRAS"
    },
    {
        "id": 35,
        "word": "Bisavô",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/bisavô.mp4",
        "description": "Bisavô em LIBRAS"
    },
    {
        "id": 36,
        "word": "Cunhado",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/cunhado.mp4",
        "description": "Cunhado em LIBRAS"
    },
    {
        "id": 37,
        "word": "Cunhada",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/cunhada.mp4",
        "description": "Cunhada em LIBRAS"
    },
    {
        "id": 38,
        "word": "Genro",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/genro.mp4",
        "description": "Genro em LIBRAS"
    },
    {
        "id": 39,
        "word": "Madrasta",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/madrasta.mp4",
        "description": "Madrasta em LIBRAS"
    },
    {
        "id": 40,
        "word": "Afilhado",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/afillhado.mp4",
        "description": "Afilhado em LIBRAS"
    },
    {
        "id": 41,
        "word": "Filho adotivo",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/filhoadotivo.mp4",
        "description": "Filho adotivo em LIBRAS"
    },
    {
        "id": 42,
        "word": "Alguém",
        "category": "Pessoas",
        "difficulty": 2,
        "video_url": "/static/videos/alguem.mp4",
        "description": "Alguém em LIBRAS"
    },
    {
        "id": 43,
        "word": "Amante",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/Amante.mp4",
        "description": "Amante em LIBRAS"
    },
    {
        "id": 44,
        "word": "Banheiro",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/banheiro.mp4",
        "description": "Banheiro em LIBRAS"
    },
    {
        "id": 45,
        "word": "Cinema",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/cinema.mp4",
        "description": "Cinema em LIBRAS"
    },
    {
        "id": 46,
        "word": "Parque",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/parque.mp4",
        "description": "Parque em LIBRAS"
    },
    {
        "id": 47,
        "word": "Garagem",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/Garagem.mp4",
        "description": "Garagem em LIBRAS"
    },
    {
        "id": 48,
        "word": "Elevador",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/elevador.mp4",
        "description": "Elevador em LIBRAS"
    },
    {
        "id": 49,
        "word": "Andar do prédio",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/Andar_predio.mp4",
        "description": "Andar do prédio em LIBRAS"
    },
    {
        "id": 50,
        "word": "Banco",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/bancodinheiro.mp4",
        "description": "Banco em LIBRAS"
    },
    {
        "id": 51,
        "word": "Brasil",
        "category": "Lugares",
        "difficulty": 2,
        "video_url": "/static/videos/brasil.mp4",
        "description": "Brasil em LIBRAS"
    },
    {
        "id": 52,
        "word": "Abajur",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/Abajur.mp4",
        "description": "Abajur em LIBRAS"
    },
    {
        "id": 53,
        "word": "Anel",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/anel.mp4",
        "description": "Anel em LIBRAS"
    },
    {
        "id": 54,
        "word": "Agulha",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/agulha.mp4",
        "description": "Agulha em LIBRAS"
    },
    {
        "id": 55,
        "word": "Abridor",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/abridor.mp4",
        "description": "Abridor em LIBRAS"
    },
    {
        "id": 56,
        "word": "Alicate",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/alicate.mp4",
        "description": "Alicate em LIBRAS"
    },
    {
        "id": 57,
        "word": "Algema",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/algema.mp4",
        "description": "Algema em LIBRAS"
    },
    {
        "id": 58,
        "word": "Baralho",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/baralho.mp4",
        "description": "Baralho em LIBRAS"
    },
    {
        "id": 59,
        "word": "Aquário",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/Aquário.mp4",
        "description": "Aquário em LIBRAS"
    },
    {
        "id": 60,
        "word": "Baixo",
        "category": "Objetos",
        "difficulty": 2,
        "video_url": "/static/videos/baixo.mp4",
        "description": "Baixo em LIBRAS"
    },
    {
        "id": 61,
        "word": "Anão",
        "category": "Pessoas",
        "difficulty": 3,
        "video_url": "/static/videos/anão.mp4",
        "description": "Anão em LIBRAS"
    },
    {
        "id": 62,
        "word": "Saudade",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/Saudade.mp4",
        "description": "Saudade em LIBRAS"
    },
    {
        "id": 63,
        "word": "Abatido",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/abatido.mp4",
        "description": "Abatido em LIBRAS"
    },
    {
        "id": 64,
        "word": "Aborrecido",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/aborrecido.mp4",
        "description": "Aborrecido em LIBRAS"
    },
    {
        "id": 65,
        "word": "Desgosto",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/desgosto.mp4",
        "description": "Desgosto em LIBRAS"
    },
    {
        "id": 66,
        "word": "Aversão",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/aversao.mp4",
        "description": "Aversão em LIBRAS"
    },
    {
        "id": 67,
        "word": "Atração",
        "category": "Sentimentos",
        "difficulty": 3,
        "video_url": "/static/videos/atracao.mp4",
        "description": "Atração em LIBRAS"
    },
    {
        "id": 68,
        "word": "Balbucio",
        "category": "Comunicação",
        "difficulty": 3,
        "video_url": "/static/videos/balbucio.mp4",
        "description": "Balbucio em LIBRAS"
    }
]

LESSONS = [
    {
        "id": 1,
        "title": "Saudações Básicas",
        "category": "Saudações",
        "difficulty": 1,
        "signs": [1, 2, 3, 4, 5, 6, 21, 22],
        "description": "Aprenda as saudações mais comuns em LIBRAS"
    },
    {
        "id": 2,
        "title": "Família Básica",
        "category": "Pessoas",
        "difficulty": 2,
        "signs": [7, 8, 9, 10, 23, 24, 25, 26],
        "description": "Palavras relacionadas a pessoas e família"
    },
    {
        "id": 3,
        "title": "Família Estendida",
        "category": "Pessoas",
        "difficulty": 3,
        "signs": [27, 28, 34, 35, 36, 37, 38, 39, 40, 41],
        "description": "Parentes mais distantes e relacionamentos"
    },
    {
        "id": 4,
        "title": "Pessoas e Idades",
        "category": "Pessoas",
        "difficulty": 2,
        "signs": [29, 30, 31, 32, 33, 42, 43, 61],
        "description": "Diferentes tipos de pessoas e idades"
    },
    {
        "id": 5,
        "title": "Objetos do Dia a Dia",
        "category": "Objetos",
        "difficulty": 2,
        "signs": [11, 12, 13, 52, 53, 54, 55, 56, 57, 58, 59, 60],
        "description": "Sinais para objetos comuns"
    },
    {
        "id": 6,
        "title": "Lugares Comuns",
        "category": "Lugares",
        "difficulty": 2,
        "signs": [14, 15, 44, 45, 46, 47, 48, 49, 50, 51],
        "description": "Sinais para lugares importantes"
    },
    {
        "id": 7,
        "title": "Respostas Simples",
        "category": "Respostas",
        "difficulty": 1,
        "signs": [16, 17],
        "description": "Como responder sim e não"
    },
    {
        "id": 8,
        "title": "Sentimentos Básicos",
        "category": "Sentimentos",
        "difficulty": 2,
        "signs": [18, 19, 20, 62],
        "description": "Expressar sentimentos em LIBRAS"
    },
    {
        "id": 9,
        "title": "Sentimentos Avançados",
        "category": "Sentimentos",
        "difficulty": 3,
        "signs": [63, 64, 65, 66, 67],
        "description": "Sentimentos mais complexos"
    },
    {
        "id": 10,
        "title": "Comunicação",
        "category": "Comunicação",
        "difficulty": 3,
        "signs": [68],
        "description": "Sinais relacionados à comunicação"
    }
]

# Rotas da API
@app.route('/api/signs', methods=['GET'])
def get_signs():
    category = request.args.get('category')
    difficulty = request.args.get('difficulty', type=int)
    
    signs = SIGNS_DATA
    if category:
        signs = [s for s in signs if s['category'] == category]
    if difficulty:
        signs = [s for s in signs if s['difficulty'] == difficulty]
    
    return jsonify(signs)

@app.route('/api/signs/<int:sign_id>', methods=['GET'])
def get_sign(sign_id):
    sign = next((s for s in SIGNS_DATA if s['id'] == sign_id), None)
    if sign:
        # Se VLibras estiver disponível, tentar gerar tradução dinâmica
        if VLIBRAS_ENABLED:
            vlibras = get_vlibras_service()
            if vlibras.is_service_ready():
                translation = vlibras.translate_text(sign['word'])
                if translation and translation.get('success'):
                    sign['vlibras_gloss'] = translation.get('translation')
                    sign['vlibras_enabled'] = True
        return jsonify(sign)
    return jsonify({'error': 'Sign not found'}), 404

@app.route('/api/translate', methods=['POST'])
def translate_text():
    """Endpoint para traduzir texto usando VLibras"""
    if not VLIBRAS_ENABLED:
        return jsonify({'error': 'VLibras não está disponível'}), 503
    
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Texto não fornecido'}), 400
    
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Texto vazio'}), 400
    
    vlibras = get_vlibras_service()
    if not vlibras.is_service_ready():
        return jsonify({'error': 'Serviço VLibras não está pronto'}), 503
    
    result = vlibras.translate_text(text)
    
    if result and result.get('success'):
        return jsonify({
            'original_text': text,
            'translation': result.get('translation'),
            'success': True
        })
    else:
        return jsonify({
            'original_text': text,
            'translation': None,
            'success': False,
            'error': result.get('error', 'Erro desconhecido') if result else 'Erro ao traduzir'
        }), 500

@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    return jsonify(LESSONS)

@app.route('/api/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    lesson = next((l for l in LESSONS if l['id'] == lesson_id), None)
    if lesson:
        # Adicionar detalhes dos sinais
        lesson['signs_details'] = [s for s in SIGNS_DATA if s['id'] in lesson['signs']]
        return jsonify(lesson)
    return jsonify({'error': 'Lesson not found'}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        username = data.get('username')
        
        if not username or not username.strip():
            return jsonify({'error': 'Username is required'}), 400
        
        username = username.strip()
        
        # Verificar se usuário já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            # Retornar usuário existente ao invés de erro
            return jsonify({
                'id': existing_user.id,
                'username': existing_user.username
            }), 200
        
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'id': user.id,
            'username': user.username
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def get_users():
    """Buscar usuário por username (query parameter)"""
    username = request.args.get('username')
    if username:
        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({
                'id': user.id,
                'username': user.username
            })
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'error': 'Username parameter required'}), 400

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'id': user.id,
        'username': user.username
    })

@app.route('/api/users/<int:user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    progress = LessonProgress.query.filter_by(user_id=user_id).all()
    progress_data = [{
        'lesson_id': p.lesson_id,
        'completed': p.completed,
        'score': p.score,
        'completed_at': p.completed_at.isoformat() if p.completed_at else None
    } for p in progress]
    
    return jsonify(progress_data)

@app.route('/api/users/<int:user_id>/complete-lesson', methods=['POST'])
def complete_lesson():
    data = request.json
    user_id = data.get('user_id')
    lesson_id = data.get('lesson_id')
    score = data.get('score', 0)
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Salvar progresso da lição
    progress = LessonProgress.query.filter_by(
        user_id=user_id, lesson_id=lesson_id
    ).first()
    
    if not progress:
        progress = LessonProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            completed=True,
            score=score,
            completed_at=datetime.utcnow()
        )
        db.session.add(progress)
    else:
        progress.completed = True
        progress.score = max(progress.score, score)
        progress.completed_at = datetime.utcnow()
    
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Lesson completed'
    })

@app.route('/api/categories', methods=['GET'])
def get_categories():
    categories = list(set([s['category'] for s in SIGNS_DATA]))
    return jsonify(categories)

@app.route('/static/<path:path>')
def serve_static(path):
    """Servir arquivos estáticos (vídeos)"""
    return send_from_directory('static', path)

@app.route('/')
def index():
    """Rota raiz - página inicial da API"""
    return jsonify({
        'message': '🤟 Bem-vindo ao HandLingo API!',
        'version': '1.0.0',
        'endpoints': {
            'signs': '/api/signs',
            'categories': '/api/categories',
            'lessons': '/api/lessons',
            'users': '/api/users',
            'health': '/health'
        },
        'status': 'online'
    })

@app.route('/health')
def health_check():
    """Health check para monitoramento"""
    return jsonify({
        'status': 'healthy',
        'service': 'HandLingo API',
        'timestamp': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("=" * 50)
        print("🤟 HandLingo Backend iniciado!")
        print("=" * 50)
        
        # Configurar porta para produção
        port = int(os.environ.get("PORT", 5000))
        debug_mode = os.environ.get("FLASK_ENV") != "production"
        
        print(f"Servidor rodando na porta: {port}")
        print("API disponível")
        
        # Verificar status do VLibras
        try:
            from vlibras_service import get_vlibras_service
            vlibras = get_vlibras_service()
            if vlibras and vlibras.is_service_ready():
                print("✅ VLibras Translator: ATIVO")
            else:
                print("⚠️ VLibras Translator: NÃO DISPONÍVEL")
        except Exception as e:
            print(f"⚠️ VLibras Translator: NÃO CONFIGURADO ({e})")
        
        print("=" * 50)
    app.run(debug=debug_mode, port=port, host='0.0.0.0')

