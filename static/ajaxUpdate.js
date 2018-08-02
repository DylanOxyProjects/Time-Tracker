    
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
    var activityID = document.getElementById("activityID");
    var activityIDInt = activityID.textContent;
    var activityIDString = activityIDInt.toString();

    xhttp.open("POST", "/timer/activities/update_stopwatch/", true);
    xhttp.withCredentials = true;
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);   
    xhttp.setRequestHeader("Accept", "application/json");
    xhttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    timeElapsedText += "$$TEXT$$" + activityIDString;
    xhttp.send(timeElapsedText);
};

function saveActivityTitleAjax(activityID){
    var xhttp = new XMLHttpRequest();
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // Typical action to be performed when the document is ready:

        }
    }
    
    xhttp.open("POST", "/timer/activities/editActivityTitle/", true);
    xhttp.withCredentials = true;
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);   
    xhttp.setRequestHeader("Accept", "application/json");
    xhttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhttp.send(activityID);
}

function deleteActivityAjax(activityID){
    var xhttp = new XMLHttpRequest();
    var csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // Typical action to be performed when the document is ready:

        }
    }
    
    xhttp.open("POST", "/timer/activities/delete_activity", true);
    xhttp.withCredentials = true;
    xhttp.setRequestHeader("X-CSRFToken", csrf_token);   
    xhttp.setRequestHeader("Accept", "application/json");
    xhttp.setRequestHeader("Content-Type", "application/json; charset=utf-8");
    xhttp.send(activityID);
}

