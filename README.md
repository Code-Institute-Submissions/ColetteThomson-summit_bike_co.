# Summit Bike Co.

## Purpose
This website has 

## High level overview of registered user roles and permissions within WMP:
*Note:  All users (with the exception of unregistered users) will need to be set up with appropriate permissions by the superuser Admin.  All users will have read-only access to the Home page (landing page).*

* **Superuser (Admin)** - has full CRUD (create, read (view), update, delete) from the admin panel (and read-only from the website), across all pages.
* **Registered User** - will have 
* **Unregistered User** - will have 
* **Store Owner** - 

## The Summit Bike Co. website pages are as follows:
* **Home** (index.html): landing page
* **All Mountain Bikes**: opens the 'product' page. <br>
The page: 'bike_detail' detail can then be accessed from 'product' page.
* **Buying Guides**: dropdown reveals:  'What is a Mountain Bike'; 'Mountain Bike Sizing Guide'. <br>
* **About Us**: dropdown reveals:  'Who We Are'; 'Cycle to Work Scheme; 'Terms and Conditions'.<br> 
* **Contact Us**: dropdown reveals:  'Contact Details'.<br>
* **My Account**: dropdown reveals:  'Add a Product'; 'My Profile'; 'Logout'.<br>
The page 'Add a Product' is permissions based and only appears if the user is 'admin'.<br>
The page 'My Profile' only appears if the user is registered. <br>
**Allauth Account pages**
* **Logout**: visible when users are logged in
* **Login**: visible when users are logged out
* **Sign Up**: visible when users are logged out

The live project can be found [here]()

## Entity Relationship Diagram (ERD) for Summit Bike Co.
There are ? models within the Summit Bike Co website:<br>
* ?

The ERD showing the relationship between models on the Summit Bike Co website can be found [here](). <br>

## Wireframes for Summit Bike Co

### HOME app
[Home page](). <br>

### PRODUCTS app
[Add Product](). <br>
[Edit Product](). <br>
[Bike Detail](). <br>
[Products](). <br>

### BAG app
[Bag](). <br>

### CHECKOUT app
[Checkout](). <br>
[Checkout Success](). <br>

### BUYING_GUIDES app
[What is a Mountain Bike](). <br>
[Mountain Bike Sizing Guide](). <br>

### INFO app
[Who We are](). <br>
[Cycle to Work](). <br>
[Terms and Conditions](). <br>
[Contact Us](). <br>

### PROFILES app
[My Profile](). <br>

### ALLAUTH ACCOUNT pages:<br>
[Log In](). <br>
[Log Out](). <br>
[Sign Up](). <br>

## User Experience Design

### User Stories
#### New User Usability Goals
* As a new user, I want to immediately understand the main purpose of the website
* As a new user, I want information on what services they offer
* As a new user, I want to be able to easily contact the organisation
* As a new user, the navigational layout must be easy to understand and follow
* As a new user, I want to be able to view the website on all device types
#### New User Functionality Goals
* As a new user, I want to register for an account, so that I can access appropriate website content
* As a new user, I want to understand what access I have to what website content

#### Returning User Functionality Goals
* As a returning user, I want to have appropriate access to website content as per my permissions
* As a returning user, I want to be able to find (read/view) the information I'm looking for
* As a returning user, I want to be able to create (add) new content, as per my permissions
* As a returning user, I want to be able to edit (update) existing content, as per my permissions
* As a returning user, I want to be able to delete existing content, as per my permissions
* As a returning user, I want to be able to view all the organisation's active projects in the Chat
* As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts
* As a returning user, I want confirmation of actions I have performed on the WMP website

## Structural Features of the Summit Bike Co. website

