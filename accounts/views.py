

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User,Profile
from .serializers import UserLoginSerializer,StaffRegistrationSerializer,CustomerRegistrationSerializer,UserProfile,ProfileSerializer

from restaurant.models import Restaurant

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User







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
                    profile = Profile.objects.create(user=user,address='',contact_number='')
                    user.save()
                    profile.save()
                    return Response('User Registered successfully',status=status.HTTP_201_CREATED)
                
            else:
                return Response('Password and Confirm Password doesnot match')
        else:
            return Response(serializer.errors)
    else:
        return Response('Welcome')


@api_view(['GET','PATCH'])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        user = User.objects.get(id=request.user.id)
        if request.method == 'GET':
            serializer = UserProfile(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

        if request.method == 'PATCH':
            pass
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# class BlacklistTokenView(APIView):
#     permission_classes=[AllowAny]
#     def post(self,request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response('Logged Out',status=status.HTTP_200_OK)
#         except Exception as e:
#             print(Exception)
#             return Response('Exception',status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def BlacklistTokenView(request):
    if request.method=='POST':
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response('Logged Out',status=status.HTTP_200_OK)
        except Exception as e:
            print(Exception)
            return Response('Exception',status=status.HTTP_400_BAD_REQUEST)
    else:
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

@api_view(['GET','POST'])
def customer_login(request):
    if request.method == 'GET':  
        return Response('WELCOME TO FOOD DELIVERY. Enter your login credentials(email and password)')
    else:    
        email = request.data['email']
        password = request.data['password']
        
        if User.objects.filter(email=email).exists()==False:
            return Response('User doesnot exists',status=status.HTTP_404_NOT_FOUND)        
        else:
            user = authenticate(email=email, password=password) 
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },status=status.HTTP_200_OK)
            else:                       
                return Response('Username or Password is incorrect',status=status.HTTP_401_UNAUTHORIZED)   

@api_view(['GET','POST'])
def staff_login(request,city,restaurant):
    if request.method == 'GET':
        res=Restaurant.objects.get(id=restaurant)
        return Response(f"WELCOME TO {res.name}  Enter Your Login Credentials(email and password)")
    else:
        email = request.data['email']
        password = request.data['password']
        if User.objects.filter(email=email,restaurant=restaurant).exists()==False:
            return Response('User doesnot exists',status=status.HTTP_404_NOT_FOUND)
        else:        
            user = authenticate(email=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },status=status.HTTP_200_OK)
            else:                       
                 return Response('Username or Password is incorrect',status=status.HTTP_401_UNAUTHORIZED)


# # @api_view(['GET'])
# # def _logout(request):
# #     logout(request)
# #     return Response('logged out')
    
