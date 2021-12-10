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






