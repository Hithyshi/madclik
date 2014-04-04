from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from zone.models import CustomerAdvertise, CustomerAdvertise2, Document, PhotoUrl
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
#from zone.models import Document, PhotoUrl
from zone.forms import DocumentForm, UploadForm
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings
import mimetypes
from datetime import datetime

# Create your views here.

def homepage(request):
  return render_to_response("homepage.html",context_instance=RequestContext(request)) 


def homesearch(request):
  try:
    search_txt = request.POST["adtitle"]
    print search_txt
#    a = CustomerAdvertise2.objects.all()
    search_res = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(Q(item_desc__icontains=search_txt) | Q(item_name__icontains=search_txt))
    temp1 = []
    for x in search_res:

#valid      photosearch_res = Document.objects.values_list('docfile').filter(item_id__exact=x[0])  
      photosearch_res = PhotoUrl.objects.values_list('url').filter(item_id__exact=x[0])

      y = tuple(photosearch_res)
      x = x + y
      temp1.append(x)
#    documents = Document.objects.values_list('docfile', 'item_id').filter(item_id__exact=13)
    temp2 = []
    split_words_list = []
    search_res2 = []
    if " " in search_txt:
      split_words_list = search_txt.split(" ")
      ignore_words = ['rent', 'renting', 'for', 'to', 'available', 'is', 'was', 'on', 'in', 'with', 'and', 'but', 'without', 'a', 'an', 'are', 'want', 'go']
#      temp2 = []
      for i in split_words_list:
        if not i in ignore_words:
          search_res2 = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(Q(item_desc__icontains=i) | Q(item_name__icontains=i))
       
        for j in search_res2:
          photosearch_res2 = PhotoUrl.objects.values_list('url').filter(item_id__exact=j[0])
          k = tuple(photosearch_res2)
          j = j + k
          temp2.append(j)
    temp3 = temp1 + temp2
    temp4 = list(set(temp3))
    return render_to_response("searchhome.html", {"search_res":search_res, "search_txt":search_txt, "search_res2":search_res2,  "split_words_list":split_words_list, "temp1":temp1, "temp4":temp4}, context_instance=RequestContext(request))
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
#valid  form = DocumentForm() # A empty, unbound form
#  documents = Document.objects.all()
#valid  return render_to_response("postform.html", {"form":form}, context_instance=RequestContext(request))
  f = UploadForm()
  return render_to_response("postform.html", {"form":f}, context_instance=RequestContext(request))

def postsuccess(request):
  try:
    def store_in_s3(filename, content):
      conn = S3Connection(settings.ACCESS_KEY, settings.PASS_KEY)
      b = conn.create_bucket("remt-estu")
      mime = mimetypes.guess_type(filename)[0]
      k = Key(b)
      k.key = filename
      k.set_metadata("Content-Type", mime)
      k.set_contents_from_string(content)
      k.set_acl("public-read")
  
    postitem = CustomerAdvertise2(item_cat=request.POST["select1"], item_subcat=request.POST["select2"], item_name=request.POST["prod_name"], item_desc=request.POST["description"], item_price=request.POST["text9"], item_price_per=request.POST["select10"], item_sec_dep=request.POST["text13"], item_tandc=request.POST["tandc"], item_owner_type=request.POST["select20"], item_owner_name=request.POST["text21"], item_owner_email=request.POST["email22"], item_mobile_num=request.POST["tel23"], state=request.POST["select24"], city=request.POST["select25"], locality=request.POST["select26"])
    postitem.save()
    maintable_id = postitem.id
#valid    form = DocumentForm(request.POST, request.FILES)
    

#valid    newdoc = Document(docfile = request.FILES['docfile'], item_id = maintable_id )
#valid    newdoc.save() 
    f = UploadForm(request.POST, request.FILES)
    file = request.FILES["file"]
    for filename, file in request.FILES.iteritems():
      name = request.FILES[filename].name
    temp8 = name.split(".")
    a = datetime.now()
    b = str(a.year) + str(a.month) + str(a.day) + str(a.hour) + str(a.minute) + str(a.second)  
    filename = b + "." + temp8[1]
    content = file.read()
    store_in_s3(filename, content)
    p = PhotoUrl(url="https://s3.amazonaws.com/remt-estu/" + filename, item_id=maintable_id)
    p.save()
    return HttpResponseRedirect("/")

#        return HttpResposeRedirect
#  return render_to_response("postsuccess.html", {"a":a, "b":b, "c":c}, context_instance=RequestContext(request))
  except KeyError:
#        postitem = CustomerAdvertise2(item_cat=request.POST["select1"], item_subcat=request.POST["select2"], item_name=request.POST["prod_name"], item_desc=request.POST["description"], item_price=request.POST["text9"], item_price_per=request.POST["select10"], item_sec_dep=request.POST["text13"], item_tandc=request.POST["tandc"], item_owner_type=request.POST["select20"], item_owner_name=request.POST["text21"], item_owner_email=request.POST["email22"], item_mobile_num=request.POST["tel23"], state=request.POST["select24"], city=request.POST["select25"], locality=request.POST["select26"])
#    postitem.save()
    return HttpResponseRedirect("/")

def searchfilter(request, search_txt):
  try:
#    if search_txt != '':  
    filter_radio = request.POST["indibizfilter"]
    filter_result = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(Q(item_owner_type__contains=filter_radio), Q(item_desc__icontains=search_txt) | Q(item_name__icontains=search_txt))
    
    temp6 = []
   
    for p in filter_result:

      photosearchfilter_res = PhotoUrl.objects.values_list('url').filter(item_id__exact=p[0])

      q = tuple(photosearchfilter_res)
      p = p + q
      temp6.append(p)
#    documents = Document.objects.values_list('docfile', 'item_id').filter(item_id__exact=13)
#    return render_to_response("searchhome.html", {"search_res":search_res, "search_txt":search_txt, "temp1":temp1}, context_instance=RequestContext(request))

    temp5 = []
    split_words_list2 = []
    search_res2 = []
    if " " in search_txt:
      split_words_list2 = search_txt.split(" ")
      ignore_words = ['rent', 'renting', 'for', 'to', 'available', 'is', 'was', 'on', 'in', 'with', 'and', 'but', 'without', 'a', 'an', 'are', 'want', 'go']
#      temp5 = []
      for i in split_words_list2:
        if not i in ignore_words:
          search_res2 = CustomerAdvertise2.objects.values_list('id', 'item_cat', 'item_subcat', 'item_name', 'item_desc', 'item_price', 'item_price_per', 'item_sec_dep', 'item_tandc', 'item_owner_type', 'item_owner_name', 'item_owner_email', 'item_mobile_num', 'state', 'city', 'locality').filter(Q(item_owner_type__contains=filter_radio), Q(item_desc__icontains=i) | Q(item_name__icontains=i))

        for j in search_res2:
          photosearch_res2 = PhotoUrl.objects.values_list('url').filter(item_id__exact=j[0])
          k = tuple(photosearch_res2)
          j = j + k
          temp5.append(j)
    temp7 = temp6 + temp5
    temp8 = list(set(temp7))

    return render_to_response("filtersuccess.html", {"filter_result":filter_result, "filter_radio":filter_radio, "search_txt":search_txt, "temp6":temp6, "temp8":temp8}, context_instance=RequestContext(request))
#    else:
#      pass
  except KeyError:
#  else:
    return HttpResponseRedirect("/")


def contactus(request):
  return render_to_response("ContactUs.html",context_instance=RequestContext(request))

