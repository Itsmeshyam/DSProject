document.getElementById('reg-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Gather form data
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        dob: document.getElementById('dob').value,
        street: document.getElementById('street').value,
        city: document.getElementById('city').value,
        state: document.getElementById('state').value,
        postal: document.getElementById('postal').value,
        country: document.getElementById('country').value,
        institution: document.getElementById('institution').value,
        'student-id': document.getElementById('student-id').value,
        message: document.getElementById('message').value
    };

    // Send data to the server
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            // Redirect to the Thank You page
            window.location.href = data.redirect;
        } else {
            // Display the response message
            document.getElementById('responseMessage').textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('responseMessage').textContent = 'An error occurred. Please try again.';
    });
});