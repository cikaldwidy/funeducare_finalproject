(function (global, $) {
  var Popper = function (reference, popper, options) {
    this.reference = reference;
    this.popper = popper;
    this.options = options || {};
    this.init();
  };

  Popper.prototype.init = function () {
    this.updatePosition();
    window.addEventListener('resize', this.updatePosition.bind(this));
    this.setupEventListeners();
  };

  Popper.prototype.updatePosition = function () {
    var rect = this.reference.getBoundingClientRect();
    var popperRect = this.popper.getBoundingClientRect();
    
    // Menentukan posisi popper
    var top = rect.bottom + window.scrollY;
    var left = rect.left + window.scrollX + (rect.width / 2) - (popperRect.width / 2);

    this.popper.style.position = 'absolute';
    this.popper.style.top = top + 'px';
    this.popper.style.left = left + 'px';
  };

  Popper.prototype.setupEventListeners = function () {
    var self = this;
    $(document).on('click', function (event) {
      // Menutup popper jika klik di luar popper
      if (!$(event.target).closest(self.popper).length && !$(event.target).is(self.reference)) {
        self.popper.style.display = 'none'; // Menyembunyikan popper
      }
    });

    // Menyembunyikan popper saat referensi diklik
    $(this.reference).on('click', function () {
      $(self.popper).toggle(); // Menampilkan atau menyembunyikan popper
      self.updatePosition(); // Memperbarui posisi setelah ditampilkan
    });
  };

  // Mengatur Popper ke dalam global namespace
  global.Popper = Popper;

})(window, jQuery);
