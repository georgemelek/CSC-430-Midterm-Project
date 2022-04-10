var jwt = localStorage.getItem("jwt");
if (jwt != null) {
  window.location.href = '../html/index.html'
}

function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const xhttp = new XMLHttpRequest();
  const baseUrl = "http://127.0.0.1:5000";
  xhttp.open("POST", "http://localhost:5000/student/login");
  console.log(xhttp.status);
  xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xhttp.send(JSON.stringify({
    "username": username,
    "password": password
  }));
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      const objects = JSON.parse(this.responseText);
      console.log(objects);
      if (objects['status'] == 'complete') {
        localStorage.setItem("jwt", objects['jwt']);
        Swal.fire({
          text: objects['message'],
          icon: 'success',
          confirmButtonText: 'OK'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = '../html/index.html';
          }
        });
      } else {
        Swal.fire({
          text: objects['message'],
          icon: 'error',
          confirmButtonText: 'OK'
        });
      }
      console.log("in login" + xhttp.responseText);
    }
  };
  return false;
}