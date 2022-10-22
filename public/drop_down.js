function drop_down_list()
{
  var state = $('#state').val();

    // Alaska and District Columbia have no counties
    if(state == 'AK' || state == 'DC')
    {
    $('#county_drop_down').hide();
    $('#no_county_drop_down').show();
    }
    else
    {
    // Show the Loading...
    $('#loading_county_drop_down').show(); 

    // Hide the drop down
    $('#county_drop_down').hide();

    // Hide the "no counties" message (if it's the case)
    $('#no_county_drop_down').hide();

    $.getScript(state.toLowerCase() +".js", function(){

    populate(document.form.county);

    // Hide the Loading...
    $('#loading_county_drop_down').hide();

    // Show the drop down
    $('#county_drop_down').show();
  });
}
}

$(document).ready(function(){
$("#state").change(drop_down_list);
});

$(window).load(drop_down_list);