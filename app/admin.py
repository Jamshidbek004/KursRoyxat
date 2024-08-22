from django.contrib import admin
from .models import Royxat

class RoyxatAdmin(admin.ModelAdmin):
    # Admin panelida ko'rsatiladigan ustunlar
    list_display = ('ism', 'familya', 'yosh', 'jinsi', 'telraqam', 'yashashjoyi')

    # Filtrlash uchun maydonlar
    list_filter = ('jinsi', 'yashashjoyi')

    # Qidiruv maydonlari
    search_fields = ('ism', 'familya', 'telraqam', 'yashashjoyi')

    # Qo'shimcha sozlamalar
    list_editable = ('telraqam', 'yashashjoyi')  # Ro'yxatdan tahrirlash mumkin bo'lgan ustunlar
    list_per_page = 20  # Har bir sahifada nechta yozuv ko'rsatiladi

admin.site.register(Royxat, RoyxatAdmin)

