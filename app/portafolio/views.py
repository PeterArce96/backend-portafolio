from flask import Flask,render_template,request,session,flash,redirect,url_for

from . import portafolio

from .forms import ContactoForm

from app import fb

@portafolio.route('/')
def index():
    dicBiografia = fb.getCollection('biografia')[0]
    session['biografia'] = dicBiografia

    return render_template('portafolio/index.html')

@portafolio.route('/proyectos')
def proyectos():
    listaProyectos = fb.getCollection('proyectos')
    
    context = {
        'proyectos':listaProyectos
    }

    return render_template('portafolio/portafolio.html',**context)

@portafolio.route('/acercade')
def acercade():
    return render_template('portafolio/acercade.html')

@portafolio.route('/contacto',methods=['GET','POST'])
def contacto():

    contacto_form = ContactoForm()
    context = {
        'contacto_form':contacto_form
    }

    if contacto_form.validate_on_submit():

        dataNuevoContacto = {
                'email' : contacto_form.email.data,
                'mensaje' : contacto_form.mensaje.data,
                'nombre' : contacto_form.nombre.data
            }
        print(dataNuevoContacto)

        nuevoContacto = fb.insertDocument('contactos',dataNuevoContacto)

        flash("Mensaje Enviado con éxito!")
        return redirect(url_for('portafolio.contacto'))
        
    return render_template('portafolio/contacto.html',**context)