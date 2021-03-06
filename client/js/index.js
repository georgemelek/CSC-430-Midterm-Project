import jwt_decode from "https://unpkg.com/jwt-decode@3.1.2?module";

var jwt = localStorage.getItem("jwt");
var decoded = jwt_decode(jwt);

if (jwt == null) {
  window.location.href = '../html/login.html'
}
console.log(decoded);

const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
  const form = document.getElementById('form');

  if (form.style.display === 'none') {
    // 👇️ this SHOWS the form
    form.style.display = 'block';
  } else {
    // 👇️ this HIDES the form
    form.style.display = 'none';
  }
});

const submitBtn = document.getElementById('submitBtn');
submitBtn.addEventListener('click', () => {
  const firstName = document.getElementById("fname").value;
  const lastName = document.getElementById("lname").value;
  const address = document.getElementById("address").value;
  const pNum = document.getElementById("pnum").value;
  const email = document.getElementById("email").value;
  console.log(firstName + " " + lastName + " " + address + " " + pNum + " " + email);
  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://127.0.0.1:5000/student/updateinfo");
  console.log(xhttp.status);
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.send(JSON.stringify({
    "username": decoded["username"],
    "first_name": firstName,
    "last_name": lastName,
    "address": address,
    "phone_number": pNum,
    "email": email,
  }));
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      console.log(objects);
      if (objects['status'] == 'complete') {
        localStorage.setItem("jwt", objects['jwt']);
      }
      console.log(xhttp.responseText);
    }
  };
  return false;
  loadStudentInfo();
});

function editInfo(){
  
}

 function loadStudentInfo() {
  console.log("in loadUser" + decoded["first_name"]);
  document.getElementsByClassName("fname")[0].innerHTML = decoded["first_name"];
  document.getElementById("fnameUser").innerHTML = decoded["first_name"];
  document.getElementById("sname").innerHTML = decoded["first_name"] + ' ' + decoded["last_name"];
  document.getElementsByClassName("username")[0].innerHTML = decoded["username"];
  document.getElementsByClassName("lname")[0].innerHTML = decoded["last_name"];
  document.getElementsByClassName("address")[0].innerHTML = decoded["address"];
  document.getElementsByClassName("pnum")[0].innerHTML = decoded["phone_number"];
  document.getElementsByClassName("email")[0].innerHTML = decoded["email"];
 }

 function loadStudentClasses() {
  const xhttp = new XMLHttpRequest();
  const baseUrl = "http://127.0.0.1:5000";
  const id = decoded["id"];
  xhttp.open("GET", baseUrl + "/student/getclasses/" + id);
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.setRequestHeader("Authorization", "Bearer " + jwt);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      //console.log("objects" + objects[0]["class_description"]);
      var className = document.getElementsByClassName('course');
      for(var index = 0; index < className.length; index++){
        const currentElement = className[index];
        if (typeof(currentElement) != 'undefined' && currentElement != null) {
          currentElement.innerHTML = objects[index]["class_title"];
        }
      }
     
    }
    else {
      //console.log(xhttp.readyState);
      //console.log(xhttp.responseText);
    }
  };
 }

loadStudentInfo();
loadStudentClasses();