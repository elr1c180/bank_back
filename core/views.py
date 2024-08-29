
from .serializers import UserSerializer
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_user(request):
    chat_id, username, name = request.data['chat_id'], request.data['username'], request.data['name']

    if len(User.objects.filter(chat_id=chat_id)) > 0:
        return Response({'message': 'User alredy exist'}, status=status.HTTP_423_LOCKED)
    else:
        new_user = User.objects.create(
            chat_id = chat_id,
            username = username,
            first_name = name,
            level = Level.objects.get(level=1)
        )
        
        new_user.save()

        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_user_info(request, pk):
    queryset = User.objects.filter(id=pk)
    serializer_class = UserSerializer(queryset, many=True)
    return Response(serializer_class.data)

@api_view(['GET'])
def get_user(request, chat_id):
    try:
        user = User.objects.get(chat_id=chat_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def update_user(request, chat_id):
    try:
        user = User.objects.get(chat_id=chat_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def  new_ref(request):
    referal, link_owner, username, name = request.data['referal'], request.data['link_owner'], request.data['username'], request.data['name']
    # проверка на то что он уже чей-то реферал, добавить  запись в бд
    # реферала не существует в бд, он уже не явлется рефералом
    
    if len(User.objects.filter(chat_id=referal)) == 0 and User.objects.get(chat_id=referal) != True:
        new_user = User.objects.create(
            chat_id = referal,
            username = username,
            first_name = name,
            balance = 25000,
            is_referal = True,
            level = Level.objects.get(level=1)
        )
        
        new_user.save()

        link_owner = User.objects.get(chat_id=link_owner)
        link_owner.balance += 50000
        link_owner.referals.add(new_user)
        
        link_owner.save()

        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Error: User  alredy exist or referal'}, status=status.HTTP_423_LOCKED)

class UserReferralsView(APIView):
    def get(self, request, chat_id):
        user = get_object_or_404(User, chat_id=chat_id)
        referrals = user.referals.all()
        serializer = UserSerializer(referrals, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)