var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
      msg: 'halo vue',
      mapel: '',
      kkm: '',
    },

    mounted() {
      this.getData()
    },

    methods: {
      async getData() {
        await fetch('http://127.0.0.1:8000/api/v1/mapel/')
          .then(response => response.json())
          .then(data => {
            let mapel = data.filter(item => item.id)
          })
      },

      submit() {
        console.log(this.kkm)
      }
    }
  })