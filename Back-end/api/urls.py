from django.urls import path
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('clubs/', ClubListCreate.as_view(), name='club-list'),
    path('clubs/<int:pk>/', ClubDetail.as_view(), name='club-detail'),
    path('clubs/<int:pk>/matches/',MatchesByClub.as_view(),name='matches_of_club'),
    path('clubs/top_20/',ClubList20.as_view(),name='20_clubs'),

    path('matches/', MatchListCreate.as_view(), name='match-list'),
    path('matches/<int:pk>/',MatchDetail.as_view(), name='match-detail'),

    path('bets/', BetListCreate.as_view(), name='bet-list'),
    path('bets/<int:pk>/',BetDetail.as_view(), name='bet-detail'),

    path('users/', UserListCreate.as_view(), name='bet-list'),
    path('users/<int:pk>/',UserDetail.as_view(), name='bet-detail'),

]