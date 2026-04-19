from django.shortcuts import render
from .serializers import CarsSeriaLizer
from .models import Cars
from .permission import IsOwnerOrReadOnly

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny



from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()

# Create your views here.


class CarsApiView(ListAPIView): 
    queryset = Cars.objects.all()
    serializer_class = CarsSeriaLizer


class CartDetailView(RetrieveAPIView): 
    queryset = Cars.objects.all()
    serializer_class = CarsSeriaLizer
    lookup_field = "id"  

class CreateCarView(CreateAPIView): 
     queryset = Cars.objects.all()
     serializer_class = CarsSeriaLizer
     permission_classes = [IsAuthenticated] # Faqat login qilganlar uchun


class CarUptadeDeleteView(RetrieveUpdateDestroyAPIView): 
    queryset = Cars.objects.all()
    serializer_class = CarsSeriaLizer
    lookup_field = "id"
    permission_classes = [IsOwnerOrReadOnly]




@method_decorator(csrf_exempt, name='dispatch')
class DirectPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        new_password = request.data.get('new_password')

        if not username or not new_password:
            return Response({"error": "Login va yangi parol to'liq kiritilishi shart!"}, 
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            # Foydalanuvchini login bo'yicha qidiramiz
            user = User.objects.get(username=username)
            user.set_password(new_password) # Parolni o'zgartirish
            user.save()
            return Response({"message": f"{username} uchun parol muvaffaqiyatli yangilandi!"}, 
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Bunday loginli foydalanuvchi topilmadi!"}, 
                            status=status.HTTP_404_NOT_FOUND)
        
    