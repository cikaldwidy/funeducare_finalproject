from django.shortcuts import render
from django.core.mail import send_mail
from datetime import date
from .forms import ProgramsCompetitionForm
from .models import (
    Program,
    ParentingSeminarModel,
    CookingClassModel,
    ChildrenExhibitionModel,
    ProgramsCompetitionModel,
)


def programs(request):
    # Daftar nama program yang ingin ditampilkan
    program_names = [
        "Infant Care", 
        "Toddler", 
        "Pre School", 
        "Pre Kindergarten"
    ]
    
    # Ambil detail untuk setiap program
    programs_details = {}
    for name in program_names:
        try:
            program = Program.objects.get(name=name)
            programs_details[name] = {
                'program': program,
                'activities': program.activities.all(),
                'facilities': program.facilities.all(),
                'fees': program.fees.all(),
                'schedules': program.schedules.all(),
                'teachers': program.teachers.all()
            }
        except Program.DoesNotExist:
            programs_details[name] = None

    # Query untuk kompetisi dan event lainnya
    participant = ProgramsCompetitionModel.objects.all()
    programs_competitions_form = ProgramsCompetitionForm(request.POST or None)
    parenting_seminar = ParentingSeminarModel.objects.all().order_by('date')
    cooking_class = CookingClassModel.objects.all().order_by('date')
    exhibition = ChildrenExhibitionModel.objects.all().order_by('date')

    if request.method == 'POST' and programs_competitions_form.is_valid():
        # Ambil data dari form
        data = programs_competitions_form.cleaned_data

        # Simpan ke database
        ProgramsCompetitionModel.objects.create(
            nama=data['nama'],
            email=data['email'],
            jenkel=data['jenkel'],
            tgl_lahir=data['tgl_lahir'],
            pesan=data['pesan'],
            agree=data['agree'],
        )

        # Kirim email konfirmasi
        subject = "Konfirmasi Pendaftaran Lomba Junior Chef Cooking Competition 2024"
        message = f"""
        Hai {data['nama']}, 
        
        Terima kasih telah mendaftar lomba Junior Chef Cooking Competition 2024! Kami sangat senang menyambut {data['nama']} dalam acara yang penuh keceriaan ini. 
        Berikut adalah detail acara yang perlu Anda ketahui:

        🗓 Waktu dan Tempat:
        - Tanggal: Minggu, 15 Januari 2024
        - Waktu: 10:00 - 14:00 WIB
        - Tempat: Jl. Mawar, Ruko Silent Hill 2 Blok ABC No. 123, GAG City, Kec. Brat, Kota Jakarta Selatan, DKI Jakarta, Indonesia
        - Dress Code: Apron berwarna cerah dan topi chef (kami akan menyediakan jika tidak ada)

        📋 Panduan dan Apa yang Perlu Dibawa?
        - Bahan utama masakan: [Nama bahan yang harus dibawa, misalnya sayuran atau bahan pilihan peserta]
        - Peralatan masak sederhana: Pisau anak, talenan, sendok ukur, dll.
        - Botol minum pribadi

        🏆 Hadiah Menarik
        Juara lomba akan mendapatkan:
        Juara 1: Piala emas, sertifikat, dan voucher belanja Rp1.000.000
        Juara 2: Piala perak, sertifikat, dan hadiah kejutan lainnya

        📅 Timeline Acara
        Berikut adalah jadwal acara pada hari kompetisi:
        09:30 - 10:00: Registrasi peserta
        10:00 - 10:15: Pembukaan oleh MC
        10:15 - 12:00: Kompetisi memasak
        12:00 - 13:00: Penjurian dan hiburan
        13:00 - 14:00: Pengumuman pemenang dan penutupan

        📍 Panduan Akses Lokasi
        Klik di sini untuk melihat lokasi acara di Google Maps:
        https://www.google.com/maps/dir/-6.2136327,106.8264328/educourse/@-6.2636359,106.673832,12z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x2e69e55e09af6f51:0x15d32286238d7a9c!2m2!1d106.6864092!2d-6.3046617?entry=ttu&g_ep=EgoyMDI0MTIwMy4wIKXMDSoASAFQAw%3D%3D

        📲 Gabung ke Grup WhatsApp
        Untuk mendapatkan informasi lebih lanjut dan update terkini seputar acara, kami mengundang Anda untuk bergabung ke dalam grup WhatsApp kami. Klik di sini untuk bergabung: https://chat.whatsapp.com/LbTNwxXLErX0QShcLYxIOI

        📑 Aturan Lomba
        Peserta wajib memasak sendiri di tempat acara.
        Bahan yang digunakan harus sesuai dengan tema "Hidangan Sehat".
        Waktu memasak maksimal 60 menit.
        Orang tua diperbolehkan menemani di area tertentu, tetapi tidak boleh membantu memasak.

        Kontak panitia
        Jika ada pertanyaan atau kebutuhan lebih lanjut, silakan hubungi kami di:
        Email: funeducare.id@gmail.com
        WhatsApp: 0812-3456-7890
        
        Kami tidak sabar untuk melihat kreativitas {data['nama']} di kompetisi ini. Sampai jumpa di acara!

        Salam,
        Tim Lomba FunEduCare 
        """
        from_email = 'funeducare.id@gmail.com'
        recipient_list = [data['email']]

        try:
            send_mail(subject, message, from_email, recipient_list)
            success_message = "Formulir berhasil dikirim dan email konfirmasi telah terkirim."
        except Exception as e:
            success_message = f"Formulir berhasil dikirim, tetapi email gagal dikirim. Error: {str(e)}"
        
        return render(request, 'programs/success.html', {'message': success_message})

    context = {
        'Judul': 'Our Programs',
        'f_competition': programs_competitions_form,
        'participants': participant,
        'parenting_seminar': parenting_seminar,
        'cooking_class': cooking_class,
        'exhibition': exhibition,
        'programs_details': programs_details
    }

    return render(request, 'programs/programs.html', context)
