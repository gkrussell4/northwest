from django.shortcuts import render
from django.http import HttpResponse

from .models import Airport, Flight

# Create your views here.
# request handler


def say_hello(request):
    # can do whatever in here like data from db
    return HttpResponse("NORTHWEST UNDER CONSTRUCTION")


def search(request):
    if request.method == 'GET': 
        airports = Airport.objects.all()
        return render(request, 'search.html', {'airports': airports})

    if request.method == 'POST':
        '''depart_airport_code = request.POST['depart_airport']
        destination_airport_code = request.POST['destination_airport']
        departure_date = request.POST['departure_date']
        is_round = request.POST['roundtrip']
        return_date = request.POST.get('return_date', None)

        depart_airport = Airport.objects.get(code=depart_airport_code)
        destination_airport = Airport.objects.get(code=destination_airport_code)

        flights = Flight.objects.filter(
            depart_airport=depart_airport,
            destination_airport=destination_airport,
            departure_date=departure_date,
        )

        if is_round:
            return_flights = Flight.objects.filter(
                depart_airport=destination_airport,
                destination_airport=depart_airport,
                departure_date=request.POST['return_date'],
            )
        else:
            return_flights = None

        return render(request, 'northwest/flights_list.html', {
            'depart_airport': depart_airport,
            'destination_airport': destination_airport,
            'departure_date': departure_date,
            'return_date': return_date,
            'flights': flights,
            'return_flights': return_flights,
        })'''
        return render(request, 'flights_list.html')
        