from flask import Flask, render_template, request, url_for, redirect, jsonify
# from flask_mysqldb import MySQL
import requests
import json

app = Flask(__name__)
# app._static_folder = '/app/static'
# coding=utf-8

@app.route("/")
def index():
    more_data = {
        'name_page': 'AIRFOODS',
        'bienvenida': 'AIRFOODS'
    }
    return render_template('index.html', more_data=more_data)


@app.route("/trays", methods=["GET"])
def get_trays():
    print(request)
    print(request.args)
    
    print("REQ1 - Sort:", request.args.get('sort'))  # sort=name
    print("REQ2 - Order:", request.args.get('order'))  # order=desc
    print("REQ3 - Page:", request.args.get('page'))  # page=4
    print("REQ4 - Size:", request.args.get('size'))  # size=50

    sort = request.args.get('sort')
    order = request.args.get('order')
    page = request.args.get('page')
    size = request.args.get('size')

    parameters = {
        'sort': sort,
        'order': order,
        'page': page,
        'size': size
    }
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/trays'
    # link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/traystrays?sort=' + sort + '&order=' + order + '&page=' + page + '&size=' + size
    response = requests.get(link, headers={'Content-type': 'application/json'}, params=parameters)
    data = json.loads(response.text)
    print(data)
    print(data["items"])
    print("Total:", data["total"])
    print("Page:", data["page"])
    print("Size:", data["size"])

    more_data = {
        'name_page': 'Bandejas',
        'bienvenida': 'MENÚ BANDEJAS'
    }
    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["items"]:
            # print(itm)
            id = itm["id"]
            plates = itm["name"]
            price = itm["price"]
            elem = [id, plates, price]
            items.append(elem)
        return render_template('trays.html', data=data, more_data=more_data, items=items)
    if response.status_code == 200:
        # for itm in data:
        #     print(itm)
        return "OK!"
    else:
        return "NOT OK!"


@app.route("/trays", methods=["GET"])  
def get_trays_name():
    print(request)
    print(request.args)
    
    print("REQ1 - Sort:", request.args.get('sort'))  # sort=name
    print("REQ2 - Order:", request.args.get('order'))  # order=desc
    print("REQ3 - Page:", request.args.get('page'))  # page=4
    print("REQ4 - Size:", request.args.get('size'))  # size=50

    sort = request.args.get('sort')
    order = request.args.get('order')
    page = request.args.get('page')
    size = request.args.get('size')

    parameters = {
        'sort': sort,
        'order': order,
        'page': page,
        'size': size
    }
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/trays'
    # link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/traystrays?sort=' + sort + '&order=' + order + '&page=' + page + '&size=' + size
    response = requests.get(link, headers={'Content-type': 'application/json'}, params=parameters)
    data = json.loads(response.text)
    print(data)
    print(data["items"])
    print("Total:", data["total"])
    print("Page:", data["page"])
    print("Size:", data["size"])
    
    more_data = {
        'name_page': 'Bandejas',
        'bienvenida': 'MENÚ BANDEJAS'
    }
    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["items"]:
            # print(itm)
            id = itm["id"]
            plates = itm["name"]
            price = itm["price"]
            elem = [id, plates, price]
            items.append(elem)
        return render_template('trays.html', data=data, more_data=more_data, items=items)
    if response.status_code == 200:
        # for itm in data:
        #     print(itm)
        return "OK!"
    else:
        return "NOT OK!"


@app.route("/trays/<tray_id>", methods=["GET"])
def get_tray_id(tray_id):
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/trays/' + tray_id
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    # print(data)
    print("Price:", data["price"])
    print("Size:", data["size"])
    print("Expiration:", data["expiration"])
    print("Id:", data["id"])
    print("Name:", data["name"])
    print("Descrpition:", data["description"])
    print("Courses:", data["courses"])

    more_data = {
        'name_page': data["name"],
        'bienvenida': data["name"]
    }

    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["courses"]:
            print(itm)
            id = itm["id"]
            name = itm["name"]
            img_url = itm["img_url"]
            category = itm["category"]
            elem = [id, name, img_url, category]
            items.append(elem)
        return render_template('tray.html', data=data, more_data=more_data, items=items)
        # for itm in data:
        #     print(itm)
        # return "OK!"
    else:
        return "NOT OK!"


@app.route("/courses", methods=['GET'])
def get_courses():  # LISTO
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/courses'
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    # print(data)
    print("Items:", data["items"])
    print("Total:", data["total"])
    print("Page:", data["page"])
    print("Size:", data["size"])

    more_data = {
        'name_page': 'Platos',
        'bienvenida': 'MENÚ PLATOS'
    }
    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["items"]:
            id = itm["id"]
            name = itm["name"]
            price = itm["price"]
            elem = [id, name, price]
            items.append(elem)
        return render_template('courses.html', data=data, more_data=more_data, items=items)
        # return "OK!"
    else:
        return "NOT OK!"
        # return jsonify(mensaje), response1.status_code


