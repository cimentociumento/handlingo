// Configuração
const API_BASE_URL = 'https://handlingo.onrender.com/api';

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const usernameInput = document.getElementById('username-input');

    startBtn.addEventListener('click', handleStart);
    
    usernameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleStart();
        }
    });
});

async function handleStart() {
    const username = document.getElementById('username-input').value.trim();
    if (!username) {
        alert('Por favor, digite seu nome!');
        return;
    }

    try {
        // Criar ou buscar usuário
        const response = await fetch(`${API_BASE_URL}/users`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username })
        });

        if (response.ok || response.status === 200) {
            const user = await response.json();
            // Salvar ID do usuário no localStorage
            localStorage.setItem('userId', user.id);
            localStorage.setItem('username', user.username);
            
            // Redirecionar para página de lições
            window.location.href = 'lessons.html';
        } else {
            const error = await response.json().catch(() => ({ error: 'Erro desconhecido' }));
            alert('Erro ao criar usuário: ' + (error.error || 'Erro desconhecido'));
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao conectar com o servidor. Certifique-se de que o backend está rodando.');
    }
}

