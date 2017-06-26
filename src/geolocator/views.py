from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from locations.models import Location

from .functions import foursquare_search, find_city_lat_lng locu_search,


def home(request):
	context = {}
	context.update(csrf(request))

	if request.method == 'POST':
		print request.POST
		query = request.POST['search']

		try:
			lat = request.POST['lat']
			lng = request.POST['lng']
			local_query = find_city_lat_lng(lat, lng)
			if query == '':
				query = local_query
		except:
			pass

		# Option 1: Locu Search
		locations = locu_search(query)
		for loc in locations:
			name, locu_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, locu_id=locu_id)
			if created:
				print "Created new id for %s with locu id of %s" % (name, locu_id)

		# Option 2: Foursquare Search
		locations = foursquare_search(query)
		for loc in locations:
			name, four_id = loc[0], loc[1]
			new_location, created = Location.objects.get_or_create(name=name, four_id=four_id)
			if created:
				print "Created new id for %s with foursquare id of %s" % (name, four_id)
	

		context['query'] = query
		context['locations'] = locations

	return render_to_response('home.html', context)