### Website Responsiveness
* Bootstrap and CSS @media queries have been used to ensure the website is viewable across laptops/desktops, tablets and mobile phones. The size and layout of text content, backgrounds and images will all adapt according to the viewing device to ensure readability and quality.
* All features on each web page are fully accessible and responsive across all viewing devices (laptops/desktops, tablets and mobile phones). 
* This feature fulfills the user story: *'As a new user, I want to be able to view the website on all device types'*. 

### Navigation Options
* This feature is intended to enable the user to quickly and easily navigate between web pages without having to utilise the browser 'back' button.
* Present on all 21 pages of the website, the fully navigational links - on the top of each page (menu links) and/or in the body of the page (hyperlinks or buttons) - will provide access to other pages in the website.
* Clicking on the 'WMP' in the navigation bar (at the top of each page) will return the user to the home page.
* This feature fulfills the user stories: *'As a new user, the navigational layout must be easy to understand and follow'* and *'As a new user, I want information on what services they offer'*.

### Footer Element
* Present on all 21 pages of the website, the footer contains copyright information and navigational links to the social media accounts of smartevents WMP.
* This feature fulfills the user stories: *'As a new user, I want information on what services they offer'*.

# Details of Summit Bike Co. Web Pages
**NB**: *Unfortunately the smartevents WMP website will not display in the 'amiresponsivedesign.is' website. Therefore, screenshots of individual pages have been provided instead. Note: all website pages have been tested (and passed) for responsive design as per the test cases.*<br>

## 1.  The 'Home' app: index.html (Home page or Landing page)

This page is intended to provide:
* an at-a-glance view of the main purpose of the website, i.e. a Workforce Management Platform (WMP) to help project managers and their teams select the right resource for the right task - and - the availability of a project Chat to encourage project team member interaction and participation.
* an at-a-glance high level view of the different WMP roles and permissions, so that potential users can immediately see what user options are available.
* contact details (email and phone) for the website Administrator, so that users can request to be set up as a registered website user
* This feature fulfills the user stories: *'As a new user, I want to immediately understand the main purpose of the website'* and *'As a new user, I want information on what services they offer* and *'As a new user, I want to be able to easily contact the organisation'* and *'As a new user, I want to register for an account, so that I can access appropriate website content'* and *'As a new user, I want to understand what access I have to what website content'* and *'As a new user, the navigational layout must be easy to understand and follow'*.

A screenshot of the 'Home' page (index.html) can be found [here](/smartevents/images/mu_home_perm.jpg). <br>

## 2.  The Product app pages: '' pages

The **All Bikes** page is intended to provide:
* a list of all the organisation's active projects.
* details of each active project listed can be accessed by clicking either the project name (eg Project 1...) or the slug (eg: energy consumption...).
* the author (i.e. the Administator) is displayed above the project name.
* the date and time the Post was created and the current amount of 'likes' for that particular project.
* This feature fulfills the user stories: *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'*

*without/no permissions :*<br> 
A screenshot of the 'All Mountain Bikes' page can be found [here](). <br>

The **Bike Model ...** page is intended to provide:
* a list ...
* product specification.
* user messaging: 
* This feature fulfills the user stories: *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'* and *'As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

## 3.  Dropdown for 'Buying Guides'

The **Bike Model ...** page is intended to provide:
* a list ...
* product specification.
* user messaging: 
* This feature fulfills the user stories: *'As a returning user, I want to be able to view all the organisation's active projects in the Chat'* and *'As a returning user, I want to be able to add my ideas or suggestions on the different Project Posts'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

The **Search...** bar:
* a search bar for users to enter their criteria (this field is case sensitive).
* a 'search' button to submit their criteria.
* a confirmation of the user's submitted search (i.e. you searched for ...).
* a listing of linked matches to the user's criteria should their search be successful.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'*.


*without/no permissions :*<br> 
A screenshot of the 'All Projects' page can be found [here](/smartevents/images/mu_all-projects_np.jpg). <br>
A screenshot of the 'All Admin People' page can be found [here](/smartevents/images/mu_all-admin-people_np.jpg). <br>
A screenshot of the 'All Tech Support People' page can be found [here](/smartevents/images/mu_all-tech-people_np.jpg). <br>

