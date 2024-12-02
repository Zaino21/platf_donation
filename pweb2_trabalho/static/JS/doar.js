// Mostrar campos específicos com base no método de pagamento selecionado
document.getElementById('metodo-pagamento').addEventListener('change', function() {
    const metodo = this.value;
    const cartaoInfo = document.getElementById('cartao-info');
    const pixInfo = document.getElementById('pix-info');

    if (metodo === 'credito' || metodo === 'debito') {
        cartaoInfo.classList.remove('d-none');
        pixInfo.classList.add('d-none');
        } else if (metodo === 'pix') {
            pixInfo.classList.remove('d-none');
            cartaoInfo.classList.add('d-none');
        } else {
            cartaoInfo.classList.add('d-none');
            pixInfo.classList.add('d-none');
        }
    });

// Formatação do valor da doação
    function formatarValor(digitado) {
        digitado = digitado.replace(/\D/g, ''); // Remove caracteres não numéricos

        if (digitado === '') return '0,00'; // Valor padrão se vazio

            // Adiciona zeros à esquerda para garantir pelo menos 3 dígitos
            digitado = digitado.padStart(3, '0');

            // Extrai reais e centavos
            const centavos = digitado.slice(-2);
            const reais = digitado.slice(0, -2).replace(/^0+(?!$)/, '').replace(/\B(?=(\d{3})+(?!\d))/g, '.'); // Remove zeros à esquerda e adiciona pontos

            return reais + ',' + centavos;
        }

        // Define comportamento no campo de valor
        const valorInput = document.getElementById('valor');
        valorInput.addEventListener('input', function() {
            const digits = valorInput.value.replace(/\D/g, ''); // Extrai apenas dígitos
            valorInput.value = formatarValor(digits);
        });

        // Define o valor inicial como "0,00" e mantém o formato padrão
        valorInput.value = '0,00';

        // CPF: Limita a 11 dígitos numéricos e aplica formatação
        function formatCPF(cpfField) {
            cpfField.value = cpfField.value
                .replace(/\D/g, '')
                .slice(0, 11)
                .replace(/(\d{3})(\d)/, '$1.$2')
                .replace(/(\d{3})(\d)/, '$1.$2')
                .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        }
        document.getElementById('cpf').addEventListener('input', function() {
            formatCPF(this);
        });
        document.getElementById('pix-cpf').addEventListener('input', function() {
            formatCPF(this);
        });

        // Número do Cartão: Limita a 16 dígitos numéricos e aplica formatação
        document.getElementById('numero-cartao').addEventListener('input', function(e) {
            e.target.value = e.target.value
                .replace(/\D/g, '')
                .slice(0, 16)
                .replace(/(\d{4})(?=\d)/g, '$1 ')
                .trim();
        });

        // CVV: Limita a 3 dígitos numéricos
        document.getElementById('codigo-seguranca').addEventListener('input', function(e) {
            e.target.value = e.target.value.replace(/\D/g, '').slice(0, 3);
        });

        // Data de Validade: Limita a 4 dígitos numéricos e aplica formatação MM/AA
        document.getElementById('validade').addEventListener('input', function(e) {
            e.target.value = e.target.value
                .replace(/\D/g, '')
                .slice(0, 4)
                .replace(/(\d{2})(\d)/, '$1/$2');
        });