from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactSerializer

class ContactSubmitView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Send email
            subject = f"New Contact from {serializer.data['name']}"
            message = f"Email: {serializer.data['email']}\n\nMessage:\n{serializer.data['message']}"
            send_mail(subject, message, 'your_email@gmail.com', ['your_email@gmail.com'], fail_silently=False)

            return Response({'message': 'Submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

