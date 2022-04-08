// import jwt_decode from 'jwt-decode';
 
// var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJnZW9yZ2UiLCJmaXJzdF9uYW1lIjoiZ2VvcmdlIiwibGFzdF9uYW1lIjoibWVsZWsiLCJhZGRyZXNzIjoiIiwicGhvbmVfbnVtYmVyIjoiIiwiZW1haWwiOiIifQ.c5TkXb_zDMM3wsmU9l44ZHwz3zFPdb9XroRaZX5Cr5E";
// var decoded = jwt_decode(token);
 
// console.log(decoded);

var jwt = localStorage.getItem("jwt");
if (jwt == null) {
  window.location.href = '../login.html'
}
console.log(jwt);
function loadUser() {
  const xhttp = new XMLHttpRequest();
  const baseUrl = "http://127.0.0.1:5000";
  const params = "username=george&password=george";
  xhttp.open("POST", baseUrl + "/student/login");
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.setRequestHeader("Authorization", "Bearer " + jwt);
  xhttp.send(params);
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      if (objects["status"] == "ok") {
        const user = objects["user"]
        document.getElementById("fname").innerHTML = user["first_name"];
        // document.getElementById("avatar").src = user["avatar"];
        // document.getElementById("username").innerHTML = user["username"];
      }
    }
  };
}

loadUser();

function logout() {
  localStorage.removeItem("jwt");
  window.location.href = '../html/login.html'
}