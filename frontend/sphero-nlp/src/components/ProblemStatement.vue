<template>
    <nav class="navbar">
      <div class="container">
        <a href="#" class="navbar-brand">MyWebsite</a>
        <ul class="navbar-menu">
          <li class="navbar-item" v-for="item in menuItems" :key="item.id">
            <a :href="item.link" class="navbar-link">{{ item.label }}</a>
          </li>
        </ul>
      </div>
    </nav>
  </template>
  
<script>
  export default {
    name: 'Navbar',
    data() {
      return {
        menuItems: [
          { id: 1, label: 'Home', link: '/' },
          { id: 2, label: 'About', link: '/about' },
          { id: 3, label: 'Contact', link: '/contact' }
        ]
      }
    }
  }
  </script>
  
  <style scoped>
  .navbar {
    background-color: #333;
    padding: 1rem 0;
  }
  .container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
  }
  .navbar-brand {
    color: #fff;
    font-size: 1.5rem;
  }
  .navbar-menu {
    list-style-type: none;
    padding: 0;
    display: flex;
    gap: 1rem;
  }
  .navbar-link {
    color: #fff;
    text-decoration: none;
  }
  </style>
  