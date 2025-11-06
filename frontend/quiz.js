// Configuração
const API_BASE_URL = 'http://localhost:5000/api';
const FALLBACK_VIDEO_URL = 'https://www.youtube.com/embed/dQw4w9WgXcQ';

// Função para converter URLs do YouTube para formato embed ou retornar vídeo local
function convertToEmbedUrl(url) {
    if (!url || url.includes('VIDEO_ID')) {
        return FALLBACK_VIDEO_URL;
    }
    
    // Se é um arquivo local (mp4), retornar como está (será usado com <video>)
    if (url.startsWith('/static/') || url.endsWith('.mp4') || url.endsWith('.MP4')) {
        return url;
    }
    
    // Se já está no formato embed, retornar como está
    if (url.includes('/embed/')) {
        return url;
    }
    
    // Se está no formato watch?v=, converter para embed
    const watchMatch = url.match(/youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)/);
    if (watchMatch) {
        return `https://www.youtube.com/embed/${watchMatch[1]}`;
    }
    
    // Se está no formato youtu.be/, converter para embed
    const shortMatch = url.match(/youtu\.be\/([a-zA-Z0-9_-]+)/);
    if (shortMatch) {
        return `https://www.youtube.com/embed/${shortMatch[1]}`;
    }
    
    // Fallback
    return url || FALLBACK_VIDEO_URL;
}

// Função para criar elemento de vídeo (iframe para YouTube ou <video> para local)
function createVideoElement(videoUrl) {
    const url = convertToEmbedUrl(videoUrl);
    
    // Se é vídeo local (mp4), usar tag <video>
    if (url.endsWith('.mp4') || url.endsWith('.MP4') || url.startsWith('/static/')) {
        const fullUrl = url.startsWith('/static/') ? `http://localhost:5000${url}` : url;
        return `<video controls autoplay loop muted playsinline class="video-player">
                    <source src="${fullUrl}" type="video/mp4">
                    Seu navegador não suporta vídeos.
                </video>`;
    }
    
    // Se é YouTube, usar iframe
    return `<iframe 
                src="${url}" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>`;
}

// Estado da aplicação
let currentLesson = null;
let currentQuestionIndex = 0;
let totalQuestions = 0;
let correctAnswers = 0;
let lessonScore = 0;

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    // Verificar se usuário está logado
    const userId = localStorage.getItem('userId');
    if (!userId) {
        window.location.href = 'index.html';
        return;
    }

    // Obter ID da lição da URL
    const urlParams = new URLSearchParams(window.location.search);
    const lessonId = urlParams.get('lesson');
    
    if (!lessonId) {
        window.location.href = 'lessons.html';
        return;
    }

    // Botão voltar
    document.getElementById('back-btn').addEventListener('click', () => {
        window.location.href = 'lessons.html';
    });

    // Carregar lição
    startLesson(lessonId);
});

async function startLesson(lessonId) {
    try {
        const response = await fetch(`${API_BASE_URL}/lessons/${lessonId}`);
        if (!response.ok) throw new Error('Erro ao carregar lição');
        
        currentLesson = await response.json();
        currentQuestionIndex = 0;
        lessonScore = 0;
        correctAnswers = 0;
        totalQuestions = currentLesson.signs_details.length;
        
        showQuestion();
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao carregar lição');
        window.location.href = 'lessons.html';
    }
}

