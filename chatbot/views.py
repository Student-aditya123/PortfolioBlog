from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_chatbot_response


@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")

            bot_reply = get_chatbot_response(user_message)

            return JsonResponse({
                "response": bot_reply
            })

        except Exception as e:
            return JsonResponse({
                "response": "Error processing request"
            })

    return JsonResponse({"response": "Invalid request"})