const addGameBtn = document.getElementById('addGameBtn');
const gameModal = document.getElementById('gameModal');
const closeModal = document.querySelector('.close');
const assetInputFile = document.getElementById('Assets');
const assetForm = document.getElementById('addAsset')

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

assetInputFile.addEventListener("change", (e) => {
  console.log(e)
  if (e.target.files.length >= 1) {
    const formData = new FormData()

    const { target: { files } } = e

    console.log(files)

    Array.from(files).forEach(file => {
      formData.append('asset[]', file)
    })
    console.log(files)

    const headers = new Headers()
    const httpConf = {
      method: "POST",
      headers,
      mode: "cors",
      cache: "default",
      body: formData
    }



    fetch('asset/', httpConf).then((response) => {
      return response
    })
  }
});