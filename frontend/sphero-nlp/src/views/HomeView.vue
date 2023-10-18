<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<template>
  <main>
    <Navbar />
    <div class="card mb-2 mt-4 mx-auto w-75">
      <div class="row g-0">
        <div class="col-md-6">
          <img src="https://149455152.v2.pressablecdn.com/wp-content/uploads/2020/05/IMG_2110-e1590167123169.jpg" class="img-fluid rounded-start">
        </div>
        <div class="col-md-6" style="background-color: rgb(179, 148, 108); color: aliceblue;">
          <div class="card-body">
            <h2 class="card-title" style="font-weight: bold;">Sphero Kurs</h2>
            <p class="card-text" style="font-size: x-large; font-weight: 600;">Započnite svoje Sphero putovanje rešavanjem interaktivnih kurseva klikom na link ispod 👇</p>
            <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
            <!-- add a button and center it -->
            <div class="d-grid gap-2 col-6 mx-auto mt-5">
              <router-link to="/courses" class="btn btn-primary btn-lg">Kursevi</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- https://img.youtube.com/vi/HDxzPI0kAzw/maxresdefault.jpg -->
    <div class="card mb-2 mt-4 mx-auto w-75">
      <div class="row g-0">
        <div class="col-md-6" style="background-color: rgb(92, 179, 219); color: aliceblue;">
          <div class="card-body">
            <h2 class="card-title" style="font-weight: bold;">YouTube Lekcije</h2>
            <p class="card-text" style="font-size: x-large; font-weight: 600;">
              Pogledajte lekcije "Učenje programiranja pomoću Sphero robota" Tare Pogančev kojima ćete savladali Sphero! 👇
            </p>
            <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
            <!-- add a button and center it -->
            <div class="d-grid gap-2 col-6 mx-auto mt-5">
              <router-link to="/courses" class="btn btn-primary btn-lg">Lekcije</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <img src="../assets/sphero-card-2.jpg" class="img-fluid rounded-start">
        </div>
      </div>
    </div>

    <div class="card mb-2 mt-4 mx-auto w-75">
      <div class="row g-0">
        <div class="col-md-6">
          <img src="../assets/sphero-2b-solo.webp" class="img-fluid rounded-start">
        </div>
        <div class="col-md-6" style="background-color: rgb(85, 199, 91); color: aliceblue;">
          <div class="card-body">
            <h2 class="card-title" style="font-weight: bold;">Više Informacija</h2>
            <p class="card-text" style="font-size: x-large; font-weight: 600;">
              Za sve dodatne informacije, posetitie zvaničan sajt
            </p>
            <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
            <!-- add a button and center it -->
            <div class="d-grid gap-2 col-6 mx-auto mt-5">
              <router-link to="#" class="btn btn-primary btn-lg">Sajt</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>

</style>