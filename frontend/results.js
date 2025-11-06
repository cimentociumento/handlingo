// Configuração da API
const API_BASE_URL = 'https://handlingo.onrender.com/api';

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    // Verificar se usuário está logado
    const userId = localStorage.getItem('userId');
    if (!userId) {
        window.location.href = 'index.html';
        return;
    }

    // Obter parâmetros da URL
    const urlParams = new URLSearchParams(window.location.search);
    const percentage = parseInt(urlParams.get('score')) || 0;
    const correct = parseInt(urlParams.get('correct')) || 0;
    const total = parseInt(urlParams.get('total')) || 0;

    // Botões
    document.getElementById('back-btn').addEventListener('click', () => {
        window.location.href = 'lessons.html';
    });
    
    document.getElementById('back-to-lessons-btn').addEventListener('click', () => {
        window.location.href = 'lessons.html';
    });

    // Mostrar resultados
    showResults(percentage, correct, total);
});

function showResults(percentage, correct, total) {
    // Atualizar estatísticas
    document.getElementById('results-score').textContent = `${percentage}%`;
    document.getElementById('results-correct').textContent = `${correct}/${total}`;
    
    // Atualizar título e mensagem
    let icon = '🎉';
    let title = 'Parabéns!';
    let message = 'Você completou a lição!';
    
    if (percentage === 100) {
        icon = '🏆';
        title = 'Perfeito!';
        message = 'Você acertou todas as questões!';
    } else if (percentage >= 70) {
        icon = '🎉';
        title = 'Muito bem!';
        message = 'Ótimo trabalho! Continue praticando!';
    } else if (percentage >= 50) {
        icon = '👍';
        title = 'Bom trabalho!';
        message = 'Você está no caminho certo! Continue praticando para melhorar.';
    } else {
        icon = '💪';
        title = 'Continue praticando!';
        message = 'Não desista! Pratique mais para melhorar sua pontuação.';
    }
    
    document.getElementById('results-title').textContent = title;
    document.getElementById('results-message').textContent = message;
    document.getElementById('result-icon').textContent = icon;
    
    // Criar gráfico
    createResultsChart(percentage, correct, total);
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function createResultsChart(percentage, correct, total) {
    const ctx = document.getElementById('results-chart');
    
    const wrong = total - correct;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Acertos', 'Erros'],
            datasets: [{
                data: [correct, wrong],
                backgroundColor: [
                    'rgba(88, 204, 2, 0.8)',
                    'rgba(255, 75, 75, 0.8)'
                ],
                borderColor: [
                    'rgba(88, 204, 2, 1)',
                    'rgba(255, 75, 75, 1)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 14,
                            family: "'Nunito', sans-serif"
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = Math.round((value / total) * 100);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

