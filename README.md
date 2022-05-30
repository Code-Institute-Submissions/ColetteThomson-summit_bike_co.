# Summit Bike Co. Mountain Bike Shop

## Purpose
Summit Bike Co. is a mountain bike stockist based in UK that offers both an online shopping experience, as well as the option of visiting their stores. Users can register as an account holder and are able to save contact, delivery and payment information under their own profile. Users without an account are also able to make purchases but their contact, delivery and payment information will not be retained by Summit Bike Co.  All products on the website will have a full specification and description of each bike model, along with price, a selection of sizes and required quantity to assist users in choosing a mountain bike best suited to their requirements. A link on each individual product page gives the user quick access to the 'Buying Guides' section, should they need help with their decision. Summit Bike Co. participates in the UK Government 'Cycle to Work' initiative and have designed a simple process to assist employers in joining the scheme.  General company information is present in the 'About Us' and 'Contact Us' sections.  Summit Bike Co. has a blog called 'BikeTalk' where registered users can read and leave comments on various mountain biking articles. Summit Bike Co. also offers users the option of subscribing to their monthly newsletter.  Users can stay in touch by following the social media of Summit Bike Co.

## E-Commerce Business Model
E-commerce sales have risen substantially over the last few years, so starting an online store would make sound business sense for Summit Bike Co. The following benefits will be realised through building an e-commerce platform:
* Increased brand awareness:  with increasing competition within the outdoor fitness community, our exposure will increase through customer centric market strategies, social media presence and digital ethics
* Open for business 24/7/365:  with our intuitive product layout; free delivery service; improved customer engagement and experience; and easy to understand buying guides - shoppers can feel secure in their choice of products.  This will drive our value stream optimisation leading to benefits realisation
* International sales: our website caters for sales and delivery to most countries in the world, thereby increasing our brand awareness and revenue
* Online stores are social: our BikeTalk blog encourages shoppers to interact with our posted articles, as well as imparting bike knowledge and general biking news and promoting of events
* Easy to re-target and re-market to customers:  with our active BikeTalk comes the potential for customers to browse through products while reading our blog posts.  The online shopping experience is also less invasive and pressured, potentially encouraging customers to browse and therefore purchase more products

## High level overview of user roles within Summit Bike Co:

* **Superuser (admin)** (and 'store owner' if applicable) - has full CRUD (create, read (view), update, delete) from the admin panel and across all frontend pages. For the 'BikeTalk' app - admin will need to approve all comments from users, before they will appear as published comments underneath the relevant article.
* **Registered Users (account holders)** - will have full CRUD to their own Profile information (My Profile page); be able to edit and delete products within their own Shopping Bag (Checkout page); and read only access to their own Order History (My Profile page) and to all other website pages.
* **Unregistered Users** - will be able to edit and delete products within their own Shopping Bag (Checkout page); and have read only access to all web pages - but no access to the My Profile page.

## The Summit Bike Co. website pages are as follows:
* **Home** (index.html): landing page
* **All Mountain Bikes**: dropdown opens the 'product' page. The options: 'By Price', By Rating'; 'By Brand'; 'By Type'; and 'All Bikes' are different sort options of the various products sold by Summit Bike Co.<br>
The page: **bike_detail** (which displays individual product information), can then be accessed from the chosen sort of the 'product' page.
* **Buying Guides**: dropdown reveals:  'What is a Mountain Bike'; 'Mountain Bike Sizing Guide'. <br>
* **About Us**: dropdown reveals:  'Who We Are'; 'Cycle to Work Scheme; 'Terms and Conditions'.<br> 
* **Contact Us**: dropdown reveals:  'Contact Details'.<br>
* **BikeTalk**: (under the 'Contact Us' dropdown) reveals: 'BikeTalk'; 'Article Name...'<br>
* **My Account**: dropdown reveals:  'Stock Management'; 'My Profile'; 'Logout'.<br>

The page **Stock Management** is permissions based and only appears if the user is a superuser (admin).<br>
The page **My Profile** only appears if the user is registered (account holder). <br>

**Allauth Account pages**
* **Logout**: visible when users are logged in
* **Login**: visible when users are logged out
* **Register**: visible when users are logged out

