<script setup>
import Navbar from '../components/Navbar.vue'

</script>

<template>
    
    <section style="background-color: #d8d8d8;">

    <main>
      <Navbar />
  
      <div class="container py-5">
        <div class="row text-center">
            <div class="col-lg-7 mx-auto">
                <h1 class="display-5">Naš tim</h1>
                <p class="lead mb-0 p-2"> Rešavanje interaktivnih kurseva i učenje programiranja uz pomoć sfero robota omogućili su vam naši programeri</p>
            </div>
        </div>
    </div><!-- End -->


    <div class="container">
        <div class="row text-center">
            <div class="col-3"></div>
            
            <div class="col-xl-3 col-sm-6 mb-5">
                <div class="bg-white rounded shadow-sm py-5 px-4">
                    <img src="https://media.licdn.com/dms/image/C5603AQE8sbzK5OZWUw/profile-displayphoto-shrink_800_800/0/1659623322719?e=2147483647&v=beta&t=_vNDrfPZlsDstF_NZ62uHDkXx4sJzznRXksaBhvJWTU" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                    <h5 class="mb-0">Pavle Glušac</h5><span class="text-muted">Data Scientist </span>
                    <ul class="social mb-0 list-inline mt-3">
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-facebook"></i></a></li>
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-twitter"></i></a></li>
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-instagram"></i></a></li>
                        <li class="list-inline-item"><a href="https://rs.linkedin.com/in/pavleglusac" class="social-link"><i class="bi bi-linkedin"></i></a></li>
                    </ul>
                </div>
            </div>
            

            <div class="col-xl-3 col-sm-6 mb-5">
                <div class="bg-white rounded shadow-sm py-5 px-4"><img src="https://s.abcnews.com/images/GMA/jlo-file-gty-ml-220725_1658757126066_hpMain_1x1_992.jpg" alt=""  width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                    <h5 class="mb-0">Nevena Radešić</h5><span class="text-muted">Master student</span>
                    <ul class="social mb-0 list-inline mt-3">
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-facebook"></i></a></li>
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-twitter"></i></a></li>
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-instagram"></i></a></li>
                        <li class="list-inline-item"><a href="#" class="social-link"><i class="bi bi-linkedin"></i></a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    </main>

</section>
  </template>
  
  <style scoped>
   body {
    background: #e8cbc0;
    background: -webkit-linear-gradient(to right, #e8cbc0, #636fa4);
    background: linear-gradient(to right, #e8cbc0, #636fa4);
    min-height: 100vh;
}

.social-link {
    width: 30px;
    height: 30px;
    border: 1px solid #ddd;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #666;
    border-radius: 50%;
    transition: all 0.3s;
    font-size: 0.9rem;
}

.social-link:hover, .social-link:focus {
    background: #ddd;
    text-decoration: none;
    color: #555;
}

section {
    height: 100%;
}

  </style>
  