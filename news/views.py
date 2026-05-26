import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

API_KEY = "37c57f995f1f4cc78a868ce2657d086b"

@api_view(['GET'])
def get_news(request):
    category = request.GET.get("category")
    search = request.GET.get("search")

    if search:
        url = f"https://newsapi.org/v2/everything?q={search}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    elif category and category != "all":
        url = f"https://newsapi.org/v2/everything?q=india {category}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    else:
        url = f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    return Response(data)


@api_view(['GET'])
def refresh_news(request):
    return Response({"message": "News refreshed"})