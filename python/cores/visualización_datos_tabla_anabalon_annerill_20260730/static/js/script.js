document.addEventListener('DOMContentLoaded', function () {
    const selectPais = document.getElementById('paises');
    const form = document.getElementById('filtro-form');

    // Al cambiar el select de país
    selectPais.addEventListener('change', function () {
        if (this.value === 'todos2') {
            // Enviar el formulario
            form.submit();
            // Después de un breve instante, cambiar a "todos"
            setTimeout(() => {
                this.value = 'todos';
            }, 10);
        }
    });
});