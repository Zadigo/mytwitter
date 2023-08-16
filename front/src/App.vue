<template>
  <router-view :key="$route.name"></router-view>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
.main {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  width: 100%;
  height: 100vh;
}

.left-section,
.right-section {
  height: 100vh;
  width: 300px;
  padding: 1rem;
}

.middle {
  width: calc(100% - 100px - 100px);
  padding-top: calc(60px + 1rem);
  margin-left: 0.5rem;
  margin-right: 0.5rem;
  padding-left: 10rem;
  padding-right: 10rem;
  overflow-y: scroll;
}

::-webkit-scrollbar {
  display: none;
}

@media (max-width: 575.98px) {
  .main {
    display: flex;
    justify-content: start;
    flex-direction: column;
  }

  .left-section,
  .right-section {
    visibility: hidden;
  }

  .middle {
    width: 100%;
    padding: 0;
    margin: 0;
  }
}

.border-light {
  border: 1px solid rgba(0, 0, 0, 0.175);
}

img:hover {
  transition: all .3s ease-in-out;
  opacity: 0.8;
}

.username:hover {
  text-decoration: underline;
}

#reply {
  position: fixed;
  bottom: 5%;
  right: 18%;
}
</style>
