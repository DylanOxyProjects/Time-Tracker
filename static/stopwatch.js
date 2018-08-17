function Stopwatch(stopwatchText, activityHoursStr, activityHoursInt){
    
    var startTimer = true;
    var time;
    var interval;
    var offset;
    var hours = activityHoursStr;
    

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
        var minutesINT = time.getMinutes();
        var seconds = time.getSeconds().toString();
        var secondsINT = time.getSeconds();
        var milliseconds = time.getMilliseconds().toString();
        if (milliseconds.length == 3){
            var milliArray = milliseconds.split("");
            var largeMilliInt =  parseInt(milliArray[0])
            var middleMilliInt =  parseInt(milliArray[1])

        }
        var millisecondsInt = time.getMilliseconds();

        


        if (minutesINT == 59 && secondsINT == 59 && largeMilliInt == 9 && middleMilliInt == 9 ){
            hoursInt = parseInt(activityHoursStr);
            hoursInt = hoursInt + 1
            minutes = "00";
            seconds = "00";
            milliseconds = "000";
            hours = hoursInt.toString();
        }


        while (hours.length < 4){
            hours = '0' + hours;
        }

        if (minutes.length < 2){
            minutes = '0' + minutes;
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
        var timeList = timeInput.split(":");
        var hourToMil = parseInt(timeList[0]) * 60000 * 60;
        var minToMil = parseInt(timeList[1]) * 60000;
        var innerList = timeList[2];
        innerList = innerList.split(".");
        var secToMil = parseInt(innerList[0]) * 1000;
        var mil = parseInt(innerList[1]);
        time = mil + secToMil + minToMil;
        return time;
    }

    

    this.isOn = false;

    this.start = function() {

        if (!this.isOn){

            if (startTimer){
                startTimer = false;
                time = timeCalculator(stopwatchText.textContent);
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




