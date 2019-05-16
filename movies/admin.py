from django.contrib import admin
from .models import Movie,Score,Genre,MovieCd,MovieDetail
# Register your models here.
admin.site.register(Movie)
admin.site.register(Score)
admin.site.register(Genre)
admin.site.register(MovieCd)
admin.site.register(MovieDetail)