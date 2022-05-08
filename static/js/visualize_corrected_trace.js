var mymap = L.map('map').setView([51.505, -0.09], 13);

//setting tiles 
L.tileLayer('https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png', {
    maxZoom: 20,
	attribution: '<a href="https://github.com/cyclosm/cyclosm-cartocss-style/releases" title="CyclOSM - Open Bicycle render">CyclOSM</a> | Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);


function visualize_corrected_trace(correctedTrace) {
    //omnivore.gpx.parse(correctedTrace).addTo(mymap);
    console.log(correctedTrace);
}

$('#downloadCorrectedTrace').on('click', function(){
    var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
    saveAs(blob, "hello world.txt");
});