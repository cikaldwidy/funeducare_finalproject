document.addEventListener("DOMContentLoaded", function () {
  // Function to show the form for adding or editing a child's profile
  function showAddChildForm() {
    // Show the form popup
    document.getElementById("popup-add-child-form").style.display = "block";
    // Show the overlay
    document.getElementById("popup-overlay").style.display = "block";
  }

  // Function to close the form when clicking outside the popup (overlay)
  function closePopup() {
    // Hide the form popup
    document.getElementById("popup-add-child-form").style.display = "none";
    // Hide the overlay
    document.getElementById("popup-overlay").style.display = "none";
  }

  // Function to cancel the action and close the form
  function cancelAddChild() {
    // Reset the form fields (optional if you want to reset the fields on cancel)
    document.querySelector("#popup-add-child-form form").reset();
    // Hide the form popup and overlay
    closePopup();
  }

  // Adding event listener for opening the form when the Edit button is clicked
  document.querySelectorAll(".btn-warning").forEach(function (button) {
    button.addEventListener("click", showAddChildForm);
  });

  // Adding event listener for closing the popup when clicking the overlay
  document
    .getElementById("popup-overlay")
    .addEventListener("click", closePopup);

  // Adding event listener to Cancel button inside the popup
  document
    .querySelector('#popup-add-child-form button[type="button"]')
    .addEventListener("click", cancelAddChild);
});
