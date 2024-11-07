const addGameBtn = document.getElementById('addGameBtn');
const gameModal = document.getElementById('gameModal');
const closeModal = document.querySelector('.close');

// Mostra o formulário quando o botão é clicado
addGameBtn.addEventListener('click', () => {
  gameModal.style.display = 'block';
});

// Oculta o formulário quando o botão de fechar é clicado
closeModal.addEventListener('click', () => {
  gameModal.style.display = 'none';
});

// Oculta o formulário quando a janela é clicada fora do formulário
window.addEventListener('click', (event) => {
  if (event.target === gameModal) {
    gameModal.style.display = 'none';
  }
});
