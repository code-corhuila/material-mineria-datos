document.addEventListener('DOMContentLoaded', function() {
    setupScrollButton();
    setupNavigation();
    setupSmoothScroll();
    highlightActiveSection();
});

// Scroll to Top Button
function setupScrollButton() {
    const scrollBtn = document.getElementById('scrollTopBtn');

    window.addEventListener('scroll', function() {
        if (document.documentElement.scrollTop > 300 || document.body.scrollTop > 300) {
            scrollBtn.style.display = 'block';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    scrollBtn.addEventListener('click', function() {
        document.documentElement.scrollTop = 0;
        document.body.scrollTop = 0;
    });
}

// Smooth Scroll
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Active Navigation Highlight
function setupNavigation() {
    const navLinks = document.querySelectorAll('.main-nav a');

    window.addEventListener('scroll', highlightActiveSection);
}

function highlightActiveSection() {
    const navLinks = document.querySelectorAll('.main-nav a');
    let current = '';

    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}

// Copy Code to Clipboard (Bonus)
document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button');
    button.textContent = '📋 Copiar';
    button.style.cssText = `
        position: absolute;
        right: 10px;
        top: 10px;
        padding: 8px 12px;
        background-color: #27ae60;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 12px;
        opacity: 0;
        transition: opacity 0.3s;
    `;

    pre.style.position = 'relative';
    pre.appendChild(button);

    pre.addEventListener('mouseenter', () => {
        button.style.opacity = '1';
    });

    pre.addEventListener('mouseleave', () => {
        button.style.opacity = '0';
    });

    button.addEventListener('click', () => {
        const code = pre.innerText;
        navigator.clipboard.writeText(code).then(() => {
            const originalText = button.textContent;
            button.textContent = '✅ Copiado!';
            setTimeout(() => {
                button.textContent = originalText;
            }, 2000);
        });
    });
});

// Lazy Load Images (Si los usas)
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Analytics (Opcional)
function trackSection(sectionId) {
    console.log(`Usuario visitó: ${sectionId}`);
    // Aquí puedes enviar a Google Analytics o tu sistema de tracking
}

window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            trackSection(section.id);
        }
    });
});