from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Item

@csrf_exempt  # ✅ Disable CSRF for API (only needed for testing)
def item_list(request):
    response = JsonResponse({'items': list(Item.objects.values())})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # ✅ Manually set CORS header
    return response
