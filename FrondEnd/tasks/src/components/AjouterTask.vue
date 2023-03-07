<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Créer une nouvelle tache</h1>
        <br />
        <form @submit.prevent="onSubmit" @reset="onReset">
          <input type="text" placeholder="Task Name" v-model="addTaskForm.name" class="form-control" />
          <br />
          <textarea placeholder="Task Description" cols="80" rows="10" v-model="addTaskForm.description"
            class="form-control"></textarea>
          <br />


          <div class="d-flex justify-content-between">
            <button type="button" class="d-grid gap-1 col-5 mx-auto btn btn-dark"><router-link to="/">Retour</router-link></button>
            <button type="button" class="d-grid gap-2 col-5 mx-auto btn btn-dark">Create</button>
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
        .then((response) => {
          console.log(response);
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
h1{
  color:darkorange ;
}
</style>
  Footer
  © 2023 GitHub, Inc.
  Footer navigation
  Terms
  