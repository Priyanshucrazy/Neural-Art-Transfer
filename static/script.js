document.addEventListener('DOMContentLoaded', (event) => {
    const contentInput = document.getElementById('contentImage');
    const styleInput = document.getElementById('styleImage');
    const contentPreview = document.getElementById('contentPreview');
    const stylePreview = document.getElementById('stylePreview');
    const form = document.getElementById('uploadForm');
    const result = document.getElementById('result');
    const resultImage = document.getElementById('resultImage');

    function previewImage(input, preview) {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    preview.innerHTML = '';
                    preview.appendChild(img);
                }
                reader.readAsDataURL(file);
            }
        });
    }

    previewImage(contentInput, contentPreview);
    previewImage(styleInput, stylePreview);

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('contentImage', contentInput.files[0]);
        formData.append('styleImage', styleInput.files[0]);

        console.log('Sending request to backend...');
        fetch('/stylize', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.blob();
        })
        .then(blob => {
            console.log('Received response from backend');
            const url = URL.createObjectURL(blob);
            resultImage.src = url;
            result.classList.remove('hidden');
        })
        .catch(error => console.error('Error:', error));
    });
});
