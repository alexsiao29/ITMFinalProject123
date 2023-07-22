from datetime import date
from django.shortcuts import render
from .models import Tables
from .models import Occupancy
from .forms import OccupancyForm
# Create your views here.

all_cafs = [
  {
    "slug": "ebais",
    "title": "Ebai's",
    "image": "ebais.jpeg",
    "menu": "jolly1.png",
    "tables": "floorplan_ebais.png",
    "description": "Ebai's Canteen",
    "availability": {
    "table1": [],
    "table2": [],
    "table3": [],
    "table4": [],
    "table5": [],
    "table6": [],
  },
  },
  {
    "slug": "gonzaga",
    "title": "Gonzaga",
    "image": "blueandgold.png",
    "menu": "jolly1.png",
    "tables": "floorplan_Gonzaga.png",
    "description": "Gonzaga food cafeteria",
    "availability": {
    "table1": [],
    "table2": [],
    "table3": [],
    "table4": [],
    "table5": [],
    "table6": []
  },
  },
  {
    "slug": "iggys",
    "title": "Iggys",
    "image": "iggys.png",
    "menu": "jolly1.png",
    "tables": "floorplan_Iggys.png",
    "description": "Iggy's Food Hub.",
    "availability": 
    {
    "table1": [],
    "table2": [],
    "table3": [],
    "table4": [],
    "table5": [],
    "table6": [],
    "table7": [],
    "table8": [],
    "table9": [],
    "table10": [],
    "table11": [],
    "table12": []
  },
  },
  {
    "slug": "irh-kravers",
    "title": "IRH",
    "image": "kravers.png",
    "menu": "jolly1.png",
    "tables": "floorplan_IRH.png",
    "description": "Kraver's canteen in the IRH food hall.",
  "availability": {
    "table1": [],
    "table2": [],
    "table3": [],
    "table4": [],
    "table5": [],
    "table6": [],
    "table7": [],
    "table8": []
  },
},
  {
    "slug": "jsec",
    "title": "JSEC",
    "image": "jsec.png",
    "menu": "jolly1.png",
    "tables": "floorplan_jsec.png",
    "description": "JGSOM Student Enterprise Center.",
    "availability": {
    "table1": [],
    "table2": [],
    "table3": [],
    "table4": [],
    "table5": [],
    "table6": [],
    "table7": [],
    "table8": [],
    "table9": [],
    "table10": [],
    "table11": [],
    "table12": []
  },
  },
]

def get_name(caf):
  return caf['title']

def starting_page(request):
  sorted_products = sorted(all_cafs, key=get_name)
  return render(request, "store/index.html", {
    "cafs": sorted_products
  })

def cafs(request):
  return render(request, "store/all_cafs.html", {
    "all_cafs": all_cafs
  })

def caf_detail(request, slug):
  identified_caf = next(caf for caf in all_cafs if caf['slug'] == slug)
  return render(request, "store/caf_detail.html", {
    "caf": identified_caf
  })

def table_detail(request, slug):
  identified_caf = next(caf for caf in all_cafs if caf['slug'] == slug)
  return render(request, "store/tables.html", {
    "caf": identified_caf
  })

def tables(request):
	tables = Tables.objects.all()
	return render(request, "store/tables.html", {
      'tables':tables
  })
  
  
def occupancy(request):
    if request.method == 'POST':
        form = OccupancyForm(request.POST) 
        if form.is_valid():
            form.save() 
            return render(request, "store/tables.html", {'form': form})
    else:
        form = OccupancyForm()
    return render(request, "store/tables.html", {'form': form})

def look(table,canteen,canteen2):
    #TABLE: TABLE user is occupying
    #CANTEEN: The CANTEEN where user occupied TABLE
    #CANTEEN2: User is asking for available tables in CANTEEN2

    #When user marks their spot in a table
    canteen[table].append('Unavailable')

    #When user asks for available tables
    make_keys=list(canteen2.keys())
    for num in make_keys:
        if canteen2[num]==[]:
            print(num) 

    #If User inputs that they've left the canteen already; makes it available
    canteen[table].remove('Unavailable') 
    #just printed the dictionary to verify na 'Unavailable' was removed
    print(canteen)