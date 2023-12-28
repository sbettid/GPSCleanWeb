// Set form 
var $form = $('.box');

// stop propagation
$('.box__file').on('click', function(e) {
    e.stopPropagation();
});

// attach click event on the whole area to triggere upload file dialog
$form.on('click', function(e) {
    $('.box__file').trigger('click');
});
var fileInput = $('.box #file');

function submit_form() {
    $form.submit();
}



var droppedFiles = null;
// prevent default behaviour on drag and drop events
$form.on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
    e.preventDefault();
    e.stopPropagation();
})
.on('dragover dragenter', function() {
    $form.addClass('is-dragover'); //on drag over add custom CSS class
})
.on('dragleave dragend drop', function() {
    $form.removeClass('is-dragover'); //and remove it when leaving the area
})
.on('drop', function(e) { //on drop...

    console.log("Pippo")

    //Get files list
    droppedFiles = e.originalEvent.dataTransfer.files;

    console.log(JSON.stringify(droppedFiles))
    
    //Dropped file lis length
    const droppedFilesLength = droppedFiles.length;
    
    if(droppedFilesLength > 1) {
        alert("The tool can correct only one trace at the time, while " + droppedFilesLength + " files were uploaded, please retry just with one.");
        return;
    }

    const trace = droppedFiles[0];
    const extension = trace['name'].slice(trace['name'].lastIndexOf('.') + 1);
    
    if(extension.toLowerCase() != "gpx") {
        alert("Only .gpx file can be corrected, while a ." + extension + " file was uploaded");
        return;
    }

    fileInput.files = droppedFiles;

    console.log(trace['name']);

    $form.submit();
});
