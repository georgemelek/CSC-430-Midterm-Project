var jwt = localStorage.getItem("jwt");
if (jwt == null) {
  window.location.href = '../login.html'
}

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