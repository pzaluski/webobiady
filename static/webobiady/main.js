function order_status_change() {
    $('.js-status-change').change(
        function() {
            var oid = $(this).attr('name').replace('order_status_', '');
            var oval = $(this).val();

            $.ajax({
              type: "GET",
              url: '/orders/order/edit/',
              data: {'id' : oid, 'status' : oval},
              dataType: 'json'
            });
        }
    );
}


function main() {
    order_status_change();
}

$(document).ready(main);