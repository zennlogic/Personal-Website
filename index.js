const hamburgerMenu = document.querySelector('#hambuger');
const navLinks = document.querySelector('.nav-links');


hamburgerMenu.addEventListener('click', () => {
    navLinks.classList.toggle('open');

})
