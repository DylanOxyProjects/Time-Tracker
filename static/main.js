var timer = document.getElementById("total-time");
var currentTime = document.getElementById("currentTime");
var startBTN = document.getElementById("start-button");
var stopBTN = document.getElementById("stop-button");


var totalTimeKeeper = new Stopwatch(timer);
var currentTimeKeeper = new Stopwatch(currentTime);

startBTN.addEventListener("click", function(){
    if (!totalTimeKeeper.isOn){
        totalTimeKeeper.start();
        currentTimeKeeper.start();
    }
});


stopBTN.addEventListener("click", function(){
    if (totalTimeKeeper.isOn){
        totalTimeKeeper.stop();
        currentTimeKeeper.stop();

        loadXMLDoc();

    }
    
});
 