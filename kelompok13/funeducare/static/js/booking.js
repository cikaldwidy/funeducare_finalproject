$(document).ready(function () {
  // Disable submit button initially
  $("#bookingButton").prop("disabled", true);

  // Listen for checkbox changes to enable/disable submit button
  $("#termsCheckbox").change(function () {
    checkFormValidity(); // Check form validity whenever checkbox state changes
  });

  // Listen for changes in form fields (child name, program, and fee)
  $("#child-select, #program-select, #fee-select").change(function () {
    checkFormValidity(); // Check form validity whenever any form field changes
  });

  // Function to check form validity
  function checkFormValidity() {
    var namaAnak = $("#child-select").val(); // Child name
    var program = $("#program-select").val(); // Program
    var fee = $("#fee-select").val(); // Fee
    var termsChecked = $("#termsCheckbox").is(":checked"); // Terms checkbox

    // Enable button if all fields are filled and terms are checked
    if (namaAnak && program && fee && termsChecked) {
      $("#bookingButton").prop("disabled", false); // Enable submit button
    } else {
      $("#bookingButton").prop("disabled", true); // Disable submit button
    }
  }

  // Handle the cancel button click event
  $("#cancelButton").on("click", function () {
    window.location.href = "{% url 'programs:programs' %}"; // Navigate to programs page
  });

  // Custom form validation on submit
  $("#bookingForm").on("submit", function (e) {
    var namaAnak = $("#child-select").val();
    var program = $("#program-select").val();
    var fee = $("#fee-select").val();
    var termsChecked = $("#termsCheckbox").is(":checked");

    // If not all fields are filled or terms not accepted, prevent form submission 
    if (!namaAnak || !program || !fee || !termsChecked) {
      e.preventDefault();
      alert("Silakan lengkapi semua field dan centang persetujuan.");
    }
  });
});
