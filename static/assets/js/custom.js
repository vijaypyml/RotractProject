// Custom Javascript
$(document).ready(function() {
    $("#form_name2, #form_name9, #form_name4").change(function(){
        var selectval = $(this).children("option:selected").val();
        var showdiv = $(this).parent().parent().next();
        if (selectval == "others") {
            $(showdiv).show();
            $(showdiv).find("input").focus();
        } else {
            $(showdiv).hide();
        }
    });
});
