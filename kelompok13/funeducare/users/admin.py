from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from .models import CustomUser, Child, ChildDevelopment

admin.site.register(CustomUser)

# PDF download action
def wrap_text(text, max_width, pdf, font_name="Helvetica", font_size=9):
    """Wrapper function to break long text into lines that fit the max width"""
    lines = []
    text_object = pdf.beginText(0, 0)
    text_object.setFont(font_name, font_size)
    text_object.setTextOrigin(0, 0)
    words = text.split(" ")

    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        text_object.textLine(test_line)
        
        # If the line exceeds max_width, break and start a new line
        if text_object.getX() > max_width:
            lines.append(line)
            line = word  # Start new line with current word
            text_object.setTextOrigin(0, 0)
        else:
            line = test_line
    if line:
        lines.append(line)
    
    return lines

def download_pdf(self, request, queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=laporan_perkembangan_anak.pdf'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle('PDF Report')

    fields = self.model._meta.fields
    header = [field.verbose_name for field in fields]
    data = [header]

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, str):  
                value = "\n".join(wrap_text(value, 30, pdf))  
            data_row.append(str(value))
        data.append(data_row)

    num_columns = len(header)
    width, height = letter
    col_width = (width - 100) / num_columns

    table = Table(data, colWidths=[col_width] * num_columns)

   
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'JUSTIFY'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    row_height = 0.7 * inch  
    table_height = (len(data) * row_height) + 50  

    # Adjust table positioning
    table.wrapOn(pdf, width - 100, table_height)
    table.drawOn(pdf, 50, height - table_height - 50)

    pdf.save()
    return response

download_pdf.short_description = "Download selected items as PDF"

# Inline for ChildDevelopment in ChildAdmin
class ChildDevelopmentInline(admin.TabularInline):
    model = ChildDevelopment
    extra = 1

# Admin for ChildDevelopment
@admin.register(ChildDevelopment)
class ChildDevelopmentAdmin(admin.ModelAdmin):
    list_display = ('child', 'category', 'level')
    list_filter = ('category', 'level')

# Admin for Child
@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['nama_anak', 'user', 'is_approved', 'program', 'usia']
    list_filter = ['is_approved']  # Filter untuk memudahkan admin
    actions = ['approve_children', download_pdf]  # Add actions here
    inlines = [ChildDevelopmentInline]

    def approve_children(self, request, queryset):
        queryset.update(is_approved=True)  # Setujui data
        self.message_user(request, "Data anak-anak terpilih telah disetujui.")

    approve_children.short_description = "Setujui Anak-Anak yang dipilih"
