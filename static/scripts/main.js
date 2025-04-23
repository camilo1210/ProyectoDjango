$(document).ready(function(){
	$('.btn-sideBar-SubMenu').on('click', function(){
		var SubMenu=$(this).next('ul');
		var iconBtn=$(this).children('.zmdi-caret-down');
		if(SubMenu.hasClass('show-sideBar-SubMenu')){
			iconBtn.removeClass('zmdi-hc-rotate-180');
			SubMenu.removeClass('show-sideBar-SubMenu');
		}else{
			iconBtn.addClass('zmdi-hc-rotate-180');
			SubMenu.addClass('show-sideBar-SubMenu');
		}
	});
	$('.btn-exit-system').on('click', function(){
		swal({
		  	title: '¿Estas seguro que quieres salir?',
		  	text: "Tu sesion se cerrara y deberas iniciar sesion nuevamente",
		  	type: 'warning',
		  	showCancelButton: true,
		  	confirmButtonColor: '#03A9F4',
		  	cancelButtonColor: '#F44336',
		  	confirmButtonText: '<i class="zmdi zmdi-run"></i> Si, Salir!',
		  	cancelButtonText: '<i class="zmdi zmdi-close-circle"></i> No, Cancelar!'
		}).then(function () {
			window.location.href="index.html";
		});
	});
	$('.btn-menu-dashboard').on('click', function(){
		var body=$('.dashboard-contentPage');
		var sidebar=$('.dashboard-sideBar');
		if(sidebar.css('pointer-events')=='none'){
			body.removeClass('no-paddin-left');
			sidebar.removeClass('hide-sidebar').addClass('show-sidebar');
		}else{
			body.addClass('no-paddin-left');
			sidebar.addClass('hide-sidebar').removeClass('show-sidebar');
		}
	});
	$('.btn-Notifications-area').on('click', function(){
		var NotificationsArea=$('.Notifications-area');
		if(NotificationsArea.css('opacity')=="0"){
			NotificationsArea.addClass('show-Notification-area');
		}else{
			NotificationsArea.removeClass('show-Notification-area');
		}
	});
	$('.btn-search').on('click', function(){
		swal({
		  title: '¿Que deseas buscar?',
		  confirmButtonText: '<i class="zmdi zmdi-search"></i>  Buscar',
		  confirmButtonColor: '#03A9F4',
		  showCancelButton: true,
		  cancelButtonColor: '#F44336',
		  cancelButtonText: '<i class="zmdi zmdi-close-circle"></i> Cancelar',
		  html: '<div class="form-group label-floating">'+
			  		'<label class="control-label" for="InputSearch">Escriba aqui</label>'+
			  		'<input class="form-control" id="InputSearch" type="text">'+
				'</div>'
		}).then(function () {
		  swal(
		    'Tu escribiste',
		    ''+$('#InputSearch').val()+'',
		    'success'
		  )
		});
	});
	$('.btn-modal-help').on('click', function(){
		$('#Dialog-Help').modal('show');
	});
});
(function($){
    $(window).on("load",function(){
        $(".dashboard-sideBar-ct").mCustomScrollbar({
        	theme:"light-thin",
        	scrollbarPosition: "inside",
        	autoHideScrollbar: true,
        	scrollButtons: {enable: true}
        });
        $(".dashboard-contentPage, .Notifications-body").mCustomScrollbar({
        	theme:"dark-thin",
        	scrollbarPosition: "inside",
        	autoHideScrollbar: true,
        	scrollButtons: {enable: true}
        });
    });
})(jQuery);
$(document).ready(function() {
    const $filtro = $('#filtro');
    const $menuFiltro = $('#menu-filtro');

    // Mostrar el filtro cuando se haga clic en el icono
    $menuFiltro.on('click', function(e) {
        e.stopPropagation(); // Evita que se propague el evento y cierre el filtro inmediatamente
        $filtro.toggle(); // Alternar entre mostrar y ocultar el filtro
    });

    // Cerrar el filtro si se hace clic fuera de él
    $(document).on('click', function(e) {
        if (!$(e.target).closest('#filtro, #menu-filtro').length) {
            $filtro.hide(); // Ocultar el filtro si el clic no está dentro del filtro ni en el icono
        }
    });
});