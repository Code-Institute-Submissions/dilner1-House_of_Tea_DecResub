# Testing

## Lighthouse

Both the Mobile and Desktop scores here were very high as expected however the performance was noticably under performing. The slow performace is likely down to the images used, this could be improved with better compression on these files.

### Desktop Lighthouse Score

![Desktop Lighthouse Score](media/lighthouse_desktop.png)


### Mobile Lighthouse Score

![Desktop Lighthouse Score](media/lighthouse_mobile.png)


## validation

### CSS
Jigsaw W3 was used to validate the CSS files
https://jigsaw.w3.org/css-validator/

![CSS Validation](media/css_validation.png)

### HTML
W3 was used to validate the HTML files
https://validator.w3.org/


#### Home Page
![HTML index Validation](media/html_index_validation.png)


#### Home Page
![HTML index Validation](media/html_index_validation.png)


#### Products Page
![HTML index Validation](media/html_products_validation.png)


#### Product info Page
![HTML index Validation](media/html_products_info_validation.png)


#### Basket Page
![HTML index Validation](media/html_basket_validation.png)


#### Checkout Page
![HTML index Validation](media/html_checkout_validation.png)


#### Checkout Success Page
![HTML index Validation](media/html_checkout_success_validation .png)


#### Suppliers Page
![HTML index Validation](media/html_suppliers_validation.png)


#### Contact Page
![HTML index Validation](media/html_contact_validation.png)


#### Newsletter Page

Unfortunately when validating the site link a 500 error was returned, I could not see why this would be the case so for now have just validated via direct input

![HTML index Validation](media/html_newsletter_validation.png)


#### Login Page
![HTML index Validation](media/html_login_validation.png)


#### Logout Page
![HTML index Validation](media/html_logout_validation.png)


#### Signup Page
![HTML index Validation](media/html_logout_validation.png)


#### Email Page
![HTML index Validation](media/html_email_validation.png)


#### Password Page
![HTML index Validation](media/html_password_validation.png)



### Javascript

JSHint was used to validate the Javascript files / scripts
https://jshint.com/

The files tested were:
1. basket.html script
2. stripe_elements.js
3. quantity_adjuster_script.html  

![JS basket.html Validation](media/html_password_validation.png)

### basket.html js

Four warnings
16	Expected an assignment or function call and instead saw an expression.
23	'template literal syntax' is only available in ES6 (use 'esversion: 6').
32	Unclosed regular expression.
32	Unrecoverable syntax error. (100% scanned).

![JS basket.html Validation](media/js_basket_validation.png)


### stripe_elements.js

The only warning was a template literal which is not an issue for functioning JS code as this has been written in ES6 specifically.


Two warnings
26	'template literal syntax' is only available in ES6 (use 'esversion: 6').
51	'template literal syntax' is only available in ES6 (use 'esversion: 6').


The only messages regarding undefined variables however these are relating to Stripe and so are defined within the site.

![JS stripe_elements.js Validation](media/js_stripe_elements_validation.png)


### quantity_adjuster_script.html

Only issue present stated one undefined variable, however several lines were highlighted without advising exactly what, the likely culprits are the html id's which is not an issue. 


![JS quantity_adjuster_script.html Validation](media/js_quantity_adjuster_script_validation.png)


Python
https://extendsclass.com/python-tester.html

contexts.py