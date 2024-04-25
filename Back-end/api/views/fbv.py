from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

import json
from ..models import Club,Match,Bet,MyUser
from ..serializers import ClubSerializer2,MatchSerializer2,BetSerializer2,MyUserSerializer2


@api_view(["GET","POST"])
def ClubListCreate(request):
    if request.method == 'GET':
        clubs= Club.objects.all()
        serializer = ClubSerializer2(clubs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClubSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def ClubDetail(request,pk=None):

    try:
        club = Club.objects.get(pk=pk)
    except Club.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = ClubSerializer2(club)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClubSerializer2(club, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        club.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET","POST"])
def MatchListCreate(request):
    if request.method == 'GET':
        matches= Match.objects.all()
        serializer = MatchSerializer2(matches, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MatchSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def MatchDetail(request,pk=None):

    try:
        match = Match.objects.get(pk=pk)
    except Match.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = MatchSerializer2(match)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MatchSerializer2(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        match.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET","POST"])
def BetListCreate(request):
    if request.method == 'GET':
        betes= Bet.objects.all()
        serializer = BetSerializer2(betes, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BetSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def BetDetail(request,pk=None):

    try:
        bet = Bet.objects.get(pk=pk)
    except Bet.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = BetSerializer2(bet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer =BetSerializer2(bet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bet.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)
@api_view(["GET"])
def MatchesByClub(request, pk=None):
    if pk is None:
        return Response({'error': 'Club ID must be provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        club = Club.objects.get(id=pk)
    except Club.DoesNotExist:
        return Response({'error': 'Club not found'}, status=status.HTTP_404_NOT_FOUND)
    
    matches = Match.objects.filter(home_club=club) | Match.objects.filter(away_club=club)
    serializer = MatchSerializer2(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(["GET"])
def ClubList20(request):
    clubs=Club.objects.order_by('-points')[:20]
    serializer = ClubSerializer2(clubs, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET","POST"])
def UserListCreate(request):
    if request.method == 'GET':
        users= MyUser.objects.all()
        serializer = MyUserSerializer2(users, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MyUserSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","DELETE","PUT"])
def UserDetail(request,pk=None):

    try:
        user = MyUser.objects.get(pk=pk)
    except MyUser.DoesNotExist as err:
        return Response({"error":str(err)},status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = MyUserSerializer2(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer =MyUserSerializer2(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"deleted":True},status=status.HTTP_204_NO_CONTENT)