// Get current path
$( ".navbar .nav-link" ).each( function() {
    if (this.pathname == window.location.pathname) {
        $( this ).addClass( "active" );
    } else {
        $( this ).removeClass( "active" );
    }
    
});