from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""
        an_apiview=[
        'Demo of api view',
        'is similar to traditional django view'
        ]

        return Response({'messages':'Get','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello messages with our name"""

        # serializer_class is function in APIView to retrive the
        # configure serialize class in our case it is HelloSerializer class
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')  #retrive the name from validated data
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """ Handle Updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'delete'})
