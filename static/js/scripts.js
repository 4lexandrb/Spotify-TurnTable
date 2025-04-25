document.addEventListener('DOMContentLoaded', function() {
    const images = [];

    fetch('/images')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            data.forEach(image => {
                images.push(`/static/images/${image}`);
            });
        })
        .catch(error => console.error('Error fetching images:', error.message));

    let currentIndex = 0;


    function changeBackground() {
        if (images.length === 0) {
            console.error('No images available to set as background.');
            return;
        }
        document.body.style.backgroundImage = `url('${images[currentIndex]}')`;
        currentIndex = (currentIndex + 1) % images.length;
    }

    document.getElementById('change-image-button').addEventListener('click', changeBackground);

    changeBackground();
});