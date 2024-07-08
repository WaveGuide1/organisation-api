from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Organisation
from .serializers import OrganisationSerializer
from user.models import User


class OrganisationListView(APIView):
    """
    View for listing and creating organisations
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        organisations = request.user.organisations.all()
        serializer = OrganisationSerializer(organisations, many=True)
        return Response({
            'status': 'success',
            'message': 'Organisations retrieved successfully',
            'data': {'organisations': serializer.data}
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            organisation = serializer.save()
            organisation.users.add(request.user)
            return Response({
                'status': 'success',
                'message': 'Organisation created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class OrganisationDetailView(APIView):
    """
    View for retrieving and adding users to an organisation
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, orgId):
        try:
            organisation = Organisation.objects.get(orgId=orgId, users=request.user)
            serializer = OrganisationSerializer(organisation)
            return Response({
                'status': 'success',
                'message': 'Organisation retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Organisation.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Organisation not found or access denied',
                'statusCode': 404
            }, status=status.HTTP_404_NOT_FOUND)


class OrganisationAddUserView(APIView):
    """
    View for adding a user to an organisation
    """
    permission_classes = [AllowAny]

    def post(self, request, orgId):
        try:
            organisation = Organisation.objects.get(orgId=orgId, users=request.user)
            user_id = request.data.get('userId')
            user = User.objects.get(userId=user_id)
            organisation.users.add(user)
            return Response({
                'status': 'success',
                'message': 'User added to organisation successfully'
            }, status=status.HTTP_200_OK)
        except Organisation.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Organisation not found or access denied',
                'statusCode': 404
            }, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'User not found',
                'statusCode': 404
            }, status=status.HTTP_404_NOT_FOUND)
