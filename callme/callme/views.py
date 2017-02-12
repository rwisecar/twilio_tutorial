from twilio import twiml
from django.shortcuts import render


def voice_view(request):
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    if request.method == 'GET' or request.method == 'POST':
        city = request.values['FromCity']

        # Start our TwiML response
        resp = twiml.Response()

        # Read a message aloud to the caller
        resp.say('Never gonna give you up, {}!'.format(city), voice='alice')

        # Play an audio file for the caller
        resp.play('https://demo.twilio.com/docs/classic.mp3')

    return render(request, {})
