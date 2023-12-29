var navbar_open = false

// Get current path
$( ".navbar .nav-link" ).each( function() {
    if (this.pathname == window.location.pathname) {
        $( this ).addClass( "active" );
    } else {
        $( this ).removeClass( "active" );
    }
});

// This is to fix an issue in pushing down the content for the mobile menu when there is scrollable content
function toggleNav() {
    console.log("Doing stuff: " + navbar_open)
    if (!navbar_open) {
        $(".mycontainer").css("margin-top", "100px");
        navbar_open = true;
    } else {
        $(".mycontainer").css("margin-top", "60px");
        navbar_open = false;
    }
}