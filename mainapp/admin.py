from django.contrib import admin
from .models import User,Talent,Employer,JobPosting,JobApplication,Consultant,Consultation,Review,Testimonial,Package,PackageInvoice
# Register your models here.

admin.site.register(User)
admin.site.register(Talent)
admin.site.register(Employer)
admin.site.register(JobPosting)
admin.site.register(JobApplication)
admin.site.register(Consultant)
admin.site.register(Consultation)
admin.site.register(Review)
admin.site.register(Testimonial)
admin.site.register(Package)
admin.site.register(PackageInvoice)

# admin.site.register(CustomUser)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff')
#     search_fields = ('username', 'email')