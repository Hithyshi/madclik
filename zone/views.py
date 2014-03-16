from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from zone.models import CustomerAdvertise
# Create your views here.

def homepage(request):
  return render_to_response("homepage.html",context_instance=RequestContext(request)) 

def homesearch(request):
  search_txt = request.POST["adtitle"]
  print search_txt
  search_res = CustomerAdvertise.objects.filter(description__contains=search_txt)
  res_list = list(search_res)
  return render_to_response("searchhome.html", {"res_list":res_list}, context_instance=RequestContext(request))
