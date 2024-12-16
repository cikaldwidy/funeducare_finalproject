from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    age_range = models.CharField(max_length=50)
    image = models.ImageField(upload_to='program_images/')
    program_start_date = models.DateTimeField(null=True, blank=True, verbose_name="Tanggal Mulai Program")
    program_end_date = models.DateTimeField(null=True, blank=True, verbose_name="Tanggal Selesai Program")
    status = models.CharField(
        max_length=10,
        choices=[('active', 'Aktif'), ('inactive', 'Tidak Aktif')],
        default='active'
    )
    def check_status(self):
        """Memeriksa apakah program sudah berakhir dan mengupdate statusnya."""
        if self.program_end_date:
         
            if timezone.is_naive(self.program_end_date):
                self.program_end_date = timezone.make_aware(self.program_end_date)

           
            if self.program_end_date < timezone.now() and self.status != 'inactive':
                self.status = 'inactive' 

    def save(self, *args, **kwargs):
        """Override save untuk memastikan status program selalu diperbarui."""
        self.check_status()
        super().save(*args, **kwargs)  
   
    def __str__(self):
        return self.name

class Activity(models.Model):
  program = models.ForeignKey(Program, related_name='activities', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  icon_class = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Facility(models.Model):
  program = models.ForeignKey(Program, related_name='facilities', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(default="Default description")
  icon_class = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class Fee(models.Model):
  program = models.ForeignKey(Program, related_name='fees', on_delete=models.CASCADE)
  type_program = models.CharField(max_length=50)
  description = models.TextField(default="Default description")
  amount = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"{self.type_program} - {self.amount}"

class Schedule(models.Model):
  program = models.ForeignKey(Program, related_name='schedules', on_delete=models.CASCADE)
  days = models.CharField(max_length=100)
  time = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.days} - {self.time}"

class Teacher(models.Model):
  program = models.ForeignKey(Program, related_name='teachers', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  bio = models.TextField()
  profile_picture = models.ImageField(upload_to='teacher_photos/', blank=True, null=True)
  experience = models.CharField(max_length=255)

  def __str__(self):
    return self.name


class ProgramsCompetitionModel(models.Model):
  #Disini kita akan menyimpan data dari forms ke model
  #Maka propertinya haruslah sama dengan di forms
  nama = models.CharField(max_length=25)
  email = models.EmailField()
  JENKEL_CHOICES = [
    ('l', 'Laki-Laki'),
    ('p', 'Perempuan')
  ]
  jenkel = models.CharField(
    max_length=1,
    choices=JENKEL_CHOICES,
    verbose_name="Jenis Kelamin"
  )
  tgl_lahir = models.DateField(verbose_name="Tanggal Lahir", null=False, blank=False)
  pesan = models.TextField()
  agree = models.BooleanField(
    verbose_name="Saya setuju untuk mengikuti lomba dan mengikuti syarat dan ketentuan yang berlaku",
    default=False
  )

  def __str__(self):
    return "%d %s" % (self.id, self.nama)
  
class ParentingSeminarModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  speaker = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  stock = models.PositiveIntegerField(default=10)

  TICKET_STATUS_CHOICES = [
    ('available', 'Tiket Tersedia'),
    ('limited', 'Tiket Hampir Habis'),
    ('sold_out', 'Tiket Habis Terjual')
  ]

  ticket_status = models.CharField(
    max_length=20,
    choices=TICKET_STATUS_CHOICES,
    default='available'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Parenting Seminar'
    verbose_name_plural = 'Parenting Seminars'

  def __str__(self):
    return f"{self.date} - {self.title}"
    
class CookingClassModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  instructor = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  stock = models.PositiveIntegerField(default=10)

  TICKET_STATUS_CHOICES = [
    ('available', 'Tiket Tersedia'),
    ('limited', 'Tiket Hampir Habis'),
    ('sold_out', 'Tiket Habis Terjual')
  ]

  ticket_status = models.CharField(
    max_length=20,
    choices=TICKET_STATUS_CHOICES,
    default='available'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Cooking Class'
    verbose_name_plural = 'Cooking Classes'

  def __str__(self):
    return f"{self.date} - {self.title}"

class ChildrenExhibitionModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  stock = models.PositiveIntegerField(default=10)


  REGISTRATION_STATUS_CHOICES = [
    ('open', 'Daftar Sekarang'),
    ('limited', 'Tempat Terbatas'),
    ('closed', 'Pendaftaran Tutup'),
  ]

  registration_status = models.CharField(
    max_length=20,
    choices=REGISTRATION_STATUS_CHOICES,
    default='open'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Children Exhibition'
    verbose_name_plural = 'Children Exhibitions'
  
  def __str__(self):
    return f"{self.date} - {self.title}"
  