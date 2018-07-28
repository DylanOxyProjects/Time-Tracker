    
function loadXMLDoc(){
    var xhttp = new XMLHttpRequest();
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // Typical action to be performed when the document is ready:

        }
    }
    var timeElapsed = document.getElementById("total-time");
    var timeElapsedText = timeElapsed.innerHTML;
    var title = document.getElementById("activity-title");
    xhttp.open("POST", "/timer/activities/update_stopwatch/", true);
    xhttp.withCredentials = true;
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);   
    xhttp.setRequestHeader("Accept", "application/json");
    xhttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    timeElapsedText += "$$TEXT$$" + title.innerHTML;
    xhttp.send(timeElapsedText);


    

};

