function abrirDetalhes(id) {
    fetch(`/servicos/detalhes/${id}/ajax/`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("det-id").innerText = data.id;
            document.getElementById("det-descricao").innerText = data.descricao;
            document.getElementById("det-veiculo").innerText = data.veiculo;
            document.getElementById("det-placa").innerText = data.placa;
            document.getElementById("det-cliente").innerText = data.cliente;
            document.getElementById("det-mecanico").innerText = data.mecanico;
            document.getElementById("det-data").innerText = data.data;
            document.getElementById("det-status").innerText = data.status;
            document.getElementById("det-prioridade").innerText = data.prioridade;

            let modal = new bootstrap.Modal(document.getElementById("modalDetalhes"));
            modal.show();
        });
}