*with permissions :*<br> 
A screenshot of the 'All Projects' page with permissions can be found [here](/smartevents/images/mu_all-projects_perm.jpg). <br>
A screenshot of the 'All Admin People' page with permissions can be found [here](/smartevents/images/mu_all-admin-people_perm.jpg). <br>
A screenshot of the 'All Tech Support People' page with permissions can be found [here](/smartevents/images/mu_all-tech-people_perm.jpg). <br>

The three **Add...** pages are intended to provide:
* depending on user permissions: the display of an empty form for the user to: 'add a new administration person' OR 'add a new technical support person' OR 'add a new project'.
* a 'submit' button to confirm the user's entry of the completed form.
* user messaging: confirmation that the user has: 'added a new administration person' OR 'added a new technical support person' OR 'added a new project'.
* This feature fulfills the user stories: *' As a returning user, I want to be able to create (add) new content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*with permissions :*<br>
A screenshot of the 'Add Project' page can be found [here](/smartevents/images/mu_add-project_perm.jpg). <br>
A screenshot of the 'Add Admin People' page can be found [here](/smartevents/images/mu_add-admin-person_perm.jpg). <br>
A screenshot of the 'Add Tech Support People' page can be found [here](/smartevents/images/mu_add-tech-person_perm.jpg). <br>

### 'Personal Details' pages for 'Admin People' and 'Tech People'
Note: these pages become accessible when clicking the 'person name...' from either the 'All Admin People' page OR the 'All Tech Support People' page.

The two **Personal Details** (**show_admin_person** and **show_techsupport_person**) pages are intended to provide:
* an overview of an individual person's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the personal details overview of: 'Admin person' OR 'Tech Support person'.
* user messaging: confirmation of 'updating' or 'deleting' of a person.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*without/no permissions :*<br> 
A screenshot of the 'Personal Details' page (from 'All Admin People') can be found [here](/smartevents/images/mu_personal-details-admin_np.jpg). <br>
A screenshot of the 'Personal Details' page (from 'All Tech Support People') can be found [here](/smartevents/images/mu_personal-details-tech_np.jpg). <br>

*with permissions :*<br>
A screenshot of the 'Personal Details' page with permissions(from 'All Admin People') can be found [here](/smartevents/images/mu_personal-details-admin_perm.jpg). <br>
A screenshot of the 'Personal Details' page with permissions (from 'All Tech Support People') can be found [here](/smartevents/images/mu_personal-details-tech_perm.jpg). <br>

### 'Project Details' page for 'Projects'
Note: this page becomes accessible when clicking the 'project name...' from the 'All Projects' page.

The **Project Details** (**show_project**) page for 'Projects' is intended to provide:
* an overview of an active project's details. 
* depending on user permissions: the inclusion of 'update...' and 'delete...' buttons. If no permissions user will only be able to view the project details overview of: 'Project Name....
* user messaging: confirmation of 'updating' or 'deleting' of a project.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*without/no permissions :*<br> 
A screenshot of the 'Project Details' page (from 'All Projects') can be found [here](/smartevents/images/mu_project-details_np.jpg). <br>

*with permissions :*<br>
A screenshot of the 'Project Details' page with permissions (from 'All Projects') can be found [here](/smartevents/images/mu_project-details_perm.jpg). <br>

### 'Update...' pages and 'Delete...' button for 'Projects', 'Admin People' and 'Tech Support People'
Note: this page is permission-based and becomes accessible when clicking the 'project name...' from the 'All Projects' page OR the 'person name...' from the 'All Admin People' OR 'All Tech Support People' pages.
This page is also accessible from the 'Personal Details' and 'Project Details' pages.

