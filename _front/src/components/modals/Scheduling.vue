<template>
  <b-modal v-model="openSchedulingModal" :hide-footer="true" centered>
    <div class="row">
      <div class="col-12">
        <v-menu ref="menu" v-model="menu1" :close-on-content-click="false" :return-value.sync="schedulingDate" transition="scale-transition" offset-y min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field v-model="schedulingDate" label="Scheduling date" readonly v-bind="attrs" v-on="on" solo></v-text-field>
          </template>

          <v-date-picker v-model="schedulingDate" width="400" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu = false">
              Cancel
            </v-btn>

            <v-btn text color="primary" @click="$refs.menu.save(schedulingDate)">
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
        
        <v-menu ref="menu" v-model="menu2" :close-on-content-click="false" :return-value.sync="schedulingTime" transition="scale-transition" offset-y min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field v-model="schedulingTime" label="Scheduling time" readonly v-bind="attrs" v-on="on" solo></v-text-field>
          </template>

          <v-time-picker @click:minute="$refs.menu.save(schedulingTime)" format="24hr" scrollable></v-time-picker>
        </v-menu>
      </div>      
    </div>
  </b-modal>
</template>

<script>
export default {
  name: 'Scheduling',
  props: {
    comment: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      schedulingDate: null,
      schedulingTime: null,

      menu1: false,
      menu2: false
    }
  },
  computed: {
    openSchedulingModal: {
      get() {
        return this.$store.state.openSchedulingModal
      },
      set() {
        this.$store.commit('toggleModal', 'openSchedulingModal')
      }
    }    
  }
}
</script>
