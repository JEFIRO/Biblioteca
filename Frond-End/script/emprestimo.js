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
        const livros = await response.json();
        if (livros.length > 0) {
            displayBookDetails(livros[0]);
        } else {
            document.getElementById('book-details').innerHTML = '<p>Livro não encontrado.</p>';
        }
    } catch (error) {
        console.error('Erro ao buscar detalhes do livro:', error);
        alert('Não foi possível carregar os detalhes do livro.');
    }
}

function displayBookDetails(livro) {
    const bookDetailsElement = document.getElementById('book-details');

    const titulo = livro.titulo || 'Título não disponível';
    const autores = livro.autores || 'Desconhecido';
    const categoria = livro.categoria || 'Categoria não disponível';
    const imagemUrl = livro.imagemUrl || 'default-image.jpg';

    bookDetailsElement.innerHTML = `
        <img src="${imagemUrl}" alt="${titulo}">
        <h2>${titulo}</h2>
        <p><strong>Autor:</strong> ${autores}</p>
        <p><strong>Categoria:</strong> ${categoria}</p>
    `;
}

async function fetchClientes() {
    try {
        const response = await fetch('http://localhost:8080/api/clientes');
        if (!response.ok) {
            throw new Error('Erro ao buscar clientes: ' + response.statusText);
        }
        const clientes = await response.json();
        populateClientesSelect(clientes);
    } catch (error) {
        console.error('Erro ao buscar clientes:', error);
        alert('Não foi possível carregar a lista de clientes.');
    }
}

function populateClientesSelect(clientes) {
    const clienteSelect = document.getElementById('clienteSelect');
    clienteSelect.innerHTML = '<option value="">Selecione um cliente</option>';

    clientes.forEach(cliente => {
        const option = document.createElement('option');
        option.value = cliente.id;
        option.textContent = cliente.nome; // Assumindo que cliente tem um campo nome
        clienteSelect.appendChild(option);
    });
}

async function finalizarEmprestimo() {
    const bookId = getBookIdFromURL();
    const clienteId = document.getElementById('clienteSelect').value;
    const dataDevolucao = document.getElementById('dataDevolucao').value;

    if (!bookId || !clienteId || !dataDevolucao) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    try {
        const response = await fetch('http://localhost:8080/api/emprestimos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                livroId: bookId,
                clienteId: clienteId,
                dataDevolucao: dataDevolucao
            }),
        });

        if (response.ok) {
            alert('Empréstimo realizado com sucesso!');
            window.location.href = 'http://127.0.0.1:5503/index.html'; // Redirecionar para a página inicial ou outra página
        } else {
            throw new Error('Erro ao realizar empréstimo: ' + response.statusText);
        }
    } catch (error) {
        console.error('Erro ao realizar empréstimo:', error);
        alert('Não foi possível realizar o empréstimo.');
    }
}

function getBookIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('livroId');
}

// Obter o ID do livro da URL e buscar os detalhes
const bookId = getBookIdFromURL();
if (bookId) {
    fetchBookDetails(bookId);
    fetchClientes(); // Carregar clientes ao carregar a página
} else {
    alert('ID do livro não encontrado.');
}