The **Update...** pages are intended to provide:
* a pre-populated form with existing information on: 'Projects' OR 'Admin People' OR 'Tech Support People'.
* an 'update...' button to confirm the user's changes to the existing form information.
* user messaging: confirmation of the 'updating' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and *'As a returning user, I want to be able to edit (update) existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

The **Delete...** button (next to the 'update' button)
Note: this button is permission-based and is accessible from the 'All Projects' page OR the 'All Admin People' page OR the 'All Tech Support People' page. This button is also accessible from the 'Personal Details' and 'Project Details' pages.
* a 'delete...' button to confirm the user's decision to delete: a 'project' from 'All Projects' OR a 'person' from 'All Admin People' OR 'All Tech Support People' pages.
* user messaging: confirmation of the 'deleting' of a project's details OR a person's details.
* This feature fulfills the user stories: *'As a returning user, I want to be able to find (read/view) the information I'm looking for'* and '*As a returning user, I want to be able to delete existing content, as per my permissions'* and *'As a returning user, I want to have appropriate access to website content as per my permissions'* and *'As a returning user, I want confirmation of actions I have performed on the WMP website'*.

*with permissions :*<br>
A screenshot of the 'Update Project' page (from 'Projects') can be found [here](/smartevents/images/mu_update-project_perm.jpg). <br>
A screenshot of the 'Update Person' page (from 'Admin People') can be found [here](/smartevents/images/mu_update-admin-person_perm.jpg). <br>
A screenshot of the 'Update Person' page (from 'Tech People') can be found [here](/smartevents/images/mu_update-tech-person_perm.jpg). <br>

## 4.  'Logout'; 'Login' and 'Register' pages

These pages are intended to provide:
* Logout - confirmation to a registered user that they want to logout
* Login - request of login information (username and password) from registered users
* Register - request of user information (username, password, re-type password, optional email) from new users

A screenshot of the 'Logout' page can be found [here](). <br>
A screenshot of the 'Login' page can be found [here](). <br>
A screenshot of the 'Register' page can be found [here](). <br>

## Design of the Summit Bike Co. website

### Colour Scheme
The colour palette for general body content comprises four basic colours: 
* colours...

### Fonts
The Summit Bike Co. logo and main page headings use **Montserrat**; body text and headings use **Lato**.  The back-up font is **sans-serif** for both Lato and Montserrat.  Fonts were downloaded from **Google Fonts**.

### Imagery
Images for the website have been downloaded from **Pexels** and are stored in **Cloudinary**.

### Limitations
No known limitations.

## Features
* Login, Logout and Register user account functionality
* Full CRUD (create, read, update, delete) functionality that is permissions- and role-based
* Messaging system confirming user actions on the website

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

## Testing
* Manual testing has been performed to check for back-end functionality (Django, Python, Javascript), as well as visual effects and website layout (HTML, Bootstrap, CSS).
* Testing has been performed to check for compatibility across three web browsers (Google Chrome, Firefox, Opera).
* Responsive design has been tested across the different screen sizes: desktops/laptops (1024px); tablets (max-width 769px); mobiles (to a max-width of 426px); and large laptops (min-width 1025px to max-width 1441px).
* All navigational links should direct to the correct html web page as per their names.<br>
Exceptions: the 'Home' page, will direct to 'index.html'; the 'show_admin_person.html' and 'show_techsupport_person.html' will direct to 'Personal Details'; the 'show_project' will direct to 'Project Details'. 

### Test Cases
* Test cases can be found here for the **index.html** (home) and base.html: <br> 
[Home app and base.html]()
* Test cases can be found here for the **Chat** app pages (post_list.html | post_detail.html) : <br> 
[Products app]()<br>
* Test cases can be found here for the various **Events** app pages (add... | update... | delete... | view... ): <br>
[Bag app]().<br>
* Test cases can be found here for the **Logout, Login, Register** and **un-registered users** pages: <br>
[Checkout app]().<br>
* Test cases can be found here for the <br>
[Buying_Guides app]().<br>
* Test cases can be found here for the <br>
[Info app](). <br>
* Test cases can be found here for the <br>
[Profiles app](). <br>
* Test cases can be found here for the <br>
[AllAuth Accounts pages]().<br>
* Test cases can be found here for the <br>

