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

$(document).ready(function () {

                const clienteSelect = $('#id_cliente');
                const veiculoSelect = $('#id_veiculo');

                function carregarVeiculos(clienteId, veiculoSelecionado = null) {
                    veiculoSelect.html('<option value="">Selecione um veículo</option>');

                    if (!clienteId) return;

                    $.ajax({
                        url: "{% url 'ajax_carregar_veiculos' %}",
                        data: {
                            cliente_id: clienteId
                        },
                        success: function (data) {
                            data.forEach(function (veiculo) {
                                let selected = veiculo.id == veiculoSelecionado ? 'selected' : '';
                                veiculoSelect.append(
                                    `<option value="${veiculo.id}" ${selected}>
                                        ${veiculo.marca_modelo} - ${veiculo.placa}
                                    </option>`
                                );
                            });
                        },
                        error: function () {
                            console.error('Erro ao carregar veículos');
                        }
                    });
                }

                // 🔹 quando troca o cliente
                clienteSelect.on('change', function () {
                    carregarVeiculos($(this).val());
                });

                // 🔹 quando está editando (carrega automático)
                const clienteInicial = clienteSelect.val();
                const veiculoInicial = veiculoSelect.val();

                if (clienteInicial) {
                    carregarVeiculos(clienteInicial, veiculoInicial);
                }

            });