The live project can be found [here](https://summit-bike-co.herokuapp.com/)

## Facebook screenshots
A mockup of the Summit Bike Co. Facebook page can be found [here](/media/SBC_facebook_mockup.jpg)

## Site Map
The site map and robots.txt are located against the root of summit_bike_co.

## Search Engine Optimisation (SEO)
###  Keywords
As Summit Bike Co. specialises in selling only mountain bikes, keywords were selected with this in mind.<br>
Placement of these keywords within the website has been implemented where possible using semantic HTML elements (i.e. headings) and one keyword utilises an anchor tag.<br>
Research (using Wordtracker.com) into short-tail and long-tail keywords suitable for Summit Bike Co. yielded
the following:<br>

#### Shortail keywords
The following **product based keyword** enquiry showed a very high volume and high level of organic competition.
* mountain bikes
Represented in multiple places throughout the website <br>

#### Longtail Keywords
The following **product based keyword** enquiries showed a mid-range volume of searches, and a mid-range level of organic competition:<br>
* full suspension mountain bikes
* hardtail mountain bikes
These are seen in both the individual 'Bike Model name ...' page and the 'All Mountain Bikes' page
and are represented as:<br>
* A 'h2' on each individual bike_detail page along with a reference in the relevant individual bike's product 'description' section
* as a dropdown option ('By Type') under the 'All Mountain Bikes' menu option
* as a sort option on both the 'Bike Model name ...' pages and the 'All Mountain Bikes' page
<br>

The following **information based keyword** enquiries showed a lower volume of searches, but also low organic
competition:<br>
* what is a mountain bike
* what are hardtail mountain bikes
* what are full suspension mountain bikes <br>
Represented as: 3 x 'h2's on the 'What is a Mountain Bike' page accessed via the dropdown option under the 'Buying Guides' menu <br>

* what size mountain bike do I need <br>
Represented as: a 'h3' on the 'Mountain Bike Sizing Guide' page accessed via the dropdown option under the 'Buying Guides' menu <br>

**Long-tail keywords pertaining to information from external 3rd party organisations:**<br>
This long-tail keyword showed a high volume, with mid to high level of organic competition.  As this particular scheme is a UK Government Initiative and is implemented by most mountain bike sellers, the high volume and high competition are deemed not have an impact on Summit Bike Co. as a business - but representation is essential in demonstrating that Summit Bike Co. both supports and offers this scheme to their customers:
* cycle to work scheme <br>
Represented as: an anchor tag on the 'Cycle to Work Scheme' page accessed via the dropdown option under the 'About Us' menu <br>

## Entity Relationship Diagram (ERD) for Summit Bike Co.
There are 6 models for the Summit Bike Co. website - contained within the following apps:<br>
* django.contrib.auth User model
* Products
* Checkout
* Profiles
* Biketalk

The ERD showing the relationship between models on the Summit Bike Co website can be found [here](/media/ERD_SBC.jpg). <br>

## Wireframes for Summit Bike Co

### HOME app pages
[Home](/media/WF_home.jpg). <br>

### PRODUCTS app pages
[Add a Product](/media/WF_add-product.jpg). <br>
[Edit a Product](/media/WF_edit-product.jpg). <br>
[Bike Model Detail](/media/WF_individual-bike-model.jpg). <br>
[All Mountain Bikes](/media/WF_all-mountain-bikes.jpg). <br>

### BAG app pages
[Shopping Bag](/media/WF_shopping-bag.jpg). <br>

### CHECKOUT app pages
[Checkout](/media/WF_checkout.jpg). <br>
[Thank You](/media/WF_thank-you.jpg). <br>

### BUYING_GUIDES app pages
[What is a Mountain Bike](/media/WF_what-is-a-mtb.jpg). <br>
[Mountain Bike Sizing Guide](/media/WF_mtb-sizing-guide.jpg). <br>

### INFO app
[Who We are](/media/WF_who-we-are.jpg). <br>
[Cycle to Work Scheme](/media/WF_cycle-to-work.jpg). <br>
[Terms and Conditions](/media/WF_terms-conditions.jpg). <br>
[Contact Us](/media/WF_contact-us.jpg). <br>

### BIKETALK app
[Bike Talk](/media/WF_biketalk.jpg).<br>
[Article Name...](/media/WF_articlename.jpg)<br>

### PROFILES app
[My Profile](/media/WF_my-profile.jpg). <br>

### ALLAUTH ACCOUNT pages:<br>
[Log In](/media/WF_account-login.jpg). <br>
[Log Out](/media/WF_account-logout.jpg). <br>
[Register](/media/WF_register.jpg). <br>

## User Experience Design

### User Stories
#### New User Usability Goals
* As a new user, I want to immediately understand the main purpose of the website
* As a new user, I want to be able to see what products they offer
* As a new user, I want to be able to easily contact the organisation
* As a new user, I want to be able to view delivery information
* As a new user, I want to be able to view the social media activity of the organisation
* As a new user, I want to be able to view the privacy policy of the organisation
* As a new user, I want to be able to view general information about the organisation
* As a new user, I want to be able to view the terms and conditions of the organisation
* As a new user, I want to be able to view the Cycle to Work Scheme for the organisation
* As a new user, I want to be able to view advice on product sizing to suit my needs
* As a new user, I want to be able to view advice on which product is best suited to my needs
* As a new user, the navigational layout must be easy to understand and follow
* As a new user, I want to be able to view the website on all device types
#### New User Functionality Goals
* As a new user, I want to be able to easily register for an account, to set up a user profile
* As a new user, I want to be able to enter personal and payment information securely
* As a new user, I want to be able to make a purchase without registering for an account
* As a new user, I want to be able to select my required size and quantity of each product
* As a new user, I want to be able to view products in my shopping bag
* As a new user, I want to be able to adjust the contents of my shopping bag before checking out
* As a new user, I want to be able to save my personal, delivery and billing info to my profile
* As a new user, I want to be able to view my order confirmation after checkout
* As a new user, I want to receive a confirmation email when I have completed an order
* As a new user, I want to be able to subscribe to the organisation's newsletter
* As a new user, I want to be able to search for a required product
* As a new user, I want to be able to view a specific product
* As a new user, I want to be able to view a specific classification of products
* As a new user, I want to be able to see all the products the organisation has on offer
* As a new user, I want to be able to continue shopping if I want to look at a variety of products before making a choice/s
* As a new user, I want to be able to easily add products to my shopping bag
* As a new user, I want to be able to read the articles and comments in 'BikeTalk'

#### Returning User Functionality Goals
* As a returning user, I want to be able to easily login into my account
* As a returning user, I want to be able to easily logout into my account
* As a returning user, I want to be able to view my order history
* As a returning user, I want to be able to update my personal and delivery details
* As a returning user, I want to be know that my personal and payment information is secure
* As a returning user, I want to be able to read and leave comments in 'BikeTalk'
* As a store owner, I want to be able to add a new product to the current stock
* As a store owner, I want to be able to edit/update an existing product
* As a store owner, I want to be able to delete an existing product

## Structural Features of the Summit Bike Co. website

### Website Responsiveness
* Bootstrap and CSS @media queries have been used to ensure the website is viewable across laptops/desktops, tablets and mobile phones. The size and layout of text content, backgrounds and images will all adapt according to the viewing device to ensure readability and quality.
* All features on each web page are fully accessible and responsive across all viewing devices (laptops/desktops, tablets and mobile phones). 
* This feature fulfills the user story: *'As a new user, I want to be able to view the website on all device types'*

### Navigation Options and Header
* This feature is intended to enable the user to quickly and easily navigate between web pages without having to utilise the browser 'back' button.
* Present on all 15 pages of the website, the fully navigational links - on the top of each page (menu links) and/or in the body of the page (hyperlinks or buttons) - will provide access to other pages in the website.
* Clicking on the 'Summit Bike Co' or the 'mountain bike shop' in the navigation bar (at the top of each page) will return the user to the home page.
* This feature fulfills the user story: *'As a new user, the navigational layout must be easy to understand and follow'*

The **Search...** bar (in the header):
* a search bar for users to enter their criteria
* a 'search' button (icon) to submit their criteria
* a confirmation of the user's submitted search (eg. '28 products found for ...')
* a listing of product matches to the user's criteria should their search be successful
* This feature fulfills the user stories: *'As a new user, I want to be able to search for a required product'* and *'As a new user, I want to be able to view a specific classification of products'* and *'As a new user, I want to be able to see what products they offer'*.

The **Free delivery on orders over £1500!** banner:
* present on all 15 pages of the website
* This feature fulfills the user story: *'As a new user, I want to be able to view delivery information'*.

The **Logout**; **Login** and **Register** pages:
* **Logout** - confirmation to a registered user that they want to logout
* This feature fulfills the user story: *'As a returning user, I want to be able to easily logout into my account'*.
A screenshot of the 'Logout' page can be found [here](/media/SS-log_out.jpg). <br>

* **Login** - request of login information (username/email and password) from registered users
* This feature fulfills the user story: *'As a returning user, I want to be able to easily login into my account'*.
A screenshot of the 'Login' page can be found [here](/media/SS-login.jpg). <br>

* **Register** - request of user information (email address, username and password) from new users
* This feature fulfills the user story: *'As a new user, I want to be able to easily register for an account, to set up a user profile'*.
A screenshot of the 'Register' page can be found [here](/media/SS-register.jpg). <br>

### Footer Element
* Present on all 15 pages of the website, the footer contains navigational links to the social media accounts of Summit Bike Co.
* Shoppers are able to subscribe to the monthly newsletter
* There is a link to the privacy policy for Summit Bike Co
* This feature fulfills the user stories: *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to be able to view the social media activity of the organisation'* and *'As a new user, I want to be able to view the privacy policy of the organisation'* and *'As a new user, I want to be able to subscribe to the organisation's newsletter'*

# Details of Summit Bike Co. Web Pages
**NB**: *Unfortunately the Summit Bike Co. website will not display in the 'amiresponsivedesign.is' website. Therefore, screenshots of individual pages have been provided instead. Note: all website pages have been tested (and passed) for responsive design as per the test cases.*<br>

## 1.  The HOME app: index.html (Home page or Landing page)

This page is intended to provide:
* an at-a-glance view of the main purpose of the website, i.e. Summit Bike Co. Mountain Bike Shop, that sells mountain bikes
* shows the current promotion: 'Summer Sale now on!'
* provides a quick access link (button) to the organisation's products: 'view our range'
* provides quick access links to 'buying guides' for shoppers who require product assistance
* provides quick access link to 'contact us' for shoppers who want to obtain contact details
* This feature fulfills the user stories: *'As a new user, I want to immediately understand the main purpose of the website'* and *'As a new user, I want to be able to see what products they offer'* and *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to be able to view advice on which product is best suited to my needs'*.
A screenshot of the 'Home' page (index.html) can be found [here](/media/SS-home.jpg). <br>

## 2.  The PRODUCT app pages: 'All Bikes' and 'Bike Model ...' and 'Stock Management Add a Product' and 'Edit a Product'

The **All Bikes** page is intended to provide:
* a listing of all products sold by Summit Bike Co. - represented with a product image, type, pricing, sort criteria and rating (if applicable). 
* product listings can be sorted as per the different options ('By Price', By Rating'; 'By Brand'; 'By Type'; and 'All Bikes') from the 'All Mountain Bikes' dropdown
* details of individual products can be accessed by selecting the chosen product
* if user is an authenticated superuser, 'edit' and 'delete' links will appear with each product
* This feature fulfills the user stories: *'As a new user, I want to be able to see what products they offer'* and *'As a new user, I want to be able to view a specific classification of products'* and *'As a new user, I want to be able to see all the products the organisation has on offer'* and *'As a store owner, I want to be able to edit/update an existing product'* and *'As a store owner, I want to be able to delete an existing product'*.
A screenshot of the 'All Bikes' page (product.html) can be found [here](/media/SS-all_mountain_bikes.jpg). <br>

The **Bike Model ...** page is intended to provide:
* the model name of the mountain bike (eg: 'Giant Anthem 29er 1 2018')
* the type (classification) of mountain bike (eg: Full Suspension Mountain Bikes)
* pricing: 'price now' and 'price was' (if applicable)
* sort criteria for type (classification)
* product rating out of 5 (if applicable)
* a product description (specification)
* a 'Need Help? link to the 'buying guides' page
* a 'contact us' link to the 'contact details' page
* a dropdown size selector box to choose required size of bike
* a quantity selector box where the user can choose required quantity of the product
* a 'keep shopping' button, should the user wish to look at other products prior to choosing a specific product/s
* a 'add to bag' button, should the user wish to add that particular product to their shopping bag
* if user is an authenticated superuser, 'edit' and 'delete' links will appear with each product
* This feature fulfills the user stories: *'As a new user, I want to be able to view a specific product'* and *'As a new user, I want to be able to view a specific classification of products'* and *'As a new user, I want to be able to select my required size and quantity of each product'* and *'As a new user, I want to be able to continue shopping if I want to look at a variety of products before making a choice/s'* and *'As a new user, I want to be able to easily add products to my shopping bag'* and *'As a store owner, I want to be able to edit/update an existing product'* and *'As a store owner, I want to be able to delete an existing product'*.
A screenshot of the 'Bike Model...' page (bike_detail.html) can be found [here](/media/SS-bike_model_name.jpg). <br>

The **Stock Management Add a Product** page is intended:
* to enable an authenticated superuser (admin/store owner) to add a new product to existing store stock
* to allow completion of fields (some mandatory) for a new product
* to enable the adding of a product image (not mandatory).  A standard 'no_image' image will appear if no product image is loaded
* to provide a 'Add Product' button, to save the entry and submit to the product database
* to provide a 'Cancel' button, which will discard the entry
* This feature fulfills the user story: *'As a store owner, I want to be able to add a new product to the current stock'*
A screenshot of the 'Stock Management Add a Product' page (add_product.html) can be found [here](/media/SS-add_product.jpg). <br>

The **Edit a Product** page is intended:
* to enable an authenticated superuser (admin/store owner) to edit/update an existing product
* to allow editing of fields, ensuring all mandatory fields are completed
* to enable the adding ('Select Image) or replacing ('Remove' tick box) of a product image (not mandatory).  A standard 'no_image' image will appear if no product image is loaded
* to provide a 'Update Product' button, to save the entry and submit to the product database
* to provide a 'Cancel' button, which will discard any changes made
* This feature fulfills the user story: *'As a store owner, I want to be able to edit/update an existing product*
A screenshot of the 'Edit a Product' page (edit_product.html) can be found [here](/media/SS-edit_product.jpg). <br>

The **Delete...** link (next to the 'edit' link) is intended:
* to enable an authenticated superuser (admin/store owner) to immediately delete an existing product
* This feature fulfills the user story: *'As a store owner, I want to be able to delete an existing product'*.

## 3.  The BAG app pages: 'Shopping Bag'

The **Shopping Bag** page is intended to provide:
* the current bag total; delivery cost (if applicable); and the grand total.
* a 'keep shopping' button, should the user wish to add additional product/s to their bag
* a 'Secure Checkout' button to take the user to 
* a summary of the contents of the user's bag including: an image; bike model name; chosen size; chosen quantity and pricing for each product in their bag
* the user with the ability to edit the quantity of each product in their bag ('update' link) or to delete a product/s from their bag ('remove' link)
* This feature fulfills the user stories: *'As a new user, I want to be able to view products in my shopping bag'* and *'As a new user, I want to be able to adjust the contents of my shopping bag before checking out'* and *'As a new user, I want to be able to easily add products to my shopping bag'*.
A screenshot of the 'Shopping Bag' page (bag.html) can be found [here](/media/SS-shopping_bag.jpg). <br>

## 4.  The CHECKOUT app pages: 'Checkout' and 'Thank You'

The **Checkout** page is intended to provide:
* a form for the user to complete their personal details; delivery information; and payment details
* the option for users to save their personal and delivery information to a user profile (checkbox)
* the user with the option to adjust the contents of their bag before completing their order
* a 'Complete Order' button to finalise the order and take secure payment for the products in their shopping bag
* an information message advising the user as to what amount their card will be charged
* an order summary of the contents of the user's bag including: an image; bike model name; chosen size; chosen quantity and pricing for each product in their bag
 * an 'order total'; 'delivery' charge (if applicable); and 'grand total' of their shopping bag
 * This feature fulfills the user stories: *'As a returning user, I want to be know that my personal and payment information is secure'* and *'As a new user, I want to be able to save my personal, delivery and billing info to my profile'* and *'As a new user, I want to be able to view products in my shopping bag'* and *'As a new user, I want to be able to adjust the contents of my shopping bag before checking out'*.
 A screenshot of the 'checkout' page (checkout.html) can be found [here](/media/SS-checkout.jpg). <br>

The **Thank You** page is intended to provide:
* an order confirmation listing 'order number'; 'order date'; 'order details'; 'delivering to'; and 'billing info'
* a 'Need Something Else' button which reverts back to the 'All Bikes' page, should the user wish to keep shopping for a new order
* This feature fulfills the user stories: *'As a new user, I want to be able to view my order confirmation after checkout'* and *'As a new user, I want to receive a confirmation email when I have completed an order'*
A screenshot of the 'Thank You' page (checkout_success.html) can be found [here](/media/SS-thank_you.jpg). <br>

## 5.  The PROFILES app pages: 'My Profile'

The **My Profile** page is intended to provide:
* a registered user's default delivery information
* the user with the ability to update their delivery information and click the 'update information' button
* the user with their 'Order History' showing 'order number; 'date' of order; 'items' for that order; and 'order total'
* each order under the 'Order History' is accessible via a link which will revert the user to the 'Thank You (order confirmation)' page for that particular order.  A 'Back to Profile' link will take the user back to their 'My Profile' page
* This feature fulfills the user stories: *'As a returning user, I want to be able to view my order history'* and *'As a returning user, I want to be able to update my personal and delivery details'*.
A screenshot of the 'My Profile' page (profile.html) can be found [here](/media/SS-my_profile.jpg). <br>

## 6.  The BUYING_GUIDES app pages: 'What is a Mountain Bike' and 'Mountain Bike Sizing Guide'

The **What is a Mountain Bike** page is intended to provide:
* information on the types of mountain bikes and their construction
* This feature fulfills the user story: *'As a new user, I want to be able to view advice on which product is best suited to my needs'*
A screenshot of the 'What is a Mountain Bike' page (what_is_a_mtb.html) can be found [here](/media/SS-what_is_a_mtb.jpg). <br>

The **Mountain Bike Sizing Guide** page is intended to provide:
* information on how to select the correct sized mountain bike
* This feature fulfills the user story: *'As a new user, I want to be able to view advice on product sizing to suit my needs'*
A screenshot of the 'Mountain Bike Sizing Guide' page (mtb_sizing.html) can be found [here](/media/SS-mountain_bike_sizing_guide.jpg). <br>

## 7.  The INFO app pages: 'Who We Are' and 'Cycle to Work Scheme' and 'Terms and Conditions' and 'Contact Details'

The **Who We Are** page is intended to provide:
* a brief history and general information about Summit Bike Co.
* Summit Bike Co.'s online shopping transaction
* This feature fulfills the user story: *'As a new user, I want to be able to view general information about the organisation'*
A screenshot of the 'Who We Are' page (who_we_are.html) can be found [here](/media/SS-who_we_are.jpg). <br>

The **Cycle to Work** page is intended to provide:
* information about Summit Bike Co's Cycle to Work Scheme and the 4-step process to assist employers in joining the Scheme
* an external link providing information on the UK Government initiative for the Cycle to Work Scheme
* This feature fulfills the user story: *'As a new user, I want to be able to view the Cycle to Work Scheme for the organisation'*
A screenshot of the 'Cycle to Work Scheme' page (cycle_to_work.html) can be found [here](/media/SS-cycle_to_work.jpg). <br>

The **Terms and Conditions** page is intended to provide:
* all information regarding the terms and conditions for Summit Bike Co. including how to order, delivery, returns and exchanges, cancellation, and warranty and liability
* a contact number for customer services
* an external link to the 'Privacy Policy' for Summit Bike Co.
* This feature fulfills the user story: *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to be able to view the privacy policy of the organisation'* and *'As a new user, I want to be able to view the terms and conditions of the organisation '* and *'As a new user, I want to be able to view general information about the organisation'*
A screenshot of the 'Terms and Conditions' page (terms_conditions.html) can be found [here](/media/SS-terms_conditions.jpg). <br>

The **Contact Details** page is intended to provide:
* a contact number for customer services and information they can provide
* how complaints are handled by Summit Bike Co.
* head office address and company information for Summit Bike Co.
* This feature fulfills the user story: *As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to be able to view general information about the organisation'*.
A screenshot of the 'Contact Us' page (contact_us.html) can be found [here](/media/SS-contact_us.jpg). <br>

## 8.  The BIKETALK app pages: 'BikeTalk' and 'Article Name...'
The **BikeTalk** page is intended to provide:
* a description of what BikeTalk is
* a list of all the organisation active articles
* details of each active article (article_content.html) listed can be accessed by clicking either the article name (eg Besk UK Tech Trails...) or the slug (eg: Dyfi Bike Park...).
* the author (i.e. the Administator) is displayed above the article name.
* the date and time the Post was created and the current amount of 'likes' for that particular article.
* a 'Comments' block: for already approved (by admin) comments left by users
* a 'Leave a Comment' block: registered users can read and leave a comment on any active article.  Unregistered users can only read articles and existing (admin approved) comments.
* This feature fulfills the user stories: *'As a new user, I want to be able to read the articles and comments in 'BikeTalk''* and *'As a returning user, I want to be able to read and leave comments in 'BikeTalk''*.
A screenshot of the 'BikeTalk' page (article_list.html) can be found [here](/media/SS-biketalk.jpg). <br>
A screenshot of the 'Article Name...' page (article_content.html) can be found [here](/media/SS-article_name.jpg). <br>

## Design of the Summit Bike Co. website

### Colour Scheme
The colour palette for general body content comprises five basic colours: 
* #FFFF00 (yellow) home page text, and buttons
* #000000 (black) general body text and headings
* #2828E8 (blue) logo and headings
* #28a745 (green) sub-headings
* #DBD6D6 (light gray) header and footer background

### Fonts
The Summit Bike Co. logo and main page headings use **Montserrat**; body text and headings use **Lato**.  The back-up font is **sans-serif** for both Lato and Montserrat.  Fonts were downloaded from **Google Fonts**.

### Imagery
Images for the website have been downloaded from **Pexels** and are stored in **Cloudinary**.

### Limitations
No known limitations.

## Features
* Login, Logout and Register user account functionality
* Full CRUD (create, read, update, delete) functionality that is role-based
* Messaging system confirming all user actions on the website

## Technologies
* Django - a framework that follows the model–template–views architectural pattern and upon which this website is built
* Python - website functionality enhanced by custom written Python
* HTML - the structure of this website project uses custom written HTML as the main language
* Bootstrap - utilised mostly for website responsiveness
* CSS - the styling of this website encompasses custom written CSS
* Javascript - website interaction provided by custom written Javascript
* [Google Fonts](https://fonts.google.com/) - utilised for the logo, brand and body text
* [FontAwesome](https://fontawesome.com/) - utilised for Chat app icons
* [GitHub](https://github.com/) - hosting site for storage of source code for the website and [Git Pages](https://pages.github.com/) for the deployment of the website
* [Git](https://git-scm.com/) - used as version control software to commit and push code to a GitHub repository where all source code is located
* [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) - these are built in developer tools used to inspect page elements (eg. responsive design; debug issues; testing of different CSS styling options; and the Lighthouse Reports
* [Balsamiq](https://balsamiq.com/) - wireframes for all pages
* [Kaggle](https://www.kaggle.com/) - dataset of mountain bike images and descriptions
* [Pexels](https://www.pexels.com/) - image for home page
* [TinyJpg](https://tinyjpg.com/) - compression of images 
* [Cloudinary](https://cloudinary.com/) - cloud storage of Chat image for smartevents WMP website; serve static files
* [PicPick](https://picpick.app/en/) - used to create screenshots of smartevents WMP Website pages
* [Heroku](https://www.heroku.com/) - final project (website) deployed to and stored on Heroku
* [Wordtracker](https://www.wordtracker.com/) - utilised for search engine optimisation
* [XML-Sitemaps.com](https://www.xml-sitemaps.com/) - generation of sitemap for website

## Testing
* Manual testing has been performed to check for back-end functionality (Django, Python, Javascript), as well as visual effects and website layout (HTML, Bootstrap, CSS).
* Testing has been performed to check for compatibility across three web browsers (Google Chrome, Firefox, Opera).
* Responsive design has been tested across the different screen sizes: desktops/laptops (1024px); tablets (max-width 769px); mobiles (to a max-width of 426px); and large laptops (min-width 1025px to max-width 1441px).
* All navigational links should direct to the correct html web page as per their names.<br>
Exception: the 'Home' page, will direct to 'index.html'. 

### Test Cases
* Test cases can be found here for the **home** app page (index.html) and base.html: <br> 
[Home app and base.html](/media/TC_base_home.jpg)
* Test cases can be found here for the **products** app pages: <br> 
[Products app](/media/TC_products.jpg)<br>
* Test cases can be found here for the **bag** app page: <br>
[Bag app](/media/TC_bag.jpg).<br>
* Test cases can be found here for the **checkout** app pages: <br>
[Checkout app](/media/TC_checkout.jpg).<br>
* Test cases can be found here for the **buying_guides** app pages: <br>
[Buying_Guides app](/media/TC_buying_guides.jpg).<br>
* Test cases can be found here for the **info** app pages:<br>
[Info app](/media/TC_info.jpg).<br>
* Test cases can be found here for the **profiles** app page:<br>
[Profiles app](/media/TC_profile.jpg). <br>
* Test cases can be found here for the **biketalk** app pages:<br>
[Biketalk app](/media/TC_biketalk.jpg). <br>
* Test cases can be found here for the **Logout, Login, Register** pages:<br>
[AllAuth Accounts pages](/media/TC_login_logout_register.jpg).<br>

### Testing Issues and Resolutions
An intermittent error arose during testing with the Checkout page.  When placing the exact same order first as a unregistered user, and then as a registered user: a 'numeric field overflow' error would occur for the registered user, but not for the unregistered user.  The 'lineitem_total' field was highlighted as the particular problem, so I adjusted the amount of 'max-digits' to resolve the issue.  I have not been able to reproduce the error again.

## Code Validation
All 17 HTML pages were run through the [W3C Markup Validation Service](https://validator.w3.org/) and showed no errors. The following web pages were checked: 
* Home app: index.html page <br>
[HTML: index.html page](/media/HTML-val_index.jpg).<br>

* Products app: <br>
[HTML: add_product.html page](/media/HTML-val_add_product.jpg).<br>
[HTML: edit_product.html page](/media/HTML-val_edit_product.jpg).<br>
[HTML: bike_detail.html page](/media/HTML-val_bike_detail.jpg).<br>
[HTML: products.html page](/media/HTML-val_products.jpg).<br>

* Bag app: <br> 
[HTML: bag.html](/media/HTML-val_bag.jpg).<br>

* Checkout app: <br> 
[HTML: checkout.html](/media/HTML-val_checkout.jpg).<br>
[HTML: checkout_success.html](/media/HTML-val_checkout_success.jpg).<br>

* Buying_Guides app: <br> 
[HTML: what_is_a_mtb.html](/media/HTML-val_what_is_a_mtb.jpg).<br>
[HTML: mtb_sizing.html](/media/HTML-val_mtb-sizing.jpg).<br>

* Info app: <br> 
[HTML: who_we_are.html](/media/HTML-val_who_we_are.jpg).<br>
[HTML: cycle_to_work.html](/media/HTML-val_cycle_to_work.jpg).<br>
[HTML: terms_conditions.html](/media/HTML-val_terms_conditions.jpg).<br>
[HTML: contact_us.html](/media/HTML-val_contact_us.jpg).<br>

* Biketalk app: <br>
[HTML: article_list.html](/media/HTML-val_biketalk.jpg)<br>
[HTML: article_content.html](/media/HTML-val_articlename.jpg)<br>

* Profiles app: <br> 
[HTML: profile.html](/media/HTML-val_profile.jpg).<br>

* The CSS stylesheet was run through the [CSS Validation Service-Jigsaw](https://jigsaw.w3.org/css-validator/) and showed no errors. <br>
[CSS validation](/media/CSS_validation.jpg).<br>

* The Javascript code was run through the [JSHint Validation Service](https://jshint.com) and showed no errors.<br>
[JS validation for summit_bike_co app and bag app](/media/JSHint_summit-bike-co-app_and_bag-app.jpg).<br>
[JS validation for products app](/media/JSHint_products-app.jpg).<br>
[JS validation for checkout app](/media/JSHint_checkout-app.jpg).<br>

## Deployment
### Project Creation
The project was created using GitHub and choosing a new repository.<br>
##### The following terminal commands were used during this project:
* create a repository on GitHub and pin to Github Workspaces
* access the terminal within GitPod and type "python3 manage.py runserver" to run the website view
* git add . - this command adds a change in the working directory to the staging area.
* git commit -m "*message*" - this command details the change/s made in the 'message' section and then commits the changes to the local repository.
* git push origin main - this command is used to push all changes to the GitHub repository.
* git push heroku main - this command is used to push all changes to Heroku.
* Final deployment of the website is on [Heroku](https://smart-events.herokuapp.com/)
##### For final deployment to Heroku:<br>
1.	Create Heroku App
2.	Install dj_database_url and psycopg2-binary in my local environment
3.	Freeze requirements.txt file
4.	In settings.py import dj_database_url
5.	Back up the local database using "./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json" in the terminal window.
6.	Add the Heroku database url via dj_database_url.parse()
7.	Run migrations to the Postgres database
8.	Configure the database so that when the app is running on Heroku it uses the Postgres database and when it's running locally it uses the SQLite database
9.	Create Procfile so that Heroku creates a web dyno so that it will run gunicorn and serve the Django app
10.	Disable Heroku collect static
11.	Add the Heroku hostname to allowed hosts in settings.py
12.	Generate a new Django secret key and add this to the Heroku config variables
13.	Replace the secret key in settings.py to grab it from the environment
14.	Set debug to True only if the environment is a development environment
15.	Commit changes and deploy to GitHub and Heroku
16.	Freeze requirements.txt file
17.	Create custom storage classes for media and static files (for Cloudinary storage)
18.	Commit and push to GitHub and Heroku
19.	Add the Stripe keys to the Heroku config variables
20.	Create a new webhook endpoint from the Stripe dashboard
21.	Add all the Stripe keys to the Heroku config variables

## Credits
### Code
* The private collaboration and knowledge sharing SaaS platform [Stack Overflow](https://stackoverflow.com/) was an invaluable resource for general coding queries.
* Use was made of Code Institute tutor support for help with persistent coding issues.
* Ideas for the Summit Bike Co was taken from Code Institute's walkthrough project 'Boutique Ado'.
* Inspiration for BikeTalk was derived from Code Institute's walkthrough project 'I think therefore I blog'.

### Content
* Ideas for Info app were taken from the website [Evans Cycles](http://www.evanscycles.com).
* Content for the Biketalk app was taken from the website [Mountain Biking UK](https://www.mbuk.com/).
