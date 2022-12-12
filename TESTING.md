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

DATABASE_URL can be shortened, currently it explicetely states the database url.

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


Aim: Test responsivness of site on multiple screen sizes

<br>

**Home page**

Test:

Outcome:

<br>

**Products Page**

Test:

Outcome:

<br>

**Product Info Page**

Test:

Outcome:

<br>

**Suppliers Page**

Test:

Outcome:

<br>

**Contact Page**

Test:

Outcome:

<br>

**Account Page**

Test:

Outcome:

<br>

**Basket Page**

Test:

Outcome:

<br>

**Checkout Page**

Test:

Outcome:

<br>

**Checkout Success Page**

Test:

Outcome:

<br>

**Register Page**

Test:

Outcome:

<br>

**Login Page**

Test:

Outcome:

<br>

**Logout Page**

Test:

Outcome:

<br>

**Email Page**

Test:

Outcome:

<br>

**Password Page**

Test:

Outcome:

<br>

---

Aim: To confirm all navbar links work on the site as intended

Test: 

Outcome:

---

Aim: To confirm all image links work on the site as intended

Test: 

Outcome:

---

Aim: To confirm all in-page text links work on the site as intended

Test: 

Outcome:

---

Aim: To confirm social footer links work on the site as intended

Test: 

Outcome:

---

Aim: To test that user registration is functional and presents correct information

Test: 

Outcome:

---

Aim: To test that user login / logout functions work correctly

Test: 

Outcome:

---

Aim: To test if a user that is not logged in can access any features they should not

Test: 

Outcome:

---

Aim: To test email and password changes update the user information correctly

Test: 

Outcome:

---

Aim: To test the functionality of adding and removing items to the user's basket in Product page

Test: 

Outcome:

---

Aim: To test the functionality of adding and removing items to the user's basket in Product info page

Test: 

Outcome:

---

Aim: To test the functionality of adding and removing items from the basket page

Test: 

Outcome:

---

Aim: To test if checkout form submits correctly with relevant information

Test: 

Outcome:

---

Aim: To test if checkout is easy to manage for the admin with a large amount of orders

Test: 

Outcome:

---

Aim: To test if Stripe payments recieves the order correctly

Test: 

Outcome:

---

Aim: To test if the newletter signup form adds and removes users information correctly

Test: 

Outcome:

---

Aim: To test the contact form submits correctly

Test: 

Outcome:

---

Aim: Confirm 404 page works for unfound page

Test: 

Outcome:

---

Aim: Confirm 500 page works for unknown page

Test: 

Outcome:



## Bugs

### Footer not sticking to bottom of page

Issue: The footer would not stick to the bottom of the page when there not enough content for example on the signout page. 

Action: Tried different combinations of position, bootstrap navbar-fixed-bottom and 100vh in body css, however when there was content that required scrolling some items would be obscured. The biggest issue was that product information and functionatility would then be hidden by the footer. A wrapper was placed around the content in conjunction with flex display as suggesterd [here](https://kiranworkspace.com/how-to-stick-footer-to-bottom-of-page/). 

Outcome: The footer now remains at the bottom of the screen regardless of the content on the page as it should.

### Development Bugs

**Aggregate alias in checkout**


**Decimal Issue**



### Unfixed Bugs

**Media Files**

**Selecting Item Weights**