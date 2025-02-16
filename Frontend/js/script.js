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
