from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status,mixins,generics

import json
from ..models import Bet,Match,Club,MyUser
from ..serializers import BetSerializer,BetSerializer2,MatchSerializer,MyUserSerializer2,ClubSerializer,ClubSerializer2,MyUserSerializer,MatchSerializer2

from rest_framework.permissions import AllowAny,IsAuthenticated

class ClubListCreate(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer2
    permission_classes=(IsAuthenticated,)


class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer2
    permission_classes=(IsAuthenticated,)



class MatchListCreate(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes=(IsAuthenticated,)


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes=(IsAuthenticated,)


class BetListCreate(generics.ListCreateAPIView):
    # queryset = Bet.objects.all()
    serializer_class = BetSerializer2
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        return Bet.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer2
    permission_classes=(IsAuthenticated,)


class UserListCreate(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer2
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        return MyUser.objects.filter(email=self.request.user.email)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer2
    permission_classes=(IsAuthenticated,)


class MatchesByClub(generics.ListAPIView):
    serializer_class = MatchSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        try:
            club = Club.objects.get(pk=pk)
        except Club.DoesNotExist:
            return Club.objects.none()
        return Match.objects.filter(home_club=club) | Match.objects.filter(away_club=club)

class ClubList20(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    queryset = Club.objects.order_by('-points')[:20]
    serializer_class = ClubSerializer2