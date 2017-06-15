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
          dataType: 'json'
        });
}

function get_menu_modal() {
    $("#menuModal").on("show.bs.modal", function(e) {
        var link = $(e.relatedTarget);
        $(this).find(".modal-body").load(link.attr("href"));
    });
}


function main() {
    order_status_change();
    set_paid();
    get_menu_modal();
}

$(document).ready(main);