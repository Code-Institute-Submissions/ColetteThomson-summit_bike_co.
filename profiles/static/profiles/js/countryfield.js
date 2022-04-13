/* store value of country field when page loads */
let countrySelected = $('#id_default_country').val();
/* if first option selected, value will be an empty string */
/* if country selected is false (i.e. first option) */
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
/* capture change event and get the value of it */
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    /* determine correct colour */
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});