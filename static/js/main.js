document.addEventListener('DOMContentLoaded', function() {
    // Image preview for file upload
    // const fileInput = document.getElementById('file');
    // const preview = document.getElementById('preview');

    // if (fileInput && preview) {
    //     fileInput.addEventListener('change', function(e) {
    //         const file = e.target.files[0];
    //         if (file) {
    //             const reader = new FileReader();
    //             reader.onload = function(e) {
    //                 preview.src = e.target.result;
    //                 preview.classList.remove('d-none');
    //             }
    //             reader.readAsDataURL(file);
    //         }
    //     });
    // }

    // Automatic dismissal of flash messages
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.classList.remove('show');
            setTimeout(function() {
                message.remove();
            }, 150);
        }, 5000);
    });
});