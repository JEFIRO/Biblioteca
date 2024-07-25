async function cadastrarCliente() {
    const nome = document.getElementById('nome').value;
    const endereco = document.getElementById('endereco').value;
    const contato = document.getElementById('contato').value;

    if (!nome || !endereco || !contato) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    const cliente = {
        nome: nome,
        endereco: endereco,
        contato: contato
    };

    try {
        const response = await fetch('http://localhost:8080/api/clientes/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(cliente)
        });

        if (response.ok) {
            document.getElementById('message').textContent = 'Cliente cadastrado com sucesso!';
        } else {
            throw new Error('Erro ao cadastrar cliente: ' + response.statusText);
        }
    } catch (error) {
        console.error(error);
        alert('Não foi possível cadastrar o cliente.');
    }
}