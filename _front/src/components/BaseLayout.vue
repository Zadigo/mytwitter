<template>
  <div class="interface">

    <div :class="color" class="col-3 p-5" id="left">
      <aside>
        <div class="aside">
            <b-link v-for="(item, index) in navItems" :key="index" :to="item.name">
              <div class="item">
                <font-awesome-icon :icon="item.icon" class="mr-3 fa-1x" />{{ item.name|title }}
              </div>
            </b-link>

            <b-link>
              <div @click="$store.commit('toggleModal', 'openNewCommentModal')" class="item text-center" id="create">
                Create new
              </div>
            </b-link>
        </div>
      </aside>
    </div>

    <div :class="color" class="col-6 pl-0 pr-0 pt-0" id="middle">
      <div class="header">
        Accueil
      </div>

      <slot></slot>
    </div>
    
    <div :class="color" class="col-3 p-5" id="right">
      <aside>
        <div class="aside">

        </div>
      </aside>
    </div>

  </div>
</template>

<script>
export default {
  name: 'BaseLayout',
  props: {
    color: {
      type: String,
      default: 'blue darken-4'
    }
  },
  data() {
    return {
      navItems: [
        { name: 'feed', icon: 'home' },
        { name: 'notifications', icon: 'bell' },
        { name: 'messages', icon: 'envelope' },
        { name: 'bookmarks', icon: 'bookmark' },
        { name: 'profile', icon: 'user' }
      ]
    }
  }
}
</script>

<style scoped>
  .interface {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    height: 100vh;
    width: 100%;
  }

  .interface #middle {
    overflow: hidden;
    overflow-y: scroll;
    border-left: 1px solid white;
    border-right: 1px solid white;
  }

  .interface #middle::-webkit-scrollbar {
    width: 0;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
  }

  .interface a {
    display: block;
    height: 100%;
    right: 100%;
    font-size: 1.2rem;
    text-align: left;
    text-decoration: none;
    color: white;
  }

  .interface .item {
    padding: 1.5rem;
    border-top-left-radius: 50px;
    border-bottom-left-radius: 50px;
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
    background-color: rgba(255, 255, 255, .2);
    margin-top: 1rem;
  }

  .interface .header {
    font-size: 1.3rem;
    font-weight: 600;
    padding: 1rem;
    color: white;
    border-bottom: 1px solid white;
  }

  .item#create {
    background-color: rgba(255, 255, 255, 1);
  }

  .router-link-exact-active {
    font-weight: 600;
  }
</style>
