var jwt = localStorage.getItem("jwt");
if (jwt != null) {
  window.location.href = '../index.html'
}

function editInfo() {


  const xhttp = new XMLHttpRequest();
  xhttp.open("POST", "https://www.mecallapi.com/api/studentInfo");
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      if (objects["status"] == "ok") {
        const user = objects["user"]
        document.getElementById("fname").innerHTML = user["fname"];
        document.getElementById("avatar").src = user["avatar"];
        document.getElementById("username").innerHTML = user["username"];
      }
    }
  };
  


  return false;
}