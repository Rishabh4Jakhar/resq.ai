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
        event.preventDefault();  // Prevent default form submission

        // ✅ Collect Form Data
        const formData = {
            name: hospitalForm.name.value,
            location: hospitalForm.location.value,
            location_link: hospitalForm.location_link.value,
            total_beds: parseInt(hospitalForm.total_beds.value),
            available_beds: parseInt(hospitalForm.available_beds.value),
            icu_beds: parseInt(hospitalForm.icu_beds.value),
            ventilators: parseInt(hospitalForm.ventilators.value),
            oxygen_supply: parseInt(hospitalForm.oxygen_supply.value)
        };

        // ✅ Send Data to Django API (POST Request)
        fetch('/api/hospital/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("message").textContent = "Hospital added successfully!";
            hospitalForm.reset();  // Clear form fields
        })
        .catch(error => {
            document.getElementById("message").textContent = "Error submitting hospital!";
            console.error("Error:", error);
        });
    });
});
