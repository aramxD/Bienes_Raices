from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.urls import reverse
from django.db import IntegrityError
from team.models import Asesor
from paginas.models import *
from .models import *
from .forms import *


# Create your views here.
def home(request):
    paginas = Pagina.objects.all()
    casas = Casa.objects.all()
    casa_landing = casas.filter(featured=True)

    departamentos = Departamentos.objects.all()
    depa_landing = departamentos.filter(featured=True)

    comercio = Comercio.objects.all()
    comercio_landing = comercio.filter(featured=True)

    terreno = Terreno.objects.all()
    terreno_landing = terreno.filter(featured=True)

    
    context = {
        'paginas':paginas,
        'casas' : casa_landing,
        'departamentos' : depa_landing,
        'comercio' : comercio_landing,
        'terreno' : terreno_landing,
    }
    return render(request, 'home.html', context)


def listado(request):
    casas = Casa.objects.all()
    departamentos = Departamentos.objects.all()
    comercio = Comercio.objects.all()
    terreno = Terreno.objects.all()
    
    context = {
        'casas' : casas,
        'departamentos' : departamentos,
        'comercio' : comercio,
        'terreno' : terreno,
    }
    return render(request, 'listado.html', context)


def detalles_casa(request, casa_id):
    paginas = Pagina.objects.all()
    detalles = get_object_or_404(Casa, pk=casa_id)
    queryfotos = CasaImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=detalles)
    
    if request.method == 'POST':
        agendar_cita = CitasForms(request.POST)
        if agendar_cita.is_valid():
            asesor = agendar_cita.save(commit=False)
            asesor.asesor = request.POST.get('vendedor', detalles.vendedor)
            asesor.save()
            note = 'Nos comunicaremos pronto contigo'

            
            #Correo Variables
            nombre_completo = request.POST.get('nombre_completo','')
            email = request.POST.get('email','')
            telefono = request.POST.get('telefono','')
            asesor = request.POST.get('vendedor', detalles.vendedor)
            asesor_email = asesor.email

            #Correo para asesor
            asesor_mail = EmailMessage(
                "{0} hay un nuevo contacto".format(asesor ),#asunto
                "Se llama {0} \n su correo es: {1}  \n Marcale al: {2}".format(nombre_completo, email, telefono), #mensaje
                "bimcapacitacion@gmail.com", #email de origen
                [asesor_email], #email destino
                reply_to=[email],
            )



            nueva_cita = CitasForms()

            context = {
            'paginas':paginas,
            'note':note,
            'nueva_cita':nueva_cita,
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
            try:
                #bienvenida_mail.send()  #se envia correctamente
                asesor_mail.send()
                return render(request, 'detalles_casa.html', context)
            except: #salio mal
                return render(request, 'detalles_casa.html', context)

    else:
        nueva_cita = CitasForms()
        context = {
            'paginas':paginas,
            'detalles' : detalles,
            'nueva_cita':nueva_cita,
            'fotos_detalles' : fotos_detalles,
        }
        return render(request, 'detalles_casa.html', context)


def detalles_depa(request, depa_id):
    paginas = Pagina.objects.all()
    detalles = get_object_or_404(Departamentos, pk=depa_id)
    queryfotos = DepartamentosImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=detalles)

    if request.method == 'POST':
        agendar_cita = CitasForms(request.POST)
        if agendar_cita.is_valid():
            asesor = agendar_cita.save(commit=False)
            asesor.asesor = request.POST.get('vendedor', detalles.vendedor)
            asesor.save()
            note = 'Nos comunicaremos pronto contigo'
            nueva_cita = CitasForms()

            context = {
            'paginas':paginas,
            'note':note,
            'nueva_cita':nueva_cita,
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
            return render(request, 'detalles_depa.html', context)

    else:
        nueva_cita = CitasForms()
        context = {
                'paginas':paginas,
                'detalles' : detalles,
                'nueva_cita':nueva_cita,
                'fotos_detalles' : fotos_detalles,
            }
        return render(request, 'detalles_depa.html', context)


def detalles_comercio(request, comercio_id):
    paginas = Pagina.objects.all()
    detalles = get_object_or_404(Comercio, pk=comercio_id)
    queryfotos = ComercioImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=detalles)

    if request.method == 'POST':
        agendar_cita = CitasForms(request.POST)
        if agendar_cita.is_valid():
            asesor = agendar_cita.save(commit=False)
            asesor.asesor = request.POST.get('vendedor', detalles.vendedor)
            asesor.save()
            note = 'Nos comunicaremos pronto contigo'
            nueva_cita = CitasForms()

            context = {
            'paginas':paginas,
            'note':note,
            'nueva_cita':nueva_cita,
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
            return render(request, 'detalles_comercio.html', context)

    else:
        nueva_cita = CitasForms()
        context = {
                'paginas':paginas,
                'detalles' : detalles,
                'nueva_cita':nueva_cita,
                'fotos_detalles' : fotos_detalles,
            }
        return render(request, 'detalles_comercio.html', context)


def detalles_terreno(request, terreno_id):
    paginas = Pagina.objects.all()
    detalles = get_object_or_404(Terreno, pk=terreno_id)
    queryfotos = TerrenoImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=detalles)

    if request.method == 'POST':
        agendar_cita = CitasForms(request.POST)
        if agendar_cita.is_valid():
            asesor = agendar_cita.save(commit=False)
            asesor.asesor = request.POST.get('vendedor', detalles.vendedor)
            asesor.save()
            note = 'Nos comunicaremos pronto contigo'
            nueva_cita = CitasForms()

            context = {
            'paginas':paginas,
            'note':note,
            'nueva_cita':nueva_cita,
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
            return render(request, 'detalles_comercio.html', context)

    else:
        nueva_cita = CitasForms()
        context = {
                'paginas':paginas,
                'detalles' : detalles,
                'nueva_cita':nueva_cita,
                'fotos_detalles' : fotos_detalles,
            }
        return render(request, 'detalles_terreno.html', context)

#CASAS
def ingreso_casa(request):
    if request.method == 'POST':
        alta_casa = CasaForms(request.POST, request.FILES)
        if alta_casa.is_valid():
            casa = alta_casa.save()

            context = {
            'form':CasaForms(),
            }
            return redirect("listado")
            
    else:

        context = {
            'form':CasaForms(),
            }
        return render(request, 'ingreso_casa.html', context)


def editar_casa(request, casa_pk): 
    casa = get_object_or_404(Casa, pk=casa_pk)
    queryfotos = CasaImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=casa)
    

    if request.method == 'GET':
        form = CasaForms(instance = casa)
        context = {
            'fotos_detalles':fotos_detalles,
            'casa' : casa,
            'form' : form,
            
        } 
        return render(request, 'editar_casa.html', context)
    else:
        try:
            form = CasaForms(request.POST, request.FILES, instance=casa)
            form.save()
            return redirect("listado")
            
        except ValueError:
            context = {
                'fotos_detalles':fotos_detalles,
                'casa' : casa,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...',
                
            }
            return render(request, 'editar_casa.html', context)


