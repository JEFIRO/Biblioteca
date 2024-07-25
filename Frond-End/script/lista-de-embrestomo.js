async function fetchEmprestimos() {
    try {
        const response = await fetch('http://localhost:8080/api/emprestimos');
        if (!response.ok) {
            throw new Error('Erro ao buscar empréstimos: ' + response.statusText);
        }
        const emprestimos = await response.json();
        displayEmprestimos(emprestimos);
    } catch (error) {
        console.error('Erro ao buscar empréstimos:', error);
        alert('Não foi possível carregar a lista de empréstimos.');
    }
}

function displayEmprestimos(emprestimos) {
    const emprestimosListElement = document.getElementById('emprestimos-list');
    emprestimosListElement.innerHTML = '';

    if (emprestimos.length === 0) {
        emprestimosListElement.innerHTML = '<tr><td colspan="4">Nenhum empréstimo encontrado.</td></tr>';
        return;
    }

    emprestimos.forEach(emprestimo => {
        const livrosList = emprestimo.livros.map(livro => livro.titulo).join(', ');
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${emprestimo.cliente.nome}</td>
            <td>${livrosList}</td>
            <td>${new Date(emprestimo.dataDeEmprestimo).toLocaleDateString()}</td>
            <td>${new Date(emprestimo.dataDeDevolucao).toLocaleDateString()}</td>
        `;
        emprestimosListElement.appendChild(row);
    });
}

window.onload = fetchEmprestimos;