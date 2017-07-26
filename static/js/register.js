/**
 * Created by Ajat Prabha on 22-07-2017.
 */
var csrf_token;
var email;
var form_bool = $('input#request').val();

$(document).ready(function () {
    csrf_token = $('.token').find('input').val();
    if (form_bool === '1') {
        $('div.reg-form').css('display', 'block');
        $('form#reg-form').css('display', 'block');
    }
    else if (form_bool === '0') {
        $('div.view').css('display', 'block');
        $('form#verify-form').css('display', 'block');
    }
});

function update_vars (username, email) {
    $('form#reg-form').find('#id_username').val(username);
    $('form#reg-form').find('#id_email').val(email);
}

$('#verify-form').submit(function (e) {
    e.preventDefault();
    $('#reg_container').find('div#error').text('');
    email = $('#verify-form').find('#id_email').val();
    if (email.endsWith('@iitj.ac.in')) {
        $('div.view').css('display', 'none');
        $('div.reg-form').css('display', 'block');
        $('form#reg-form').css('display', 'block');
        var username = email.split("@")[0];
        update_vars(username, email);
    }
    else {
        $('#reg_container').find('div#error').text('Not a Valid Email!');
    }
});