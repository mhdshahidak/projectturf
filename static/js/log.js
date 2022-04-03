function login(){
    var username=document.getElementById("uname")
    var password=document.getElementById("psw")

    if(username==""){
        document.getElementById('uerror').innerHTML="Please Enter username"
        console.log("working")
        return false
    }
}