from flask import render_template,redirect,url_for,session,flash

from . import admin
from .forms import LoginForm,BiografiaForm,ProyectoForm

import pyrebase
from app.firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

from app import fb

@admin.route('/')
def index():
    if('token' in session):
        return render_template('admin/index.html')
    else:
        return redirect(url_for('admin.login'))

################### LOGIN ############################
@admin.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    if login_form.validate_on_submit():
        #realizamos el login de usuarios
        usuarioData = login_form.usuario.data
        passwordData = login_form.password.data
        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            dataUsuarioValido = auth.get_account_info(usuario['idToken'])
            print(dataUsuarioValido)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
        except:
            print("error al autenticarse")
            flash("Usuario o password invalidos")


    return render_template('admin/login.html',**context)

@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.login'))

################### PANEL DE ADMINISTRACIÓN ############################
@admin.route('/biografia',methods=['GET','POST'])
def biografia():
    if ('token' in session):
        biografiaData = fb.getDocument('biografia','hLdesa3kYksf0ijobWoA')
        print(biografiaData)

        biografia_form = BiografiaForm(data=biografiaData)

        if biografia_form.validate_on_submit():
            dataBiografiaActualizada = {
                'nombre' : biografia_form.nombre.data,
                'resumen' : biografia_form.resumen.data,
                'rol' : biografia_form.rol.data,
                'foto' : biografia_form.foto.data,
                'ubicacion' : biografia_form.ubicacion.data,
                'cv' : biografia_form.cv.data,
                'github' : biografia_form.github.data,
                'linkedin' : biografia_form.linkedin.data,
                'twitter' : biografia_form.twitter.data
            }
            resultadoUpdateBiografia = fb.updateDocument('biografia','hLdesa3kYksf0ijobWoA',dataBiografiaActualizada)
            flash("Datos Actualizados")
            #biografia_form = BiografiaForm(data=dataBiografiaActualizada)


        context = {
            'biografia_form':biografia_form
        }
        return render_template('admin/biografia.html',**context)
    else:
        return redirect(url_for('admin.login'))

@admin.route('/proyectos',methods=['GET','POST'])
def proyectos():
    if('token' in session):
        listaProyectos = fb.getCollection('proyectos')

        #formulario de proyectos
        proyecto_form = ProyectoForm()

        if proyecto_form.validate_on_submit():

            dataNuevoProyecto = {
                'codigo' : proyecto_form.codigo.data,
                'nombre' : proyecto_form.nombre.data,
                'descripcion' : proyecto_form.descripcion.data,
                'imagen': proyecto_form.imagen.data,
                'url':proyecto_form.url.data
            }

            nuevoProyecto = fb.insertDocument('proyectos',dataNuevoProyecto)
            print(nuevoProyecto)

            return redirect(url_for('admin.proyectos'))

        context = {
            'proyectos':listaProyectos,
            'proyecto_form':proyecto_form
        }
        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))

@admin.route('/contactos')
def contactos():
    if('token' in session):
        listaContactos = fb.getCollection('contactos')

        context = {
            'contactos':listaContactos,
        }
        return render_template('admin/contactos.html',**context)
    else:
        return redirect(url_for('admin.login'))

@admin.route('/proyecto/<id>',methods=['GET','POST'])
def proyecto(id=''):
    if('token' in session):
        listaProyectos = fb.getCollection('proyectos')
        proyectoData = fb.getDocument('proyectos',id)
        print(proyectoData)
        proyecto_form = ProyectoForm(data=proyectoData)

        if proyecto_form.validate_on_submit():

            dataProyectoActualizar = {
                'codigo' : proyecto_form.codigo.data,
                'nombre' : proyecto_form.nombre.data,
                'descripcion' : proyecto_form.descripcion.data,
                'imagen': proyecto_form.imagen.data,
                'url':proyecto_form.url.data
            }

            resultadoActualizarProyecto = fb.updateDocument('proyectos',id,dataProyectoActualizar)

            return redirect(url_for('admin.proyectos'))

        context = {
            'proyectos':listaProyectos,
            'proyecto_form':proyecto_form
        }
        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))

@admin.route('/delproyecto/<id>')
def delProyecto(id=''):
    fb.deleteDocument('proyectos',id)
    return redirect(url_for('admin.proyectos'))