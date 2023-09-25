from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import subprocess   
from .serializers import interestSerializer

from memodel.ML_suggestions import ML


class getinfo(APIView):
    """Getting the info from main backend."""
    serializer_class = interestSerializer
    def post(self, request):
        """getting the information from main backend"""
        # serializer = self.serializer_class(data=request.data)
        # if serializer.is_valid():
        #     first = serializer.validated_data['first']
        #     second = serializer.validated_data['second']
        #     third = serializer.validated_data['third']
        # first = request.data.get('first')
        # second = request.data.get('second')
        # third = request.data.get('third')

        suggestion = ML()
        print(suggestion)
        suggestion_html = suggestion.replace('\n', '<br>')
        return HttpResponse(f'Suggestion: <br>{suggestion_html}', content_type="text/html")

        # subprocess.call(['python', './ML_suggestions.py', first, second, third])
        # result = subprocess.run(['python', './ML_suggestions.py'], capture_output=True)
        # return HttpResponse(f'Suggestion: {suggestion}')
