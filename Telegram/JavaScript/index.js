$.get({
    url:"http://localhost:5000?name=bolin",
    Headers:{"Access-Control-Allow-Origin":true},
    success:function(data){
        console.log(data)
    },
    error:function(err){
        console.log(err)
    }

})