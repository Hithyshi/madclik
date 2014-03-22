from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from zone.models import CustomerAdvertise, CustomerAdvertise2
from django.http import HttpResponseRedirect
# Create your views here.

def homepage(request):
  return render_to_response("homepage.html",context_instance=RequestContext(request)) 

def homesearch(request):
  try:
#  if request.META.HTTP_REFERER == "http://localhost:5000/zone/ or 
    search_txt = request.POST["adtitle"]
#  if search_txt:
    print search_txt
    search_res = CustomerAdvertise2.objects.values_list('item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(item_desc__contains=search_txt)
#  res_list = list(search_res)
    return render_to_response("searchhome.html", {"search_res":search_res, "search_txt":search_txt}, context_instance=RequestContext(request))
  except KeyError:
#  else:
    return HttpResponseRedirect("/")
    


def postadv(request):
  return render_to_response("postform.html",context_instance=RequestContext(request))

def postsuccess(request):
#  a = request.POST["select1"]
#  b = request.POST["select2"]
#  c = request.POST["prod_name"]
  postitem = CustomerAdvertise2(item_cat=request.POST["select1"], item_subcat=request.POST["select2"], item_name=request.POST["prod_name"], item_desc=request.POST["description"], item_price=request.POST["text9"], item_price_per=request.POST["select10"], item_sec_dep=request.POST["text13"], item_tandc=request.POST["tandc"], item_owner_type=request.POST["select20"], item_owner_name=request.POST["text21"], item_owner_email=request.POST["email22"], item_mobile_num=request.POST["tel23"], state=request.POST["select24"], city=request.POST["select25"], locality=request.POST["select26"])
  postitem.save() 
  return HttpResponseRedirect("/")
#  return render_to_response("postsuccess.html", {"a":a, "b":b, "c":c}, context_instance=RequestContext(request))

def searchfilter(request, search_txt):
  filter_radio = request.POST["indibizfilter"]
  filter_result = CustomerAdvertise2.objects.values_list('item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(item_owner_type__contains=filter_radio, item_desc__contains=search_txt)
  return render_to_response("filtersuccess.html", {"filter_result":filter_result, "filter_radio":filter_radio, "search_txt":search_txt}, context_instance=RequestContext(request))

#def iframetesting(request):
#  return render_to_response("index.html",context_instance=RequestContext(request))

