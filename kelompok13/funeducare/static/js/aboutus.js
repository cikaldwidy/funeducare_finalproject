$(document).ready(function () {
  /* FITUR LIHAT INFORMASI SELENGKAPNYA */
  $(".more-info").on("click", function (e) {
    e.preventDefault();
    $(this).siblings(".additional-info").slideToggle();
  });
  /* EFEK KETIKA KURSOR DIARAHKAN KE BOX CAROUSEL GURU DAN GALERI MAKA AKAN MEMPERBESAR */
  $(".pengajar-item, .gallery-item").hover(
    function () {
      $(this).css({
        transform: "scale(1.05)",
        transition: "transform 0.3s ease",
      });
    },
    function () {
      $(this).css({
        transform: "scale(1)",
        transition: "transform 0.3s ease",
      });
    }
  );
  /* EFEK LOGO DIBAWAH TULISAN SIAPA KAMI  MEMPERBESAR DAN MEMPERKECIL*/
  function pulsateLogo() {
    $(".jumbotron img").animate({ scale: 1.1 }, 1000, function () {
      $(this).animate({ scale: 1 }, 1000, pulsateLogo);
    });
  }
  pulsateLogo();
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
