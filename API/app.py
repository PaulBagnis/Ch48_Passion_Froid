# Imports API
from flask import jsonify
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
import mysql.connector
from mysql.connector.constants import ClientFlag
import datetime

config = {
    'user': 'root',
    'password': 'challenge48h',
    'host': '104.197.252.23',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem',
    'database': 'challenge'
}

# Initiate APP
app = Flask(__name__)
# Initiate API
api = Api(app)

# Create Img, Delete Img (picture + picture_tag)
# Update sur picture_tag
# Crud sur tag

# Pictures
class GetImages(Resource):
    #Vérifier les doublons
    def get(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor(buffered=True)
        get_no_tagged = 0
        imgs = []
        # On récupère les tags dans le body de la request
        req = request.json
        tags = req["tags"]
        # Test si on veut avoir les images sans tags
        if 'notags' in tags:
            get_no_tagged = 1
        # S'ils y a des tags et que 'notag' n'est pas le seul tag
        if tags and get_no_tagged == 1 and len(tags) >= 2 :
            # On formate une string avec les tags pour concaténer a la requete SQL
            formated_tags = "("
            for tag in tags :
                formated_tags = formated_tags + "\'" + tag + "\',"
            formated_tags = formated_tags[:-1] + ")"
            # On Récupère les ids des tags
            search_tags = "SELECT * FROM tag where name IN " + formated_tags
            cursor.execute(search_tags)
            id_tags = cursor.fetchall()
            # On formate une string avec les tags pour concaténer a la requete SQL
            formated_result = "("
            for id_tag in id_tags :
                formated_result = formated_result +  str(id_tag[0]) + ","
            formated_result = formated_result[:-1] + ")"
            # On récupère les ids des pictures en fonction des tags
            get_pics = ("SELECT id_picture FROM picture_tag where id_tag IN " + formated_result)
            cursor.execute(get_pics)
            id_pics = cursor.fetchall()
            # On formate une string avec les tags pour concaténer a la requete SQL
            formated_pics = "("
            for id_pic in id_pics :
                formated_pics = formated_pics + str(id_pic[0]) + ","
            formated_pics = formated_pics[:-1] + ")"
            # récupérer les paths des pictures
            get_paths = ("SELECT * FROM picture where id IN " + formated_pics)
            cursor.execute(get_paths)
            imgs.append(cursor.fetchall())
        # Si le seul tag c'est les images sans tag
        if tags and get_no_tagged == 1 and len(tags) == 1:
            # on récupère tous les ids des photos qui ne sont pas dans la table de relation entre tags et images
            get_pics_ids = ("SELECT * FROM picture_tag")
            cursor.execute(get_pics_ids)
            get_pics_ids = cursor.fetchall()
            # On formate une string avec les tags pour concaténer a la requete SQL
            formated_pics_ids = "("
            for id_pic_id in get_pics_ids :
                formated_pics_ids = formated_pics_ids + str(id_pic_id[0]) + ","
            formated_pics_ids = formated_pics_ids[:-1] + ")"
            # On recherche les images qui ont un id pas dans le résultat de la requête précédente
            get_imgs_not_tagged = ("SELECT * FROM picture where id NOT IN " + formated_pics_ids)
            cursor.execute(get_imgs_not_tagged)
            imgs.append(cursor.fetchall())
        cnxn.close()
        print(imgs)
        response = make_response(jsonify('200'))
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET"
        return response

class Image(Resource):
    # récupérer
    def get(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()
        # On récupère les tags dans le body de la request
        req = request.json
        img_id = req['id']
        get_paths = ("SELECT * FROM picture where id = " + str(img_id))
        cursor.execute(get_paths)
        image = cursor.fetchall()
        print(image)
        cnxn.close()
        return
    
    # Ajouter
    def post(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()
        req = request.json
        img_nom                             = req['nom']
        type_image                          = req['type_image']
        photo_avec_produit                  = req['photo_avec_produit']
        photo_avec_humain                   = req['photo_avec_humain']
        photo_institutionnelle              = req['photo_institutionnelle']
        format_img                          = req['format_img']
        credits_photo                       = req['credits_photo']
        droits_utilisation_limite           = req['droits_utilisation_limite']
        copyright_img                       = req['copyright_img']
        date_de_fin_droits_utilisation      = req['date_de_fin_droits_utilisation']
        image                               = req['image']
        date                                = str(datetime.datetime.now())
        add_pic = ("INSERT INTO picture (nom, type_image, photo_avec_produit, photo_avec_humain, photo_institutionnelle, format, credits_photo, droits_utilisation_limite, copyright, date_de_fin_droits_utilisation, image)"
        " VALUES (" + img_nom + type_image + photo_avec_produit + photo_avec_humain + photo_institutionnelle + format_img + credits_photo + droits_utilisation_limite + copyright_img + date_de_fin_droits_utilisation + image + date + ")")
        cursor.execute(add_pic)
        cnxn.commit()
        cnxn.close()
        return 200
    
    # Mettre a jour
    def update(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()
        req = request.json
        update_pic_start = "INSERT INTO picture ("
        if req['nom'] :
            update_pic_start = update_pic_start + 'nom, '
        if req['type_image'] :
            update_pic_start = update_pic_start + 'type_image, '
        if req['photo_avec_produit'] :
            update_pic_start = update_pic_start + 'photo_avec_produit, '
        if req['photo_avec_humain'] :
            update_pic_start = update_pic_start + 'photo_avec_humain, '
        if req['photo_institutionnelle'] :
            update_pic_start = update_pic_start + 'photo_institutionnelle, '
        if req['format_img'] :
            update_pic_start = update_pic_start + 'format_img, '
        if req['credits_photo'] :
            update_pic_start = update_pic_start + 'credits_photo, '
        if req['droits_utilisation_limite']:
            update_pic_start = update_pic_start + 'droits_utilisation_limite, ' 
        if req['copyright_img']:
            update_pic_start = update_pic_start + 'copyright_img, '
        if req['date_de_fin_droits_utilisation']:
            update_pic_start = update_pic_start + 'date_de_fin_droits_utilisation, '
        if req['image']:
            update_pic_start = update_pic_start + 'image, '
        if req['date']:
            update_pic_start = update_pic_start + 'date'
        update_pic_end = ") VALUES ("
        if req['nom'] :
            update_pic_end = update_pic_end + req['nom']
        if req['type_image'] :
            update_pic_end = update_pic_end + req['type_image']
        if req['photo_avec_produit'] :
            update_pic_end = update_pic_end + req['photo_avec_produit']
        if req['photo_avec_humain'] :
            update_pic_end = update_pic_end + req['photo_avec_humain'] 
        if req['photo_institutionnelle'] :
            update_pic_end = update_pic_end + req['photo_institutionnelle']
        if req['format_img'] :
            update_pic_end = update_pic_end + req['format_img']
        if req['credits_photo'] :
            update_pic_end = update_pic_end + req['credits_photo']
        if req['droits_utilisation_limite']:
            update_pic_end = update_pic_end + req['droits_utilisation_limite']  
        if req['copyright_img']:
            update_pic_end = update_pic_end + req['copyright_img'] 
        if req['date_de_fin_droits_utilisation']:
            update_pic_end = update_pic_end + req['date_de_fin_droits_utilisation']
        if req['image']:
            update_pic_end = update_pic_end + req['image']
        if req['date']:
            update_pic_end = update_pic_end + req['date'] 
        update_pic_end = update_pic_end + ")"   
        update_pic = update_pic_start + update_pic_end
        cursor.execute(update_pic)
        cnxn.commit()
        cnxn.close()
        return

    def delete(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()
        req = request.json
        img_id = req['id']
        delete_pic = ("DELETE * FROM picture where id = " + str(img_id))
        cursor.execute(delete_pic)
        cnxn.commit()
        cnxn.close()
        return

# Tags
class GetTags(Resource):
    def get(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cnxn.close()
        return

class Tag(Resource):
    def get(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cnxn.close()
        return

    def post(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cnxn.close()
        return

    def update(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cnxn.close()
        return

    def delete(self):
        cnxn = mysql.connector.connect(**config)
        cursor = cnxn.cursor()

        cnxn.close()
        return

api.add_resource(GetImages, "/images")
api.add_resource(Image,     "/image")
api.add_resource(GetTags,   "/tags")
api.add_resource(Tag,       "/tag")

if __name__ == "__main__":
    app.run(debug=True)