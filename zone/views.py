from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from zone.models import CustomerAdvertise, CustomerAdvertise2, Document
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#from zone.models import Document
from zone.forms import DocumentForm
# Create your views here.

def homepage(request):
  return render_to_response("homepage.html",context_instance=RequestContext(request)) 

def homesearch(request):
  try:
    search_txt = request.POST["adtitle"]
    print search_txt
#    a = CustomerAdvertise2.objects.all()
    search_res = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(item_desc__contains=search_txt)
    temp1 = []
    for x in search_res:

      photosearch_res = Document.objects.values_list('docfile').filter(item_id__exact=x[0])  

      y = tuple(photosearch_res)
      x = x + y
      temp1.append(x)
#    documents = Document.objects.values_list('docfile', 'item_id').filter(item_id__exact=13)
    return render_to_response("searchhome.html", {"search_res":search_res, "search_txt":search_txt, "temp1":temp1}, context_instance=RequestContext(request))
  except KeyError:
#  else:
    return HttpResponseRedirect("/")
    


def postadv(request):
#  if request.method == 'POST':
#    form = DocumentForm(request.POST, request.FILES)
#    if form.is_valid():
#      newdoc = Document(docfile = request.FILES['docfile'])
#      newdoc.save()

            # Redirect to the document list after POST
#      return HttpResponseRedirect(reverse('zone.views.postadv'))
#    pass
#  else:
  form = DocumentForm() # A empty, unbound form
#  documents = Document.objects.all()
  return render_to_response("postform.html", {"form":form}, context_instance=RequestContext(request))

def postsuccess(request):
  try:
    postitem = CustomerAdvertise2(item_cat=request.POST["select1"], item_subcat=request.POST["select2"], item_name=request.POST["prod_name"], item_desc=request.POST["description"], item_price=request.POST["text9"], item_price_per=request.POST["select10"], item_sec_dep=request.POST["text13"], item_tandc=request.POST["tandc"], item_owner_type=request.POST["select20"], item_owner_name=request.POST["text21"], item_owner_email=request.POST["email22"], item_mobile_num=request.POST["tel23"], state=request.POST["select24"], city=request.POST["select25"], locality=request.POST["select26"])
    postitem.save()
    maintable_id = postitem.id
    form = DocumentForm(request.POST, request.FILES)
    

    newdoc = Document(docfile = request.FILES['docfile'], item_id = maintable_id )
    newdoc.save() 
    return HttpResponseRedirect("/")

#        return HttpResposeRedirect
#  return render_to_response("postsuccess.html", {"a":a, "b":b, "c":c}, context_instance=RequestContext(request))
  except KeyError:
#        postitem = CustomerAdvertise2(item_cat=request.POST["select1"], item_subcat=request.POST["select2"], item_name=request.POST["prod_name"], item_desc=request.POST["description"], item_price=request.POST["text9"], item_price_per=request.POST["select10"], item_sec_dep=request.POST["text13"], item_tandc=request.POST["tandc"], item_owner_type=request.POST["select20"], item_owner_name=request.POST["text21"], item_owner_email=request.POST["email22"], item_mobile_num=request.POST["tel23"], state=request.POST["select24"], city=request.POST["select25"], locality=request.POST["select26"])
#    postitem.save()
    return HttpResponseRedirect("/")

def searchfilter(request, search_txt):
  try:  
    filter_radio = request.POST["indibizfilter"]
    filter_result = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(item_owner_type__contains=filter_radio, item_desc__contains=search_txt)
    
    temp2 = []
   
    for p in filter_result:

      photosearchfilter_res = Document.objects.values_list('docfile').filter(item_id__exact=p[0])

      q = tuple(photosearchfilter_res)
      p = p + q
      temp2.append(p)
#    documents = Document.objects.values_list('docfile', 'item_id').filter(item_id__exact=13)
#    return render_to_response("searchhome.html", {"search_res":search_res, "search_txt":search_txt, "temp1":temp1}, context_instance=RequestContext(request))
    return render_to_response("filtersuccess.html", {"filter_result":filter_result, "filter_radio":filter_radio, "search_txt":search_txt, "temp2":temp2}, context_instance=RequestContext(request))
  except KeyError:
#  else:
    return HttpResponseRedirect("/")

