async function fetchLivros() {
    try {
        const response = await fetch('http://localhost:8080/api/livros');
        if (!response.ok) {
            throw new Error('Erro ao buscar livros: ' + response.statusText);
        }
        const livros = await response.json();
        displayLivros(livros, 'book-list');
    } catch (error) {
        console.error('Erro ao buscar livros:', error);
        alert('Não foi possível carregar a lista de livros.');
    }
}

async function buscarLivros() {
    const searchInput = document.getElementById('searchInput').value;
    if (!searchInput) {
        alert('Por favor, digite o nome do livro.');
        return;
    }

    try {
        const response = await fetch(`http://localhost:8080/api/livros/buscar?nome=${encodeURIComponent(searchInput)}`);
        if (!response.ok) {
            throw new Error('Erro ao buscar livros: ' + response.statusText);
        }
        const livros = await response.json();
        displayLivros(livros, 'search-results');
        toggleSidebar(true);
    } catch (error) {
        console.error('Erro ao buscar livros:', error);
        alert('Não foi possível carregar a lista de livros.');
    }
}

function displayLivros(livros, elementId) {
    const bookListElement = document.getElementById(elementId);
    bookListElement.innerHTML = '';

    if (livros.length === 0) {
        bookListElement.innerHTML = '<p>Nenhum livro encontrado.</p>';
        return;
    }

    livros.forEach(livro => {
        const bookItemElement = document.createElement('div');
        bookItemElement.className = 'book-item';
        bookItemElement.onclick = () => window.location.href = `book-details.html?id=${livro.id}`;

        const autores = Array.isArray(livro.autores) ? livro.autores.join(', ') : livro.autores || 'Desconhecido';

        bookItemElement.innerHTML = `
            <img src="${livro.imagemUrl || 'default-image.jpg'}" alt="${livro.titulo}">
            <h2>${livro.titulo}</h2>
            <p><strong>Autor:</strong> ${autores}</p>
            <p><strong>Publicação:</strong> ${livro.dataDePublicacao}</p>
        `;

        bookListElement.appendChild(bookItemElement);
    });
}

function toggleSidebar(open = false) {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('open', open);
}

// Exibir todos os livros ao carregar a página
window.onload = fetchLivros;