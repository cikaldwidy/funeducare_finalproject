// Ambil elemen modal dan tombol edit
const editButton = document.getElementById("editButton");
const editModal = document.getElementById("editModal");
const closeModal = document.querySelector(".close");

// Fungsi untuk menampilkan modal
editButton.addEventListener("click", function () {
  editModal.style.display = "block"; // Menampilkan modal
});

// Fungsi untuk menutup modal saat klik tombol close
closeModal.addEventListener("click", function () {
  editModal.style.display = "none"; // Menyembunyikan modal
});

// Menutup modal jika area di luar modal diklik
window.addEventListener("click", function (event) {
  if (event.target === editModal) {
    editModal.style.display = "none"; // Menyembunyikan modal jika area luar diklik
  }
});
