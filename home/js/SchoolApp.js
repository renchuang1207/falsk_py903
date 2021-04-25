let data = {
    schools:[]
};
let vm = new Vue({
    el:'#school-app',
    data,
    mounted(){
        fetch('http://127.0.0.1:5000/bank/finds')
        .then(resp=>resp.json())
        .then(data=>{
//            this.schools.splice(0,data.data.length,data.data)
              for (i in data.data){
                  this.schools.push(data.data[i])
              }
        })
    }
},
);