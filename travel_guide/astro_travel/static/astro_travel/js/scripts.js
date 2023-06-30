document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.getElementById('user-input-form');
    const astroSunInput = document.getElementById('astro-sun');
    const astroMoonInput = document.getElementById('astro-moon');
    const countryInput = document.getElementById('country');
    const itineraryDiv = document.getElementById('itinerary');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        submitForm();
    });

    function submitForm() {
        const astroSun = astroSunInput.value;
        const astroMoon = astroMoonInput.value;
        const country = countryInput.value;

        fetch('/get_itinerary/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                'astro_sun': astroSun,
                'astro_moon': astroMoon,
                'country': country
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.form_valid) {
                itineraryDiv.innerHTML = data.itinerary;
            } else {
                alert('Invalid input. Please try again.');
            }
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});