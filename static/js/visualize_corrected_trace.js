var mymap = L.map('map').setView([51.505, -0.09], 13);

//setting tiles 
var base_layer = L.tileLayer('https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png', {
    maxZoom: 20,
	attribution: '<a href="https://github.com/cyclosm/cyclosm-cartocss-style/releases" title="CyclOSM - Open Bicycle render">CyclOSM</a> | Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

var traceStyleLayer = L.geoJson(null, {
     // http://leafletjs.com/reference.html#geojson-style
     style: function(feature) {
        return { color: '#3388ff' };
    }
});

var originalStyleLayer = L.geoJson(null, {
    // http://leafletjs.com/reference.html#geojson-style
    style: function(feature) {
       return { color: '#f5ab00' };
   }
});

var baseMaps = {
    "CyclOSM": base_layer
};

function visualize_corrected_trace(correctedTrace, original_trace) {
    $('#downloadCorrectedTrace').on('click', function(){
        var blob = new Blob([correctedTrace], {type: "text/plain;charset=utf-8"});
        saveAs(blob, "correctedTrace.gpx");
    });


    var traceLayer = omnivore.gpx.parse(correctedTrace, null, traceStyleLayer);
    traceLayer.addTo(mymap)
    var originalTraceLayer = omnivore.gpx.parse(original_trace, null, originalStyleLayer);

    var overlayMaps = {
        "Original Trace": originalTraceLayer,
        "Corrected Trace": traceLayer
    };

    var layerControl = L.control.layers(null, overlayMaps).addTo(mymap);

    mymap.fitBounds(traceLayer.getBounds());
}