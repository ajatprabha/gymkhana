/**
 * Created by Ajat Prabha on 22-07-2017.
 */
var csrf_token;
var email;
var form_bool = $('input#request').val();

$(document).ready(function () {
    csrf_token = $('.token').find('input').val();
    if (form_bool === '1') {
        $('form#verify-form').css('display', 'none');
        $('form#reg-form').css('display', 'block');
    }
    else if (form_bool === '0') {
        $('form#verify-form').css('display', 'block');
        $('form#reg-form').css('display', 'none');
    }
});

$('#verify-form').submit(function (e) {
    e.preventDefault();
    $('#reg_container').find('div#error').text('');
    email = $('#verify-form').find('#id_email').val();
    if (email.endsWith('@iitj.ac.in')) {
        $('form#verify-form').css('display', 'none');
        $('form#reg-form').css('display', 'block');
    }
    else {
        $('#reg_container').find('div#error').text('Not a Valid Email!');
    }
});