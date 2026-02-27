let login_btn=document.getElementById("login_btn")
login_btn.addEventListener("click",(e)=>{
    e.preventDefault()
    let email=document.getElementById("email").value 
    let password=document.getElementById("password").value 
    let role=document.getElementById("role").value 

    let login_p_d={
     e:email,
     p:password,
     r:role
    }
    console.log(login_p_d)

    fetch("http://127.0.0.1:8000/login_validation/",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(login_p_d)
    }).then(res=>res.json()).then(res=>{
        console.log(res,"drs")
        window.location.href=`/${res.r_url}/${res.id}`
        // window.location.href=`/${res.r_url}`
    })
})