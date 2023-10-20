const confirmBttn = document.getElementById('confirm-button')
const alertBox = document.getElementById('alert-box')

var $image = $('#image')
$image.cropper({
    aspectRatio: 16 / 9,
    crop: function(event) {
        console.log(event.detail.x);
        console.log(event.detail.y);
        console.log(event.detail.width);
        console.log(event.detail.height);
        console.log(event.detail.rotate);
        console.log(event.detail.scaleX);
        console.log(event.detail.scaleY);
    }
});
var cropper = $image.data('cropper');

confirmBttn.addEventListener('click',()=>{
    cropper.getCroppedCanvas().toBlob((blob) => {
        const formData = new FormData();
      // Pass the image file name as the third parameter if necessary
        formData.append('file', blob, 'my-image.png');
        
        $.ajax('/crop-Img/',{
            method: 'POST',
            enctype: 'multipart/form-data',
            data: formData,
            success: function(response){
                console.log('success', response)
                alertBox.classList.remove("hide");
                alertBox.classList.add("show");
                setTimeout(function(){
                    alertBox.classList.remove("show");
                    alertBox.classList.add("hide")
                },1000);

            },
            error: function(error){
                console.log('error', error)

            },
            cache: false,
            processData: false,
            contentType: false,
        });
    }/*, 'image/png' */);
})

