<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">

                <h1>Afficher les taches disponibles </h1>
                <hr><br><br>
                <router-link to="/AjouterTask"><button type="submit"
                        class="d-grid gap-1 col-3 mx-auto btn btn-primary">Créer une nouvelle Tache</button></router-link>


                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Nom</th>
                            <th scope="col">Discription</th>
                            <th scope="col">Date de la tache</th>
                            <th>
                            </th>

                            <th scope="col">Action</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(task, index) in tasks" v-bind:key="task.id">
                            <td>{{ task.name }}</td>
                            <td>{{ task.description }}</td>
                            <td>{{ moment(task.date).format("MM-DD-YYYY ") }}</td>

                            <td>
                            </td>
                            <td>
                                <div class="btn-group" role="group">

                                    <button type="button" class="btn btn-danger btn-sm"
                                        v-on:click="deleteTask(task, index)">
                                        Delete
                                    </button>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div v-if="notification" class="notification">
                    Tâche supprimée avec succès.
                </div>
            </div>
        </div>


    </div>
</template>

<script>

import axios from 'axios';
import moment from 'moment'


export default {

    name: ' Accueil',
    data() {
        return {
            tasks: [],
            notification: false
        };

    },
    mounted() {
        this.getTasks();
    },


    methods: {

        // Pour récupérer les donner dans la table avec axios  
        getTasks() {
            const url = 'http://127.0.0.1:5000/allTask';
            axios.get(url).then((response) => {
                if (response.data.length > 0) {
                    this.tasks = response.data;
                }
            }).catch(error => {
                console.log(error)

            })
        },


        // Pour supprimer une tache avec sont ID avec axios
        deleteTask(task, index) {
            const url = `http://127.0.0.1:5000/delete/${task.id}`;
            axios.post(url)
                .then(() => {
                    this.tasks.splice(index, 1);
                    this.notification = true; // activation de la notification
                    setTimeout(() => {
                        this.notification = false; // désactivation de la notification après 3 secondes
                    }, 3000);

                })
                .catch((error) => {
                    console.error(error);
                });
        },
        //fonction moment pour format dateTime
        moment: function () {
            return moment();
        },


    },



}

</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.notification {
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 9999;
}
h1 {
    color: coral;
    margin: 40px 0 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>
  