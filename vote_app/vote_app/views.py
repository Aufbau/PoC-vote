from rest_framework.views import APIView
from django.shortcuts import render

class VoteApp(APIView):
	def get(self, request):
		return render(request, 'voter_page.html')

	def post(self, request):
		voted_fruit = request.data['fruit']
		return render(request, 'voted_page.html', {'data': voted_fruit})