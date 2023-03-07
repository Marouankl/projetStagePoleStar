<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Créer une nouvelle tache</h1>
        <br />
        <form @reset="onReset()">
          <input type="text" placeholder="Task Name" v-model="addTaskForm.name" class="form-control" />
          <br />
          <textarea placeholder="Task Description" cols="80" rows="10" v-model="addTaskForm.description"
            class="form-control"></textarea>
          <br />


          <div class="d-flex justify-content-between">
            <button type="button" class="d-grid gap-1 col-5 mx-auto btn btn-dark"><router-link
                to="/">Retour</router-link></button>
            <button v-on:click="onSubmit()" type="button" class="d-grid gap-2 col-5 mx-auto btn btn-dark">Create</button>
          </div>



        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {

  data() {
    return {
      addTaskForm: {
        name: '',
        description: '',
      },
    };
  },
  methods: {

    //methode onSubmit pour lancé evenement de la bouton create  avec message alert
    onSubmit() {
      const task = {
        name: this.addTaskForm.name,
        description: this.addTaskForm.description,
      };
      if (task.name === "" && task.description === "") {
        this.$refs.alert.showAlert(
          'error', // Type de l'alerte (success, info, warning, error)
          35, // Taille de l'icône (px)
          'solid', // Style de l'icône (solid ou regular)
          'Erreur 400', // Titre de l'alerte
          'Le nom et la description de la tache ne peuvent pas être vides.' // Message de l'alerte
        );
        return;
      } else if (task.name === "") {
        this.$refs.alert.showAlert(
          'error', // Type de l'alerte (success, info, warning, error)
          35, // Taille de l'icône (px)
          'solid', // Style de l'icône (solid ou regular)
          'Erreur 400', // Titre de l'alerte
          'Le nom de la tache ne peut pas être vide.' // Message de l'alerte
        );
        return;
      } else if (task.description === "") {
        this.$refs.alert.showAlert(
          'error', // Type de l'alerte (success, info, warning, error)
          35, // Taille de l'icône (px)
          'solid', // Style de l'icône (solid ou regular)
          'Erreur 400', // Titre de l'alerte
          'La description de la tache ne peut pas être vide.' // Message de l'alerte
        );
        return;
      } else {
        this.addTask(task);
        this.onReset();
        this.$refs.alert.showAlert(
          'success', // Type de l'alerte (success, info, warning, error)
          35, // Taille de l'icône (px)
          'solid', // Style de l'icône (solid ou regular)
          'Success 200', // Titre de l'alerte
          'Votre tache a bien été créée.' // Message de l'alerte
        );
      }
    },
    // Reset la page après la ajouter les données 
    onReset() {
      this.addTaskForm.name = '';
      this.addTaskForm.description = '';
    },

    // pour ajouter les donner  a la base donnée avec axios 
    addTask(task) {
      const url = 'http://127.0.0.1:5000/create';
      axios.post(url, task)
        .then((response) => {
          console.log(response);
          this.$router.push('/')
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
  
<style>
.form {
  margin-top: 5rem;
}

h1 {
  color: darkorange;
}
</style>
  Footer
  © 2023 GitHub, Inc.
  Footer navigation
  Terms
  