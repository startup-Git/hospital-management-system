from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Home.models import ChooseU, ShortAbout, CounterSection
from About.models import MissionVission, AboutDescription, AboutDescriptionAside

# Create your views here.
def about(request):
    template = loader.get_template('AboutUS.html')
    about = ShortAbout.objects.all()
    counter = CounterSection.objects.all()
    chooseUS = ChooseU.objects.all()
    missionVission = MissionVission.objects.all()
    AboutDesc = AboutDescription.objects.all()
    AboutAside = AboutDescriptionAside.objects.all()
    data = {
        'about': about,
        'counter': counter,
        'chooseUS': chooseUS,
        'missionVission': missionVission,
        'AboutDesc': AboutDesc,
        'AboutAside': AboutAside,
    }
    return HttpResponse(template.render(data, request))
