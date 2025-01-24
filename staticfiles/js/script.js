console.log("Script carregado");

document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('barra-pesquisa'); // ID da barra de pesquisa
    const dropdown = document.getElementById('dropdown-resultados'); // ID do dropdown

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;
        console.log(query);

        if (query.length > 0) {
            fetch(`/buscar-produtos/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    // Limpa os resultados anteriores
                    dropdown.innerHTML = '';

                    if (data.produtos.length > 0) {
                        console.log(data.produtos);
                        data.produtos.forEach(produto => {
                            const item = document.createElement('li');
                            item.classList.add('dropdown-item', 'd-flex', 'align-items-center'); // Classe para estilização

                            // Cria o elemento de imagem
                            const img = document.createElement('img');
                            img.src = produto.foto;
                            img.style.width = '60px';
                            img.style.height = '40px';
                            img.style.objectFit = 'cover';
                            img.classList.add('me-2'); // Adiciona espaçamento e borda arredondada

                            // Cria o texto do item
                            const text = document.createElement('span');
                            text.textContent = produto.nome;

                            // Monta o item
                            item.appendChild(img);
                            item.appendChild(text);

                            // Adiciona evento de clique para redirecionar à página do produto
                            item.addEventListener('click', () => {
                                window.location.href = produto.url; // Redireciona para a URL do produto
                            });

                            dropdown.appendChild(item);
                        });
                    } else {
                        const noResult = document.createElement('li');
                        noResult.textContent = 'Nenhum resultado encontrado';
                        noResult.classList.add('dropdown-item');
                        dropdown.appendChild(noResult);
                    }

                    dropdown.style.display = 'block'; // Exibe o dropdown
                });
        } else {
            dropdown.style.display = 'none'; // Oculta o dropdown quando a barra está vazia
        }
    });

    // Ocultar o dropdown se clicar fora
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !dropdown.contains(e.target)) {
            dropdown.style.display = 'none';
        }
    });
});