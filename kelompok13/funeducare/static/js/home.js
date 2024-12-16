// scroll explore
$(document).ready(function () {
  $("#scrollButton").on("click", function (event) {
    event.preventDefault();
    $("html, body").animate(
      {
        scrollTop: $("#marqueForm").offset().top,
      },
      1500
    );
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelectorAll(".readMoreBtn");

  btn.forEach(function (button) {
    button.addEventListener("click", function () {
      const index = button.dataset.index;
      const shortText = document.getElementById(`short-text-${index}`);
      const fullText = document.getElementById(`full-text-${index}`);

      if (fullText.style.display === "none") {
        fullText.style.display = "inline";
        shortText.style.display = "none";
        button.innerText = "Sembunyikan";
      } else {
        fullText.style.display = "none";
        shortText.style.display = "inline";
        button.innerText = "Tampilkan lebih banyak";
      }
    });
  });
});

// back to top
$(document).ready(function () {
  // Menampilkan atau menyembunyikan tombol saat menggulir
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $("#backToTop").fadeIn(); // Tampilkan tombol
    } else {
      $("#backToTop").fadeOut(); // Sembunyikan tombol
    }
  });

  // logic klik pada tombol
  $("#backToTop").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500); // Menggunakan animasi
  });
});

// animasi pop up formwali
$(document).ready(function () {
  $("#getStarted").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal").modal("show");
  });

  $("#waliForm").on("submit", function (event) {
    event.preventDefault(); // Mencegah form dari pengiriman default
    showModal(); // Menampilkan modal
  });
  // Menutup modal hanya jika tombol OK diklik
  $(".close").on("click", function () {
    $("#verificationModal").modal("hide");
  });
  $(".close-btn").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
  });
  $(".close-btn2").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
    window.location.href = "dashboard.html"; // Pindah ke halaman homepage.html
  });
});
// pop up verified
$(document).ready(function () {
  $("#getStarted").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal").modal("show");
  });

  $("#waliForm").on("submit", function (event) {
    event.preventDefault();
    showModal();
  });

  $(".close").on("click", function () {
    $("#verificationModal").modal("hide");
  });
  $(".close-btn").on("click", function () {
    window.location.href = "login.html";
  });
});

// animasi pop up form login
$(document).ready(function () {
  $("#getLogin").on("click", function (event) {
    event.preventDefault();
    $("#verificationModal2").modal("show");
  });

  $("#loginForm").on("submit", function (event) {
    event.preventDefault(); // Mencegah form dari pengiriman default
    showModal(); // Menampilkan modal
  });
  // Menutup modal hanya jika tombol OK diklik
  $(".close").on("click", function () {
    $("#verificationModal2").modal("hide");
  });
  $(".close-btn3").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman homepage.html
    window.location.href = "login.html"; // Pindah ke halaman homepage.html
  });
  $(".close-btn4").on("click", function () {
    // Setelah modal ditutup, pindahkan pengguna ke halaman dashboard.html
    window.location.href = "signup.html"; // Pindah ke halaman dashboardwali.html
  });
});
// teks sembuyikan login
$(document).ready(function () {
  $("#toggleButton").click(function () {
    $("#infoText").toggle(); // Menyembunyikan atau menampilkan teks
    $(this).text(
      $(this).text() === "Sembunyikan Teks"
        ? "Tampilkan Teks"
        : "Sembunyikan Teks"
    ); // Mengubah teks tombol
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const alertModal = document.getElementById("alertModal");
  if (alertModal) {
    const bootstrapModal = new bootstrap.Modal(alertModal);
    bootstrapModal.show();
  }
});

// wa
document.addEventListener("DOMContentLoaded", function () {
  const waLink = document.getElementById("wa-link");
  const consultMessage = document.getElementById("consult-message");

  waLink.addEventListener("mouseover", function () {
    consultMessage.style.display = "block"; // Tampilkan pesan
  });

  waLink.addEventListener("mouseout", function () {
    consultMessage.style.display = "none";
  });
});

$(document).ready(function () {
  const $formContainer = $("#testimoniFormContainer");
  const $toggleBtn = $("#toggleFormBtn");

  $toggleBtn.on("click", function () {
    const isVisible = $formContainer.css("display") === "block";

    if (isVisible) {
      $formContainer.css("display", "none");
      $toggleBtn.html(
        '<i class="fa-regular fa-message me-2"></i> Berikan Testimoni Anda'
      );
    } else {
      $formContainer.css("display", "block");
      $toggleBtn.text("Tutup Testimoni");
    }
  });
});

// greeting.js

// Fungsi untuk menampilkan salam berdasarkan waktu
function getGreeting() {
  const hours = new Date().getHours();
  let greeting = "";

  // Menentukan salam berdasarkan jam
  if (hours >= 5 && hours < 10) {
    greeting = "Selamat Pagi";
  } else if (hours >= 10 && hours < 18) {
    greeting = "Selamat Siang";
  } else if (hours >= 18 || hours < 5) {
    greeting = "Selamat Malam";
  }

  return greeting;
}

// jam
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("greeting").innerText = getGreeting();
});

function updateClock() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, "0");
  const minutes = now.getMinutes().toString().padStart(2, "0");
  const seconds = now.getSeconds().toString().padStart(2, "0");

  // Menampilkan waktu pada elemen HTML
  document.getElementById("hours").textContent = hours;
  document.getElementById("minutes").textContent = minutes;
  document.getElementById("seconds").textContent = seconds;
}

// Memperbarui jam setiap detik
setInterval(updateClock, 1000);

updateClock();
