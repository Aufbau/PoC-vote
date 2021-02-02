import random
from django.shortcuts import render
from rest_framework.views import APIView
from redis import Redis
import json
import logging

logging.basicConfig(level=logging.INFO)

r = Redis(host="super-redis", port=6379)
logging.info("Connected to super-redis ...")

class VoteApp(APIView):

    def get(self, request):
        if request.session.session_key is None:
            request.session.create()
        logging.info('session_key: {}'.format(request.session.session_key))
        return render(request, 'voter_page.html')

    def post(self, request):
        voted_fruit = request.data['fruit']
        data = json.dumps({'client_id': request.session.session_key, 'vote_option': voted_fruit})
        r.rpush('votes', data)
        return render(request, 'voted_page.html', {'data': voted_fruit})