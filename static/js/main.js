const footerMenuButtons = document.querySelectorAll(".footer-menu-toggle");

footerMenuButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const menu = button.nextElementSibling;
        const arrow = button.querySelector(".footer-arrow");

        menu.classList.toggle("hidden");
        arrow.classList.toggle("rotate-180");

    });

});

const mobileMenuButton = document.querySelector("#mobile-menu-button");
const mobileMenu = document.querySelector("#mobile-menu");
const mobileMenuClose = document.querySelector("#mobile-menu-close");
const mobileMenuOverlay = document.querySelector("#mobile-menu-overlay");
const menuIcon = document.querySelector("#menu-icon");


function openMobileMenu() {

    mobileMenu.classList.remove("translate-x-full");
    mobileMenuOverlay.classList.remove("hidden");

    mobileMenuButton.setAttribute("aria-expanded", "true");

    menuIcon.innerHTML = `
        <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6 6l12 12M6 18L18 6"
        />
    `;
}


function closeMobileMenu() {

    mobileMenu.classList.add("translate-x-full");
    mobileMenuOverlay.classList.add("hidden");

    mobileMenuButton.setAttribute("aria-expanded", "false");

    menuIcon.innerHTML = `
        <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M4 6h16M4 12h16M4 18h16"
        />
    `;
}


if (mobileMenuButton) {
    mobileMenuButton.addEventListener("click", openMobileMenu);
}

if (mobileMenuClose) {
    mobileMenuClose.addEventListener("click", closeMobileMenu);
}

if (mobileMenuOverlay) {
    mobileMenuOverlay.addEventListener("click", closeMobileMenu);
}