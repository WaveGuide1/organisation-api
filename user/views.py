from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserSerializer
from organisation.serializers import OrganisationSerializer
from .models import User


class RegisterView(APIView):
    """
    View for user registration
    """
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Create default organisation
            org_name = f"{user.firstName}'s Organisation"
            org_data = {"name": org_name}
            org_serializer = OrganisationSerializer(data=org_data)
            if org_serializer.is_valid():
                organisation = org_serializer.save()
                organisation.users.add(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'success',
                'message': 'Registration successful',
                'data': {
                    'accessToken': str(refresh.access_token),
                    'user': UserSerializer(user).data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    """
    View for user login
    """
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 'success',
                'message': 'Login successful',
                'data': {
                    'accessToken': str(refresh.access_token),
                    'user': UserSerializer(user).data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'Bad request',
            'message': 'Authentication failed',
            'statusCode': 401
        }, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(APIView):
    """
    View for retrieving user details by userId
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, userId):
        try:
            user = User.objects.get(userId=userId)
            if user == request.user:
                serializer = UserSerializer(user)
                return Response({
                    'status': 'success',
                    'message': 'User details retrieved successfully',
                    'data': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'error',
                    'message': 'You do not have permission to view this user',
                    'statusCode': 403
                }, status=status.HTTP_403_FORBIDDEN)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'User not found',
                'statusCode': 404
            }, status=status.HTTP_404_NOT_FOUND)
