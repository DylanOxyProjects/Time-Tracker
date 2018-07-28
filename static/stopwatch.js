function Stopwatch(stopwatchText){
    
    var startTimer = true;
    var time;
    var interval;
    var offset;
    var hours = "0000";
    var hoursINT = 0;

    function update() {

        if (this.isOn){
            time += delta();
        }

        var formattedTime = timeFormatter(time);
        stopwatchText.textContent = formattedTime;

    }
    function delta() {

        var now = Date.now();
        var timePassed = now - offset;
        offset = now;
        return timePassed;


    }
    function timeFormatter(timeInMilliseconds) {

        var time = new Date(timeInMilliseconds);
        var minutes = time.getMinutes().toString();
        var minutesINT = time.getMinutes;
        var seconds = time.getSeconds().toString();
        var secondsINT = time.getSeconds();
        var milliseconds = time.getMilliseconds().toString();

        

        if (minutes.length < 2){
            minutes = '0' + minutes;
        }
        else if(minutesINT == 60 && secondsINT == 60 && milliseconds == 999){
            hoursINT += 1;
            hours = hoursINT.toString();
            while (hours.length < 3){
                hours = "0" + hours;
            }
        }

        if (seconds.length < 2){
            seconds = '0' + seconds;
        }

        while (milliseconds.length < 3){
            milliseconds = '0' + milliseconds;
        }

        return hours + ":" + minutes + ":" + seconds  + "." + milliseconds;


    }

    function timeCalculator(timeInput){

        if(stopwatchText.textContent == "0000:00:00.000"){
            time = 0;
            return
        }
        else{
            var timeList = timeInput.split(":");
            var hourToMil = parseInt(timeList[0]) * 60000 * 60;
            var minToMil = parseInt(timeList[1]) * 60000;
            var secMilList = timeList[2].split(".");
            var secToMil = parseInt(secMilList[0]) * 1000;
            time = parseInt(secMilList[1]) +  secToMil + minToMil + hourToMil;
            return
        }

    }


    this.isOn = false;

    this.start = function() {

        if (!this.isOn){

            if (startTimer){
                timeCalculator(stopwatchText.textContent)
                startTimer = false;
            }

            interval = setInterval(update.bind(this), 10);
            offset = Date.now();
            this.isOn = true;
        }

    };
    this.stop = function() {

        if (this.isOn){
            clearInterval(interval);
            this.interval = null;
            this.isOn = false;
            startTimer = true;
        }

    };

}




