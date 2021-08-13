from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API VIEW"""
    
    
    def get(self,request,format=None):
        """Returns API features """
        an_apiview=['Uses HTTP methods as functions(get,post,patch,put,delete)',
                    'Is similar to traditional api view'
                    'Gives you most control over your application logic',
                    'is mapped manually to URLS',
                    ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})