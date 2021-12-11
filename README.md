![logo](https://github.com/alisadiq91/xena_designs/blob/main/media/logo.PNG)

# **Ali Sadiq MS4 – Xena Designs**

[View the live project here.]( https://xena-designs.herokuapp.com/)

## **Project Overview**

Welcome to the fourth and final project of my software development career. I have decided to create an e-commerce site for a friend of mine who has a resin art business. The business currently makes all their sales through instagram and I feel as though a website will increase their sales massively. The website will give users the opportunity to view all the products, filter through them and purchase products, as well as many other functions. The site will be made using the Python framework Django, as it is something new that I have learnt over the last few months. I will also be using languages I have learnt in previous modules such as HTML, JavaScript, CSS, as well as other frameworks. The main focus of this website is to create a fully functioning e-commerce store that is useful to guests, registered users and also the admin.

The website is called Xena Designs. They are a small business that creates resin products for use around the home, as well as other personalised products.

## **Table of Contents**

  * [1. **UX**](#UX)
    + [**First time users**](#first-time-visitor-goals)
    + [**Returning users**](#returning-visitor-goals)
    + [**Frequent users**](#frequent-user-goals)
    + [**Admin users**](#admin-user-goals)

  * [2. **Design**](#DESIGN)
    + [**Colour Scheme**](#colour-scheme)
    + [**Typography**](#typography)

  * [3. **Wireframes & Features**](#wireframes-and-features)
    + [**Header**](#header)
    + [**Footer**](#footer)
    + [**Home**](#home-page)
    + [**Products**](#products-page)
    + [**Product details**](#products-detail)
    + [**Login**](#login-page)
    + [**Register**](#register-page)
    + [**Profile**](#profile-page)
    + [**Product Management**](#product-management-page)
    + [**Wishlist**](#wishlist-page)
    + [**Reviews**](#reviews-page)
    + [**Basket**](#basket-page)
    + [**Checkout**](#checkout-page)
    + [**Toasts**](#toasts)

  * [4. **Technologies Used**](#Technologies)

  * [5. **Testing**](#testing)

  * [6. **Deployment**](#deployment)

  * [7. **Content**](#content)

  * [8. **Media**](#media)

  * [9. **Acknowledgements**](#acknowledgements)

# **UX**

## First Time Visitor Goals

1.  As a First Time Visitor, I want to view the products the business sells.

2.  As a First Time Visitor, I want to be able to register to create an account.

3.  As a First Time Visitor, I want to be able to view any social media presence the company has.

4.  As a First Time Visitor, I want to be able to search for a product by name or description.

5.  As a First Time Visitor, I want to be able to navigate easily through the website, on desktop, mobile and tablet.

6. As a First Time Visitor, I want to be able to see feedback/reviews from other users.

## Returning Visitor Goals

1.  As a Returning Visitor, I want to be able to log in to my account easily. 

2.  As a Returning Visitor, I want to be able to view my profile to see my details.

3.  As a Returning Visitor, I want to be able to add items to a wishlist to purchase in the future.

4.  As a Returning Visitor, I want to be able to view my basket and purchase a product.

5.  As a Returning Visitor, I want to be able to logout of my profile before ending my session.


## Frequent User Goals

1.  As a Frequent User, I want to be able to add a review to the business, as well as edit or delete previous reviews.

2.  As a Frequent User, I want to be able to update my profile information.

3.  As a Frequent User, I want to be able to view my previous orders.

4.  As a Frequent User, I want to be able to reset my password if I forget it.

## Admin User Goals

1. As an Admin User, I want to be able to add, edit and delete products.

2. As an Admin User, I want to be able to view all users and orders.

# **DESIGN**

## Colour Scheme

* The three main colours used are grey, white, and black.

## Typography

* The El Messiri (from google fonts) is the font used for this site, with different weights and italics. 

* Sans Serif is used as the fall-back font if for any reason the above font is not functioning. 

* A sharp, professional yet artsy theme is set which the El Messiri font achieves. The font is clear and easy to read.

# **WIREFRAMES AND FEATURES**

# **Header**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap, Django, JQuery

### Desktop Header wireframe

![wireframe-header-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-header-dt.jpeg)

### Mobile Header wireframe

![wireframe-header-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-header-mb.jpeg)

### Desktop Header

![header-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/header-dt.png)

## Features:

1. Free delivery banner - This shows at the top of each page to stand out to the user. It tells them how much they need to spend to achieve free delivery.

2.  The logo – this is of course in the header to the left, so it is on every page. On mobile devices the logo sits under the navbar. This also links you back to the homepage.

3.  Burger Menu – in mobile view, the navigation menu becomes a burger menu, which the user can click to open the rest of the menu. This saves space for the user, allowing them to easily navigate through the website. The burger menu is beside a search button, a link to the users account and a link to the basket.

![header-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/header-mb.png)

4. Search bar - search bars are a huge part of e-commerce sites so this is in the middle of the navbar

5. Main links - to the right on desktop is a dropdown menu for account functions, a wishlist link (which links to the login page if a user is not logged in) and to the users basket. The dropdown items for the account vary depending on whether a user is signed in or not. Each main link has an icon from font awesome and changes colour to grey when hovering.

My Account dropdown list :

•	When the user is not logged in, they are shown 2 links, Login and Register.

•	When the user is logged in, they are shown 2 links, My Profile and Logout.

•	When the user is logged in as a superuser, they are shown 3 links, Product Management, My Profile and Logout.

6. Shop links - there are 8 links here, 1 to the homepage, 6 to different categories of items, and the last one to the review page. 

## Features considered or to implement:

1. A feature I considered was to have a preview of the basket once someone clicks the basket icon - similar to the toast success message you get when adding to the basket. 

# **Footer**

* Languages used – HTML, CSS

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap

### Footer wireframe desktop

![wireframe-footer-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-footer-dt.jpeg)

### Footer wireframe mobile

![wireframe-footer-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-footer-mb.jpeg)

## Features:

1. Social media – the footer contains social media links to the company’s Facebook, Instagram and TikTok. These external links all open in a new tab.

2. About us - to give the user a short description of the business.

3. Contact Us - a link straight to the users email to send a message to the business.

### Footer on desktop:

![footer-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/footer-dt.png)

### Footer on mobile:

![footer-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/footer-mb.png)

# **Home page**

* Languages used – HTML, CSS, Python, javaScript

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap, Django, JQuery

### Desktop wireframe

![wireframe-home-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-home-dt.jpeg)

### Mobile wireframe

![wireframe-home-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-home-mb.jpeg)

## Features

1.  Video with overlay – Here is a video showing how the business makes their products. This entices the viewer and has an overlay of text telling the user to shop now! If the video does not load for any reason, the user is shown a packaged product from the business.

2.  Mobile - on mobile view, the shop now button is placed below the video.

3.  Carousel - there is a feedback carousel which using python shows the user all the reviews that have been made on the website. Each card shows the review title, comments and who it was created by. There is a link below the carousel for users to go to the review page and see all the feedback.

### Homepage desktop

![homepage-desktop-video](https://github.com/alisadiq91/xena_designs/blob/main/media/README/video-dt.png)

![homepage-desktop-carousel](https://github.com/alisadiq91/xena_designs/blob/main/media/README/carousel-dt.png)

### Homepage mobile

![homepage-mobile-video](https://github.com/alisadiq91/xena_designs/blob/main/media/README/video-mb.png)

![homepage-mobile-carousel](https://github.com/alisadiq91/xena_designs/blob/main/media/README/carousel-mb.png)

## Features to implement:

1.  I had the idea to have a carousel with new arrivals to the shop but decided against it as I thought the review carousel was more important.

2. I thought to have a step by step guide showing the user how the products are made, but decided against it as I wanted to keep the page simple.

# **Products page**

* Languages used – HTML, CSS, JavaScript, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Django, AWS, Jquery

#### Products page desktop wireframe

![wireframe-products-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-products-dt.jpeg)

#### Products page mobile wireframe

![wireframe-products-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-products-mb.jpeg)

#### Products page desktop

![products-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/products-dt.png)

#### Products page mobile

![products-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/products-mb.png)

## Features

1.  Title - the title of the page varies depending on which category you are looking at.

2. Product Count - you are told how many products you are looking at through your search/filter. If you search a word then you are told "27 Products found for 'word'".

3. Sort By - you are given the option to sort by price ascending or descending.

4.  Products – the products are displayed as cards. Each card contains the product image, name, category it is in, and the price. The cards have horizontal rules after them, which depends on how many cards are on one line depending on screen size. 

5. Edit/Delete - if the user is a superuser, they are also shown edit/delete options under each product.

6. Link to product detail - the user is taken to the product detail page once they click a product.

## Features to implement

1. If I had more time I would have added a fixed button for the user to jump back to the top of the page.

2. I could also have added pagination to ensure the page does not become too long when more products are added.

# **Product details page**

* Languages used – HTML, CSS, JavaScript, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Django, AWS, Jquery

#### Product details page desktop wireframe

![wireframe-product-details-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-detail-dt.jpeg)

#### Product details page mobile wireframe

![wireframe-product-details-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-detail-mb.jpeg)

#### Products detail page desktop

![product-details-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/detail-dt.png)

#### Product detail page mobile

![product-details-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/detail-mb.png)

## Features

1. Product Card - Similar to the product page but with more details. There is now a description of the product along with the name, category and price.

2. Size options - If the product has sizes, the user is given the option to select the size of the product they would like.

3. Quantity selection - The user can choose the quantity of the item that they would like to add to their basket.

4. Add to Basket - this button adds the item to the users basket. If the process is successful the user is met with a toast success giving them a preview of their basket.

5. Add to Wishlist - this button adds the item to the users wishlist. If the user is not logged in this button takes them to the login page. Once the item is added to the wishlist, this button changes to "remove from wishlist". 

6. Keep shopping - this button takes the user back to the products page. 

# **Login page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, Django

#### **Login page**

![login-page](https://github.com/alisadiq91/xena_designs/blob/main/media/README/login.png)

## Features

1.	This page uses the django allauth function. The validation of the form is already provided by the templates. As shown below:

![login-fail](https://github.com/alisadiq91/xena_designs/blob/main/media/README/login-fail.png)

2. Forgotten password - also provided by the allauth templates

![forgot-password](https://github.com/alisadiq91/xena_designs/blob/main/media/README/password-reset.png)

3.  Register – above the form, the user is shown where to Register in case they do not have an account already. 

5.  Once the user has successfully logged in, the user is taken back to the homepage.

## Features to implement:

1. I wanted to add the option where the user can log in via their social media accounts or email accounts but I did not have the time to do this.

# **Register page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, Django

#### **Register page**

![register-page](https://github.com/alisadiq91/xena_designs/blob/main/media/README/register.png)

## Features

1.	This page uses the django allauth function. The validation of the form is already provided by the templates. As shown below:

![register-fail](https://github.com/alisadiq91/xena_designs/blob/main/media/README/register-fail.png)

2.  Login – above the form, the user is shown where to login in case they have an account already. 

3. Once the user has registered, they are told they must confirm their registration using the email they recieve. 

## Features to implement:

1. I wanted to add the option where the user can register via their social media accounts or email accounts but I did not have the time to do this.

# **Profile page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap, Django

### Profile page Wireframe

![wireframe-profile-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-profile.jpeg)

### Profile page desktop

![profile-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/profile-dt.png)

![profile-mobile-1](https://github.com/alisadiq91/xena_designs/blob/main/media/README/profile-mb-1.png)
![profile-mobile-2](https://github.com/alisadiq91/xena_designs/blob/main/media/README/profile-mb-2.png)

## Features

1. Default Delivery Information - here the user will see their saved delivery information. When the user checks out, if they are logged in they are given the option to save the information to their profile. The user can update their information through their profile at any time. 

2. Order History - here the user will see all the orders they have placed. This is done as a table, where the headings are order number, date, items, and order total. The user can click the order number which will take them to their order confirmation screen giving them more information about the order.

## Features to implement:

1. I had the idea that a user could add and manage their debit/credit cards on their profile so they could use these during the checkout.


# **Product Management page**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - Bootstrap, Django, JQuery

### Product Management page Wireframe

![wireframe-management](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-addproduct.jpeg)

### Product Management page desktop

![add-product-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/add-product-dt.png)

![edit-product](https://github.com/alisadiq91/xena_designs/blob/main/media/README/edit-product.png)

## Features

1. This page is only available to admin/superusers. If the user tries to access this page without being a superuser, they will be redirected to the login page (if not logged in) or the home page (if logged in but not a superuser).

2. The form - the form to add the product has the following fields:

  1. Category - using a dropdown list
  2. Sku
  3. Name 
  4. Description
  5. Has sizes - using a dropdown list
  6. Price
  7. Image URL
  8. Image Upload

  The form uses crispy forms from django. The validation of these form is all provided by this.

3. If the superuser is editing a product, the same form is shown but it is pre-filled with the relevant product details. 

## Features to implement:

1. I had the idea to have a card for each product on the management page where the admin can easily navigate products and edit/delete them without having to find them through the products page. 

2. I also had the idea of having different types of users. For example having a manager user who can perform all actions. Where as a sales manager user who can only edit products instead of deleting them.


# **Wishlist**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - Bootstrap, Django, JQuery

### Wishlist page Wireframe

![wireframe-wishlist](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-wishlist.jpeg)

### Wishlist page desktop

![wishlist-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wishlist-dt.png)

### Wishlist page mobile

![wishlist-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wishlist-mb.png)

## Features

1. This page is only available to users who are logged in. If a user is not logged in and try to access this page they are taken to the login page.

2. The Wishlist - the page is very simple. It shows all the products the user has added to their wishlist in a table, similar to the basket. 

3. Add/Remove options - the user is given the option to remove the item from the wishlist. The user is also given the option to add the item to their basket. Clicking this link will take the user to the product detail page.

## Features to implement:

1. If I had more time I would have wanted to add an option where the user can add the item straight to their basket from the wishlist, instead of going through the product detail page. 

2. It would also have been a good idea to include a "share your wishlist" option. Where the user can send their wishlist via email/social media to a friend. 


# **Reviews**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, Django

### Review page Wireframe desktop

![wireframe-review-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-reviews-dt.jpeg)

### Review page Wireframe mobile

![wireframe-review-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-reviews-mb.jpeg)

### Reviews page desktop

![reviews-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/reviews-dt.png)

### Reviews page mobile

![reviews-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/reviews-mb.png)

## Features

1. This is a simple page which shows the users the reviews that have been added by other users.

2. The cards show the review title, comment, date, and who it was created by.

3. Add review - if the user is logged in, they are shown a link where they can add a review. They are taken to a form for them to add a review. This is shown below:

### Add review Wireframe

![wireframe-add-review]()

### Add review page desktop

![add-review-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/add-review-dt.png)

### Add review page mobile

![add-review-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/add-review-mb.png)

4. Edit/Delete - the user is shown buttons to both edit and delete their review if they were the one who created it. If the user chooses to edit their review they are taken to the page shown below which is a pre-filled form with the relevant title and comment :

### Edit Review page

![edit-review](https://github.com/alisadiq91/xena_designs/blob/main/media/README/edit-review.png)

5. Mobile responsiveness - the cards are shown one on each line if the device is a smaller screen. 

## Features to implement:

1. I was considering having only users that have bought a product to be allowed to write a review. However the business has all of it's sales from instagram at the moment, so this would rule customers out from being able to write a review.

2. If I had more time I would have added the option for customers to review individual products that they buy.

3. I would have liked to be able to add a star rating to the reviews.

# **Basket**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - Bootstrap, Django, JQuery, [Font Awesome](https://fontawesome.com/)

### Basket page Wireframe desktop

![wireframe-basket-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-basket-dt.jpeg)

### Basket page Wireframe mobile

![wireframe-basket-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-basket-mb.jpeg)

### Basket page desktop

![basket-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/basket-dt.png)

### Basket page mobile

![basket-mobile-1](https://github.com/alisadiq91/xena_designs/blob/main/media/README/basket-mb-1.png)
![basket-mobile-2](https://github.com/alisadiq91/xena_designs/blob/main/media/README/basket-mb-2.png)

## Features

1. The user is shown a table summarising the products they have bought. The table has the following headings - Product Info, price, quantity, and subtotal. The product info contains an image of the product, as well as it's name, product code, and size if applicable.

2. Quantity - the quantity column gives the user the option to increase or decrease the quantity. Once they do this, there is an update option for them to click once the quantity has changed. There is also a remove option where the user can remove the product from the basket completely.

3. Price summary - underneath the table the user is shown the basket total, along with the delivery charge. If the delivery charge is less than the free delivery threshold, the user is told how much they need to spend before they qualify for free delivery. The grand total is then shown.

4. Buttons - at the bottom of the page the user is shown a checkout button, as well as a keep shopping button. The checkout button takes the user to a secure checkout. The keep shopping button returns the user to the products page.

5. Empty basket - if the user has no items in their basket, they are told their basket is empty and shown a button to return the user to the products page, as well as a button to view their wishlist. This is shown below:

![empty-basket](https://github.com/alisadiq91/xena_designs/blob/main/media/README/basket-empty.png)

6. Mobile responsiveness - to get the table to respond to mobiles, I had to create seperate HTML files and use includes to include them in the main HTML file. This allowed me to easily adjust the table and have it respond to mobile devices.

# **Checkout**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - Bootstrap, Django, JQuery, [Font Awesome](https://fontawesome.com/)

### Checkout page Wireframe desktop

![wireframe-checkout-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-checkout-dt.jpeg)

### Checkout page Wireframe mobile

![wireframe-checkout-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/wireframes/wf-checkout-mb.jpeg)

### Checkout page desktop

![checkout-desktop](https://github.com/alisadiq91/xena_designs/blob/main/media/README/checkout-dt.png)

### Checkout page mobile

![checkout-mobile](https://github.com/alisadiq91/xena_designs/blob/main/media/README/checkout-mb.png)

## Features

1. This is a simple page which contains a form for the user to fill out their delivery and billing details, as well as a basket summary.

2. Basket Summary - to the right of the page the user is shown an order summary. This shows the user the items they are ordering with subtotal, order total, delivery, and grand total.

3. Details form - the page contains a crispy form for the user to fill out. It asks for their contact details, delivery information and their card details. The form validation is done by Django. 

4. Save information - if the user is logged in, they are given an option to tick a checkbox to save their delivery information for use later. If the user is not logged in they are still told they can register or login to save this information.

5. Buttons - at the bottom of the form the user is shown 2 buttons, one to adjust their basket and the other to complete their order.

6. Stripe Payment - the card details are checked by stripe. If the card details are incorrect the user will be shown an error message that is relevant. An example is shown below : 

![card-error](https://github.com/alisadiq91/xena_designs/blob/main/media/README/card-error.png)

7. Loading overlay - once the user attempts to checkout, they are shown a loading overlay. This will either take the user to the checkout success page or return them to the checkout page if there is an error.

8. Stripe webhooks - I set up stripe webhooks by following the boutique ado project. This is done to ensure that if users place an order and there is an error at some point, the order will still reach the business if the error is not because of any incorrect details. The business can still view the order in the django admin and also in their stripe account. 

9. Checkout Success - once the order has gone through, the user is taken to a checkout success page where they are shown their order confirmation. This shows the user the details of their order and lets them know that they will recieve a confirmation email also. These two are shown below :

 - Checkout Success:
 ![checkout-success](https://github.com/alisadiq91/xena_designs/blob/main/media/README/order-confirm-dt.png)

 - Order confirmation email:
 ![email-confirmation](https://github.com/alisadiq91/xena_designs/blob/main/media/README/email-confirm.png)

10. Mobile responsiveness - on mobiles the basket summary is placed above the checkout form.

## Features to implement:

1. As mentioned above in the profile section, I was considering adding an option for a user to save their card details for future purchases. 

# **Toasts**

* Languages used – HTML, CSS, Python, JavaScript

* Frameworks, Libraries & Programs Used - Bootstrap, Django, JQuery, [Font Awesome](https://fontawesome.com/)

### Toast Success example

![toast-success](https://github.com/alisadiq91/xena_designs/blob/main/media/README/toast-sucess.png)

### Toast Success with Basket

![toast-basket](https://github.com/alisadiq91/xena_designs/blob/main/media/README/toast-sucess-basket.png)

## Features

1. These toasts are shown whenever a user interacts with the website. For example if a user signs in they are met with an alert telling them that they have signed in as user. There are 4 types of toasts - error, info, success, and warning.

2. Basket summary - if the user adds a product to their basket they are shown a preview of their basket as well as the success message. If there are no items in the users basket, no preview is shown. 

# **TECHNOLOGIES**

## Languages Used

* HTML5

* CSS3 

* JavaScript

* Python

## Frameworks, Libraries & Programs Used

* Bootstrap

    * Bootstrap was used to assist with the responsiveness and styling of the website.

* Google Fonts:

    * Google fonts was used to obtain the El Missiri font.

* Font Awesome:

    * Font Awesome icons were used regularly on the website

* JQuery:

    * JQuery was used to make it easier to use JavaScript. It gives me cleaner code and is very effective.

* Django:

    * Django was used as it enables rapid development of secure and maintainable websites. It saved me a vast amount of time. 

* AWS (Amazon Web Services):

    * AWS was used to store all the images and videos through a web interface.

* Stripe Payments:

    * Stripe Payments were used to allow the website to take card payments. It is a fast and easy to implement service.

* [JSON Formatter](https://jsonformatter.org/):

    * A JSON formatter was used to make my code more readable when uploading the products.  

* Git

    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* GitHub:

    * GitHub is used to store the projects code after being pushed from Git.

* Heroku:

    * Heroku is used for remote hosting the website.


# **TESTING**

[This section can be found here.](https://github.com/alisadiq91/xena_designs/blob/main/testing.md)

# **DEPLOYMENT**

This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. 

I had to deploy the project to Heroku as Github can only host static websites. Heroku is a compatible hosting platform for a back-end focused projects like this one.

The Code Institute student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

### Project and Repository Creation

Follow these steps to clone/create a similar repository:

1. Navigate to [Github](https://github.com/).

2. Login 

3. Create a new repository by clicking new.

4. Select the Code Institute template in the templates section.

5. Give the repository a name.

6. Click the green 'Create Repository' button at the bottom of the page.

7. Inside the repository click the green 'gitpod' button to initialize your repository.

8. If you want to load this workspace in the future, this must be done through gitpod.

9. Use the `git add .` command to add all modified and new files to the staging area.

10. Use the `git commit -m` command to commit a change to the local repository. Ensure you write a short statement saying what you have 

11. Use the `git push` command to push all committed changes to Github.   

Before deploying the website to Heroku, the steps below should be followed:

1. Create a requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development. This is done by using this command:

    - pip freeze --local > requirements.txt

2. Create a Procfile that contains the name of the application file so that Heroku knows what to run.

3. Push these files to GitHub using the way explained above. 

4. Install `psycopg2` and `dj_datatbase_url` in your workspace CLI.

Once those steps are done, the website can be deployed in Heroku using the steps listed below:

### Deployment Steps

1. Log into Heroku.

2. Click the New button.

3. Click the option to create a new app.

4. Enter the app name in lowercase letters. This must be unique and Heroku will tell you if the app name has already been used.

5. Select the correct geographical region closest to you. 

### Connect Heroku app to Github repository

1. In Heroku select the deploy tab.

2. Click the GitHub button.

3. Enter the repository name and click search.

4. Select the relevant repository and click connect. 

### Add Heroku Postgres Database

1. Click the resources tab in Heroku.

2. Under Add-ons search for Heroku Postgres.

3. Click on Heroku Postgres when it appears. 

4. Select the Hobby Dev-Free option in plans. 

5. Click submit order form.

### Setting up environment variables

1. In the heroku settings click the reveal config vars button and set the following variables:

    - AWS_ACCESS_KEY_ID

    - AWS_SECRET_ACCESS_KEY

    - DATABASE_URL

    - EMAIL_HOST_PASS

    - EMAIL_HOST_USER

    - SECRET_KEY

    - STRIPE_PRICE_ID

    - STRIPE_PUBLIC_KEY

    - STRIPE_SECRET_KEY

    - STRIPE_WH_SECRET
    
    - USE_AWS

- The values of these variables are secret and for security purposes wont be shared here. 

### Setting up the AWS s3 bucket
1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
    - Allow public access
3. Under Properties > Static website hosting
    - Enable
    - index.html as index.html
    - save
4. Under Permissions > CORS use the following:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": [

      ]
  }
]
```
5. Under Permissions > Bucket Policy:
    - Generate Bucket Policy and take note of Bucket ARN
    - Chose S3 Bucket Policy as Type of Policy
    - For Principal, enter *
    - Enter ARN noted above
    - Add Statement
    - Generate Policy
    - Copy Policy JSON Document
    - Paste policy into Edit Bucket policy on the previous tab
    - Save changes
6. Under Access Control List (ACL):
    - For Everyone (public access), tick List
    - Accept that everyone in the world may access the Bucket
    - Save changes

**AWS IAM (Identity and Access Management) setup**
1. From the IAM dashboard within AWS, select User Groups:
    - Create a new group
    - Click through and Create Group
2. Select Policies:
    - Create policy
    - Under the JSON tab, click Import managed policy
    - Choose AmazonS3FullAccess
    - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    - Click next step and go to Review policy
    - Give the policy a name and description of your choice
    - Create policy
3. Go back to User Groups and choose the group created earlier
    - Under Permissions > Add permissions, choose Attach Policies and select the one just created
    - Add permissions
4. Under Users:
    - Choose a username 
    - Select Programmatic access as the Access type
    - Click Next
    - Add the user to the Group just created
    - Click Next and Create User
5. Download the `.csv` containing the access key and secret access key.
    - **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN, BE SURE TO SAVE THE FILE SOMEWHERE.**

**Connecting Heroku to AWS S3**
1. Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
3. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
    - **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**


### Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.


### Connect app to Github Repository

1. Click the deploy tab and connect to GitHub.
2. Type the name of the repository into the search bar presented.
3. Click the Code dropdown button next to the green Gitpod button.
4. When the correct repository displays click the connect button.

### Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/adilkhr/my-ms4-project).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively, copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone’ and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project has been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

### How to Fork the repository.

1. Log into GitHub.
2. In Github go to (https://github.com/adilkhr/my-ms4-project).
3. In the top right-hand corner click "Fork".


# **CONTENT**

### All content was written by the coder apart form those listed below.

* [Bootstrap footer](https://mdbootstrap.com/docs/b4/jquery/navigation/footer/)

* [Bootstrap carousel](https://www.codeply.com/go/EIOtI7nkP8/bootstrap-carousel-with-multiple-cards)

* Parts of this project were completed using the Boutique Ado project.

# **MEDIA**

### I obtained my images personally from the business owner. The only images not from the business owner are below:

* [No Image](https://media.istockphoto.com/vectors/no-image-available-icon-vector-id1216251206?k=20&m=1216251206&s=612x612&w=0&h=BANco7qp0Ofqkod-ODPsbZVqVok7R5qUSznMN0AsMx8=)

# **ACKNOWLEDGEMENTS**

* My Mentor for continuous helpful feedback.

* The Code Institute tutor support team for pointing me in the right direction when I needed help.

* The Slack community for helping me with some queries

# **Thank you!!**

#### Thank you for taking the time to enjoy my fourth project as a web developer. I thoroughly enjoyed creating this website, as I got to create an e-commerce website which is something I have always wanted to do! This is a website that I would like to go live in the near future as the business is something that is important to me. I hope you enjoy using my website!

