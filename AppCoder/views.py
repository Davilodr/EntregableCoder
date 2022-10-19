from django.shortcuts import render
from AppCoder.models import Datos_Familiar
from django.http import HttpResponse

# Create your views here.

def Familiar(request, Nombre, Apellido, Edad, Fecha_Carga):
    
    Familiar = Datos_Familiar(Nombre = Nombre, Apellido = Apellido, Edad = Edad, Fecha_Carga = Fecha_Carga)
    Familiar.save()

    return HttpResponse(f"""
    <p>Familiar: {Familiar.Nombre} - {Familiar.Apellido} - {Familiar.Edad} - {Familiar.Fecha_Carga} </p>
    - Agregado
    """)
    
def Lista_Familiar(request):
    
    lista = Datos_Familiar.objects.all()
  
    return render(request, "ListaFamiliar.html",{"ListaFamiliar": lista})
    
        
