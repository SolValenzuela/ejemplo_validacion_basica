from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ubicacion = data['ubicacion']
        self.lenguaje = data['lenguaje']
        self.comentarios = data['comentarios']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (nombre,apellido,ubicacion,lenguaje,comentarios) VALUES (%(nombre)s,%(apellido)s,%(ubicacion)s,%(lenguaje)s,%(comentarios)s);"
        return connectToMySQL('dojo_survey').query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey').query_db(query)
        return Dojo(results[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        nombre=dojo['nombre'].strip()
        if nombre == '':
            flash('El nombre y/o apellido no puede estar vacío')
            is_valid = False
        if len(dojo['nombre']) < 3:
            is_valid = False
            flash("Nombre y/o apellido debe tener al menos 3 letras.")
        apellido=dojo['apellido'].strip()
        if apellido == '':
            flash('')
        if len(dojo['apellido']) < 3:
            is_valid = False
        if len(dojo['ubicacion']) < 1:
            is_valid = False
            flash("Debe elegir una ubicación para el Dojo.")
        if len(dojo['lenguaje']) < 1:
            is_valid = False
            flash("Debe elegir su lenguaje favorito.")
        if len(dojo['comentarios']) < 3:
            is_valid = False
            flash("Los comentarios deben tener al menos 3 caracteres.")
        return is_valid