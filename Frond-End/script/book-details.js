async function fetchBookDetails(id) {
    try {
        const response = await fetch(`http://localhost:8080/api/livros/${id}`);
        if (response.status === 404) {
            document.getElementById('book-details').innerHTML = '<p>Livro não encontrado.</p>';
            return;
        }
        if (!response.ok) {
            throw new Error('Erro ao buscar detalhes do livro: ' + response.statusText);
        }
        const livro = await response.json();
        console.log(livro); // Adicione esta linha para inspecionar o JSON retornado
        displayBookDetails(livro[0]);
    } catch (error) {
        console.error('Erro ao buscar detalhes do livro:', error);
        alert('Não foi possível carregar os detalhes do livro.');
    }
}
function irParaEmprestimo() {
            const bookId = getBookIdFromURL();
            if (bookId) {
                window.location.href = `emprestimo.html?livroId=${bookId}`;
            } else {
                alert('ID do livro não encontrado.');
            }
        }
function displayBookDetails(livro) {
    const bookDetailsElement = document.getElementById('book-details');

    const titulo = livro.titulo || 'Título não disponível';
    const autores = livro.autores || 'Desconhecido';
    const descricao = livro.descricao || 'Descrição não disponível';
    const dataDePublicacao = livro.dataDePublicacao || 'Data não disponível';
    const categoria = livro.categoria || 'Categoria não disponível';
    const avaliacao = livro.avaliacao || 'Avaliação não disponível';
    const numeroDePaginas = livro.numeroDePaginas || 'Número de páginas não disponível';
    const imagemUrl = livro.imagemUrl || 'default-image.jpg';

    bookDetailsElement.innerHTML = `
        <img src="${imagemUrl}" alt="${titulo}">
        <h2>${titulo}</h2>
        <p><strong>Autor:</strong> ${autores}</p>
        <p><strong>Publicação:</strong> ${dataDePublicacao}</p>
        <p><strong>Número de Páginas:</strong> ${numeroDePaginas}</p>
        <p><strong>Categoria:</strong> ${categoria}</p>
        <p><strong>Avaliação:</strong> ${avaliacao}</p>
        <p>${descricao}</p>
    `;
}

        function getBookIdFromURL() {
            const params = new URLSearchParams(window.location.search);
            return params.get('id');
        }

        // Obter o ID do livro da URL e buscar os detalhes
        const bookId = getBookIdFromURL();
        if (bookId) {
            fetchBookDetails(bookId);
        } else {
            alert('ID do livro não encontrado.');
        }