from django.contrib import admin
from .models import Chaiverity, ChaiReview, ChaiCertificate, Store

# Register your models here.
class chaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVerityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [chaiReviewInLine]

class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')

admin.site.register(Chaiverity, ChaiVerityAdmin)
admin.site.register(Store, ChaiStoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)