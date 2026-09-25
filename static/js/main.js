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

const skillsSwiper = new Swiper(".skills-swiper", {
    slidesPerView: 2,
    spaceBetween: 12,

    breakpoints: {
        640: {
            slidesPerView: 3,
            spaceBetween: 16,
        },

        768: {
            slidesPerView: 4,
            spaceBetween: 16,
        },

        1024: {
            slidesPerView: 6,
            spaceBetween: 16,
        },

        1280: {
            slidesPerView: 8,
            spaceBetween: 16,
        },
    },

    grabCursor: true,

    direction: "horizontal",

    observer: true,
    observeParents: true,
});


document.addEventListener("DOMContentLoaded", () => {

    const counters = document.querySelectorAll(".counter");

    const observer = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach((entry) => {

                if (!entry.isIntersecting) {
                    return;
                }

                const counter = entry.target;

                const target = Number(
                    counter.dataset.target
                );

                const suffix =
                    counter.dataset.suffix || "";

                let current = 0;

                const duration = 1200;
                const startTime = performance.now();

                function updateCounter(currentTime) {

                    const elapsed =
                        currentTime - startTime;

                    const progress =
                        Math.min(elapsed / duration, 1);

                    // easeOut
                    const eased =
                        1 - Math.pow(1 - progress, 3);

                    current =
                        Math.floor(target * eased);

                    counter.textContent =
                        current + suffix;

                    if (progress < 1) {

                        requestAnimationFrame(
                            updateCounter
                        );

                    } else {

                        counter.textContent =
                            target + suffix;
                    }
                }

                requestAnimationFrame(
                    updateCounter
                );

                observer.unobserve(counter);
            });
        },
        {
            threshold: 0.4
        }
    );


    counters.forEach((counter) => {
        observer.observe(counter);
    });

});
