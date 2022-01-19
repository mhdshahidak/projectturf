function validate(){
    var fname=document.getElementById("fullname").value
    var semail=document.getElementById("mail").value
    var num=document.getElementById("ph").value
    var txtpsw=document.getElementById("psw").value

    if(fname==""){
        document.getElementById("name_err").innerHTML="*please fill the field*"
        document.getElementById("name_err").style.color="red"
        document.getElementById("fullname").style.border="1px solid red"
        return false
    }
    else{
        document.getElementById("name_err").innerHTML=""
        document.getElementById("fullname").style.border="1px solid black"
        
    }

    if(semail==""){
        document.getElementById("mail_err").innerHTML="*please enter the email*"
        document.getElementById("mail_err").style.color="red"
        document.getElementById("mail").style.border="1px solid red"
        return false

    }
    else{
        document.getElementById("mail_err").innerHTML=""
        document.getElementById("mail").style.border="1px solid black"
    }



    if(num==""){
                
        document.getElementById("ph_err").innerHTML="*Enter phone number*"
            document.getElementById("ph_err").style.color="red"
            document.getElementById("ph").style.border="1px solid red"
            return false
    }
    else{
        document.getElementById("ph_err").innerHTML=""
        document.getElementById("ph").style.border="1px solid black"
    }
    if(txtpsw.length<8){
                
        document.getElementById("psw_err").innerHTML="*password should be minimum 8 characters long*"
            document.getElementById("psw_err").style.color="red"
            document.getElementById("psw").style.border="1px solid red"
            return false
    }
    else{
        document.getElementById("psw_err").innerHTML=""
        document.getElementById("psw").style.border="1px solid black"
    }

    if(document.getElementById("psw").value !== document.getElementById("repsw").value){
        document.getElementById("repsw_err").innerHTML="*please confirm correct password you entered above*"
        document.getElementById("repsw_err").style.color="red"
        document.getElementById("repsw").style.border="1px solid red"
        return false
    }

    else{
        document.getElementById("repsw_err").innerHTML=""
        document.getElementById("repsw").style.border="1px solid black"
    }

    
}