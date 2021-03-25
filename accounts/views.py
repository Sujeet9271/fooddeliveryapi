

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .serializers import UserLoginSerializer,StaffRegistrationSerializer,CustomerRegistrationSerializer

from restaurant.models import Restaurant

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny






@api_view(['GET','POST'])
def staff_register(request,city,restaurant):
    if request.method == 'POST':
        serializer=StaffRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
            password2 = request.data['confirm']
            if password == password2:
                if User.objects.filter(username=username).exists():
                    return Response('User with same username already exists')
                elif User.objects.filter(email=email).exists():
                    return Response('User with same email already exists')
                else:
                    user = User.objects.create_user(username=username, password=password, firstname=firstname, lastname=lastname, email=email,staff=True,restaurant=restaurant)
                    user.save()
                    return Response('User Registered successfully',status=status.HTTP_201_CREATED)
            else:
                return Response('Password and Confirm Password doesnot match')
        else:
            return Response(serializer.errors)
    else:
        res=Restaurant.objects.get(id=restaurant)
        return Response(f"Welcome to {res.name}.")

@api_view(['GET','POST'])
def customer_register(request):
    if request.method == 'POST':

        serializer = CustomerRegistrationSerializer(data=request.data)        
        if serializer.is_valid():
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            username = request.data['username']
            email = request.data['email']
            password = request.data['password']
            password2 = request.data['confirm']        
            if password == password2:
                if User.objects.filter(username=username).exists():
                    return Response('User with same username already exists')
                elif User.objects.filter(email=email).exists():
                    return Response('User with same email already exists')
                else:
                    user = User.objects.create_user(username=username, password=password, firstname=firstname, lastname=lastname, email=email,staff=False,restaurant=0)
                    user.save()
                    return Response('User Registered successfully',status=status.HTTP_201_CREATED)
                return redirect('auth_user')
            else:
                return Response('Password and Confirm Password doesnot match')
        else:
            return Response(serializer.error)
    else:
        return Response('Welcome')

class BlacklistTokenView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def _logout(request):
#     print(request.user)
#     logout(request)
#     return Response('logged out')

# # @api_view(['GET','POST'])
# # def login(request):
# #     if request.method == 'GET':  
# #         return Response('WELCOME TO FOOD DELIVERY. Enter your login credentials(email and password)')
# #     else:    
# #         email = request.data['email']
# #         password = request.data['password']
        
# #         if User.objects.filter(email=email).exists()==False:
# #             return Response('User doesnot exists')
        
# #         user = authenticate(email=email, password=password)
 
# #         if user is not None:
# #             login(request, user)
# #             return Response('Logged in')
# #         else:                       
# #             return Response('Username or Password is incorrect')

# # @api_view(['GET','POST'])
# # def customer_login(request):
# #     if request.method == 'GET':
  
# #         return Response('WELCOME TO FOOD DELIVERY. Enter your login credentials(email and password)')
# #     else:
    
# #         email = request.data['email']
# #         password = request.data['password']
        
# #         if User.objects.filter(email=email).exists()==False:
# #             return Response('User doesnot exists')
        
# #         user = authenticate(email=email, password=password)
 
# #         if user is not None:
# #             login(request, user)
# #             return Response('Logged in')
# #         else:                       
# #             return Response('Username or Password is incorrect')   

# # @api_view(['GET','POST'])
# # def staff_login(request,city,restaurant):
# #     if request.method == 'GET':
# #         res=Restaurant.objects.get(id=restaurant)
# #         return Response(f"WELCOME TO {res.name}  Enter Your Login Credentials(email and password)")
# #     else:
# #         email = request.data['email']
# #         password = request.data['password']

# #         if User.objects.filter(email=email,restaurant=restaurant).exists()==False:
# #             return Response('User doesnot exists')
# #         else:        
# #             user = authenticate(email=email, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 return Response('Logged in')
# #             else:                       
# #                  return Response('Username or Password is incorrect')





# # @api_view(['GET'])
# # def _logout(request):
# #     logout(request)
# #     return Response('logged out')
    
