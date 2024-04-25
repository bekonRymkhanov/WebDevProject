from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
import json
from ..models import Bet,Match,Club,MyUser
from ..serializers import BetSerializer,BetSerializer2,MatchSerializer,MyUserSerializer2,ClubSerializer,ClubSerializer2,MyUserSerializer,MatchSerializer2


class ClubListCreate(APIView):
    def get(self, request):
        clubs = Club.objects.all()
        serializer = ClubSerializer2(clubs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClubSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ClubDetail(APIView):
    def get_object(self, pk=None):
        try:
            return Club.objects.get(pk=pk)
        except Club.DoesNotExist as err:
            raise Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        club = self.get_object(pk)
        serializer = ClubSerializer2(club)
        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        club = self.get_object(pk)
        serializer = ClubSerializer2(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        club = self.get_object(pk)
        club.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MatchListCreate(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchSerializer2(matches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MatchSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchDetail(APIView):
    def get_object(self, pk=None):
        try:
            return Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Response({'error': 'Match not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        match = self.get_object(pk)
        serializer = MatchSerializer2(match)
        return Response(serializer.data)

    def put(self, request, pk=None):
        match = self.get_object(pk)
        serializer = MatchSerializer2(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        match = self.get_object(pk)
        match.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)

class BetListCreate(APIView):
    def get(self, request):
        bets = Bet.objects.all()
        serializer = BetSerializer2(bets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BetSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BetDetail(APIView):
    def get_object(self, pk=None):
        try:
            return Bet.objects.get(pk=pk)
        except Bet.DoesNotExist:
            return Response({'error': 'Bet not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        bet = self.get_object(pk)
        serializer = BetSerializer2(bet)
        return Response(serializer.data)

    def put(self, request, pk=None):
        bet = self.get_object(pk)
        serializer = BetSerializer2(bet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        bet = self.get_object(pk)
        bet.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)

class UserListCreate(APIView):
    def get(self, request):
        users = MyUser.objects.all()
        serializer = MyUserSerializer2(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyUserSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    def get_object(self, pk=None):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = MyUserSerializer2(user)
        return Response(serializer.data)

    def put(self, request, pk=None):
        user = self.get_object(pk)
        serializer = MyUserSerializer2(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        user = self.get_object(pk)
        user.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)
    

class MatchesByClub(APIView):

    def get(self, request,pk=None):
        try:
            club = Club.objects.get(pk=pk)
        except Club.DoesNotExist as err:
            return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)

        matches = Match.objects.filter(home_club=club) | Match.objects.filter(away_club=club)
        
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClubList20(APIView):

    def get(self, request):
        clubs = Club.objects.order_by('-points')[:20]
        serializer = ClubSerializer2(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RegisterView(APIView):
    def post(self,request):
        serializer=MyUserSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=MyUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        return Response({
            "message success":True
        })
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        
        return Response({
            "message":"logged out successfully"
        })