$(document).ready(function () {
  // Handle click event for VA (BCA Virtual Account)
  $("#VA").click(function () {
    $("#descBCA").collapse("toggle");
    // Hide other descriptions if clicked
    if ($("#descQRIS").hasClass("show")) {
      $("#descQRIS").collapse("hide");
    }
  });

  // Handle click event for QRIS
  $("#QRIS").click(function () {
    $("#descQRIS").collapse("toggle");
    // Hide other descriptions if clicked
    if ($("#descBCA").hasClass("show")) {
      $("#descBCA").collapse("hide");
    }
  });
});

// JavaScript untuk menangani klik tombol dan menampilkan kode VA

$(document).ready(function () {
  // Saat tombol "Bayar Sekarang" diklik
  $("#showVA").click(function () {
    // Sembunyikan formulir
    $("#paymentForm").hide();

    // Tampilkan kode VA
    $("#vaCode").show();
  });
});
