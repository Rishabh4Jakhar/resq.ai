function navigateTo(page) {
    window.location.href = page;
}

function fetchHospitals() {
    fetch('/api/hospital/')
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById('hospital-list');
            list.innerHTML = "";  // Clear old data
            // Show all hospitals in the list with complete data
            data.forEach(hospital => {
                let item = document.createElement("li");
                item.textContent = `${hospital.name} - Beds: ${hospital.available_beds} / ${hospital.total_beds} - ICU: ${hospital.icu_beds} - Ventilators: ${hospital.ventilators} - Oxygen: ${hospital.oxygen_supply}`; // Hospital data
                list.appendChild(item);
            });
        })
        .catch(error => console.error('Error fetching hospitals:', error));
}

function fetchShortagePredictions() {
    fetch('/api/ai/shortages/')
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById('shortage-list');
            list.innerHTML = "";
            data.shortages.forEach(item => {
                let listItem = document.createElement("li");
                listItem.textContent = `⚠ Shortage Alert: ${item}`;
                list.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching shortages:', error));
}

function fetchSupplierSuggestions() {
    let resource = document.getElementById("resource-input").value;
    if (!resource) {
        alert("Enter a resource name!");
        return;
    }

    fetch(`/api/ai/suppliers/${resource}/`)
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById('supplier-list');
            list.innerHTML = "";
            data.suggestions.forEach(supplier => {
                let listItem = document.createElement("li");
                listItem.textContent = `${supplier.name} (Score: ${supplier.score}, Cost Efficiency: ${supplier.cost})`;
                list.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching suppliers:', error));
}

function fetchSafetyInstructions() {
    let crisisType = document.getElementById("crisis-input").value;
    if (!crisisType) {
        alert("Enter a crisis type!");
        return;
    }

    fetch(`/api/safety/${crisisType}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("dos").textContent = data.dos;
            document.getElementById("donts").textContent = data.donts;
        })
        .catch(error => console.error('Error fetching safety instructions:', error));
}


function fetchAlerts() {
    fetch('/api/alerts/')
        .then(response => response.json())
        .then(data => {
            data.alerts.forEach(alert => {
                showPopup(alert.message, alert["crisis_event__location"]);
            });
        })
        .catch(error => console.error('Error fetching alerts:', error));
}

function showPopup(message, location) {
    let alertBox = document.createElement("div");
    alertBox.classList.add("alert-popup");
    alertBox.innerHTML = `<strong>Alert:</strong> ${message} <br> 📍 ${location}`;
    
    document.getElementById("alert-container").appendChild(alertBox);

    setTimeout(() => {
        alertBox.remove();
    }, 10000);  // Alert disappears after 10 seconds
}

setInterval(fetchAlerts, 30000); // Fetch alerts every 30 seconds


document.addEventListener("DOMContentLoaded", function () {
    const hospitalForm = document.getElementById("hospital-form");

    hospitalForm.addEventListener("submit", function (event) {
        event.preventDefault();  // ✅ Prevent default form submission

        // ✅ Collect Form Data properly
        const formData = {
            name: document.getElementById("name").value.trim(),
            location: document.getElementById("location").value.trim(),
            location_link: document.getElementById("location_link").value.trim(),
            total_beds: parseInt(document.getElementById("total_beds").value) || 0,
            available_beds: parseInt(document.getElementById("available_beds").value) || 0,
            icu_beds: parseInt(document.getElementById("icu_beds").value) || 0,
            ventilators: parseInt(document.getElementById("ventilators").value) || 0,
            oxygen_supply: parseInt(document.getElementById("oxygen_supply").value) || 0
        };

        console.log("Submitting:", formData);  // ✅ Debug: Check form data before sending

        // ✅ Ensure fields are not empty before submitting
        if (!formData.name || !formData.location) {
            document.getElementById("message").textContent = "❌ Please fill in all required fields!";
            return;
        }

        // ✅ Send Data to Django API (POST Request)
        fetch('/api/hospital/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(JSON.stringify(err)); });
            }
            return response.json();
        })
        .then(data => {
            document.getElementById("message").textContent = "✅ Hospital added successfully!";
            hospitalForm.reset();  // ✅ Clear form fields
            fetchHospitals();  // ✅ Refresh list after adding
        })
        .catch(error => {
            document.getElementById("message").textContent = "❌ Error submitting hospital!";
            console.error("Error:", error);
        });
    });
});

// ✅ Show login/register modal
function openAuthModal(isRegister) {
    document.getElementById("authModal").style.display = "block";
    document.getElementById("authTitle").textContent = isRegister ? "Register" : "Login";
    document.getElementById("is_vendor").checked = false;
    document.getElementById("vendorFields").style.display = "none";
}

// ✅ Close modal
function closeAuthModal() {
    document.getElementById("authModal").style.display = "none";
}

// ✅ Show vendor fields if "Register as Vendor" is checked
function toggleVendor() {
    document.getElementById("vendorFields").style.display = document.getElementById("is_vendor").checked ? "block" : "none";
}

// ✅ Submit login/register form
document.addEventListener("DOMContentLoaded", function () {
    const authForm = document.getElementById("authForm");

    authForm.addEventListener("submit", function (event) {
        event.preventDefault();  // Prevent default form submission

        let formData = {
            name: authForm.name.value,
            password: authForm.password.value,
            age: parseInt(authForm.age.value),
            gender: authForm.gender.value,
            location: authForm.location.value,
            mobile_no: authForm.mobile_no.value,
            is_vendor: document.getElementById("is_vendor").checked,
            organization: document.getElementById("is_vendor").checked ? authForm.organization.value : null
        };

        let url = formData.is_vendor ? "/api/auth/register/" : "/api/auth/login/";

        fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            closeAuthModal();
        })
        .catch(error => console.error("Error:", error));
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const alerts = [
        "Stay Updated! Check the latest reports on disaster response.",
        "New Variant Detected! Follow health guidelines and get vaccinated.",
        "Critical: Oxygen Supply Low in North District.",
        "Emergency Lockdown! Government announces new restrictions.",
        "New Travel Rules: RT-PCR test required for international flights.",
    ];

    const alertList = document.getElementById("alert-list");

    // Populate alert feed dynamically
    alerts.forEach(alert => {
        let listItem = document.createElement("li");
        listItem.textContent = alert;
        alertList.appendChild(listItem);
    });
});