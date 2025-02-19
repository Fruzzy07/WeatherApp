import requests
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import City, Weather
from .serializers import WeatherSerializer

class WeatherView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.city:
            return Response({"error": "Город не указан"}, status=400)

        city = user.city
        weather = Weather.objects.filter(city=city).first()

        if weather and (now() - weather.updated_at).seconds < 600:
            serializer = WeatherSerializer(weather)
            return Response(serializer.data)

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather',
                                params={'q': city.name, 'appid': 'd5c4914c01efc474714dabaef73ab79a', 'units': 'metric'})
        if response.status_code == 200:
            data = response.json()
            weather, _ = Weather.objects.update_or_create(
                city=city,
                defaults={'temperature': data['main']['temp'], 'description': data['weather'][0]['description']}
            )
            serializer = WeatherSerializer(weather)
            return Response(serializer.data)

        return Response({"error": "Не удалось получить данные"}, status=400)
