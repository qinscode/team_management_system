// Add any custom JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    // Example: Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this member?')) {
                e.preventDefault();
            }
        });
    });
}); 