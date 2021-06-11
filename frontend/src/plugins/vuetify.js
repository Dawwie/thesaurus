import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
            primary: '#264653',
            secondary: '#E9C46A',
            error: '#E76F51',
            info: '#2A9D8F',
            success: '#8AB17D',
            warning: '#E9C46A',
            },
        },
    },
});
