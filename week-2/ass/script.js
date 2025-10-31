$(document).ready(function () {
    $('#lang').select2({
        placeholder: 'Select the languages known',
        allowClear: true,
        width: '100%'
    });

    const pic = document.getElementById('pic');
    const form = document.getElementById('userForm');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        let valid = true;

        const name = document.getElementById('name').value.trim();
        const dob = document.getElementById('dob').value;
        const mobile = document.getElementById('mobile').value.trim();
        const email = document.getElementById('email').value.trim();
        const gender = document.querySelector('input[name="gender"]:checked');
        const languages = $('#lang').val();
        const file = pic.value;

        document.querySelector('.error_name').innerText = '';
        document.querySelector('.error_dob').innerText = '';
        document.querySelector('.error_mob').innerText = '';
        document.querySelector('.error_email').innerText = '';
        document.querySelector('.error_gender').innerText = '';
        document.querySelector('.error_lang').innerText = '';
        document.querySelector('.error_pic').innerText = '';

        if (name === '') {
            document.querySelector('.error_name').innerText = 'Name is required';
            valid = false;
        }

        if (dob === '') {
            document.querySelector('.error_dob').innerText = 'Select date of birth';
            valid = false;
        }

        if (mobile === '' || !/^[0-9]{10}$/.test(mobile)) {
            document.querySelector('.error_mob').innerText = 'Enter valid 10-digit mobile number';
            valid = false;
        }

        if (email === '' || !email.includes('@') || !email.includes('.')) {
            document.querySelector('.error_email').innerText = 'Enter valid email address';
            valid = false;
        }

        if (!gender) {
            document.querySelector('.error_gender').innerText = 'Select your gender';
            valid = false;
        }

        if (!languages || languages.length === 0) {
            document.querySelector('.error_lang').innerText = 'Select at least one language';
            valid = false;
        }

        if (file === '') {
            document.querySelector('.error_pic').innerText = 'Upload a profile picture';
            valid = false;
        }

        if (valid) {
            const langBadges = languages.map(lang => `<span class="badge bg-info text-dark me-1">${lang}</span>`).join('');

            const modalContent = `
                <div class="text-center mb-3">
                    <img src="${URL.createObjectURL(pic.files[0])}" class="rounded-circle" width="100" height="100">
                    <p class="m-0"><strong>Name:</strong> ${name}</p>
                    <p class="m-0"><strong>Languages:</strong> ${langBadges}</p>
                </div>
                <hr>
                <h5><strong>BIO :</strong></h5>
                <br>
                <div class="d-flex justify-content-between">
                    <div class="text-start p-0 d-flex flex-column">
                        <p class="m-0"><strong>DOB:</strong></p>
                        <p class="m-0"><strong>Mobile:</strong></p>
                        <p class="m-0"><strong>Email:</strong></p>
                        <p class="m-0"><strong>Gender:</strong></p>
                    </div>
                    <div class="text-end p-0 d-flex flex-column">
                        <p class="m-0">${dob}</p>
                        <p class="m-0">${mobile}</p>
                        <p class="m-0">${email}</p>
                        <p class="m-0">${gender.value}</p>
                    </div>
                </div>
        
            `;

            document.getElementById('show').innerHTML = modalContent;
            const modal = new bootstrap.Modal(document.getElementById('model'));
            modal.show();
        }
    });
});
