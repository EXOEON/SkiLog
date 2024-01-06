function toggleDropdown() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
}

// Use JavaScript to update checkboxes status on click
document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('click', function() {
            const checkboxId = this.id;
            const isChecked = this.checked;

            // Send an AJAX request to the server to update checkbox status
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/update_checkbox', true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log(xhr.responseText);
                }
            };
            xhr.send(JSON.stringify({ id: checkboxId, checked: isChecked }));
        });
    });

    // Fetch initial checkbox statuses from the server
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_checkbox_states', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const checkboxStates = JSON.parse(xhr.responseText);

            checkboxes.forEach(checkbox => {
                const checkboxId = checkbox.id;
                if (checkboxStates[checkboxId]) {
                    checkbox.checked = true;
                }
            });
        }
    };
    xhr.send();
});