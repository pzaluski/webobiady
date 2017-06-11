function order_status_change() {
    $('.js-status').change(
        function() {
            set_ajax_data($(this));
        }
    );
}

function set_paid() {
    $('.js-paid').click(
        function() {
            set_ajax_data($(this));
        }
    );
}

function set_ajax_data(obj) {

    var form = obj.parents('form')[0]
    $.ajax({
          type: "POST",
          data: $(form).serialize(),
          dataType: 'json' /*,
          beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCsrfToken());
                }
            }
            */
        });
}


function getCsrfToken() {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    return csrftoken;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function get_menu_from_url(url) {
    $.ajax({ url: url, success: function(data) { console.log(data); } });
}


function main() {
    order_status_change();
    set_paid();

    //get_menu_from_url('https://www.pyszne.pl/orientalna-li-long');
}

$(document).ready(main);