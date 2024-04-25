from django.contrib import admin
from .models import MyUser,Bet,Match,Club
# Register your models here.
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'balance') 
    search_fields=('email','balance')

    def bet(self, obj):
        return obj.bets.count()

@admin.register(Bet)
class VacancyAdmin(admin.ModelAdmin):
    list_display=('id','match','state_chosen','amount','user')
    search_fields=('id','match','state_chosen','amount','user')

@admin.register(Match)
class VacancyAdmin(admin.ModelAdmin):
    list_display=('home_club','away_club','match_date','state1','state2','state3')
    search_fields=('home_club','away_club','match_date','state1','state2','state3')

@admin.register(Club)
class VacancyAdmin(admin.ModelAdmin):
    list_display=('id','name','points')
    search_fields=('id','name','points')