<script setup>
import Navbar from "../components/Navbar.vue";
</script>

<template>
  <main>
    <Navbar />
    <div class="mb-2 mt-4 mx-auto w-50">
      <h1>Lekcije</h1>

      <div v-for="(chapter, index) in lessons" :key="index">
        <h2>{{ chapter.name }}</h2>
        <ul>
          <div v-for="(lesson, index) in chapter.tasks" :key="index">
            <a :href="'/problem/' + chapter.id + '/' + lesson.id" style="text-decoration: none">
              <li>
                {{ lesson.name }}
              </li>
            </a>
          </div>
        </ul>
      </div>
    </div>
  </main>
</template>

<script>
import lessons from "../data/lessons.json";
export default {
  name: "LessonsView",
  data() {
    return {
      lessons: lessons,
    };
  },
};
</script>

<style scoped>
.mb-2.mt-4.mx-auto.w-50 {
  margin: 2rem auto;
  width: 50%;
  font-family: "Arial", sans-serif;
}

h1,
h2 {
  color: #333;
  margin-bottom: 1rem;
}

ul {
  list-style: none;
  padding: 0;
  margin-left: 0;
}

ul li {
  background-color: #f0f0f0;
  margin-bottom: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 10px;
  transition: background-color 0.3s;
  color: #333;
}

ul li:hover {
  background-color: #e0e0e0;
  cursor: pointer;
}
</style>
