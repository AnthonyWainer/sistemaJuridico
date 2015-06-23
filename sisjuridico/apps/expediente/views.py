from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.seguridad.models import permisos
from .forms import formCategoria, formExpediente, formHojadeEnvio, formResolucion, formExpedienteA, formHojadeEnvioU,formResolucionA
from .models import categoria, expedientes, hojaEnvio, accion, oficina, resolucion

# Crea tus vista aqui.
def permi(request,url):
    idp = request.user.idperfil_id
    mod = permisos.objects.filter(idmodulo__url=url, idperfil_id=idp).values('idmodulo__url','buscar','eliminar','editar','insertar','imprimir','ver')
    return mod

@login_required(login_url='/')
def registro_expediente(request):
    estado =  permi(request, "registro_expediente")
    listaCategoria = [{'id':con.id,'descripcion':con.descripcion} for con in categoria.objects.all()]
    listaResolucion = [{'id':con.id,'numero':con.numero} for con in resolucion.objects.all()]

    #print(request.POST)
    if request.method == 'POST': 
        idd = request.POST.get("id","")
        if idd == "undefined":
            idc = 1
            formu = formExpediente(request.POST,request.FILES )
            if formu.is_valid():
                formu.save()
        else:
            idc = request.POST.get("idc","")
        
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')    

        return render(request,'expediente/expediente/ajax_expediente.html',{'expediente':expediente,'n':'expedienteU','estado':estado})            
    else:
        idc= 1
        expediente = expedientes.objects.filter(idcategoria= idc).order_by('id')
        formu = formExpediente()
        #print (formu.as_p())

        return render(request,'expediente/expediente/expediente.html',{'formu':formu,'expediente':expediente, 'url':'registro_expediente/','n':'expedienteU','estado':estado,'idcategoria':listaCategoria, 'idresolucion':listaResolucion})

@login_required(login_url='/')
def actualizar_expediente(request):
    expediente = expedientes.objects.all().order_by('id')
    estado =  permi(request, "registro_expediente")
    if request.method == 'POST': 
        idp = request.POST.get("id","")
        a=get_object_or_404(expedientes,pk=idp)
        form=formExpedienteA(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'expediente/expediente/ajax_expediente.html',{'expediente':expediente,'n':'expedienteU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(expedientes,pk=idp)
        form= formExpedienteA(instance=a)
        return render(request,'expediente/modal.html',{'nombre':form,'url':'actualizar_expediente/','n':'expedienteU','u':'expedienteU','estado':estado})  

@login_required(login_url='/')
def eliminar_expediente(request):
    expediente = expedientes.objects.all().order_by('id')
    estado =  permi(request, "registro_expediente")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(expedientes,pk=idb).delete()
        return render(request,'expediente/expediente/ajax_expediente.html',{'expediente':expediente,'n':'expedienteU','estado':estado})     


@login_required(login_url='/')
def registro_hoja_envio(request):
    hojaEnvios = hojaEnvio.objects.all().order_by('id')
    estado =  permi(request, "registro_hoja_envio")
    listaAccion = [{'id':con.id,'accion':con.accion} for con in accion.objects.all()]
    listaOficina = [{'id':con.id,'oficina':con.oficina} for con in oficina.objects.all()]
    listaExpediente = [{'id':con.id,'nro': con.nro} for con in expedientes.objects.all()]

    if request.method == 'POST': 
        formH = formHojadeEnvio(request.POST,request.FILES )
        if formH.is_valid():
            formH.save()
        return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})            
    else:
        formH = formHojadeEnvio()
        return render(request,'expediente/hoja_envio/hoja_envio.html',{'formuH':formH,'hoja_envio':hojaEnvios, 'url':'registro_hoja_envio/','n':'hoja_envioU','estado':estado,'idaccion':listaAccion,'idoficina':listaOficina,'idexpediente':listaExpediente})

@login_required(login_url='/')
def actualizar_hoja_envio(request):
    hojaEnvios = hojaEnvio.objects.all().order_by('id')
    estado =  permi(request, "registro_hoja_envio")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(hojaEnvio,pk=idp)
        form=formHojadeEnvioU(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})            
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(hojaEnvio,pk=idp)
        form= formHojadeEnvioU(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_hoja_envio/','n':'hoja_envioU','u':'hoja_envioU','estado':estado})  

@login_required(login_url='/')
def eliminar_hoja_envio(request):
    hojaEnvios = hojaEnvio.objects.all().order_by('id')
    estado =  permi(request, "registro_hoja_envio")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(hojaEnvio,pk=idb).delete()
        return render(request,'expediente/hoja_envio/ajax_hoja_envio.html',{'hoja_envio':hojaEnvios,'n':'hoja_envioU','estado':estado})     


@login_required(login_url='/')
def registro_resolucion(request):
    resoluciones = resolucion.objects.all().order_by('id')
    estado =  permi(request, "registro_resolucion")

    if request.method == 'POST': 
        formH = formResolucion(request.POST,request.FILES )
        print (formH)
        if formH.is_valid():
            formH.save()
        return render(request,'expediente/resolucion/ajax_resolucion.html',{'resolucion':resoluciones,'n':'resolucionU','estado':estado})            
    else:
        formH = formResolucion()
        return render(request,'expediente/resolucion/resolucion.html',{'formuH':formH,'resolucion':resoluciones, 'url':'registro_resolucion/','n':'resolucionU','estado':estado})

@login_required(login_url='/')
def actualizar_resolucion(request):
    resoluciones = resolucion.objects.all().order_by('id')
    estado =  permi(request, "registro_resolucion")
    if request.method == 'POST': 
        idp = request.POST.get("id","")
        a=get_object_or_404(resolucion,pk=idp)
        form=formResolucionA(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'expediente/resolucion/ajax_resolucion.html',{'resolucion':resolucion,'n':'resolucionU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(resolucion,pk=idp)
        form= formResolucionA(instance=a)
        return render(request,'expediente/modal.html',{'nombre':form,'url':'actualizar_resolucion/','n':'resolucionU','u':'resolucionU','estado':estado})  


@login_required(login_url='/')
def eliminar_resolucion(request):
    resoluciones = resolucion.objects.all().order_by('id')
    estado =  permi(request, "registro_resolucion")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(resolucion,pk=idb).delete()
        return render(request,'expediente/resolucion/ajax_resolucion.html',{'resolucion':resoluciones,'n':'resolucionU','estado':estado})     



@login_required(login_url='/')
def registro_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        formu = formCategoria(request.POST)
        if formu.is_valid():
            formu.save()
        return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado})            
    else:
        formu = formCategoria()
        return render(request,'expediente/categoria/categoria.html',{'formu':formu,'categoria':categorias, 'url':'registro_categoria/','n':'categoriaU','estado':estado})

@login_required(login_url='/')
def eliminar_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'GET' and request.is_ajax(): 
        idb = request.GET.get("id","")
        get_object_or_404(categoria,pk=idb).delete()
        return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado})     

@login_required(login_url='/')
def actualizar_categoria(request):
    categorias = categoria.objects.all().order_by('id')
    estado =  permi(request, "registro_categoria")
    if request.method == 'POST' and request.is_ajax(): 
        idp = request.POST.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form=formCategoria(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return render(request,'expediente/categoria/ajax_categoria.html',{'categoria':categorias,'n':'categoriaU','estado':estado}) 
    else:
        idp = request.GET.get("id","")
        a=get_object_or_404(categoria,pk=idp)
        form= formCategoria(instance=a)
        return render(request,'seguridad/modal.html',{'nombre':form,'url':'actualizar_categoria/','n':'categoriaU','u':'categoriaU','estado':estado})  
