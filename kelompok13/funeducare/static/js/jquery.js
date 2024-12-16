$(document).ready(function () {
  // Fungsi untuk tombol kembali ke halaman utama
  $(".btn-back").on("click", function () {
    window.location.href = "index.html"; // Ganti dengan URL halaman utama Anda
  });

  // Fungsi hover untuk menu sidebar
  $(".menu a").hover(
    function () {
      $(this).css("background-color", "#15a6f5"); // Warna hover biru
      $(this).css("color", "#fff"); // Warna teks putih saat hover
    },
    function () {
      $(this).css("background-color", "transparent"); // Kembalikan warna default
      $(this).css("color", "#1f1f1f"); // Warna teks hitam saat tidak hover
    }
  );

  // Fungsi untuk animasi scroll pada konten utama
  $("a").on("click", function (event) {
    if (this.hash !== "") {
      event.preventDefault();

      var hash = this.hash;

      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top,
        },
        800,
        function () {
          window.location.hash = hash;
        }
      );
    }
  });

  // Fungsi animasi untuk kartu profil saat di-hover
  $(".profile-card").hover(
    function () {
      $(this).css("transform", "scale(1.05)");
    },
    function () {
      $(this).css("transform", "scale(1)");
    }
  );

  // Fungsi untuk memuat gambar anak secara dinamis
  let childrenData = [
    {
      name: "Mayanda Bella",
      program: "Infant Care",
      age: "5 Bulan",
      img: "./assets/images/anak1.jpg",
    },
    {
      name: "Arya Dinata",
      program: "Toddler Program",
      age: "2 Tahun",
      img: "./assets/images/anak2.jpg",
    },
    {
      name: "Arumi Khanza",
      program: "Pre-School Program",
      age: "3 Tahun",
      img: "./assets/images/anak3.jpg",
    },
    {
      name: "Rafif Akbar",
      program: "Pre-Kindergarten",
      age: "5 Tahun",
      img: "./assets/images/anak4.jpg",
    },
  ];

  $.each(childrenData, function (index, child) {
    let card = `<div class="col-md-3">
                  <div class="card profile-card">
                    <img src="${child.img}" alt="Foto ${child.name}" class="card-img-top profile-img " />
                    <div class="card-body">
                      <h5 class="card-title">${child.name}</h5>
                      <p><strong>Program:</strong> ${child.program}</p>
                      <p><strong>Umur Anak:</strong> ${child.age}</p>
                    </div>
                  </div>
                </div>`;

    $(".profile-cards").append(card);
  });

  // Pesan sambutan untuk orang tua
  alert("Selamat datang di dashboard orang tua!");
});

// pengaturan akun popup
function simpanPerubahan(event) {
  event.preventDefault(); // Mencegah reload halaman setelah submit
  alert("Perubahan berhasil disimpan!"); // Menampilkan pesan konfirmasi
}
