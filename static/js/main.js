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

    navigation: {
        nextEl: "#skills-next",
        prevEl: "#skills-prev",
    },
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

document.addEventListener("DOMContentLoaded", () => {
    const revealElements = document.querySelectorAll(
        ".reveal, .reveal-card, .skill-reveal, .timeline-item, .skill-progress"
    );

    if (!revealElements.length) {
        return;
    }

    const observer = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("is-visible");

                observer.unobserve(entry.target);
            });
        },
        {
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px",
        }
    );

    revealElements.forEach((element) => {
        observer.observe(element);
    });
});

function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');

        for (let cookie of cookies) {
            cookie = cookie.trim();

            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );

                break;
            }
        }
    }

    return cookieValue;
}

document.addEventListener('click', (event) => {
    const gallery = event.target.closest('.galleries');

    if (!gallery) return;

    const image_id = gallery.dataset.imgId;

    async function changeImgGallery(image_id) {
        const mainImg = document.getElementById('img-id');
        const csrfToken = getCookie('csrftoken');
        const response = await fetch('/change-img/' + image_id, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrfToken,
            },
        });

        const result = await response.json();

        mainImg.src = result.src;
    }

    changeImgGallery(image_id);
});


const orderForm = document.getElementById('order-form');

if (orderForm) {

    const submitBtn = document.getElementById('submit-btn');
    const submitContent = document.getElementById('submit-content');
    const submitLoading = document.getElementById('submit-loading');
    const successMessage = document.getElementById('success-message');
    orderForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        // نمایش Loading
        submitBtn.disabled = true;
        submitContent.classList.add('hidden');
        submitLoading.classList.remove('hidden');
        submitLoading.classList.add('flex');

        // مخفی کردن پیام موفقیت قبلی
        successMessage.classList.add('hidden');

        const formData = new FormData(orderForm);

        try {
            const response = await fetch(
                orderForm.action,
                {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                }
            );
            const data = await response.json();
            if (response.ok && data.success) {
                successMessage.textContent = data.message;
                successMessage.classList.remove('hidden');

                orderForm.reset();

                // مخفی کردن پیام بعد از 5 ثانیه
                setTimeout(() => {
                    successMessage.classList.add('hidden');
                }, 5000);
            } else {
                console.log(data.errors);
            }
        } catch (error) {
            console.error(error);
        } finally {
            // خاموش کردن Loading
            submitBtn.disabled = false;
            submitContent.classList.remove('hidden');
            submitLoading.classList.add('hidden');
            submitLoading.classList.remove('flex');
        }

    });

}

const contactForm = document.getElementById('contact-form');

if (contactForm) {

    const submitBtn = document.getElementById('contact-submit-btn');
    const submitContent = document.getElementById('contact-submit-content');
    const submitLoading = document.getElementById('contact-submit-loading');
    const successMessage = document.getElementById('contact-success-message');

    contactForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        // نمایش loading
        submitBtn.disabled = true;

        submitContent.classList.add('hidden');

        submitLoading.classList.remove('hidden');
        submitLoading.classList.add('flex');

        successMessage.classList.add('hidden');

        const formData = new FormData(contactForm);

        try {

            const response = await fetch(
                contactForm.action,
                {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                }
            );

            const data = await response.json();

            if (response.ok && data.success) {

                // نمایش پیام موفقیت
                successMessage.textContent = data.message;
                successMessage.classList.remove('hidden');

                // پاک کردن فرم
                contactForm.reset();

                // مخفی کردن پیام بعد از 5 ثانیه
                setTimeout(() => {
                    successMessage.classList.add('hidden');
                }, 5000);

            } else {

                console.log(data.errors);

            }

        } catch (error) {

            console.error('Contact form error:', error);

        } finally {

            // برگشت دکمه به حالت عادی
            submitBtn.disabled = false;

            submitContent.classList.remove('hidden');

            submitLoading.classList.add('hidden');
            submitLoading.classList.remove('flex');
        }
    });
}

