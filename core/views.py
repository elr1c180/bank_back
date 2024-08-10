
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

# class handleClick(generics.RetrieveAPIView, id):
#     user = User.objects.get(id=id)

#     user.balance += user.tap_count
#     user.energy -= user.tap_count

#     user.save

