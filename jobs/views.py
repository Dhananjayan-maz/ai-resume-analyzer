import os
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def recommend_jobs(request):

    role = request.GET.get("role")

    if not role:
        return Response({"error": "Role is required"}, status=400)

    url = "https://jsearch.p.rapidapi.com/search-v2"

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
        "X-RapidAPI-Host": os.getenv("RAPID_API_HOST"),
    }

    params = {
        "query": role,
        "page": "1",
        "num_pages": "1",
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return Response(response.json())