function showQuestion() {
    if (!currentLesson || !currentLesson.signs_details) return;
    
    const container = document.getElementById('lesson-container');
    
    // Verificar se terminou todas as questões
    if (currentQuestionIndex >= totalQuestions) {
        completeLesson();
        return;
    }
    
    const progress = ((currentQuestionIndex + 1) / totalQuestions) * 100;
    document.getElementById('lesson-progress-fill').style.width = `${progress}%`;
    document.getElementById('lesson-progress-text').textContent = 
        `Questão ${currentQuestionIndex + 1} de ${totalQuestions}`;
    
    const currentSign = currentLesson.signs_details[currentQuestionIndex];
    const questionType = Math.random() > 0.5 ? 'video' : 'word';
    
    if (questionType === 'video') {
        container.innerHTML = createVideoQuestion(currentSign, currentQuestionIndex + 1);
    } else {
        container.innerHTML = createWordQuestion(currentSign, currentQuestionIndex + 1);
    }
    
    // Adicionar event listeners aos botões
    document.querySelectorAll('.option-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            handleAnswer(this);
        });
    });
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function createVideoQuestion(sign, questionNumber) {
    const allSigns = currentLesson.signs_details;
    const wrongOptions = allSigns
        .filter(s => s.id !== sign.id)
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);
    
    const options = [sign, ...wrongOptions].sort(() => Math.random() - 0.5);
    
    return `
        <div class="question-card">
            <div class="question-header">
                <div class="question-number">Questão ${questionNumber}</div>
                <div class="question-title">Assista ao sinal</div>
                <div class="question-instruction">Qual palavra está sendo sinalizada?</div>
            </div>
            <div class="video-container">
                ${createVideoElement(sign.video_url)}
            </div>
            <div class="question-options">
                ${options.map(opt => `
                    <button class="option-btn" data-correct="${opt.id === sign.id}" data-sign-id="${opt.id}">
                        ${opt.word}
                    </button>
                `).join('')}
            </div>
        </div>
    `;
}

function createWordQuestion(sign, questionNumber) {
    const allSigns = currentLesson.signs_details;
    const wrongOptions = allSigns
        .filter(s => s.id !== sign.id)
        .sort(() => Math.random() - 0.5)
        .slice(0, 3);
    
    const options = [sign, ...wrongOptions].sort(() => Math.random() - 0.5);
    
    return `
        <div class="question-card">
            <div class="question-header">
                <div class="question-number">Questão ${questionNumber}</div>
                <div class="question-title">Qual é o sinal para "${sign.word}"?</div>
                <div class="question-instruction">Assista aos vídeos e escolha o correto</div>
            </div>
            <div class="question-options">
                ${options.map(opt => `
                    <div style="display: flex; flex-direction: column; gap: 10px;">
                        <div class="video-container" style="max-width: 100%;">
                            ${createVideoElement(opt.video_url)}
                        </div>
                        <button class="option-btn" data-correct="${opt.id === sign.id}" data-sign-id="${opt.id}">
                            Esta é a resposta
                        </button>
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function handleAnswer(button) {
    const isCorrect = button.dataset.correct === 'true';
    const allButtons = document.querySelectorAll('.option-btn');
    
    // Desabilitar todos os botões
    allButtons.forEach(btn => {
        btn.classList.add('disabled');
        if (btn.dataset.correct === 'true') {
            btn.classList.add('correct');
        } else if (btn === button && !isCorrect) {
            btn.classList.add('incorrect');
        }
    });
    
    if (isCorrect) {
        lessonScore += 10;
        correctAnswers++;
    }
    
    // Avançar para próxima questão após 1.5 segundos
    setTimeout(() => {
        currentQuestionIndex++;
        showQuestion();
    }, 1500);
}

async function completeLesson() {
    const percentage = Math.round((correctAnswers / totalQuestions) * 100);
    
    try {
        const userId = localStorage.getItem('userId');
        if (userId) {
            const response = await fetch(`${API_BASE_URL}/users/${userId}/complete-lesson`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: parseInt(userId),
                    lesson_id: currentLesson.id,
                    score: lessonScore
                })
            });
        }
        
        // Redirecionar para página de resultados
        window.location.href = `results.html?lesson=${currentLesson.id}&score=${percentage}&correct=${correctAnswers}&total=${totalQuestions}`;
    } catch (error) {
        console.error('Erro ao completar lição:', error);
        window.location.href = `results.html?lesson=${currentLesson.id}&score=${percentage}&correct=${correctAnswers}&total=${totalQuestions}`;
    }
}

