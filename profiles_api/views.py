from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import  viewsets
# from rest_framework.renderers import JSONRenderer

from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer

    # renderer_classes = [JSONRenderer]

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


class HelloViewset(viewsets.ViewSet):
    """Tets API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset=['User actions (list,Create,retrive,update,patial update)',
                    'Authomatically maps with Routers',
                    'Provide more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset':a_viewset})

    def create(self,request):
        """Create a new line hello message"""

        serializer = self.serializer_class(data=request.data)  # Inside the method accessing serializer_class so use self.serializer_class

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