def ingreso_casa_foto(request):
    pass

def eliminar_casa(request, casa_pk):
    casa = get_object_or_404(Casa, pk=casa_pk)
    if request.method == 'POST':
        casa.delete()
        return redirect('listado') 


def eliminar_casa_fotos(request, foto_pk):
    fotos = get_object_or_404(CasaImagen, pk=foto_pk)
    if request.method == 'POST':
        fotos.delete()
        return redirect('listado')   

        
#DEPAS
def ingreso_depa(request):
    if request.method == 'POST':
        alta_depa = DepaForms(request.POST, request.FILES)
        if alta_depa.is_valid():
            depa = alta_depa.save()
            context = {
            'form':DepaForms(),
            }
            return redirect("listado")
            
    else:

        context = {
            'form':DepaForms(),
            }
        return render(request, 'ingreso_depa.html', context)


def editar_depa(request, depa_pk):
    depa = get_object_or_404(Departamentos, pk=depa_pk)
    
    if request.method == 'GET':
        form = DepaForms(instance = depa)
        context = {
            'depa' : depa,
            'form' : form,
        } 
        return render(request, 'editar_depa.html', context)
    else:
        try:
            form = DepaForms(request.POST, request.FILES, instance=depa)
            form.save()
            return redirect("listado")
            
        except ValueError:
            context = {
                'depa' : depa,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...'
            }
            return render(request, 'editar_depa.html', context)


