from django.contrib import admin
from .models import Chaivariety, ChaiReview, Store, ChaiCertificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1 



admin.site.register(Chaivariety)