import random
from django.shortcuts import render
from rest_framework.views import APIView
from redis import Redis
import json
import logging
from .forms import VoteForm

logging.basicConfig(level=logging.INFO)

r = Redis(host="super-redis", port=6379)
logging.info("Vote app connected to super-redis ...")

form = VoteForm()

class VoteApp(APIView):

    def get(self, request):

        if request.session.session_key is None:
            return render(request, 'voter_page.html', {'form': form})
            
        logging.info('session_key: {}'.format(request.session.session_key))
        return render(request, 'voter_page.html', {'data': request.session['vote_option'],'form': form})
     
    def post(self, request):

        voted_fruit = request.data['fruit']
        validity = form.validate_input(voted_fruit)

        if request.session.session_key is None and validity:
            request.session.create()
            logging.info('session_key: {}'.format(request.session.session_key))
        
        if validity:
            request.session['vote_option'] = voted_fruit
            data = json.dumps({'client_id': request.session.session_key, 'vote_option': voted_fruit})
            r.rpush('votes', data)
            return render(request, 'voted_page.html', {'data': voted_fruit})

        return render(request, 'voted_page.html')
