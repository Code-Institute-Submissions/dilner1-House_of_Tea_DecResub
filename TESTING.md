# Testing

## Lighthouse

Both the Mobile and Desktop scores here were very high as expected however the performance was noticably under performing. The slow performace is likely down to the images used, this could be improved with better compression on these files.

### Desktop Lighthouse Score

![Desktop Lighthouse Score](media/lighthouse_desktop.png)

<br>

### Mobile Lighthouse Score

![Desktop Lighthouse Score](media/lighthouse_mobile.png)

<br>

## Validation

## CSS
[Jigsaw W3](https://jigsaw.w3.org/css-validator/) was used to validate the CSS files, below are the results for this:


![CSS Validation](media/css_validation.png)

<br>

### HTML
[W3](https://validator.w3.org/) was used to validate the HTML files, below are the results for this:



**Home Page**
![HTML index Validation](media/html_index_validation.png)


**Products Page**
![HTML index Validation](media/html_products_validation.png)


**Product info Page**
![HTML index Validation](media/html_products_info_validation.png)


**Basket Page**
![HTML index Validation](media/html_basket_validation.png)


**Checkout Page**
![HTML index Validation](media/html_checkout_validation.png)


**Checkout Success Page**
![HTML index Validation](media/html_checkout_success_validation .png)


**Suppliers Page**
![HTML index Validation](media/html_suppliers_validation.png)


**Contact Page**
![HTML index Validation](media/html_contact_validation.png)


**Newsletter Page**

Unfortunately when validating the site link a 500 error was returned, I could not see why this would be the case so for now have just validated via direct input

![HTML index Validation](media/html_newsletter_validation.png)


**Login Page**
![HTML index Validation](media/html_login_validation.png)


**Logout Page**
![HTML index Validation](media/html_logout_validation.png)


**Signup Page**
![HTML index Validation](media/html_logout_validation.png)


**Email Page**
![HTML index Validation](media/html_email_validation.png)


**Password Page**
![HTML index Validation](media/html_password_validation.png)

<br>

### Javascript

JSHint was used to validate the Javascript files / scripts
https://jshint.com/

The files tested were:
1. basket.html script
2. stripe_elements.js
3. quantity_adjuster_script.html  


### basket.html js

JS Hint picked up seven warnings below, the first three are because I included the script tag which was unneccessary. Issue 4 is irrelevant as the purpose is just to submit the form. Issue 5 relating to template literals is also not an issue here as the code works as intended, it is only an issue for JSHint - this is also how it was taught on the course. The last issues appear to be purely because of the script tag mentioned before.

1. 11 Expected an identifier and instead saw '<'
2. 11 Expected an assignment or function call and instead saw an expression.
3. 11 Missing semicolon.
4. 16 Expected an assianment or function call and instead saw an expression.
5. 23 template literal syntax' is only available in ES6 (use
'esversion: 61).
6. 32 Unclosed regular expression.
7. 32 Unrecoverable syntax error. (100% scanned)


![JS basket.html Validation](media/js_basket_validation.png)


### stripe_elements.js

The only warnings here were relating to template literals again which is not an issue for functioning JS code, this is an issue only JSHint seems to bring up.


1. 26	'template literal syntax' is only available in ES6 (use 'esversion: 6').
2. 51	'template literal syntax' is only available in ES6 (use 'esversion: 6').

<br>

There were several messages regarding undefined variables however these are relating to Stripe and so are defined within the site.


![JS stripe_elements.js Validation](media/js_stripe_elements_validation.png)

<br>

### quantity_adjuster_script.html

The only issue present stated one undefined variable, however several lines were highlighted without advising exactly what, the likely culprits are the html id's which is not an issue. 


![JS quantity_adjuster_script.html Validation](media/js_quantity_adjuster_script_validation.png)


<br>

**JSON**

All JSON files located in the fixtures files (under the products and suppliers app) passed validation through [JSON Lint](https://jsonlint.com/). I'm not providing the image proof as this is much simpler syntax then the js files and not really necessary.

1. categories.json
2. products.json
3. suppliers.json


### Python

Pep8 was used to validate code within Gitpod, this can be done by insatlling Pep8 from [here](https://pypi.org/project/pep8/)

I also checked the code with a python formatter called  [Python Checker](https://www.pythonchecker.com). I did notice it would flag many more erros that Pep8 but quite often these were in conflict with each other, for example:


**return HttpResponse(status=200)**:
Python checker would request a space on either side of the '=' sign however python actually throws and error in Github and requires this to be connected.

**@login_required(login_url='/accounts/login/')**
**def addToBasketView(request, pk)**:
Python Checker would require a double space inbetween these lines however as this login required line solely related to this view and only this it is best practice to keep them together. 

Almost all files passed validation - there are notes the explain why this is the case in the relevant app.


**Basket**

1. apps.py
2. contexts.py
3. urls.py
4. views.py


**Checkout**

Line 38 of checkout models does not validate due to an integer issue, however this is necessary for the code to work so I did not make amendments to this. It also is too long however I also could not break this up without affecting the functionality.

1. admin.py
2. apps.py
3. forms.py
4. models.py
5. urls.py
6. views.py
7. signals.py
8. innit.py

**Contact**

1. admin.py
2. apps.py
3. forms.py
4. models.py
5. urls.py
6. views.py


**Home**

1. apps.py
2. forms.py
3. models.py
4. urls.py
5. views.py


**House of Tea**

DATABASE_URL can be shortened, currently it explicetely states the database url. Unfortunately there were issues with accessing my Heroku account for some time now so the site needed to be honsted on render directly. At the time of writing I could not correct without breaking the sites database.

AUTH_PASSWORD_VALIDATORS are too long for validation however these lines cannot be split any further without breaking the site.

1. asgi.py
2. settings.py
3. urls.py
4. wsgi.py


**Newsletter**

1. admin.py
2. apps.py
3. forms.py
4. models.py
5. urls.py
6. views.py


**Products**

1. admin.py
2. apps.py
3. models.py
4. urls.py
5. views.py


**Suppliers**

1. admin.py
2. apps.py
3. models.py
4. urls.py
5. views.py


**customer_storages.py**


**manage.py**


## Manual Testing


Aim: Test responsivness of site on multiple screen sizes.

Method: Changing the screen size by opening the inspection tool and loading page on a mobile device.


<br>

**Home page**

Outcome: On a large size screen the product page images are spaced out evenly. On most mobile sizes this was also the case as they cascade down the page, however on the Galaxy Fold and Samsung Galaxy S6 there was some overlap to the side of the screen. This same issue occured with a medium to large size screen such as the Nest Hub. The images sizes were changed to rem instead of px which corrected the problem.


The navbar successfully changes state from a standard web layout to mobile drop down without any issues.

Result: Success

<br>

**Products Page**

Outcome: There is no overlap with the product cards, however on some varying sizes of screens there is a lot of whitespace to the side. This is not critical but work could be done to imrpove it.

Problem Devices:
* iPhone XR
* Pixel 5
* Surface Duo

Result: Success but more efforts could be made to improve the amount of whitespace.

<br>

**Product Info Page**

Outcome: On almost all devices the image scales well alongside the text, alowing the user to easily read about the product whilst having easy access to the add to basket functionality. Only the Galaxy Fold really stood out as the image was very squashed to the side, whilst the long stream of text meant users had to scroll to access the functionality. This seems more of an edge case and could be improved by implimenting scrolling text or moving the image position.

Problem Devices:
* Galaxy Fold

Result: Success

<br>

**Suppliers Page**

Outcome: The suppliers page only displays in a cascading fashion so for mobile and desktop devices alike the view remains the same.

Result: Success

<br>

**Contact Page**

Outcome: The contact page is a centered form so does not change between screen sizes.

Result: Success

<br>

**Basket Page**

Outcome: The images scale well on all sizes, on very small devices under 520 pixels wide the layout of the table means users have to scroll across to use some of the functionality. Whislt there is no overlapping, forcing the user to scroll is not good user experience, this would require a fundimental restucturing of the layout.

Problem Devices:
* Galaxy Fold
* Pixel 5
* iPhone SE]
* Samsung Galaxy S8
* Samsung Galaxy S20 Ultra

Result: Partial success, improvements to UX could be made.

<br>

**Checkout Page**

Outcome: On all screen sizes the form fits the screen without overlapping.

Result: Success

<br>

**Checkout Success Page**

Outcome: On smaller devices the order number takes up more space than the screen will allow so a horizontal scroll was added to alleviate the issue.

Result: Success

<br>

**Register Page**

Outcome: The register page is a centered form so does not change between screen sizes.

Result: Success

<br>

**Login Page**

Outcome: The login page is a centered form so does not change between screen sizes.

Result: Success

<br>

**Logout Page**

Outcome: The logout page is a centered form so does not change between screen sizes.

Result: Success

<br>

**Account / email Page**

Outcome: On all but the very smallest devices the form displays well, some of the button positioning could be improved. A margin was added to each button to prevent users from accidentaly clicking incorrectly. On the Galaxy Fold white space can be seen to the side as if the content is slightly too large, it is hard to tell in this instance if it is just the scroll bar without physically having the device to test.

Potential Problem Devices:
* Galaxy Fold

Result: Success

<br>

**Password Page**

Outcome: The email page is a centered form so does not change between screen sizes.

Result: Success

<br>

---

Aim: To confirm all navbar links work on the site as intended.

Test: All links were tested whilst signed in to an account and as an unregistered user.

Outcome: All navigation links worked as expected.

Result: Success

---

Aim: To confirm all image links work on the site as intended.

Test: All links were tested whilst signed in to an account and as an unregistered user.

Outcome: All image navigation links worked as expected.

Result: Success

---

Aim: To confirm all in-page text links work on the site as intended.

Test: Tested in account, basket, checkout, checkout success and newsletter links whilst signed in and out.

Outcome: The links that allow you to purchase items or sign up to the newsletter require the user to login first. Because of this an unregisteres user will never be able to add items to a basket and be shown a physical link to the basket as intended. Users cannot access these pages without a link.

Result: Success

---

Aim: To confirm social footer links work on the site as intended.

Test: Clicked links from each page.

Outcome: Always redirected to the correct page in a seperate tab.

Result: Success

---

Aim: To test that user registration is functional and presents correct information.

Test: Try registration with incorrect information and when logged in.

Outcome: Form does not submit when giving an incomplete email address (with just an @ or @gmail) , this is the correct functionality. Form does not submit on a password that is too common, too similar to name or less than 8 characters. When trying to reach the register site when logged in the user is redirected to the home page.

Result: Success

---

Aim: To test that user login / logout functions work correctly

Test: Attempt to login and logout as intended, then when not already signed-in / signed-out.

Outcome: Login and logout works on every page. User is returned to the home page when trying to sign-in when already signed-in, the same with logging out.

Result: Success

---

Aim: To test if a user that is not logged in can access any features they should not

Test: Attempt to redirect to site locations when not logged in, or use functions such as adding to basket when not signed in

Outcome: When not signed in you can select an item to add to the basket which will direct you to sign in as expected, however when signed in the user is immediately shown an 500 error. They can continue using the site with a logged in account but the item is not saved to the basket. When a user has a checkout success message this cannot be accessed by an unauthorised user as expected.

Result: Partial succes

---

Aim: To test email and password changes update the user information correctly

Test: Try to amend email and check via the admin page if changes have been made. Amend password, check by logging out and then in, 

Outcome: The primary email updates in the database, new password also works correctly.

Result: Success

---

Aim: To test the functionality of adding and removing items to the user's basket in Product page.

Test: Test in product page the add to basket button with varying quantities.

Outcome: The user can add any amount from the product page, any inputs of negative numbers throws an error message and prevents the request from submitting.

Result: Success

---

Aim: To test the functionality of adding and removing items to the user's basket in Product info page

Test: Test in the products info page the quantity selectors increase the amounts and that the amounts are correct in the basket.

Outcome: The functionality in the product info page also acts in the same way when selecting negative numbers, the quantity adjusters work as expected.

Result: Success

---

Aim: To test the functionality of adding and removing items from the basket page

Test: Test in the basket page the quantity selectors increase the amounts and that the amounts are correct when update is clicked. Click the bin button to check it removes all of 1 specific item.

Outcome: Update function works for both positive and negative amounts, negative digits completely removes the item without any consequence to re-adding. The bin also removes items immediately and only on the product selected.

Result: Success

---

Aim: To test if checkout form submits correctly with relevant information

Test: Attempt to submit the checkout form with complete and incomplete data. Check that it has submitted in stripe and that this correlates with the admin panel

Outcome: The user is not able to submit the form without a correct email address or without any of the necessary sections completed. The user is able to give an incorrect number, and is able to use letters to pass this section which should not be the case.

Result: Failure

---

Aim: To test if checkout is easy to manage for the admin with a large amount of orders.

Test: Once a payment has been submitted check the admin panel for incorrect or missing information.

Outcome: The admin can see the order number, name, date of payment, delivery charge, order total and grand total. As mentioned in the previous test the charged amounts often do not show and are not correct so this test fails. When the order is opened you can see all the users information which is successful bar the payment amounts.

Result: Failure

---

Aim: To test if Stripe payments recieves the order correctly

Test: Make a payment and check stripe for the amount.

Outcome: The payment is successful on stripe and gives the correct payment amount including any delivery charges.

Result: Success

---

Aim: To test if the newletter signup form adds and removes users information correctly

Test: Signup to email, the next time the form is used it should instead show an unsubscribe button and when clicked remove the users email from the database.

Outcome: The user is able to sign up to the newsletter with their email address, they can change their primary email address in the account page which does not affect which email is in the newsletter database. This could be improved but the user is able to add and remove email addresses easily, the subscribe / unsubscribe button indicats to the user they are already signed up if their email is in the database.

Result: Success

---

Aim: To test the contact form submits correctly

Test: Check the form cannot be submitted without all fields being valid, then check the form has been submitted to the database.

Outcome: Form cannot be submitted without all fields containing valid information as intended, the form appears in the amin panel.

Result: Success

---

Aim: Confirm 404 page works for unfound page

Test: Try to access an unknown page

Outcome: 404 page was displayed.

Result: Success

---

Aim: Confirm 500 page works for unknown page

Test: Force an error to make the 500 page appear

Outcome: Throughout testing 500 pages have appeared when an error has occured.

Result: Success



## Bugs

### Footer not sticking to bottom of page

### Development Bugs

**Footer Placement**

Issue: The footer would not stick to the bottom of the page when there not enough content for example on the signout page. 

Action: Tried different combinations of position, bootstrap navbar-fixed-bottom and 100vh in body css, however when there was content that required scrolling some items would be obscured. The biggest issue was that product information and functionatility would then be hidden by the footer. A wrapper was placed around the content in conjunction with flex display as suggesterd [here](https://kiranworkspace.com/how-to-stick-footer-to-bottom-of-page/). 

Outcome: The footer now remains at the bottom of the screen regardless of the content on the page as it should.

**Newsletter Signup**

Issue: When signing up the email entered the database however the button does not change state. When clicking the signup button again it does remove the users email from the database. After changing primary emails in the account page this caused some issues. The new primary email deleted correctly on occasion, which is a failure. When reverting back to the original primary email this would now not delete.

Action: Much older commits were confirmed to work through ongoing testing, I tried several older versions of code to deduce the issue. After removing the success page and redirect the function works as intended. This is not ideal but the user has the main functionality working now.


**Media Files**

Issue: When switching the debug feature off any images could not be viewed. 

Action: Initially it was believed this was due to the media and static files being set up incorrectly with S3. As the static files would load correctly it was discovered to be a formatting issue instead. For the images used in the home page these were not in the database, so the url was taken directly from S3. For the remaining images these could be found in the database, the issue was the formatting as {{ product.image.url }}, changing this to {{ product.image_url }} solved the issue.


**Aggregate alias in checkout**

Issue: When proceeding to the checkout the error Complex aggregates require an alias, so the checkout would not submit.

Action: In the save function self.product did not have a price, correcting this to self.product.price solved the error.


### Unfixed Bugs

**Adding an item to the basket when not signed in**

As mentioned in the testing, a user cannot add an item to the basket whenthey are not signed in, they will be redirected to the signin page which is the intended result. The user is signed in but a 500 error is show, the item is also not added to the basket so users must go back to the products page to select it again.

For a better user experience the site should allow the user to sign in and immediately have the item added to the basket, although I am not sure how to tackle this currently.


**Checkout submitting with all information**

There are several issues here. The user is able to give an invalid phone number number, for example letters instead of numbers. Whenever a user is has reached the delivery threshold charged amounts are shown but not correctly, the delivery information is also missing. When a user has not met the threshold no monetary value is shown apart from the bottom of the page. This seems to be an issue with the views and contexts files. 

If this issue were to be resolved then the amounts would likely be incorrect due to the deciaml module not being able to function correctly as shown in the course. When added this would cause a 500 error across the site with the message: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'. As this error was so severe it was left out but is not correct, several attempts were made to prevent this by consulting stack overflow but no suggestions proved to be fruitful.


**Selecting Different Item Weights**

Orignally the tea products were designed with a weight amount, this was planned to be selectable which would also increase the price. Unfortunately when attempting this, items with weights would not show the quantity in the basket page, this would also affect the chackout submission.

The error could be corrected in the checkout app's OrderLineItems model in the save function. This would require an if stetement to determine if the item is a dictionary, iterrate through the values to get each item weight and the corresponding quantity. This would need to be split further however due to the time this took to attemtp to rectify a simpler solution was opted for. Now all tea amounts simply have one weight, compared to other online tea stores this is a missing functionality that would be greatly preferred. This has also led to some redundant code that initially took the weight of an item into concideation. 

In the future this would be a particularly nice function to implement for the user experience.


