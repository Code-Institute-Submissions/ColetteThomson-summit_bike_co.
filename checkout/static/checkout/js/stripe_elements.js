/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

/* obtain stripe_public_key and client_secret from checkout.html using jquery.
    use 'text' to get their ids and 'slice' off first & last character (i.e. quotation marks) */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
/* create variable using stripe public key (using stripe js from base.html) */
var stripe = Stripe(stripePublicKey);
/* create an instance of stripe.elements */
var elements = stripe.elements();
/* card element styling (adapted from stripe js documentation) */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        /* bootstrap danger class color */
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
/* use 'elements' to create a card element with style parameters */
var card = elements.create('card', {style: style});
/* mount card to div in checkout.html*/
card.mount('#card-element');


/* handle realtime validation errors on the card element */
/* add listener to listen for changes */
card.addEventListener('change', function (event) {
    /* check if any errors */
    var errorDiv = document.getElementById('card-errors');
    /* if there is an error, display message (card-error div in checkout.html) */
    if (event.error) {
        /* alert icon from font awesome */
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

/* Handle form submit (adapted from js stripe docs)*/

/*  obtain form element */
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    /* eventlistener to prevent default action of post, and instead execute this code */
    ev.preventDefault();
    /* disable card element */
    card.update({ 'disabled': true});
    /* disable submit button */
    $('#submit-button').attr('disabled', true);
    /* fade payment-form */
    $('#payment-form').fadeToggle(100);
    /* trigger overlay (over payment form) */
    $('#loading-overlay').fadeToggle(100);
    /* send card information securely to stripe */
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            /* add payment info into webhook (from Stripe) */
            billing_details: {
                name: $.trim(form.full_name.value), // trim off excess whitespace
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        },
        shipping: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postal_code: $.trim(form.postcode.value),
                state: $.trim(form.county.value),
            }
        },
    /* execute this function on the result */
    }).then(function(result) {
        /* if there is an error, display message (card-error div in checkout.html) */
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            /* alert icon from font awesome */
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            /* if there's an error, re-enable card element and submit button
            to allow user to fix this */
            $(errorDiv).html(html);
            /* fade payment-form */
            $('#payment-form').fadeToggle(100);
            /* trigger overlay (over payment form) */
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            /* if payment intent is successful, submit the form */
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});