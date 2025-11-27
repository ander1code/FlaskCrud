$(function(){
    // CPF
    $('#cpf').mask('000.000.000-00', {placeholder: "___.___.___-__"});

    // income_range
    var $income = $('#salary');

    $income.maskMoney({
        prefix: 'R$ ',
        allowNegative: false,
        thousands: '.',
        decimal: ',',
        affixesStay: true
    });

    if ($income.val()) {
        $income.maskMoney('mask');
    }

    birthday = $('#birthday').val();

    var $picker = $('#birthday_picker');          
    var $input = $('#birthday');              
    var maxDate = moment().subtract(18, 'years'); 

    $picker.datetimepicker({
        format: 'DD/MM/YYYY',
        locale: 'pt-br',
        maxDate: maxDate,
    });

    if(birthday){
        $('#birthday').val(moment(birthday, 'YYYY-MM-DD').format('DD/MM/YYYY'));
    }else{
        $('#birthday').val(moment().subtract(18, 'years').format('DD/MM/YYYY'));
    }

    $('#id_birthday').on('keydown paste', function(e) {
        e.preventDefault();
    });

    setTimeout(function() {
        $("#errors_alert").fadeOut(5000);
    }, 5000);
});