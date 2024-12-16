document
  .getElementById("toggle-password1")
  .addEventListener("click", function () {
    var passwordField = document.getElementById("id_password1");
    var icon = document.getElementById("toggle-password1");

    if (passwordField.type === "password") {
      passwordField.type = "text";
      icon.classList.remove("bi-eye-slash");
      icon.classList.add("bi-eye");
    } else {
      passwordField.type = "password";
      icon.classList.remove("bi-eye");
      icon.classList.add("bi-eye-slash");
    }
  });

document
  .getElementById("toggle-password2")
  .addEventListener("click", function () {
    var passwordField = document.getElementById("id_password2");
    var icon = document.getElementById("toggle-password2");

    if (passwordField.type === "password") {
      passwordField.type = "text";
      icon.classList.remove("bi-eye-slash");
      icon.classList.add("bi-eye");
    } else {
      passwordField.type = "password";
      icon.classList.remove("bi-eye");
      icon.classList.add("bi-eye-slash");
    }
  });
document.addEventListener("DOMContentLoaded", function () {
  const alertModal = document.getElementById("alertModal");

  // If there's any message in the modal, show it
  if (alertModal && alertModal.classList.contains("fade")) {
    const bootstrapModal = new bootstrap.Modal(alertModal);
    bootstrapModal.show();
  }
});
