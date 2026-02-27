console.log("reg form js file");

// let f= document.getElementById("reg_form")
// console.log(f)
// let name=document.getElementById("name").value ;
// let email = document.getElementById("email").value;

// console.log(name, "name");

let reg_btn = document.getElementById("reg_btn");

reg_btn.addEventListener("click", (e) => {
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let phNum = document.getElementById("phNum").value;
  let password = document.getElementById("password").value;
  let c_password = document.getElementById("c_password").value;
  let role = document.getElementById("role").value;
  let spec = document.getElementById("spec").value;

  console.log(role)
  e.preventDefault();
  let r_user = {
    n: name,
    e: email,
    ph: phNum,
    p: password,
    cp: c_password,
    r:role,
    s:spec
  };

  console.log(r_user)
  fetch("http://127.0.0.1:8000/register/",{
    method:"POST",
    headers:{
        "Content-Type":"application/json"
    },
    body:JSON.stringify(r_user)
  }).then(res=>res.json()).then(res=>console.log(res)).catch(err=>console.log(err))
//   console.log(r_user);
});
