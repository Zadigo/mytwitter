var secondsettings = {
    template: "\
    <div class='settings-group'>\
        <ul class='collapsible'>\
            <li>\
                <div class='collapsible-header'><i class='material-icons'>person</i>First</div>\
                <div class='collapsible-body'><span>Lorem ipsum dolor sit amet.</span></div>\
            </li>\
            <li>\
                <div class='collapsible-header'><i class='material-icons'>filter_drama</i>First</div>\
                <div class='collapsible-body'><span>Lorem ipsum dolor sit amet.</span></div>\
            </li>\
        </ul>\
    </div>\
    "
}

var firstsettings = {
    template: "\
    <div class='settings-group'>\
        <div v-for='option in options' :key='option.title' class='setting flex-setting'>\
            <span class='title'>{{ option.title }}</span>\
            <div class='switch'>\
                <label>\
                    <input @click='applysetting(option.title), option.selected=!option.selected' :checked='option.selected' type='checkbox' name='nightmode' id='nightmode'>\
                    <span class='lever'></span>\
                </label>\
            </div>\
        </div>\
    </div>\
    ",
    data() {
        return  {
            options: [
                {title: "Night mode", selected: false},
                {title: "Another option", selected: false},
            ]
        }
    },
    computed: {
        selectedoptions() {
            return this.$data.options.filter(option => {
                return option.selected === true
            })
        }
    },
    methods: {
        applysetting: function(optiontitle) {
            this.$emit('applysetting', optiontitle)
        }
    }
}

var settingstemplate = {
    // The base component for the settings
    // page of the dashboard
    components: {firstsettings, secondsettings},
    template: "\
        <div>\
            <firstsettings @applysetting='sendrequest' />\
            <secondsettings @applysetting='sendrequest' />\
        </div>\
    ",
    methods: {
        sendrequest: function() {

        }
    }
}