var contactform = new Vue({
    el: "#app",
    template: "\
        <form @submit.prevent='doemail'>\
            <div v-show='formmessage.show' :class='messageclass'>{{ formmessage.message }}</div>\
            <div v-show='!formmessage.show'>\
                <div v-for='field in fields' :key='field.name' class='input-field'>\
                    <input v-model='user[field.name]' :type='field.type' :name='field.name' :id='field.name' :placeholder='field.placeholder'>\
                </div>\
                <button class='btn-large red darken-3 waves-effect waves-light' type='submit' id='btn_send_message'><i class='material-icons left'>send</i>Send</button>\
            </div>\
        </form>\
    ",
    data() {
        return  {
            formmessage: {show: false, error: false, message: ""},
            fields: [
                {type: "email", name: "email", placeholder: "Email"},
                {type: "text", name: "telephone", placeholder: "Telephone"},
                {type: "text", name: "message", placeholder: "Message"}
            ],
            user: {email: "", telephone: "", message: ""}
        }
    },
    computed: {
        messageclass() {
            if (this.$data.formmessage.error === true) {
                return "message red lighten-4"
            } else {
                return "message green lighten-4"
            }
        }
    },
    methods: {
        doemail: function() {
            var self = this
            var data = self.$data.user
            data["csrfmiddlewaretoken"] = $(".csrf input[name='csrfmiddlewaretoken']").val()

            if (self.$data.user.message === "" || self.$data.user.email === "" || self.$data.user.telephone === "") {
                self.$data.formmessage.show = true
                self.$data.formmessage.error = true
                self.$data.formmessage.message = "Veuillez remplir le formulaire"
                return
            }

            $.ajax({
                type: "post",
                url: window.location.href,
                data: data,
                dataType: "json",
                success: function (response) {
                    self.$data.formmessage.show = true
                    self.$data.formmessage.error = false
                    self.$data.formmessage.message = "Message envoyé"
        
                }
            });
        }
    }
})