@app.route("/courses/<course_id>", methods=["GET"])
def get_course_id(course_id):
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/courses/' + course_id
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    # print(data)
    print("Price:", data["price"])
    print("Size:", data["size"])
    print("Expiration:", data["expiration"])
    print("Id:", data["id"])
    print("Category:", data["category"])
    print("Name:", data["name"])
    print("Description:", data["description"])
    print("Img_URL:", data["img_url"])
    print("Ingredients:", data["ingredients"])

    more_data = {
        'name_page': data["name"],
        'bienvenida': data["name"]
    }

    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["ingredients"]:
            print(itm)
            id = itm["id"]
            name = itm["name"]
            quantity = itm["quantity"]
            elem = [id, name, quantity]
            items.append(elem)
        return render_template('course.html', data=data, more_data=more_data, items=items)
        # for itm in data:
        #     print(itm)
        # return "OK!"
    else:
        return "NOT OK!"


@app.route("/ingredients", methods=['GET'])
def get_ingredients():  # LISTO
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/ingredients'
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    # print(data)
    # print("Items:", data["items"])
    # print("Total:", data["total"])
    # print("Page:", data["page"])
    # print("Size:", data["size"])

    more_data = {
        'name_page': 'Ingredientes',
        'bienvenida': 'MENÚ INGREDIENTES'
    }
    items = []
    if response.status_code == 200:
        elem = []
        for itm in data["items"]:
            id = itm["id"]
            name = itm["name"]
            price = itm["price"]
            elem = [id, name, price]
            items.append(elem)

        return render_template('ingredients.html', data=data, more_data=more_data, items=items)
        # return "OK!"
    else:
        return "NOT OK!"
        # return jsonify(mensaje), response1.status_code


@app.route("/ingredients/<ingredient_id>", methods=["GET"])
def get_ingredient_id(ingredient_id):
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/ingredients/' + ingredient_id
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    print(data)
    print("DATAAAAAAA")
    # print("Id:", data["id"])
    # print("Name:", data["name"])
    # print("Descrpition:", data["description"])
    # print("Img_URL:", data["img_url"])
    # print("Price:", data["price"])
    # print("Size:", data["size"])
    # print("Expiration:", data["expiration"])

    more_data = {
        'name_page': data["name"],
        'bienvenida': data["name"]
    }
    if response.status_code == 200:
        return render_template('ingredient.html', data=data, more_data=more_data)
        # for itm in data:
        #     print(itm)
        return "OK!"
    else:
        return "NOT OK!"


@app.route("/search/trays", methods=['GET'])
def search_trays():  # LISTO
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/trays'
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    print(data)
    # print("Items:", data["items"])
    # print("Total:", data["total"])
    # print("Page:", data["page"])
    # print("Size:", data["size"])

    if response.status_code == 200:
        for itm in data:
            print(itm)
        # for itm in data["items"]:
        #     print(itm["id"])
        return "OK!"
        # return jsonify(resp_json), response1.status_code
    else:
        return "NOT OK!"
        # return jsonify(mensaje), response1.status_code


@app.route("/search/courses", methods=['GET'])
def search_courses():  # LISTO
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/courses'
    response = requests.get(link, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    print(data)
    # print("Items:", data["items"])
    # print("Total:", data["total"])
    # print("Page:", data["page"])
    # print("Size:", data["size"])

    if response.status_code == 200:
        for itm in data:
            print(itm)
        # for itm in data["items"]:
        #     print(itm["id"])
        return "OK!"
        # return jsonify(resp_json), response1.status_code
    else:
        return "NOT OK!"
        # return jsonify(mensaje), response1.status_code


@app.route("/search/ingredients", methods=['GET'])
def search_ingredients():  # LISTO
    link = 'https://tarea-4.2022-1.tallerdeintegracion.cl/search/ingredients'
    body = "Pollo"
    response = requests.get(link, json=body, headers={'Content-type': 'application/json'})
    data = json.loads(response.text)
    print(data)
    # print("Items:", data["items"])
    # print("Total:", data["total"])
    # print("Page:", data["page"])
    # print("Size:", data["size"])

    if response.status_code == 200:
        for itm in data:
            print(itm)
        # for itm in data["items"]:
        #     print(itm["id"])
        return "OK!"
        # return jsonify(resp_json), response1.status_code
    else:
        return "NOT OK!"
        # return jsonify(mensaje), response1.status_code


def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    # return redirect(url_for('index'))


# @app.before_request
# def before_request():
#     print("Antes de la peticion...")


# @app.after_request
# def after_request(response):
#     print("Despues de la peticion")
#     return response


# @app.route('/')
# def index():
#     # return "<h1>UskoKruM2010 - Suscríbete!</h1>"
#     cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
#     data = {
#         'titulo': 'Index123',
#         'bienvenida': '¡Saludos!',
#         'cursos': cursos,
#         'numero_cursos': len(cursos)
#     }
#     return render_template('index.html', data=data)


# @app.route('/contacto/<nombre>/<int:edad>')
# def contacto(nombre, edad):
#     data = {
#         'titulo': 'Contacto',
#         'nombre': nombre,
#         'edad': edad
#     }
#     return render_template('contacto.html', data=data)


# def query_string():
#     print(request)
#     print(request.args)
#     print(request.args.get('param1'))
#     print(request.args.get('param2'))
#     return "Ok"


if __name__ == '__main__':
    # app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
