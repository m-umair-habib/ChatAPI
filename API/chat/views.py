from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chat.models import Chat
from chat.serializers import ChatSerializer

class ChatbotView(APIView):
    def get(self, request):
        user = request.query_params.get('user')
        chats = Chat.objects.filter(user=user)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get('user')
        message = request.data.get('message')

        # Dummy AI response - replace with actual AI call later
        response = f"Echo: {message}"

        chat = Chat.objects.create(user=user, message=message, response=response)
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
