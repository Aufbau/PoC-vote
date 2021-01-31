import random
from django.shortcuts import render
from rest_framework.views import APIView
from redis import Redis
import json

class VoteApp(APIView):
    def get(self, request):
        return render(request, 'voter_page.html')

    def post(self, request):
        r = Redis(host="super-redis", port=6379)
        voted_fruit = request.data['fruit']
        data = json.dumps({'client_id': str(random.randint(100, 1000000)), 'vote_option': voted_fruit})
        r.rpush('votes', data)
        return render(request, 'voted_page.html', {'data': voted_fruit})