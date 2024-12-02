let isLoggedIn = false;

// Função de verificação de login ao clicar no botão de criar campanha
function checkLogin(event) {
    if (!isLoggedIn) {
        // Impede a submissão do formulário
        event.preventDefault();

        // Exibe o modal de autenticação diretamente
        const loginAlertModal = new bootstrap.Modal(document.getElementById('authModal'));
        loginAlertModal.show();
    }
}

// Simulação de login ao submeter os formulários de login e cadastro
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    isLoggedIn = true;
    const loginModal = bootstrap.Modal.getInstance(document.getElementById('authModal'));
    loginModal.hide();
    alert('Login realizado com sucesso!');
});

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    isLoggedIn = true;
    const signupModal = bootstrap.Modal.getInstance(document.getElementById('authModal'));
    signupModal.hide();
    alert('Cadastro realizado com sucesso!');
});

// Adiciona o evento de verificação de login ao formulário de criação de campanha, se existir na página
document.addEventListener('DOMContentLoaded', function () {
    const criarCampanhaForm = document.querySelector('form[action="#"]');
    if (criarCampanhaForm) {
        criarCampanhaForm.addEventListener('submit', checkLogin);
    }

    // Carregar campanhas automaticamente ao rolar a página, se presente
    let page = 1;
    const MAX_CAMPAIGNS = 10;
    let campaignCount = 0;

    function carregarMaisCampanhas() {
        if (campaignCount >= MAX_CAMPAIGNS) return;

        const campanhaList = document.getElementById('campanha-list');
        const loading = document.getElementById('loading');
        loading.style.display = 'block';

        setTimeout(() => {
            for (let i = 0; i < 2; i++) {
                if (campaignCount >= MAX_CAMPAIGNS) break;

                // Valores simulados para Meta e Total Doado
                const meta = 10000;
                const totalDoado = Math.floor(Math.random() * meta);
                const progresso = Math.floor((totalDoado / meta) * 100);

                const campanha = document.createElement('div');
                campanha.className = 'col-md-8 offset-md-2 mb-4';
                campanha.innerHTML = `
                    <div class="card shadow-sm">
                        <div class="card-header">
                            <h5 class="card-title">Título da Campanha ${page}-${i + 1}</h5>
                        </div>
                        
                        <div class="carousel slide" data-bs-ride="carousel">
                            <div class="carousel-inner">
                                <div class="carousel-item active">
                                    <img src="assets/uploads/exemplo1.jpg" class="d-block w-100" alt="Imagem da campanha">
                                </div>
                            </div>
                        </div>
                        
                        <div class="card-body">
                            <p><strong>Meta:</strong> R$ ${meta.toLocaleString('pt-BR')}</p>
                            <p><strong>Total Doado:</strong> R$ ${totalDoado.toLocaleString('pt-BR')}</p>
                            <div class="progress mb-3">
                                <div class="progress-bar" role="progressbar" style="width: ${progresso}%;" aria-valuenow="${progresso}" aria-valuemin="0" aria-valuemax="100">${progresso}%</div>
                            </div>
                            <a href="doacao.html" class="btn btn-success w-100" onclick="checkLogin(event)">Doar</a>
                        </div>
                    </div>`;
                campanhaList.appendChild(campanha);
                campaignCount++;
            }
            loading.style.display = 'none';
            page++;
        }, 1000);
    }

    window.addEventListener('scroll', () => {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 10) {
            carregarMaisCampanhas();
        }
    });
});
