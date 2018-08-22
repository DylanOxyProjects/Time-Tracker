$(document).ready(function(){

    var hourAppendTxt = "00";
    var minAppendTxt = "00";
    $("#firstActivityItem").hide(); 


    function saveTime(){    
        var activityID = $("#activityID").text();

        var currentTime = $("#total-time").text();
        currentTimeList = currentTime.split(":");
        currentTimeHours = parseInt(currentTimeList[0]);

        var currentLevel = $("#activityLVL").text();
        var newLvl = levelWatch(currentLevel, currentTimeHours);
        $("#activityLVL").text(newLvl);




        $.ajax({
            url:'/timer/activities/autoSave/',
            type: 'POST',
            data:JSON.stringify({ 
                activityID: activityID,
                currentTime: currentTime, 
                newLvl: newLvl
            }) 
        });
    }



    $("#delBTN").click(function(){
        var activityID = $("#activityID").text();
        jQuery('#activitiesNav')[0].click();

        $.ajax({
            url:'/timer/activities/deleteActivity/',
            type: 'POST',
            data:JSON.stringify({ 
                acitivityID: activityID
            }) 
        });

        
        


    });

    // set txt of activities drop down
    $('#activitiesTXT').text($("#highlightActivity").text());

    // listener to change txt on button click of activity drop down
    $(".activityChoice").click(function(){
        $('#activitiesTXT').text(this.text);

        if ($('#activitiesTXT').text() == $("#highlightActivity").text()){
            $('#activitiesTXT').css("font-weight", "Bold");
        }
        else{
            $('#activitiesTXT').css("font-weight", "normal");
        }
    });



    $(".hourChoice").click(function(){
        $("#hourTXT").text(this.text);
        hourAppendTxt = this.text;
        if (parseInt(hourAppendTxt) < 10){
            hourAppendTxt = "0" + hourAppendTxt;
        }
        $("#submitTxt").text(hourAppendTxt + ":" + minAppendTxt + ":00.000");

    });

    $(".minsChoice").click(function(){
        $("#minTXT").text(this.text);
        minAppendTxt = this.text;
        if (parseInt(minAppendTxt) < 10){
            minAppendTxt = "0" + minAppendTxt;
        }
        $("#submitTxt").text(hourAppendTxt + ":" + minAppendTxt + ":00.000");

    });

    $("#submitTxt").text(hourAppendTxt + ":" + minAppendTxt + ":00.000");
    
    $("#submitTimeBTN").click(function(){
        $("#stopBTN").click();
        var activityID = $("#activityID").text();
        var hours = $("#hourTXT").text();
        var minutes = $("#minTXT").text();

        $.ajax({
            url:'/timer/activities/insertTime/',
            type: 'POST',
            data:JSON.stringify({ 
                acitivityID: activityID,
                hours: hours, 
                minutes: minutes
            }) 
        });
    });


    window.setInterval(function(){saveTime()}, 5000);





});