### Testing Issues and Resolutions
The following issue arose ...

## Code Validation
All 21 HTML pages were run through the [W3C Markup Validation Service](https://validator.w3.org/) and showed no errors. The following web pages were checked: 
* Home app: index.html page <br>
[HTML: index.html page]().<br>

* Products app: <br>
[HTML: add_product.html page]().<br>
[HTML: edit_product.html page]().<br>
[HTML: bike_detail.html page]().<br>
[HTML: products.html page]().<br>

* Bag app: <br> 
[HTML: bag.html]().<br>

* Checkout app: <br> 
[HTML: checkout.html]().<br>
[HTML: checkout_success.html]().<br>

* Buying_Guides app: <br> 
[HTML: what_is_a_mtb.html]().<br>
[HTML: mtb_sizing.html]().<br>

* Info app: <br> 
[HTML: who_we_are.html]().<br>
[HTML: cycle_to_work.html]().<br>
[HTML: terms_conditions.html]().<br>
[HTML: contact_us.html]().<br>

* Profiles app: <br> 
[HTML: profile.html]().<br>

* The CSS stylesheet was run through the [CSS Validation Service-Jigsaw](https://jigsaw.w3.org/css-validator/) and showed no errors. <br>
[CSS validation]().<br>

* The Javascript file was run through the [JSHint Validation Service](https://jshint.com) and showed no errors.<br>
[JS validation]().<br>

## Lighthouse Reports
* Home app: index.html page <br>
[Lighthouse: index.html]().<br>
* Products app: <br>
[Lighthouse: Add a Product]().<br>
[Lighthouse: Edit a Product]().<br>
[Lighthouse: Bike Model (name...)]().<br>
[Lighthouse: All Mountain Bikes]().<br>
* Bag app: <br>
[Lighthouse: Shopping Bag]().<br>
* Checkout app: <br>
[Lighthouse: Checkout]().<br>
[Lighthouse: Thank You]().<br>
* Buying_Guides app: <br>
[Lighthouse: What is a Mountain Bike]().<br>
[Lighthouse: Mountain Bike Sizing Guide]().<br>
* Info app: <br>
[Lighthouse: Who We Are]().<br>
[Lighthouse: Cycle to Work Scheme]().<br>
[Lighthouse: Terms and Conditions]().<br>
[Lighthouse: Contact Details]().<br>
* Profiles app: <br>
[Lighthouse: My Profile]().<br>

## Deployment
### Project Creation
The project was created using GitHub and choosing a new repository.<br>
The following terminal commands were used during this project:
* git add . - this command adds a change in the working directory to the staging area.
* git commit -m "*message*" - this command details the change/s made in the 'message' section and then commits the changes to the local repository.
* git push - this command is used to push all changes to the GitHub repository.
* Final deployment of the website is on [Heroku](https://smart-events.herokuapp.com/)

### Using GitHub Pages
* Navigate to the GitHub repository [smartevents WMP](https://github.com/ColetteThomson/smartevents_WMP).
* Select 'Settings'.
* Scroll down to 'GitHub Pages'.
* Select 'Main' branch as the source and click 'Save' button.
* Select link to go to live published page.

## Credits
### Code
* The private collaboration and knowledge sharing SaaS platform [Stack Overflow](https://stackoverflow.com/) was an invaluable resource for general coding queries.
* Use was made of Code Institute tutor support for help with persistent coding issues.
* Ideas for the Summit Bike Co was taken from Code Institute's walkthrough project 'Boutique Ado'.

### Content
* Ideas for Info app were taken from the website [Evans Cycles](http://www.evanscycles.com).
