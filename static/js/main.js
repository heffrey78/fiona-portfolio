/**
* Template Name: Laura
* Updated: Mar 10 2023 with Bootstrap v5.2.3
* Template URL: https://bootstrapmade.com/laura-free-creative-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
document.addEventListener('DOMContentLoaded', function() {
  "use strict";

  console.log("DOM fully loaded");

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    console.log(`Attempting to add ${type} event listener to ${el}`);
    let selectEl = select(el, all)
    if (selectEl) {
      console.log(`Element found: `, selectEl);
      if (all) {
        selectEl.forEach(e => {
          try {
            e.addEventListener(type, listener)
          } catch (error) {
            console.error(`Error adding event listener to element:`, e, error);
          }
        })
      } else {
        try {
          selectEl.addEventListener(type, listener)
        } catch (error) {
          console.error(`Error adding event listener to element:`, selectEl, error);
        }
      }
      console.log(`Event listener added successfully`);
    } else {
      console.log(`Element not found: ${el}`);
    }
  }

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    console.log(`Scrolling to element: ${el}`);
    let header = select('#header')
    let offset = header ? header.offsetHeight : 0

    let elementPos = select(el).offsetTop
    if ('scrollBehavior' in document.documentElement.style) {
      window.scrollTo({
        top: elementPos - offset,
        behavior: 'smooth'
      })
    } else {
      window.scrollTo(0, elementPos - offset)
    }
  }

  /**
   * Handle down button behavior
   */
  const handleDownButton = () => {
    console.log("Handling down button");
    const currentPage = window.location.pathname.split('/').pop();
    if (currentPage === '' || currentPage === 'home.html' || currentPage === 'index.html') {
      const downButton = select('#hero .btn-scroll.scrollto');
      if (downButton) {
        downButton.addEventListener('click', function(e) {
          console.log("Down button clicked");
          e.preventDefault();
          const homeSection = select('#home');
          if (homeSection) {
            console.log("Scrolling to home section");
            scrollto('#home');
          } else {
            console.log("Home section not found");
          }
        });
        console.log("Down button event listener added successfully");
      } else {
        console.log("Down button not found");
      }
    } else {
      console.log("Not on home page, skipping down button setup");
    }
  }

  /**
   * Scroll with offset on links with a class name .scrollto
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

  // Call the handleDownButton function after the DOM is fully loaded
  handleDownButton();

  // Manual check for down arrow functionality
  console.log("Checking down arrow functionality");
  const downArrow = select('#hero .btn-scroll.scrollto');
  if (downArrow) {
    console.log("Down arrow found:", downArrow);
    console.log("Down arrow click event:", downArrow.onclick);
    // Add a click event listener to log when the down arrow is clicked
    downArrow.addEventListener('click', function() {
      console.log("Down arrow clicked");
    });
  } else {
    console.log("Down arrow not found");
  }
});