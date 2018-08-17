$(document).ready(function(){
    $("#insertDivID").hide();

    $("#insertTimeBTN").click(function(){
        $("#insertDivID").toggle();
        $("#stopBTN").click();
    });

    $("#delBTN").click(function(){
        var activityID = $("#activityID").text();

        $.ajax({
            url:'/timer/activities/deleteActivity/',
            type: 'POST',
            data:JSON.stringify({ 
                acitivityID: activityID
            }) 
        });
        
        $(activityID).text("hi");


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
    });

    $(".minsChoice").click(function(){
        $("#minTXT").text(this.text);

    });
    
    $("#submitTimeBTN").click(function(){
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

        //var totalTime = $("#total-time").text();
       //var totalTimeSplit = totalTime.split(":");




        
    });


});