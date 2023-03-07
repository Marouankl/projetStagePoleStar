
import datetime
import os
from flask import Flask, json, request
from flask_cors import CORS
from flaskext.mysql import MySQL
import collections


import logging

mysql = MySQL()

app = Flask(__name__)
cors = CORS(app)
app.debug = True

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'projetstage'
mysql.init_app(app)


@app.route("/")
def home():
    return "Hello, Flask!"

# Pour récupérer  tous les taches dans la base de donnee


@app.route('/allTask')
def getTasks():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM task')
        results = cursor.fetchall()
        if len(results) == 0:
            conn.commit()
            return json.dumps({'message': 'aucune tache trouvée !'})
        else:
            # converture le résultatt en forma json 
            taskJson = []
            for row in results:
                d = collections.OrderedDict()
                d['id'] = row[0]
                d['name'] = row[1]
                d['description'] = row[2]
                d['date'] = row[3]
                taskJson.append(d)
                
             # return le résultat  en forma  JSON response
            respone = json.dumps(taskJson)
            return respone

# Pour récupérer  un élement by ID  dans la base de donnee


@app.route('/task/<id>', methods=['GET'])
def getTaskById(id):
        conn = mysql.connect()
        cursor = conn.cursor()
       # app.logger.warning(id)
        cursor.execute('SELECT * FROM task WHERE id=%s', [id])
        results = cursor.fetchone()
        if results is None:
            return "Error"
    
    # # return le résultat  en forma  JSON response
        return json.dumps(results)

 # Pour creer une nouvelle tache
@app.route('/create', methods=['GET', 'POST'])
def createTask():

        conn = mysql.connect()
        cursor = conn.cursor()
        if request.method == 'POST':
            post_data = request.get_json(silent=True)
            name = post_data.get('name')
            description = post_data.get('description')
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            sql = "INSERT INTO task (name, description, date) VALUES (%s, %s, %s)"
            data = (name, description, date)
            cursor.execute(sql, data)
             # return le résultat  en forma  JSON response
            return json.dumps({'message': 'Votre tache bien ajouter !'})
        else:
             return ('error')


# Pour mise a jour les taches
@app.route('/update', methods=['PUT'])
def updateTask():
       conn = mysql.connect()
       cursor = conn.cursor()
       if request.method == 'PUT':
            post_data = request.get_json(silent=True)
            _id = post_data.get('id')
            _name = post_data.get('name')
            _description = post_data.get('description')
            _date = datetime.datetime.now().strftime('%Y-%m-%d')
            sql = 'UPDATE task SET name=%s, description=%s, date=%s WHERE id=%s'
            data = (_name, _description, _date, _id)
            cursor.execute(sql, data)
            conn.commit()
             # return le résultat  en forma  JSON response
            return json.dumps({'message': 'Votre tache a été mise à jour !'})
       else:
            return ('error')
         
         
         
#La methode pour supprimer une tache                  
@app.route('/delete/<id>',methods=['GET','POST'])
def deleteTask(id):   
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM task WHERE id=%s',[id])
        conn.commit()
         # return le résultat  en forma  JSON response
        return json.dumps({'message':'tache supprimée !'})

       
                         
       
if __name__ == "__main__":
    port = int ( os . environ . get ( 'PORT' , 5000 )) 
    app . run ( debug = True , host = '0.0.0.0' , port = port ) 
    #app.run(debug=True)

        
        
   

