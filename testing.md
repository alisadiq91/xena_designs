![logo](https://github.com/alisadiq91/xena_designs/blob/main/media/logo.PNG)

# TESTING

## **Table of Contents**

  * [1. **HTML Validation**](#HTML-validation)
    
  * [2. **CSS Validation**](#CSS-validation)
   
  * [3. **Javascript Code Quality Tool**](#Javascript-Code-Quality-Tool)
   
  * [4. **PEP8 Validation**](#PEP8-validation)

  * [5. **Bugs**](#bugs)

  * [6. **UX Testing**](#ux-testing)

  * [7. **Further Testing**](#further-testing)

  ## HTML Validation

* I used [W3C Markup Validation Service](https://validator.w3.org/) to validate all my html pages. For the pages that are only available by a logged in user or superuser I had to view page source to ensure these were validated correctly.

* I did come accross some errors which are listed below:

  1. Carousel - the feedback carousel on the home page came up with a duplicate ID error. This was because the #activecarousel ID was in a for loop and I could not figure out a different way to make it work. I spent a long time trying to fix this issue while trying to also make sure the carousel works. 

  2. Crispy forms - I had a few errors that were due to the forms created using crispy forms. These were created following the Boutique Ado project. I did not feel as though these could be rectified as the HTML errors were coming from Python files. These errors showed in the edit product form and the review forms.

  3. Basket - I had an error with a duplicate ID. These ID's were created for responsiveness to different devices. Due to each ID being only shown once, I felt that this was okay.

## CSS Validation

* I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

* There were no errors found. 

## JavaScript code quality tool

* I used [JSHint](https://jshint.com/) to check my JavaScript code for errors.

* There were no errors for any of my javascript files or javascript code within HTML files.

## PEP8 Validation

* I used [PEP8 Online Check](http://pep8online.com/) to check that .py files were PEP8 compliant.

* I also used the command python3 -m flake8 to check if any files have any imports that are not being used.

* There were only a few warnings that I could not fix. These were lines that were too long but these were necessary as trying to fix this would cause invalid syntax errors. There was also a warning to avoid null=True on string based fields but I felt that was necessary as I was following boutique ado.

## Bugs 

1. When using the carousel I had an issue because I wanted to use a for loop. The first item in the carousel needed to have an "active" class. To overcome this I had to use some Javascript. The code is shown below :

  * ![bug-coaster](https://github.com/alisadiq91/xena_designs/blob/main/media/README/bug-coaster.png)

2. Toasts from allauth - I have a bug where the toasts that are supposed to show when a user logs in/registers/logs out are not showing. The toast div is appearing as I can see using the inspect tool but the actual text box is not showing. I tried to fix this but have had no luck. I did not have enough time to look more into it or contact student support as my deadline was approaching. Due to this bug, once a user logs in some of the toast box is covering the menu icons.

# **UX Testing**

## First time visitors

#### Aim

* As a First Time Visitor, I want to view the products the business sells. 

#### Result

* The user is drawn to the homepage straight away with a video that has an overlay showing the user where they can view the products.

* The navbar contains all the categories of products that the business has.

#### Aim

* As a First Time Visitor, I want to be able to register to create an account.

#### Result

* In the navbar the user has a link to be able to register.

#### Aim

* As a First Time Visitor, I want to be able to view any social media presence the company has.

#### Result 

* The footer contains external links to all the social media the business has.

#### Aim

* As a First Time Visitor, I want to be able to search for a product by name or description.

#### Result

* The header has a large search bar in the middle to catch the eye of the user. On mobile view the search bar drops down once the user clicks the search icon.

* The search function looks through item names and descriptions.

* The user is shown how many products their search has produced.

#### Aim

* As a First Time Visitor, I want to be able to navigate easily through the website, on desktop, mobile and tablet.

#### Result

* Using bootstrap classes and css media queries the website is responsive to all devices.

#### Aim

* As a First Time Visitor, I want to be able to see feedback/reviews from other users.

#### Result 

* In the header navigation links is a link to the review page. This page shows the user all the reviews from other users.

* The home page has a carousel that scrolls through all the reviews left by other users.

## **Returning users** 

#### Aim 

* As a Returning Visitor, I want to be able to log in to my account easily.

#### Result

* The user is able to click a remember me checkbox to make it easier to next time.

* Every page contains the header which has a link to the login page.

#### Aim

* As a Returning Visitor, I want to be able to view my profile to see my details.

#### Result 

* The header has a link to the users profile, where they can see their saved details or previous orders.

#### Aim

* As a Returning Visitor, I want to be able to add items to a wishlist to purchase in the future.

#### Result

* If a user is logged in, they are able to add items to their wishlist from the product details page. They can then view this wishlist which is in the header.

* There is an option for the user to add the item to their bag on the wishlist page which takes them to the product detail page. 

#### Aim

* As a Returning Visitor, I want to be able to view my basket and purchase a product.

#### Result 

* Each time adds something or edits their basket, as long as there is an item in the basket they are shown a preview through a toast message box. 

* In the header the user is shown the total of the items in their basket and can click this icon to be taken to their basket.

* Stripe payments is used for the user to be able to pay for their products.

* The user is sent a checkout confirmation email.

#### Aim

* As a Returning Visitor, I want to be able to logout of my profile before ending my session.

#### Result

* The header has a link for the user to logout. They are taken to the logout page which asks the user to confirm whether this is something they want to do.

## **Frequent users**

#### Aim 

* As a Frequent User, I want to be able to add a review to the business, as well as edit or delete previous reviews.

#### Result

* Only logged in users can add a review to the website.

* The review page has a link which takes the user to the add review page, where they can add a title and comments to their review.

* On the review page, if the user was the creator of the review, they can edit or delete this by clicking the buttons that are shown. If they edit the review they are taken to a pre-filled form which is editable.

#### Aim 

* As a Frequent User, I want to be able to update my profile information.

#### Result

* On the profile page, the user is shown a pre-filled form with their information. They are able to edit this and update their information at any time.

#### Aim

* As a Frequent User, I want to be able to view my previous orders.

#### Result 

* On the profile page, the user is shown a table of their previous orders. They can click the order number to show a more detailed confirmation of their order.

#### Aim

* As a Frequent User, I want to be able to reset my password if I forget it.

#### Result 

* On the login page, the user is given the option to click forgot password. This takes the user to a page where they can enter their email in. Once the form is submitted they are sent an email where they can reset their password by clicking the link.

## **Admin users**

#### Aim

* As an Admin User, I want to be able to add, edit and delete products.

#### Result

* If the user is logged in as an admin they are able to see a product management link. This takes the user to the add product page.

* On the products and product detail pages, if the user is logged in as an admin they are shown edit/delete buttons.

* The user can also go to the django admin page to add, edit, and delete products.

#### Aim

* As an Admin User, I want to be able to view all users and orders.

#### Result 

* The user can go to the django admin page where they can see all the users registered and all the orders that have been placed and by who.

# **Further Testing**

* The Website was tested on Google Chrome, Internet Explorer, Mozilla Firefox and Safari browsers.

* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone11 (portrait and landscape), iPad (portrait and landscape), Samsung Galaxy S10 (portrait and landscape) and other android devices.

* I used the chrome inspect extension tool to make sure it responded to all devices.

* Each link was clicked various times on each page and each device to ensure they were all working correctly.

* Products were added and updated quantites in the basket numerous times, as well as checkout using stripe.

* All the forms were filled out numerous times. Each form was filled out deliberately with errors to see if the form validation was working correctly. 

* I asked 10 family and friends to use the website and look for any errors or bugs. I asked them all to view the website on their laptop, phone, and tablet. I also asked them to try all the links, and to fill the forms out with errors to see if it allowed them to submit.
