$(document).ready(function() {

    const csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $('.btn-eliminarNota').click(function() {
        const notaId = $(this).data('nota-id');

        // Enviando id de la nota al modal
        $('#btn-confirm-eliminarNota').data('nota-id', notaId); 
    });


    $('#btn-confirm-eliminarNota').click(function() {
        const notaId = $(this).data('nota-id');
        
        $.ajax({
            url: 'notas/eliminar-nota/' + notaId + '/',
            type: 'POST',
            headers: { "X-CSRFToken": csrfToken },
            success: function(data) {
                // Actualizando la pagina
                location.reload();
            },
            error: function(error) {
                console.error('Error al eliminar la nota:', error);
            }
        });
    })


    $('.btn-editarNota').click(function() {
        const notaId = $(this).data('nota-id');
        
        $.ajax({
            url: '/notas/' + notaId + '/',
            type: 'GET',
            success: function(response) {
                
                const {titulo, contenido, color, imagen, fuente, autores} = response;
                
                $('#titulo').val(titulo);
                $('#contenido').val(contenido);
                $('#color').val(color);
                $('#imagen').val(imagen);

                // Seleccionando opcion 
                $(`#fuente option:contains("${fuente}")`).prop('selected', true);

                $('#autores option').each(function() {
                    var autor_id = $(this)[0].innerText;
                    console.log(autores)
                    autores.forEach(autor => {
                        if(autor.username === autor_id) {
                            // Marcar la opcion como seleccionada
                            $(this).prop('selected', true);
                        }
                    });
                });
            },
            error: function(error) {
                console.error('Error al obtener la información de la nota:', error);
            }
        });

        $('#editarNota').data('nota-id', notaId); 
    })


    // Formulario para editar notas
    $('#editarNota').submit(function(e) {
        
        const notaId = $(this).data('nota-id');

        document.querySelector('#editarNota').action = `notas/editar/${notaId}/`

    })

});