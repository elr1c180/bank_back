
from .serializers import UserSerializer
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    if len(User.objects.filter(chat_id=link_owner)) != 0:
        return Response({'message': 'User not exist or alredy referal'}, status=status.HTTP_423_LOCKED)
    else:
        new_user = User.objects.create(
            chat_id = referal,
            username = username,
            first_name = name,
            level = Level.objects.get(level=1)
        )
        
        new_user.save()

        link_owner = User.objects.get(chat_id=link_owner)

        link_owner.referals.add(new_user)

        return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
