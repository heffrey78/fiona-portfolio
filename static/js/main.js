/**
* Template Name: Laura
* Updated: Mar 10 2023 with Bootstrap v5.2.3
* Template URL: https://bootstrapmade.com/laura-free-creative-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
document.addEventListener('DOMContentLoaded', function() {
  "use strict";

  // ... (keep all existing code)

  /**
   * Handle down button behavior
   */
  const downButton = document.querySelector('.btn-scroll');
  if (downButton) {
    downButton.addEventListener('click', function(e) {
      e.preventDefault();
      const currentPage = window.location.pathname.split('/').pop();
      if (currentPage === '' || currentPage === 'home.html') {
        // On home page, scroll to the about section
        const aboutSection = document.querySelector('about.html');
        if (aboutSection) {
          aboutSection.scrollIntoView({ behavior: 'smooth' });
        }
      } else {
        // On other pages, scroll to reveal the full content
        const mainContent = document.querySelector('main');
        if (mainContent) {
          mainContent.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }



    /**
   * Scrool with ofset on links with a class name .scrollto
   */
    on('click', '.scrollto', function(e) {
      if (select(this.hash)) {
        e.preventDefault()
  
        let navbar = select('#navbar')
        if (navbar.classList.contains('navbar-mobile')) {
          navbar.classList.remove('navbar-mobile')
          let navbarToggle = select('.mobile-nav-toggle')
          navbarToggle.classList.toggle('bi-list')
          navbarToggle.classList.toggle('bi-x')
        }
        scrollto(this.hash)
      }
    }, true)

});