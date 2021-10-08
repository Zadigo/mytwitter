<template>
  <div class="interface">

    <div :class="color" class="col-3 p-5">
      <aside>
        <div class="aside">
          <ul class="navigation">
            <li>Home</li>
            <li>Messages</li>
          </ul>
        </div>
      </aside>
    </div>

    <div :class="color" class="col-6" id="messages">
      <slot></slot>
    </div>
    
    <div :class="color" class="col-3 p-5">
      <aside>
        <div class="aside">
          Side
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
  }
}
</script>

<style scoped>
  .interface {
    display: flex;
    flex-direction: row;
    height: 100vh;
    width: 100%;
  }

  .navigation ul li {
    padding: 3rem;
    font-size: 2.5rem;
    color: white;
  }

  #messages {
    overflow: hidden;
    overflow-y: scroll;
  }
</style>
