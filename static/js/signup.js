function validate(){
    var name=document.getElementById('name').value
    var email = document.getElementById('email').value
    var phno = document.getElementById("phno").value

    if(name==""){
        document.getElementById('name_err').innerHTML="Please enter name"
        document.getElementById('name_err').style.color="red"
        document.getElementById('name').style.border="1px solid red"
        return false
    }
    else{
        document.getElementById('name_err').innerHTML=""
        document.getElementById('name').style.border="1px solid black"
    }
    if (email == "") {
        document.getElementById("email_err").innerHTML = "*please enter the email*"
        document.getElementById("email_err").style.color = "red"
        document.getElementById("email").style.border = "1px solid red"
        return false

    }
    else {
        document.getElementById("email_err").innerHTML = ""
        document.getElementById("email").style.border = "1px solid black"
    }
    if (phno=="") {
        document.getElementById("ph_err").innerHTML = "*please enter phone number*"
        document.getElementById("ph_err").style.color = "red"
        document.getElementById("phno").style.border="1px solid black"
        return false

    }
    else{
        document.getElementById("ph_err").innerHTML = ""
        document.getElementById("phno").style.border = "1px solid black"
    }
}