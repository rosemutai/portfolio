const menuLinks = document.getElementById('menu-links')
const hamburger = document.getElementById('hamburger')
const lineOne = document.getElementById('line-one')



hamburger.addEventListener('click', () => {
    menuLinks.classList.toggle('active')
    // hamburger.style.backgroundColor == "red"
    lineOne.style.transform.translate()
})