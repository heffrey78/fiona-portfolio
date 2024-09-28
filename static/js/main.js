document.addEventListener('DOMContentLoaded', function() {
    console.log('Main JavaScript file loaded');

    // Add a simple animation to the main heading
    const mainHeading = document.querySelector('h1');
    if (mainHeading) {
        mainHeading.style.opacity = '0';
        mainHeading.style.transition = 'opacity 1s ease-in-out';
        setTimeout(() => {
            mainHeading.style.opacity = '1';
        }, 500);
    }

    // Add a click event to the CTA buttons
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const href = this.getAttribute('href');
            console.log(`Navigating to: ${href}`);
            // Add a small delay before navigation for visual feedback
            setTimeout(() => {
                window.location.href = href;
            }, 200);
        });
    });
});