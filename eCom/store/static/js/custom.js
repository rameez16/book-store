$(document).ready(function () {
    console.log("jQuery + custom.js are working!");



    // increment function
    $(".increment-button").on("click", function (e) {

        e.preventDefault();



        let input = $(this).closest(".input-group").find(".product_qty");
        //  ✔️ $(this).closest(..).find(..)
        // → Tells jQuery:
        // “Start from the button I clicked, go up until you find the nearest parent container, then look inside that container only.”
        // This makes sure each product controls its own quantity.

        let quantity = parseInt(input.val(), 10)

        console.log(quantity)

        let max = parseInt(input.attr("max"));

        if (quantity < max) {

            quantity++

        }

        input.val(quantity)


    });

    // decrement function


    $(".decrement-button").on("click", function (e) {

        e.preventDefault();

        let input = $(this).closest(".input-group").find(".product_qty");


        let quantity = parseInt(input.val(), 10)



        if (quantity > 1) {

            quantity--

        }

        input.val(quantity)


    });


    $(".addtocartbtn").on("click", function (e) {

        e.preventDefault();

        let product_id = $(this).closest(".prod").find('.product-id').val();
        let quantity = $(this).closest(".prod").find(".product_qty").val();
        let token = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax({
            method: 'POST',
            url: '/add-to-cart',
            data: {
                'product_id': product_id,
                'product_qty': quantity,
                csrfmiddlewaretoken: token
            },
            dataType: 'json',
            success: function (response) {

                if (response.status === 'User not Authenticated') {

                    alertify.confirm(
                        "Login Required",
                        response.message,
                        function () {
                            window.location.href = response.redirect_url;
                        },
                        function () {
                            alertify.error("Login cancelled");
                        }
                    );
                }

                else {
                    alertify.success(response.status);
                }
            }
        });

    });


    // Initialize Alertify with custom settings
    function initAlertify() {
        // Basic settings
        alertify.defaults = {
            // Notifier settings
            notifier: {
                position: 'top-right',
                delay: 4,
                closeButton: true,
                maxItems: 4
            },

            // Dialog settings
            modal: true,
            basic: false,
            frameless: false,
            movable: true,
            resizable: true,
            autoReset: true,
            closable: true,
            closableByDimmer: true,
            maintainFocus: true,

            // Theme settings
            theme: {
                input: 'form-control',
                ok: 'btn btn-primary btn-lg',
                cancel: 'btn btn-secondary btn-lg'
            },

            // Text
            glossary: {
                title: 'Notification',
                ok: 'Confirm',
                cancel: 'Cancel',
                acccpt: 'Accept',
                deny: 'Deny',
                confirm: 'Are you sure?',
                buttons: {
                    ok: 'OK',
                    cancel: 'Cancel',
                    yes: 'Yes',
                    no: 'No'
                }
            }
        };

        // Set specific positions
        alertify.set('notifier', 'position', 'top-right');

        // Customize success messages
        alertify.success = function (message, wait) {
            alertify.notify(message, 'success', wait || 4, function () {
                console.log('Success message closed:', message);
            });
        };

        // Customize error messages
        alertify.error = function (message, wait) {
            alertify.notify(message, 'error', wait || 5, function () {
                console.log('Error message closed:', message);
            });
        };

        // Customize warning messages
        alertify.warning = function (message, wait) {
            alertify.notify(message, 'warning', wait || 4);
        };
    }


    $('.change-quantity').on("click", function (e) {

        e.preventDefault()

        let product_id = $(this).closest('.input-group').find('.prod-id').val()
        let quantity = $(this).closest('.input-group').find('.product_qty').val()
        let token = $('input[name="csrfmiddlewaretoken"]').val();

        console.log(product_id, quantity, token)


        $.ajax(

            {
                method: 'POST',
                url: '/update-cart',
                data: {
                    'product_id': product_id,
                    'product_qty': quantity,
                    csrfmiddlewaretoken: token
                },

                success: function (response) {

                    console.log(response)

                }
            }

        )


    })


    $('.remove-item').on("click", function (e) {

        e.preventDefault()

        let product_id = $(this).closest('.remove').find('.prod-id').val()

        console.log(product_id)
        let token = $('input[name="csrfmiddlewaretoken"]').val();

        $.ajax(

            {

                method: 'POST',
                url: '/delete-cart-item',
                data: { 'product_id': product_id, csrfmiddlewaretoken: token },
                success: function (response) {
                    console.log(response);
                    alertify.success("item removed from cart");
                    location.reload();
                }

            }
        )

    })





});