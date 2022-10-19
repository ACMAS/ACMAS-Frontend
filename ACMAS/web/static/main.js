const confirmBttn = document.getElementById('confirm-button')
const alertBox = document.getElementById('alert-box')
const imageForm = document.getElementById('image-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
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
    console.log("clicked")
    cropper.getCroppedCanvas().toBlob((blob) => {
        console.log('confirmed')
        const formData = new FormData();
      // Pass the image file name as the third parameter if necessary
        formData.append('csrfmiddlewaretoken', csrf[0].value)
        formData.append('file', blob, 'my-image.png');



        $.ajax('/crop-Img/',{
            method: 'POST',
            enctype: 'multipart/form-data',
            data: formData,
            success() {
                console.log('Upload success');
            },
            error() {
                console.log('Upload error');
            },
            cache: false,
            processData: false,
            contentType: false,
        });
    }/*, 'image/png' */);
})

