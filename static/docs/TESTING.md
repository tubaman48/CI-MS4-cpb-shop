# Testing Steps

[Click here to return to the main README file](README.md)


# Contents

* [Icon Key](#icon-key)

* [Manual Testing](#manual-testing)
  * [Functional Testing by App](#functional-testing-by-apps)
    * [Bag App](#bag-app)
    * [Band App](#band-app)
    * [Blog App](#blog-app)
    * [Checkout App](#checkout-app)
    * [Home App](#home-app)
    * [Product App](#product-app)
    * [Profiles App](#profiles-app)
    * [Reviews App](#reviews-app)
    * [Omitted Code](#omitted-code)
  * [Devices and Browsers](#devices-and-browsers)
  * [Testing User Stories](#testing-user-stories)
  * [Testing Technologies](#testing-technologies)
  * [Links and Navigation](#links-and-navigation)
    * [Navigation Bar](#navigation-bar)
    * [External Links](#external-links)
  * [Styling and Layout](#styling-and-layout)

* [User Access](#user-access)

* [Functions](#functions)
  * [Register](#register)
  * [Log In](#log-in)
  * [Log Out](#log-out)
  * [Add Products](#add-products)
  * [Edit Products](#edit-products)
  * [Delete Products](#delete-products)
  * [Search Products](#search-products)
  * [Messages](#messages)
  * [Stripe](#stripe)
  * [400](#400)
  * [401](#401)
  * [403](#403)
  * [404](#404)
  * [405](#405)
  * [500](#500)
  * [Validation](#validation)

* [Database](#database)

* [Accessibility](#accessibility)
  * [Tap Targets](#tap-targets)
  * [Color Contrast](#color-contrast)
  * [Visually-Impaired Users](#visually-impaired-users)
  * [Assistive Technologies](#assistive-technologies)
  * [Reading Level](#reading-level)

* [Site Performance and Optimisation](#site-performance-and-optimisation)
  * [Lighthouse](#lighthouse)
  * [WebPageTest](#webpagetest)

* [Responsive Design](#responsive-design)
  * [Mobile Testing](#mobile-testing)
  * [Tablet Testing](#tablet-testing)
  * [Laptop Testing](#laptop-testing)

* [Images](#images)
  * [Desktop and Laptop Screenshots](#desktop-and-laptop-screenshots)
  * [Tablet Screenshots](#tablet-screenshots)
  * [Mobile Screenshots](#mobile-screenshots)

---

# Icon key

&#128272; <-- Superuser only access

&#128100; <-- Logged In Only

&#128683; <-- Logged Out only

[Back to the top](#testing-steps)

---

# Manual Testing

## Functional Testing Required

### Bag App

#### Bag Views

* Test the view_bag URL
* Test the add_to_bag URL
* Test that the add_to_bag view adds a product to the shopping bag
* Test the adjust_bag URL
* Test the remove_from_bag URL
* Test the add_to_bag view
* Test that the add_to_bag view updates the quantity of an item if it already exists in the bag
* Test the adjust_bag view
* Test that the adjust_bag view removes the item when the quantity is less than 1
* Test the remove_from_bag view
* Test that the remove_from_bag view throws an error if something goes wrong

#### Bag Others

* Test that the delivery cost is calculated correctly
* Test that the calc_subtotal function works

![Bag App testing report from coverage](to be done)

### Band App

#### Band Views

* Test that the Contact Us page URL exists
* Test that the Contact Us page URL is accessible by name
* Test that the Contact Us page uses the correct template
* Test that the Upcoming Gigs page URL exists
* Test that the Upcoming Gigs page URL is accessible by name
* Test that the Upcoming Gigs page uses the correct template

![Band App testing report from coverage](to be done)

### Blog App

#### Blog Forms

#### Blog Views

* Test (to be done)

![Blog App testing report from coverage](to be done)

### Checkout App

#### Checkout Forms

* Test that full name is required
* Test that email is required
* Test that phone_number is required
* Test that country is required
* Test that town_or_city is required
* Test that street_address1 is required
* Test that the form fields are correct in the meta class

#### Checkout Models

* Test that the order string method returns the order number
* Test the checkout_details model
* Test the update_total model
* Test that the OrderLineItem string method returns the correct string

#### Checkout Views

* Test the cache_checkout_data view
* Test that the Checkout page URL exists
* Test that the Checkout page URL is accessible by name
* Test that the Checkout page uses the correct template
* Test that an error displays when there is nothing in the shopping bag
* Test that an error displays when the Stripe key isn't set
* Test the get in the checkout view
* Test that the user's details are auto-filled if the user is logged in and has saved information

![Checkout App testing report from coverage](to be done)

### Home App

#### Home Views

* Test that the Home page URL exists
* Test that the Home page URL is accessible by name
* Test that the Home page uses the correct template

![Home App testing report from coverage](to be done)

### Products App

#### Products Models

* Test the product name
* Test the product description
* Test the product has_sizes
* Test the category name
* Test the category friendly_name

#### Products Views

* Test that the Products page URL exists
* Test that the Products page URL is accessible by name
* Test that the Products page uses the correct template
* Test the products page view
* Test the categories view
* Test the product_detail view
* Test that the product detail page URL exists
* Test the product sort functionality
* Test the product search functionality
* Test the product search error message shows correctly
* Test that a regular user cannot access the add a product page
* Test that the add a product page displays for a superuser
* Test that a regular user cannot access the edit a product page
* Test that the edit a product page displays for a superuser
* Test that a regular user cannot access the delete a product view
* Test that the delete a product view works for a superuser

![Products App testing report from coverage](to be done)

### Profiles App

#### Profiles Forms

* Test that the user profile form fields aren't required
* Test the meta class of the user profile form

#### Profiles Models

* Test the getting user profile model

#### Profiles Views

* Test that the Profiles page URL exists
* Test that the Profiles page URL is accessible by name
* Test that a logged-in user can view the profile
* Test that the profile information gets saved correctly
* Test that the order history displays when requested

![Profiles App testing report from coverage](to be done)

### Reviews App

#### Reviews Forms

#### Reviews Views

* Test (to be done)

![Reviews App testing report from coverage](to be done)

### Omitted Code

* The main `manage.py` file has been omitted, as this is all required for the site to run.
* The Bag App `contexts.py` file has a few lines of omitted code, as these are either from the Code Institute Boutique Ado walkthrough, or are simply defining variables.
* The Band App `test_views.py` file has been omitted, as this is just testing code.
* The Checkout App `update_total`, `__str__()` and `save` functions have been omitted, as these are taken from the Code Institute Boutique Ado walkthrough.
* The Checkout App `signals.py` file has been omitted, as this sets up the basic update functionality that is used in other files, which is clear to be working because other functions wouldn't work without it.
* The Checkout App `test_models.py` file has been omitted, as this is just testing code.
* The Products App `__init__()` function has been omitted, as this code is not necessary to the functionality of the site.
* One line in the Profiles App `__init__()` function has been omitted, as this code is not necessary to the functionality of the site.
* The Profiles App `models.py` still has one line of omitted code - the `__str__()` function. I could not find a place where this function was called across the site.
* Various lines from the `settings.py` file have been omitted, as these set the variables for use throughout the site, and do not require testing.



## Devices and Browsers

### Desktop / Laptop

1. Google Chrome
    * All tested and working correctly.

2. Microsoft Edge
    * All tested and working correctly.

### Tablet

1. Safari
    * No suitable device available to carry out tablet tests.

### Mobile

1. Safari
    * All tested and working correctly.

### Full devices and browsers

* The website was tested on Google Chrome, Microsoft Edge, and Safari Internet browsers.
* Testing was not done on Internet Explorer due to it being deprecated in favour of Microsoft Edge.
* The website was viewed on joust one laptop PC and an iPhone:
  * HP Pavilion 15 laptop PC, running Windows 10
  * iPhone 11

A large amount of manual testing was done to ensure that all pages were displayed correctly at all screen sizes, and all functionality worked as it should. 

Responsive design was tested from 320px to 1900px, to account for the smallest of mobile devices, and the largest of monitors that the general public would be using.

[Back to the top](#testing-steps)

---

## Testing From User Stories

## User Stroies implpemented thus far

> - _"As a customer I wish to be able to view all merchandise available without any kind of filtering"_
> - - Catered for via the All Merchandise menu option available to all users.
> - _"As a customer I wish to be able to view merchandise filtered by categories of clothing, homeware, and music"_
> - - Catered for via the Clothing, Homeware and Music menu options available to all users.
> - _"As a customer I wish to be able to view merchandise filtered by a search function"_
> - - Catered for via the Search function available to all users in the header section across all pages.
> - _"As a customer I wish to be able to view merchandise ordered on price either listing on the cheapest or most expensive first"_
> - - Catered for via the Sort by... drop down box available to all users within the Products page reached via anyone one of the Clothing, Homeware, Music or All Merchandise menu options within in the header section.
> - _"As a customer I wish to be able to view merchandise ordered on customer ratings either listing on the highest or lowest first"_
> - - Catered for via the Sort by... drop down box available to all users within the Products page reached via anyone one of the Clothing, Homeware, Music or All Merchandise menu options within in the header section.
> - _"As a customer I wish to be able to easily specify the quantity of each item required"_
> - - Catered for with Quantity increment and decrement buttons available from both the Product Details page when adding items to the shopping bag, or from the Shopping Bag summary screen.
> - _"As a customer I wish to be able to select from a range of sizes for clothing items"_
> - - Catered for within the Product Details screen where the product has_sizes attribute is set to true. When true a size dropdown selection is presented to pick one of the values from XS, S , M , L, or XL.
> - _"As a customer I wish to be able to easily add items to / remove items from a virtual shopping bag"_
> - - Catered for within the bag app on the Shopping Bag page.
> - _"As a customer I wish to be able to easily change the quantity of individual items in the virtual shopping bag"_
> - - Catered for within the bag app on the Shopping Bag page.
> - _"As a customer I wish to be able to see the total cost of the items in the virtual shopping bag, with that value being automatically updated when the contents of the shopping bag are altered"_
> - - Catered for within the bag app on the Shopping Bag page.
> - _"As a customer I wish to be able to automatically receive an email copy of my order at the time it is placed"_
> - - Catered for by functionality that sends an email from a special store email account that sends to the email address specified in the user's profile.
> - _"As a customer I wish to be able to view, select and order merchandise regardless of whether or not I'm logged into a personal profile"_
> - - Functionaility provided.
> - _"As a customer I wish to be able to register a profile by secure access which maintains my personal details and order history"_
> - - Functionaility provided.
> - _"As a customer I wish my email to be verified when I set up a profile to prove the integrity of the email address provided"_
> - - Functionaility provided.
> - _"As a customer I wish my login password to be stored in encrypted form and only known to me"_
> - - Functionaility provided.

> - _"As a store admin I wish to be able to add/alter/delete product entries including the pricing, category, rating and images for those products"_
> - - Functionaility provided.
> - _"As a store admin I wish to be able to add/alter/delete blog entries used to promote the merchandise"_
> - - Functionaility provided.
> - _"As a user of this resource (in any capacity) I would like a responsive design that caters for mobile and non-mobile devices"_
> - - Catered for by use of the Bootstrap CSS framework.
> - _"As a registered user of this resource I would like to be able to provide a review of products and be able to edit and delete my own reviews"
> - - Functionaility provided.
> - _"As a user of this resource (in any capacity) I would like to see reviews made by other users"_
> - - Functionaility provided.
> - _"As a user of this resource (in any capacity) I would like to be able to provide comments to blog entries"_
> - - Functionaility provided.

[Back to the top](#testing-steps)

---

## Testing technologies

* HTML was validated using [W3C HTML Markup Validator](https://validator.w3.org/).
* CSS was validated using [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
* JavaScript was validated using [JSHint](https://jshint.com/).
* Python was validated using [Flake8](https://flake8.pycqa.org/en/latest/).
* Responsive design was tested using a variety of devices, as listed above in [Full devices and browsers](#full-devices-and-browsers), as well as being tested with [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse), [Am I Responsive Design](http://ami.responsivedesign.is/#), and [Responsinator](http://www.responsinator.com/).
* Accessibility was checked via [WebAim's W.A.V.E](https://wave.webaim.org/), [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/), and [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse).
* [Toptal Color-Blind Filter](https://www.toptal.com/designers/colorfilter/) was used to check that the site was suitable for color-blind users, as well as manually testing it with my color-blind partner.
* Unit Testing was done using [Django’s testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/) and [Travis CI](https://www.travis-ci.com/)'s continuous integration testing functionality.

1. W3C HTML Markup Validator
    * [Homepage](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2F)
    * [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fproducts%2F)
    * [Product Details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fproducts%2F2%2F)
    * [Shopping Bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fbag%2F)
    * [Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fcheckout%2F)
    * [Order Confirmation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fcheckout%2Fcheckout_success%2FD4C0F37FA19D4F51B2D16392BCE55B7C)
    * [Contact Us](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fband%2Fcontact-us%2F)
    * [Upcoming Gigs](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fband%2Fgigs%2F)
    * Unfortunately, as it's not possible to log in using the Validator, it was only possible to test the pages available to a user who isn't logged in.

2. W3C CSS Validator
    * [Homepage](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Products](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fproducts%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Product Details](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fproducts%2F2%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Shopping Bag](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fbag%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Checkout](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fcheckout%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Order Confirmation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fcheckout%2Fcheckout_success%2FD4C0F37FA19D4F51B2D16392BCE55B7C&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Contact Us](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fband%2Fcontact-us%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * [Upcoming Gigs](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-ms4-cpb-shop.herokuapp.com%2Fband%2Fgigs%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
    * Unfortunately, as it's not possible to log in using the Validator, it was only possible to test the pages available to a user who isn't logged in.

3. JSHint
    * [JSHint](https://jshint.com/)
    * The only comments from JSHint are about template literals, the `let` keyword, and the `$` from jQuery, all of which are JSHint making the developer aware that those features aren't available outside of ES6 and jQuery.
    * There are no JavaScript errors in this project.
    * Stripe payments
    * ![JSHint results for Stripe payments](not yet tested)
    * Social media icon hover functions
    * ![JSHint results for social media hover functions](not yet tested)
    * Country field functionality
    * ![JSHint results for country field functionality](not yet tested)
    * Quantity input field
    * ![JSHint results for quantity input functionality](not yet tested)

4. Flake8
    * [Flake8](https://pypi.org/project/flake8/)
    * `Class 'x' has no 'objects' member` and `Class 'UserProfile' has no 'DoesNotExist' member`:
        * These are just warnings from pylint. Django adds the `objects` and 'DoesNotExist' properties to all model classes, so the IDE isn't aware of this.
    * `Avoid using null=True on string-based fields such CharField`:
        * This error is there to avoid a field having two values if left blank - an empty string, and `null`. This would usually be a valid error, but because I need to allow empty values in forms, this is required, as the `null` parameter only affects database storage.
    * There are also several warnings being shown from the migrations files. These are acceptable to ignore, as they are created by Django, and [this issue has been marked as a 'won't fix'](https://code.djangoproject.com/ticket/30555) by the Django team.
    * [Click here to view the full Flake8 results](not yet available)

[Back to the top](#testing-steps)

---

## Links and Navigation

On every device and browser listed above, I plan to test the following:

### Navigation Bar

#### Logo Testing

* Click the Logo to take the user to the Home page from the Home page.
* Click the Logo to take the user to the Home page from the Products page.
* Click the Logo to take the user to the Home page from the Product Details page.
* Click the Logo to take the user to the Home page from the Shopping Bag page.
* Click the Logo to take the user to the Home page from the Checkout page.
* Click the Logo to take the user to the Home page from the Order Success page.
* &#128100; Click the Logo to take the user to the Home page from the Order Confirmation page.
* Click the Logo to take the user to the Home page from the Contact Us page.
* Click the Logo to take the user to the Home page from the Upcoming Gigs page.
* &#128100; Click the Logo to take the user to the Home page from the Profile page.
* &#128272; Click the Logo to take the user to the Home page from the Product Management page.
* &#128683; Click the Logo to take the user to the Home page from the Log In page.
* &#128683; Click the Logo to take the user to the Home page from the Register page.

#### Products Testing

* Click the All Merch button to take the user to the Products page from the Home page.
* Click the All Merch button to take the user to the Products page from the Products page.
* Click the All Merch button to take the user to the Products page from the Product Details page.
* Click the All Merch button to take the user to the Products page from the Shopping Bag page.
* Click the All Merch button to take the user to the Products page from the Checkout page.
* Click the All Merch button to take the user to the Products page from the Order Success page.
* &#128100; Click the All Merch button to take the user to the Products page from the Order Confirmation page.
* Click the All Merch button to take the user to the Products page from the Contact Us page.
* Click the All Merch button to take the user to the Products page from the Upcoming Gigs page.
* &#128100; Click the All Merch button to take the user to the Products page from the Profile page.
* &#128272; Click the All Merch button to take the user to the Products page from the Product Management page.
* &#128683; Click the All Merch button to take the user to the Products page from the Log In page.
* &#128683; Click the All Merch button to take the user to the Products page from the Register page.
* Click the Keep Shopping button to take the user to the Products page from the Shopping Bag page.
* Click the Keep Shopping button to take the user to the Products page from the Product Details page.

#### Product Details Testing

* Click the product card to take the user to the Product Details page for that product from the Products page.
* Click the product card to take the user to the Product Details page for that product from the T-Shirts Products page.
* Click the product card to take the user to the Product Details page for that product from the Music Products page.
* Click the product card to take the user to the Product Details page for that product from the Misc. Products page.
* Click the product card to take the user to the Product Details page for that product from the Product Search page.

#### Shopping Bag Testing

* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Home page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Products page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Product Details page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Shopping Bag page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Checkout page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Order Success page.
* &#128100; Click the Shopping Bag icon to take the user to the Shopping Bag page from the Order Confirmation page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Contact Us page.
* Click the Shopping Bag icon to take the user to the Shopping Bag page from the Upcoming Gigs page.
* &#128100; Click the Shopping Bag icon to take the user to the Shopping Bag page from the Profile page.
* &#128272; Click the Shopping Bag icon to take the user to the Shopping Bag page from the Product Management page.
* &#128683; Click the Shopping Bag icon to take the user to the Shopping Bag page from the Log In page.
* &#128683; Click the Shopping Bag icon to take the user to the Shopping Bag page from the Register page.
* Click the Go To Secure Checkout button on the toast message to take the user to the Shopping Bag page from any page.
* Click the Adjust Bag button to take the user to the Shopping Bag page from the Checkout page.

#### Checkout Testing

* Click the Secure Checkout button to take the user to the Checkout page from the Shopping Bag page.

#### Order Success Testing

* Click the Complete Order button and complete a purchase successfully to take the user to the Order Success page from the Checkout page.

#### Order Confirmation Testing

* Click the Order number link for a past purchase to take the user to the Order Confirmation page from the Profile page.

#### Contact Us Testing

* Click the Contact Us button in the footer to take the user to the Contact Us page from the Home page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Products page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Product Details page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Shopping Bag page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Checkout page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Order Success page.
* &#128100; Click the Contact Us button in the footer to take the user to the Contact Us page from the Order Confirmation page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Contact Us page.
* Click the Contact Us button in the footer to take the user to the Contact Us page from the Upcoming Gigs page.
* &#128100; Click the Contact Us button in the footer to take the user to the Contact Us page from the Profile page.
* &#128272; Click the Contact Us button in the footer to take the user to the Contact Us page from the Product Management page.
* &#128683; Click the Contact Us button in the footer to take the user to the Contact Us page from the Log In page.
* &#128683; Click the Contact Us button in the footer to take the user to the Contact Us page from the Register page.

#### Upcoming Gigs Testing

* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Home page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Products page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Product Details page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Shopping Bag page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Checkout page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Order Success page.
* &#128100; Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Order Confirmation page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Contact Us page.
* Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Upcoming Gigs page.
* &#128100; Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Profile page.
* &#128272; Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Product Management page.
* &#128683; Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Log In page.
* &#128683; Click the Upcoming Gigs button in the footer to take the user to the Upcoming Gigs page from the Register page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Home page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Products page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Product Details page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Shopping Bag page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Checkout page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Order Success page.
* &#128100; Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Order Confirmation page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Contact Us page.
* Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Upcoming Gigs page.
* &#128100; Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Profile page.
* &#128272; Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Product Management page.
* &#128683; Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Log In page.
* &#128683; Click the Upcoming Gigs button in the main nav bar to take the user to the Upcoming Gigs page from the Register page.

#### Profile Testing

* &#128100; Click the Profile button to take the user to the Profile page from the Home page.
* &#128100; Click the Profile button to take the user to the Profile page from the Products page.
* &#128100; Click the Profile button to take the user to the Profile page from the Product Details page.
* &#128100; Click the Profile button to take the user to the Profile page from the Shopping Bag page.
* &#128100; Click the Profile button to take the user to the Profile page from the Checkout page.
* &#128100; Click the Profile button to take the user to the Profile page from the Order Success page.
* &#128100; Click the Profile button to take the user to the Profile page from the Order Confirmation page.
* &#128100; Click the Profile button to take the user to the Profile page from the Contact Us page.
* &#128100; Click the Profile button to take the user to the Profile page from the Upcoming Gigs page.
* &#128100; Click the Profile button to take the user to the Profile page from the Profile page.
* &#128272; Click the Profile button to take the user to the Profile page from the Product Management page.

#### Product Management Testing

* &#128272; Click the Product Management button to take the user to the Product Management page from the Home page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Products page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Product Details page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Shopping Bag page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Checkout page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Order Success page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Order Confirmation page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Contact Us page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Upcoming Gigs page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Profile page.
* &#128272; Click the Product Management button to take the user to the Product Management page from the Product Management page.

#### Edit / Delete Product Testing

* &#128272; Click the Edit button to take the user to the Edit Product page from the main Products page.
* &#128272; Click the Edit button to take the user to the Edit Product page from the Product Details page.
* &#128272; Click the Delete button to open the Delete modal from the main Products page.
* &#128272; Click the Delete button to open the Delete modal from the Product Details page.
* &#128272; Click the Delete button on the Delete modal from the main Products page to delete the product.
* &#128272; Click the Delete button on the Delete modal from the Product Details page to delete the product.

#### Log Out Testing

* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Home page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Products page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Product Details page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Shopping Bag page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Checkout page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Order Success page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Contact Us page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Upcoming Gigs page.
* &#128100; Click the Log Out button to log the user out and take them to the Home page from the Profile page.
* &#128272; Click the Log Out button to log the user out and take them to the Home page from the Product Management page.

#### Log In Testing

* &#128683; Click the Log In button to take the user to the Log In page from the Home page.
* &#128683; Click the Log In button to take the user to the Log In page from the Register page.
* &#128683; Click the Log In button to take the user to the Log In page from the Product Details page.
* &#128683; Click the Log In button to take the user to the Log In page from the Shopping Bag page.
* &#128683; Click the Log In button to take the user to the Log In page from the Checkout page.
* &#128683; Click the Log In button to take the user to the Log In page from the Order Success page.
* &#128683; Click the Log In button to take the user to the Log In page from the Contact Us page.
* &#128683; Click the Log In button to take the user to the Log In page from the Upcoming Gigs page.
* &#128683; Click the Log In button to take the user to the Log In page from the Log In page.

#### Register Testing

* &#128683; Click the Register button to take the user to the Register page from the Home page.
* &#128683; Click the Register button to take the user to the Register page from the Register page.
* &#128683; Click the Register button to take the user to the Register page from the Product Details page.
* &#128683; Click the Register button to take the user to the Register page from the Shopping Bag page.
* &#128683; Click the Register button to take the user to the Register page from the Checkout page.
* &#128683; Click the Register button to take the user to the Register page from the Order Success page.
* &#128683; Click the Register button to take the user to the Register page from the Contact Us page.
* &#128683; Click the Register button to take the user to the Register page from the Upcoming Gigs page.
* &#128683; Click the Register button to take the user to the Register page from the Log In page.

[Back to the top](#testing-steps)

---

### Modals

* &#128272; The Delete modal is visible in front of all other items on the screen, and clearly displays the Cancel and Delete buttons.
* &#128272; The Delete modal only deletes the specific product that it is related to.

[Back to the top](#testing-steps)

---

### External Links

* The email icon opens up the user's email client with the Crystal Palace Band email in the recipient line.
* The Facebook social media icon opens up the Crystal Palace Band Facebook page in a new tab.
* The Instagram social media icon opens up the Crystal Palace Band Instagram page in a new tab.
* The Twitter social media icon opens up the Crystal Palace Band Twitter page in a new tab.

[Back to the top](#testing-steps)

---

## Styling and Layout

* Ensure all images load correctly.
* Ensure all images are correctly sized, and the correct aspect ratio is maintained.
* Ensure all grid layouts size correctly on all screen sizes.
* Ensure all modals appear in front of all other content on the screen.
* When hovered over the navbar links turn a dark grey color.
* When hovered over, other links turn Crystal Palace Band yellow.
* When hovered over, the email icon and related text turn yellow.
* When hovered over, the Facebook social media icon and related text turn blue.
* When hovered over, the Instagram social media icon and related text turn pink.
* When hovered over, the Twitter social media icon and related text turn blue.

[Back to the top](#testing-steps)

---

# User Access

## Logged Out Users

* &#128683; Navigation bar dropdown shows Log In, Register.

## Logged In Users

* &#128100; Navigation bar dropdown shows Profile, Log Out.

## Admin Users

* &#128272; Navigation bar dropdown shows Profile, Product Management, Log Out.

[Back to the top](#testing-steps)

---

# Functions

## Register

* &#128683;
* Creates a new user account.
* Confirm password field is checked against password field to ensure no typos are made.
* Confirm email field is checked against email field to ensure no typos are made.
* If the username already exists, it informs the user and clears the form.
* If the passwords don't match, the user is informed.
* Google Social Register takes the user to sign up via Google.

## Log In

* &#128683;
* Logs the user into their existing account.
* Checks their password entry against the stored password for their user.
* If either username or password don't match what's in the database, it returns a message.
* Google Social Sign In takes the user to sign in via Google.

## Log Out

* &#128100;
* Logs the user out of the current session user account.
* Removes all session data.

## Homepage

* &#128683;
* All products are displayed on this page.
* There is a search function, as explained below in [Search Products](#search-products).

## Profile

* &#128100;
* Only accessible for logged-in users.
* It allows users to view any order that they have made.
* It allows users to edit their personal details.

## Add Products

* &#128272;
* Only accessible for the superuser.
* Provides a form for the superuser to fill in, with placeholder text.
* All input elements have the correct validation.
* Once submitted, it adds an item into the database, which then populates it onto the site.

## Edit Products

* &#128272;
* Only accessible for the superuser.
* Provides a form for the superuser to fill in, with placeholder text.
* All input elements have the correct validation.
* The form is pre-filled in with the current item details, for easy editing.
* Once submitted, it edits the item in the database, which then populates those edits onto the site.

## Delete Products

* &#128272;
* Only accessible for the superuser.
* Creates a modal to confirm if the superuser wishes to delete this item.
* Once submitted, it deletes the item from the database, so the item can no longer be viewed on the site.
* The item will be permanently deleted from the database.

## Search Products

* Accessible by all users.
* Searches through the database for what the user has entered into the search box.
* It uses the product name and description to search within.
* It returns all results.
* It populates a message if there are no results.
* It displays the search term that the user has searched for.
* It displays the total number of items returned under that search query.

## Messages

* &#128272; If products are added to the database, the phrase '{Item} Successfully Added' should display.
* &#128272; If products are deleted from the database, the phrase '{Item} Successfully Deleted' should display.
* &#128272; If products are edited in the database, the phrase '{Item} Successfully Updated' should display.
* If a product is added to the user's shopping bag, the phrase '{Item} successfully added to your bag' should display, with a summary of the user's shopping bag.
* If a product is removed from the user's shopping bag, the phrase '{Item} successfully removed from your bag' should display, with a summary of the user's shopping bag.
* If a product quantity is updated in the user's shopping bag, the phrase '{Item} quantity successfully updated to {quantity}' should display, with a summary of the user's shopping bag.
* &#128100; If a logged-in user without access rights tries to access a restricted page, it redirects them to the homepage, and presents them with a message saying 'You do not have access to this page'.

## Stripe

* To test the webhooks and payment process, I used the following Stripe testing card numbers:
  * No authentication required, successful payment: 4242 4242 4242 4242
  * Failed payment: 4000 0000 0000 9995
  * Authentication required: 4000 0025 0000 3155
  * Any expiry date in the future, 3-digit CVC code, and 5-digit ZIP code can be used.
* The no authentication required, successful card was run, didn't ask for authentication, and successfully paid.
* The failed payment card was run and the card payment failed.
* The authentication required card was run, asked for authentication, was given authentication, and successfully paid.
* The authentication required card was run, asked for authentication, was not given authentication, and failed.
* After each payment event, a message was shown to the user to explain the action that had just happened.
* After a successful payment, the user is then redirected to the Order Success page.

## 400

* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It states clearly that it's a 400 error, and that the page does not exist.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## 401

* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It states clearly that it's a 400 error, and that the page does not exist.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## 403

* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It states clearly that it's a 403 error, and that the page does not exist.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## 404

* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It states clearly that it's a 404 error, and that the page does not exist.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## 405

* Accessible by all users
* This page will display if a user has tried to access a page that doesn't exist, or if a user doesn't have access to the page they're trying to reach.
* It states clearly that it's a 405 error, and that the page does not exist.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## 500

* Accessible by all users
* This page will display if an internal server error occurs.
* It states clearly that it's a 500 error, and that something went wrong.
* It directs the user to click the button to continue back to the safety of the site.
* The navigation bar is also available for the user to navigate back to the main site.

## Validation

* Form validation
  * This has been used on every form input on the site to ensure the correct data is added.
  * If incorrect data is added, red warning text appears, to instruct the user on how to fix the error.
* Adding products to the bag
  * Custom validation has been added to ensure that users can't:
    * Add less than one of a product into their bag (such as adding a 0 quantity of a product).
    * Add more than 50 of a product into their bag.
* Password validation
  * When a user is registering for an account, the site ensures no typos happen by prompting the user to enter the password twice, with the site checking to confirm that the passwords match.
* Email validation
  * When a user is registering for an account, the site ensures the correct email address has been entered by sending a verification email to the email address the user has supplied.
  * The account cannot be used until the user has verified that their email address is correct by following the link in the validation email.
* Image validation
  * A default image will display if there is no image added.
  * A default image will display if the image link has broken.
* Page validation
  * A custom 404 error page will show if the user attempts to visit a page that doesn't exist.
* Webhook validation
  * Webhooks form a notification system for every secure action on your site.
  * Webhooks return an event object, containing all the relevant information about the action, including the type of action, and the data associated with it.
  * If the user leaves the page before the order is complete but the payment goes through, the billing details and shipping address will be sent with the payment and can be accessed via webhooks.
* Login validation
  * If a logged-out user tries to access a restricted page, they will be redirected to the login page.
  * If a logged-in user without access rights tries to access a restricted page, it redirects them to the homepage, and presents them with a message saying 'You do not have access to this page'.

[Back to the top](#testing-steps)

---

# Database

* When the superuser adds products to the database, the information should be stored.
* When the superuser edits a product in the database, the information should be populated from the current product data into the form.
* When the superuser saves an edit to a product in the database, the information should be stored.
* When the superuser deletes a product from the database, the product should be permanently removed.
* If products are added to the database, the phrase '{Item} Successfully Added' should display.
* If products are deleted from the database, the phrase '{Item} Successfully Deleted' should display.
* If products are edited in the database, the phrase '{Item} Successfully Updated' should display.

[Back to the top](#testing-steps)

---

# Accessibility

## Tap Targets

* All tap targets are a minimum of 40px width and 40px height, to comply with WCAG Accessibility standards.
* All tap targets have a minimum of an 8px gap between them, to avoid any overlapping tap targets.

## Color Contrast

* All background and foreground colors have a sufficient contrast ratio.
* This site has been checked by a user with deuteranopia color blindness with no issues present.
* [Toptal Color-Blind Filter](https://www.toptal.com/designers/colorfilter/) was used to check every accessible page against every type of color-blindness, with no issues present. Unfortunately, the checker doesn't support logging in, so the logged-in-only pages were not able to be checked this way.
* All color contrasts were checked using [WebAIM's Contrast Checker](https://webaim.org/resources/contrastchecker/), with all large-scale text having a contrast ratio of at least 3:1, and all other text having a contrast ratio of at least 4.5:1.

## Visually-Impaired Users

* All images have meaningful alt text.
* All icons have an aria-label to describe them unless semantic text is also visible.
* All buttons that need more description for a visually-impaired user have an aria-labelledby attribute attached to them if required.

## Assistive Technologies

* All actions are keyboard-focusable.
* All interactable elements have hover and focus styling applied to them.
* All images have meaningful alt text for screen reader users.
* All icons have an aria-label to describe them unless semantic text is also visible.

## Reading Level

* All text content on the site has a maximum reading level of age 11 using the Automated Readability Index (ARI), to aid people with cognitive impairments, and people who don't speak English as a first language, among others.
* While this isn't ideal, as the recommended maximum reading level is age 9, given the site is for a ska punk band with swear words in their songs, I decided that this was an acceptable level to be at.
* All text content on this site has been tested against the ARI on [Readability Formulas](https://readabilityformulas.com/free-readability-formula-tests.php).
* The full report of all text on the site can be viewed in the [Readability Checker Results file](READABILITY.md).

[Back to the top](#testing-steps)

---

# Site Performance and Optimisation

I have picked up from mentions in other CI student MS4 projects that [Chris Anstey](https://github.com/ansteychris), a Digital Experience Lead at Google, has recommended testing with both Lighthouse and WebPageTest. Whilst they both test for the same things, Lighthouse often suffers from inaccurate readings for a wide variety of reasons. This ranges from how many browser tabs / windows you have open while you're doing the test, to how well your internet speed is performing that day. WebPageTest bypasses all of these issues, as it tests externally.

## Lighthouse

I tested my website using DevTools Lighthouse feature, and got these results:

### Desktop Lighthouse

![Lighthouse desktop first try](static/docs/img/MS4-lighthouse-desktop.png)

### Mobile Lighthouse

![Lighthouse mobile first try](static/docs/img/MS4-lighthouse-mobile.png)

### Performance Lighthouse

* On mobile screens, this score was brought down due to the images not being of a set width and height. This is because I wanted the images to be fully responsive, so explicit width and height have not been set to achieve this.
* Besides this issue on mobile, I was happy with this score.

### Accessibility Lighthouse

* I was very happy with this score.
* Please see the [Accessibility section](#accessibility) for full details of the steps I took to ensure this site was fully accessible.

### Best Practices Lighthouse

* I was very happy with this score.
* All external links are secure.
* All images are displayed with the correct aspect ratio and resolution.
* There are no issues in the Devtools Issues panel.

### SEO Lighthouse

* I was very happy with this score.
* All relevant meta tags were included.
* Each page has different meta tags, to relate to the page content.
* All links have descriptive text.

## WebPageTest

I tested my website using WebPageTest, and got these results:

* [WebPageTest Results](https://www.webpagetest.org/result/220113_AiDcZV_6bc85ccb63ff20a755f7e922e02472d5/)

[Back to the top](#testing-steps)

---

# Responsive Design

## Mobile Testing

* The Home page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Products page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Product Details page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Shopping Bag page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Checkout page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Order Success page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Order Confirmation page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Contact Us page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Upcoming Gigs page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Profile page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Product Management page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Edit Product page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Add Product page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Login page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log Out page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Register page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Delete Product modal looks good, is placed in front of all other content, and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The buttons have well-sized text, not so big it takes up too much screen space, and not so small that they're difficult to read.
* All the font sizes aren't too big or too small for the screen size.
* All fonts are easy to read.
* All images are scaled to the screen size, whilst maintaining the correct aspect ratio.

* Formal testing for Blog and Reviews apps not yet documented

## Tablet Testing

NOT ABLE TO TEST DUE TO NON-AVAILABILITY OF DEVICE

## Laptop Testing

* The Home page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Products page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Product Details page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Shopping Bag page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Checkout page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Order Success page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Order Confirmation page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Contact Us page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Upcoming Gigs page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Profile page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Product Management page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Edit Product page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Add Product page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Login page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Log Out page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Register page looks good and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The Delete Product modal looks good, is placed in front of all other content, and nothing wraps where it shouldn't or disappears off the edge of the viewport.
* The buttons have well-sized text, not so big it takes up too much screen space, and not so small that they're difficult to read.
* All the font sizes aren't too big or too small for the screen size.
* All fonts are easy to read.
* All images are scaled to the screen size, whilst maintaining the correct aspect ratio.

* Formal testing for Blog and Reviews apps not yet documented

[Back to the top](#testing-steps)

---

# Images

NONE CAPTURED YET

## Desktop and Laptop Screenshots

### Chrome Desktop Screenshots

![Home page](to be done)

![Products page](to be done)

![Product detail page](to be done)

![Order Confirmation page](to be done)

![Order Success page](to be done)

![Toast](to be done)

![Shopping Bag page](to be done)

![Checkout page](to be done)

![Upcoming Gigs page](to be done)

![Contact Us page](to be done)

![Profile page](to be done)

![Log In page]to be done)

![Log Out page](to be done)

![Register page](to be done)

![Add Merchandise page](to be done)

![Edit Merchandise page](to be done)

![Delete Merchandise modal](to be done)

[Back to the top](#testing-steps)

---

### Edge Desktop Screenshots

To be stored under testing/desktop/edge/*.png

![Home page](to be done)

![Products page](to be done)

![Product detail page](to be done)

![Order Confirmation page](to be done)

![Order Success page](to be done)

![Toast](to be done)

![Shopping Bag page](to be done)

![Checkout page](to be done)

![Upcoming Gigs page](to be done)

![Contact Us page](to be done)

![Profile page](to be done)

![Log In page](to be done)

![Log Out page](to be done)

![Register page](to be done)

![Add Merchandise page](to be done)

![Edit Merchandise page](to be done)

![Delete Merchandise modal](to be done)

[Back to the top](#testing-steps)

---

## Tablet Screenshots

### Safari Tablet Screenshots

NOT ABLE TO TEST DUE TO NON-AVAILABILITY OF DEVICE

[Back to the top](#testing-steps)

---

## Mobile Screenshots

### Safari Mobile Screenshots

To be stored under testing/mobile/safari/*.png

![Home page](to be done)

![Products page](to be done)

![Product detail page](to be done)

![Order Confirmation page](to be done)

![Order Success page](to be done)

![Toast](to be done)

![Shopping Bag page](to be done)

![Checkout page](to be done)

![Upcoming Gigs page](to be done)

![Contact Us page](to be done)

![Profile page](to be done)

![Log In page](to be done)

![Log Out page](to be done)

![Register page](to be done)

![Add Merchandise page](to be done)

![Edit Merchandise page](to be done)

![Delete Merchandise modal](to be done)

[Back to the top](#testing-steps)