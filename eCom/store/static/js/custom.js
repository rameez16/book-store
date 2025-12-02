$(document).ready(function () {
    console.log("jQuery + custom.js are working!");

    $(".decrement-button").on("click", function () {
        alert("DECREMENT CLICKED");
    });

    // increment function
    $(".increment-button").on("click", function (e) {

        e.preventDefault();
        alert("clicked");

         let input = $(this).closest(".input-group").find(".qty-input");
        //  ✔️ $(this).closest(..).find(..)
        // → Tells jQuery:
        // “Start from the button I clicked, go up until you find the nearest parent container, then look inside that container only.”
        // This makes sure each product controls its own quantity.

        let quantity = parseInt(input.val(),10)

        let max = parseInt(input.attr("max"));

        if (quantity < max) {

            quantity++

        }

        input.val(quantity)


    });

    // decrement function


    $(".decrement-button").on("click", function (e) {

        e.preventDefault();

         let input = $(this).closest(".input-group").find(".qty-input");
     

        let quantity = parseInt(input.val(),10)

        console.log("clicked decrement")

        console.log(quantity)

        if (quantity > 1) {

            quantity--

        }

        input.val(quantity)


    });


 
});