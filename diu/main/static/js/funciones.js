$(document).ready(function() {

    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    function obtenerFuentes() {
        $.ajax({
            url: '/notas/fuentes/',
            type: 'GET',
            success: function(response) {
                console.log(response)
                const {fuentes} = response;

                return fuentes 
            },
            error: function(error) {
                console.error('Error al obtener las fuentes:', error);
            }
        });

        return null;
    }

    function obtenerAutores() {
        $.ajax({
            url: '/notas/autores/',
            type: 'GET',
            success: function(response) {
                
                const {autores} = response;

                return autores 
            },
            error: function(error) {
                console.error('Error al obtener los autores:', error);
            }
        });

        return null;
    }


    $('.btn-eliminarNota').click(function() {
        const notaId = $(this).data('nota-id');

        // Enviando id de la nota al modal
        $('#btn-confirm-eliminarNota').data('nota-id', notaId); 
    });

    $('.btn-editarNota').click(function() {
        const notaId = $(this).data('nota-id');
        
        $.ajax({
            url: '/notas/' + notaId + '/',
            type: 'GET',
            success: function(response) {
                
                const {titulo, contenido, color, fuente, autores} = response;

                $('#titulo').val(titulo);
                $('#contenido').val(contenido);
                $('#color').val(color);

            },
            error: function(error) {
                console.error('Error al obtener la información de la nota:', error);
            }
        });

        obtenerFuentes()
    })

    $('#btn-confirm-eliminarNota').click(function() {
        const notaId = $(this).data('nota-id');
        
        $.ajax({
            url: 'notas/eliminar-nota/' + notaId + '/',
            type: 'POST',
            headers: { "X-CSRFToken": csrfToken },
            success: function(data) {
                // Actualizando al pagins
                location.reload();
            },
            error: function(error) {
                console.error('Error al eliminar la nota:', error);
            }
        });
    })

});