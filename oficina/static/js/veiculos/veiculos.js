function abrirDetalhesveiculo(id) {
    fetch(`/veiculos/detalhes/${id}/ajax/`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("det-id").innerText = data.id;
            document.getElementById("det-placa").innerText = data.placa;
            document.getElementById("det-marca_modelo").innerText = data.marca_modelo;
            document.getElementById("det-ano").innerText = data.ano;
            document.getElementById("det-cor").innerText = data.cor;
            document.getElementById("det-proprietario").innerText = data.proprietario;
            document.getElementById("det-descricao").innerText = data.descricao;

            let modal = new bootstrap.Modal(
                document.getElementById("modalDetalhes")
            );
            modal.show();
        });
}
