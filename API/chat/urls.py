from django.urls import path
from chat.views import ChatbotView

urlpatterns = [
    path('chat/', ChatbotView.as_view(), name='chatbot')
]
