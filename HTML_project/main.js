const togglePasswordVisibility=(inputElement,toggleElement) => {
    if (inputElement.type==="password") {
        inputElement.type= "text";
        toggleElement.innerHTML='<i class="far fa-eye"></i>';
    
    } else {
        inputElement.type="password";
        toggleElement.innerHTML='<i class="far fa-eye-slash"></i>'
    }
}
const togglePassword=document.getElementById("togglePassword")
const togglePasswordConfirm=document.getElementById("togglePasswordConfirm")
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm_password");

togglePassword.addEventListener("click",() => {
    togglePasswordVisibility(password,togglePassword)
})
togglePasswordConfirm.addEventListener("click",() => {
    togglePasswordVisibility(confirmPassword,togglePasswordConfirm)
})


function validateForm() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;
    var email = document.getElementById("email").value;
    var birthdate = document.getElementById("birthdate").value;
    var gender = document.getElementById("gender").value;
    var agreeTerms = document.getElementById("agree_terms").checked;

    // Validate password length
    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return false;
    }

    // Validate password and confirm password match
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    // Validate email format
    if (!isValidEmail(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Validate birthdate format
    if (!isValidDate(birthdate)) {
        alert("Please enter a valid birthdate between 1/1/1900 and 31/12/2006.");
        return false;
    }

    // Validate gender selection
    if (gender === "") {
        alert("Please select a gender.");
        return false;
    }

    // Validate agreement to terms
    if (!agreeTerms) {
        alert("Please agree to the terms.");
        return false;
    }
    alert("Registration successful!");
    return true;
}

function isValidEmail(email) {
    // Simple email validation regex
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidDate(dateString) {
    // Simple date validation
    var dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(dateString)) {
        return false; // Date format is invalid
    }
    // Parse the date string to a Date object
    var dateParts = dateString.split("-");
    var year = parseInt(dateParts[0]);
    var month = parseInt(dateParts[1]);
    var day = parseInt(dateParts[2]);

    // Get the current year
    var currentYear = (new Date()).getFullYear();

    // Check if the year is not bigger than the current year
    if (year > currentYear ) {
        return false; // Birthdate year is in the future
    }
    if (year < 1900 ) {
        return false; 
    }

    // Create a Date object representing the birthdate
    var birthDate = new Date(year, month - 1, day); // month is 0-based in Date constructor

    // Calculate the minimum birthdate required (18 years ago from today)
    var eighteenYearsAgo = new Date();
    eighteenYearsAgo.setFullYear(eighteenYearsAgo.getFullYear() - 18);

    // Compare birthdate with the minimum birthdate required
    return birthDate <= eighteenYearsAgo;
    }