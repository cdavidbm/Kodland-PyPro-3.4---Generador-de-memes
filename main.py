# Importar
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Ruta principal para manejar el formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Recepción del texto superior e inferior
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')        

        # Recepción de la posición del texto superior e inferior
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Visualización del texto superior e inferior
                               text_top=text_top,
                               text_bottom=text_bottom,

                               # Visualización del color seleccionado
                               selected_color=selected_color,
                        
                               # Visualización de la posición del texto superior e inferior
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y
                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')

# Ruta para servir imágenes estáticas
@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)