def eliminar_depa(request, depa_pk):
    depa = get_object_or_404(Departamentos, pk=depa_pk)
    if request.method == 'POST':
        depa.delete()
        return redirect('listado') 



#COMERCIO
def ingreso_comercio(request):
    if request.method == 'POST':
        alta_comercio = ComercioForms(request.POST, request.FILES)
        if alta_comercio.is_valid():
            try:
                comercio = alta_comercio.save()
                context = {
                'form':ComercioForms(),
                }
                return redirect("listado")
            except IntegrityError:
                context = {
                'error':'Error de datos',
                'form':ComercioForms(),
                }
                return render(request, 'ingreso_comercio.html', context)
    else:

        context = {
            'form':ComercioForms(),
            }
        return render(request, 'ingreso_comercio.html', context)


def editar_comercio(request, comercio_pk):
    comercio = get_object_or_404(Comercio, pk=comercio_pk)
    
    if request.method == 'GET':
        form = ComercioForms(instance = comercio)
        context = {
            'comercio' : comercio,
            'form' : form,
        } 
        return render(request, 'editar_comercio.html', context)
    else:
        try:
            form = ComercioForms(request.POST, request.FILES, instance=comercio)
            form.save()
            return redirect("listado")
            
        except ValueError:
            context = {
                'comercio' : comercio,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...'
            }
            return render(request, 'editar_comercio.html', context)


def eliminar_comercio(request, comercio_pk):
    comercio = get_object_or_404(Comercio, pk=comercio_pk)
    if request.method == 'POST':
        comercio.delete()
        return redirect('listado') 

#TERRENOS
def ingreso_terreno(request):
    if request.method == 'POST':
        alta_terreno = TerrenoForms(request.POST, request.FILES)
        if alta_terreno.is_valid():
            try:
                terreno = alta_terreno.save()
                context = {
                'form':TerrenoForms(),
                }
                return redirect("listado")
            except IntegrityError:
                context = {
                'error':'Error de datos',
                'form':TerrenoForms(),
                }
                return render(request, 'ingreso_terreno.html', context)
    else:

        context = {
            'form':TerrenoForms(),
            }
        return render(request, 'ingreso_terreno.html', context)


def editar_terreno(request, terreno_pk):
    terreno = get_object_or_404(Terreno, pk=terreno_pk)
    
    if request.method == 'GET':
        form = TerrenoForms(instance = terreno)
        context = {
            'terreno' : terreno,
            'form' : form,
        } 
        return render(request, 'editar_terreno.html', context)
    else:
        try:
            form = TerrenoForms(request.POST, request.FILES, instance=terreno)
            form.save()
            return redirect("listado")
            
        except ValueError:
            context = {
                'comercio' : terreno,
                'form' : form,
                'error' : 'Reviza la informacion, algo esta mal...'
            }
            return render(request, 'editar_terreno.html', context)


def eliminar_terreno(request, terreno_pk):
    terreno = get_object_or_404(Terreno, pk=terreno_pk)
    if request.method == 'POST':
        terreno.delete()
        return redirect('listado') 



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

from django.views import View

def render_pdf_view(request, casa_id):
    template_path = 'detalles_casa_pdf.html'
    detalles = get_object_or_404(Casa, pk=casa_id)
    queryfotos = CasaImagen.objects.all()
    fotos_detalles = queryfotos.filter(casa=detalles)

    context = {
            'detalles' : detalles,
            'fotos_detalles' : fotos_detalles,
            }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #La siguiente linea es para que el documento se descargue
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response )
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

    
data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",     
    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
    }

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index(request):
	context = {}
	return render(request, 'app/index.html', context)