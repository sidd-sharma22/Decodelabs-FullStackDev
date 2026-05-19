// Hamburger menu toggle
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener('click', function () {
  const isOpen = nav.classList.toggle('open');
  this.classList.toggle('active');
  this.setAttribute('aria-expanded', isOpen);
});

// Close menu when clicking a link
document.querySelectorAll('.nav-links a').forEach(function (link) {
  link.addEventListener('click', function () {
    nav.classList.remove('open');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
  });
});

// Close menu on outside click
document.addEventListener('click', function (e) {
  if (!hamburger.contains(e.target) && !nav.contains(e.target)) {
    nav.classList.remove('open');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
  }
});
