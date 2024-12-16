document
  .getElementById("toggle-password")
  .addEventListener("click", function () {
    var passwordField = document.getElementById("id_password1");
    var icon = document.getElementById("toggle-password");

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
  if (alertModal) {
    const bootstrapModal = new bootstrap.Modal(alertModal);
    bootstrapModal.show();
  }
});
