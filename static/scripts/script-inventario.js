// Usando jQuery
$(document).ready(function() {
    const $filtro = $('#filtro');
    const $menuFiltro = $('#menu-filtro');

    // Mostrar/ocultar el filtro cuando se haga clic en el icono
    $menuFiltro.on('click', function(e) {
        e.stopPropagation(); // Evita que se propague el evento y cierre el filtro inmediatamente
        $filtro.toggle(); // Alterna entre mostrar y ocultar el filtro
    });

    // Cerrar el filtro si se hace clic fuera de él
    $(document).on('click', function(e) {
        if (!$(e.target).closest('#filtro, #menu-filtro').length) {
            $filtro.hide(); // Oculta el filtro si el clic no está dentro del filtro ni en el icono
        }
    });

    // Evitar que el clic dentro del filtro cierre el menú
    $filtro.on('click', function(e) {
        e.stopPropagation(); // Evita que el clic dentro del filtro cierre el menú
    });
});
