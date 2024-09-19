
document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.opacity = i === index ? '1' : '0';
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    // Set interval for 8 seconds (8000 milliseconds) for a slow transition
    setInterval(nextSlide, 8000);

    // Show initial slide
    showSlide(currentIndex);
});
function changeColor(color) {
    // Example function to change the button color
    const buttons = document.querySelectorAll('.nav-buttons button');
    buttons.forEach(button => {
        button.style.backgroundColor = color;
    });
}
