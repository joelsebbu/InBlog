
function customFetch(url,type,data){

    if(type== "GET"){
        fetch(url,{
            methods: type
        })
        .then( res => {
            if(res.ok){
                console.log("GET Successfull")
                // window.location.href=url
            }
            
        })
        
    }
    else if(type == "POST"){
        fetch(url,{
            methods: type,
            headers: {
                "Content-type": "application/json"
            },
            body : JSON.stringify(data)
        })
        .then( res => {
            if(res.ok){
                console.log("POST Successfull")
            }
        })
        
    }
}

function signup(){
    let email = document.getElementById("email").value
    let name = document.getElementById("name").value
    let pass = document.getElementById("password").value
}

function login(){
    let submit =document.getElementById("submit").value
    let email = document.getElementById("email").value
    let pass = document.getElementById("password").value
    console.log(email)
    console.log(pass)
    
    let data ={
        "email":email,
        "password": pass
    }
    alert("home")
    customFetch('/login',"POST",data)

}