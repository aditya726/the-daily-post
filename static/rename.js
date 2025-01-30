// let button = document.getElementById('bg');
// let file = document.getElementById('fileInput');
// let img;

// file.addEventListener('change', (event) => {
//     img = event.target.files[0];  // Update the image when the user selects a new file
// });

// function addImage() {
//     if (img) {
//         var read = new FileReader();
//         read.onload = function(e) {
//             document.body.style.backgroundImage = 'url(' + e.target.result + ')';
//             document.body.style.backgroundSize = 'cover';
//             document.body.style.backgroundPosition = 'center center';
//             document.body.style.backgroundRepeat = 'no-repeat';
//         }
//         read.readAsDataURL(img);
//     } else {
//         alert('Please upload an image');
//     }
// }

// button.addEventListener('click', (event) => {
//     event.preventDefault(); // Prevent form submission (if it's a submit button)
//     addImage();
// });
