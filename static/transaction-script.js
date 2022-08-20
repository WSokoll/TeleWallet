$().ready(function () {

let stan = parseFloat($("#stan-konta").text());

$("#stan-po").text(stan);

$( "#kwota" ).keyup(function() {
    let kwota = parseFloat($("#kwota").val());
    let wynik;
    if(kwota <= stan){
        wynik = (stan - kwota).toString();
    }else{
        wynik = "Nie posiadasz wystarczających środków";
    }
    $("#stan-po").text(wynik);
});


});