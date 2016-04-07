from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import UploadFileForm
from .models import ContactList
import csv

def csv_upload(request):
    if request.method == 'POST':
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
            parse_csv(request.FILES['file'])
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form}, context_instance=RequestContext(request))

def delete_records(request):
    if request.method == 'POST':
	checked_records = request.POST.getlist('checked')
	for record in checked_records:
	    to_delete = ContactList.objects.get(pk=int(record))
	    to_delete.delete()
	return HttpResponseRedirect('/success')

class SuccessView(ListView):
    template_name="success.html"
    def get_queryset(self):
    	return ContactList.get_contacts()

def parse_csv(csv_file):
            reader = csv.DictReader(csv_file)
	    for row in reader:
	    	name = row['name']
		address1 = row['address1']
		city = row['city']
		state = row['state']
		postal_code = row['postal_code']
		country = row['country']
		phone_number = row['phone_number']
		obj = ContactList(name=name, address1=address1, city=city, state=state, postal_code=postal_code, country=country, phone_number=phone_number)
		obj.save()
