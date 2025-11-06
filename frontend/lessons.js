// Configuração
const API_BASE_URL = 'https://handlingo.onrender.com/api';

// Verificar se usuário está logado
document.addEventListener('DOMContentLoaded', () => {
    const userId = localStorage.getItem('userId');
    const username = localStorage.getItem('username');
    
    if (!userId) {
        window.location.href = 'index.html';
        return;
    }
    
    // Exibir nome do usuário
    document.getElementById('username-display').textContent = username || 'Usuário';
    
    // Carregar lições
    loadLessons();
});

async function loadLessons() {
    try {
        const userId = localStorage.getItem('userId');
        if (!userId) {
            window.location.href = 'index.html';
            return;
        }

        // Buscar progresso do usuário
        const progressResponse = await fetch(`${API_BASE_URL}/users/${userId}/progress`);
        let userProgress = {};
        if (progressResponse.ok) {
            const progress = await progressResponse.json();
            progress.forEach(p => {
                userProgress[p.lesson_id] = p;
            });
        }

        // Buscar lições
        const response = await fetch(`${API_BASE_URL}/lessons`);
        if (!response.ok) throw new Error('Erro ao carregar lições');
        
        const lessons = await response.json();
        const container = document.getElementById('lessons-grid');
        container.innerHTML = '';

        lessons.forEach(lesson => {
            const card = createLessonCard(lesson, userProgress);
            container.appendChild(card);
        });
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao carregar lições');
    }
}

function createLessonCard(lesson, userProgress) {
    const card = document.createElement('div');
    card.className = `lesson-card ${userProgress[lesson.id]?.completed ? 'completed' : ''}`;
    
    const icons = ['👋', '👨‍👩‍👧‍👦', '👨‍👩‍👧‍👦', '👥', '🏠', '📍', '✅', '❤️', '💭', '💬'];
    const icon = icons[lesson.id - 1] || '📚';
    
    const difficultyDots = '🟢'.repeat(lesson.difficulty) + '⚪'.repeat(3 - lesson.difficulty);
    
    card.innerHTML = `
        <div class="lesson-icon">${icon}</div>
        <div class="lesson-title">${lesson.title}</div>
        <div class="lesson-description">${lesson.description}</div>
        <div class="lesson-meta">
            <span class="lesson-difficulty">
                <span>Dificuldade:</span>
                <span>${difficultyDots}</span>
            </span>
            <span>${lesson.signs.length} sinais</span>
        </div>
    `;
    
    card.addEventListener('click', () => {
        window.location.href = `quiz.html?lesson=${lesson.id}`;
    });
    
    return card;
}

