/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

/* obtain stripe_public_key and client_secret from checkout.html using jquery.
    use 'text' to get their ids and 'slice' off first & last character (i.e. quotation marks) */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
/* create variable using stripe public key (using stripe js from base.html) */
var stripe = Stripe(stripe_public_key);
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