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


          <div v-if="notification" class="notification">
            Tâche ajouter avec succès.
          </div>
          <div v-if="notification" class="notification2">
            Tâche supprimée avec succès.
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
      notification: false
    };
  },
  methods: {
    onSubmit() {
      const task = {
        name: this.addTaskForm.name,
        description: this.addTaskForm.description,
      };
      this.addTask(task);
      this.onReset();
    },
    onReset() {
      this.addTaskForm.name = '';
      this.addTaskForm.description = '';
    },
    addTask(task) {
      const url = 'http://127.0.0.1:5000/create';
      axios.post(url, task)
        .then(() => {
          this.notification = true; // activation de la notification
                    setTimeout(() => {
                        this.notification = false; // désactivation de la notification après 3 secondes
                    }, 3000);
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
.notification2 {
  position: fixed;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color:red;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  z-index: 9999;
}
h1 {
  color: darkorange;
}
</style>
  Footer
  © 2023 GitHub, Inc.
  Footer navigation
  Terms
  