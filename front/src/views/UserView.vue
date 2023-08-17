<template>
  <section class="user">
    <div class="header">
      <img src="https://placehold.co/1200x600" class="img-fluid" alt="">
      <div class="p-4">
        <h3 class="text-light m-0">Some user</h3>
        <p class="text-light">@some-user</p>
        <p class="mt-3">Chargée de Mission Culture. Paris. "Castigat ridendo mores" (cherche dans le Gaffiot !)</p>
        <div class="d-flex justify-content-left gap-3">
          <span>1 992 abonnements</span>
          <span>31,7 k abonnés</span>
        </div>
      </div>
    </div>
    <replies-item />
  </section>
</template>

<script>
import { defineAsyncComponent } from 'vue'
import { loadComponent } from '@/composables/utils'
import LoadingPostItem from '@/components/LoadingPostItem.vue'
export default {
  components: {
    RepliesItem: defineAsyncComponent({
      loader: loadComponent('RepliesItem'),
      loadingComponent: LoadingPostItem,
      delay: 1000
    })
  }
}
</script>

<style scoped>
.header {
  min-height: 300px;
  width: 100%;
}
</style>
