// Add loading state to forms
document.addEventListener('DOMContentLoaded', function() {
    // Form submission loading
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.classList.contains('loading')) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
            }
        });
    });

    // Image lazy loading
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.add('loaded');
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'fadeOut 0.5s';
            setTimeout(() => message.remove(), 500);
        }, 5000);
    });
});

// Toast notification function
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
        <span class="toast-icon">
            ${type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️'}
        </span>
        <span class="toast-message">${message}</span>
    `;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'slideOutRight 0.4s ease-out';
        setTimeout(() => toast.remove(), 400);
    }, 3000);
}

@keyframes fadeOut {
    to {
        opacity: 0;
        transform: translateY(-10px);
    }
}

@keyframes slideOutRight {
    to {
        transform: translateX(400px);
        opacity: 0;
    }
}