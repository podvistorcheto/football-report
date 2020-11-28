 ## Testing


### Automated Testing

The entire development process had time contstraints to meet deadlines. Hence, 
I tested manually every new piece of code thourougly while developing. 
Near the submission version I did some automated unit tests and then a 
performance test report with the lighthouse feature in devtools for Chrome.

#### Unit Test

| App Tested    | Test Info     | File Location | 
| ------------- | ------------- | --------------| 
| blog  | Testing the homepage view | blog/test_views.py  |
| blog |  Testing showing the articles list  | blog/test_views.py  |
| blog  | Testing click and view single article from the article list | blog/test_views.py  |
| blog  | Testing the update functuanalities  | blog/test_views.py  |
| blog  | Testing create new article functuanality  | blog/test_views.py  |
| blog  | Testing delete existing article functuanality  | blog/test_views.py|
| cart    | Test the login required to load the cart view template| cart/test_views.py |
| cart    | Tests if the cart renders correctly after login | cart/test_views.py |
| checkout    | Tests if the form is validated correctly after correct user input | checkout/test_forms.py |
| checkout    | Tests if the form gives error feedback in case the user input is incorrect | checkout/test_forms.py  |
| profiles    | Tests if the signup page loads | profiles/test_views.py |
| profiles    | Tests if the login page loads | profiles/test_views.py |
| profiles    | Tests if the logout responds correctly | profiles/test_views.py |


Chome DevTools Test

I user the lighthouse test to check for the performance, best practices and search enging optimisatition (SEO).
The first report generated form the lighthouse tool showed some average results. 
On each circle indicator this tool takes you to the several points that may be causing the reduced results. 
Here is the first test tesults:

<a  href="/documents/lighthouse1.PNG"  target="_blank"><img  src="/documents/lighthouse1.PNG" alt="lighthouse1"/></a>

Looking into the error I adjusted the width and height of the image in the info section of home.html. 
The second step was to remove redundant JavaScript code. After this I added missing aria-labels
for all ```<button>``` tags. After this ended up with results which are bit better.

<a  href="/documents/lighthouse2.PNG"  target="_blank"><img  src="/documents/lighthouse2.PNG"  alt="lighthouse2"/></a>

While taking into the account the score in the performance indicator I didn't plan to proceed with refactoring further because
the advice under the lighthouse tool for performance indicated to remove the JQuery and some Stripe JavaScript code which is risky.
I did took into account that the landing page has some images and media files which may cause the lower results while loading. The results
in the performance component may vary as sometime scores above 70. 

### Manual Testing

This manual testing phase is comprised by manually checking consistency between project goals 
and the user stories. It also helped detecting bugs and find workarounds. While testing the user stories I tried to stick to 
the [kanban](https://en.wikipedia.org/wiki/Kanban_(development)) method to prioritise and not get stucked on one of the stories, thus saving time and 
limit bottlenecks. 

#### Not logged-in users

| User Story Tested | Expected   | Pass    |
| ----------------- | -------- | --------- |
| User can access the landing page | Landing page loads correctly with slider, video modal, gallery access. Navbar shrinks responsively  | Yes |
| Not logged-in user can access the sample articles from the slider | All users can access the free sampled articles from the carousel slider | Yes |
| Not logged-in can't access the reports page  | The page is restricted correctly and non-logged user can't access the sample articles and is prompt to login | Yes |
| User can access the about page without being logged in | Page displays without error consistently on mobile(picture hidden) and desktop  | Yes |
| User cannnot access the articles list without being logged in | When not logged in the user is prompt to login for access the full list of articles. Page displays without error and consistently on mobile and desktop  |  Yes|
| User can view the pricing page | The page loads with three price categories and if not logged in user clicks on add to cart leades to login page| Yes |
| User can access the login and signup | The login and signup pages load with no errors | Yes |
| Signup Page | The sing up page functions correctly and sends a link to the verification email to listed email. Email is send successfully| Yes |
| Login Page| User can login successfully with valid username and password and the page shows a toast message which greenlights the successful login. | Yes |
| Sending Emails| User can request a password reset and emails is sent successfully | Yes |


#### Logged In User

|  User Story Tested | Expected | Pass |
|--|--|--|
| User can access the reports page when logged in | Reports page loads correctly the pagination is active and displays three articles per page both on mobile and desktop  | Yes |
| Article List Page |  Each article card dispays responsively with thumbnail picture, date and author of the article plus title of the report | Yes
| Access to Article Detailed Page | User can either click on the image or the article title and redirect to the article detail page | Yes |
| Article Detail Page | User can view the full article picture, date published with author name plus thumbnal picture, and the entire text of the article |Yes|
| User can access the pricing page | Pricing page loads without error and user can click on get it to proceed to checkout page |  Yes|
| Cart page | User can see the summary of the chosen subscription with option to proceed to checkout and remove option available too | Yes | 
| Remove the Subscription from the cart | Partner can successfully remove the description before proceeding to checkout with button to return to pricing | Yes |
| Checkout Page | The checkout page loads without errors with two colums. In the left column is payment form details. In the right column the subscription summary | Yes |
| Checkout Page Purchase | User can fill out the the form to submit the payment with all fields are required. | Yes |  
| Charges Checkout Page | Before submitting the paymennt user can read the price at three places in the checkout page. It dispays an alert text how much the credit card will be charged right next to the complete purchase button. User can return back and adjust the card too. | Yes |
| Checkout Success Page | After successfull payment the user is redirected to a Payment successfull page with summary of the purchase and the unique ID of the subscription. Confirmation email sent.| Yes |



| Subcribed User Story |  Result| Ready |
|--|--|--|
| Profile Page | If there is payment confirmation users can view their subscription in the order history | Yes |
| Profile Page Details | If payment is successfull users have access to an active button to publish article located in the profile page | Yes |
| Publish Article Page | Page load successfully and users can upload article with a title, picture, text content with using the text editor.| Yes 
| Article List | User can see the articles list with own published articles in the left column of the article page | Yes |
| Update and Delete Page | User who authored the article can update the article or remove it. The option is restricted to the authors of the article only | Yes |
| Article Delete Confirmation | If user goes for the delete option there is confirmation page with confirm and cancel option. If confirms the user is redirected to the home page. Clicking the cancel button returns the user to the article view page. | Yes |
| Logout Page | User can logout after confirming the sign out intention. If confirmed, the log out is successful and redirects to the home page | Yes |


### Testing the payment system

#### Webhook Method

The standard testing module is provided in the Stripe. A payment is successfully tested with the test credit details 4242 4242 4242 4242. 
An common scenario in submitting test_forms is error related to the internet connectivity disruption, accidentally closing the browser and other problems that may occur which might cause the form to crash. 
It a real world website may result in a processed payment but no order confirmation. Such events can be handled with method called 'webhook'. 
In short a webhook is aimed to adjust the way an web programme reacts to a specific event by adding tailored callback or a method that is called after 
previously executed function. This callback method monitors the data flow of the first function.  Thanks to the video tutorial for the Boutique Ado 
e-commerce website the Code Institute the risk of events might be mitigated via the code from ```webhook_handler.py```:

#### Test:

If comment out the form.submit(): functionality in the stripe.elements.js it means that the form does not submit. Such an event triggers the code in the ```webhook_handler.py``` to look for the order in the database. 
In case the order is not there the it creates the order. 

#### Result:

Passed and successfully saves the order in such event. In addition even before commenting out the form.subit(); I experienced some internet outage after which the the payment and the order were saved successfully.



### Bugs & Workarounds


After the first end-to-end testing phase I identified several issues:

1. User cannot access the samplae articles from the slider page.
    Fix: added small piece of url code simply to specify the argument after the url. 
    ~~~
    <a href="{% url 'article_detail' 41 %}" class="btn btn-info btn-lg">Read Now</a>
    ~~~
    After trying many much more complicated arguments a tutor from Code Institute 
    named Scott deserves credit for pointing me in the right direction to provide the
    correct arguement for the article detail.

2. Non-logged users can access the reports page - fixed in the testing phase 
    with simple loop which restricts to login page in if user did not pass authnetication
    ~~~
    {% if user.is_authenticated %}
            <li class="nav-item">
                <a href="{% url 'article_list' %}" class="nav-link">Reports</a>
            </li>
    {% else %}
            <li class="nav-item">
                <a href="{% url 'account_login' %}" class="nav-link">Reports</a>
            </li>
    {% endif %}
    ~~~
    
3. Mobile view lacks responsivess for the home page. The titles and read links of the sample article do not materialize. 
    Fix:  added some media queries in the base.css file:
    ~~~
    @media only screen and (max-width: 600px) {
    .display-3 {
        font-size: 36px;
    }
    }

    @media only screen and (max-width: 600px) {
    .mobile {
        display: none;
    }
    }

    @media only screen and (max-width: 600px) {
    #gallery {
        display: none;
    }
    }
    ~~~

4. Emails are sent successfully but only in the console not sent outside Django. Near the deployment phase I tried to add the functionality
    to send emails outside the console using gmail. After adding this feature I encountered an error which first prevented a user from receving 
    positive outcome to complete the signup. The signup crashed and age loaded with 405 error. Though the new user actually was added in the admin panel, 
    the Gitpod console showed this 101 error message.

    <a  href="/documents/gmailbug.png"  target="_blank"><img  src="/documents/gmailbug.png"  alt="error_one"/></a>
    
    When discussed with the tutors from Code Institute it seemed that the gmail blocks emails sent from the Gitpod environment and was advised 
    to look into after deployment to Heroku.
    
4. Picture artice doesnot sync well with desktop screen unless is 1100pxx700px. To workaround this I changed the design of the article page and made it more 
    simple which made the picture to display on all devices. Furthermore, I added a message that recommends the size of the picture upload. 
    It is common practice for professional websites from the industry. For example LinkedIn recommends picture sizes for the user profile page. 
    In the publish article_form I inform the users about the default article photo feature which allows the author to publish 
    the text with the default website picture. Authors may return later to update the picture with proper sizing.

5. Update and delete buttons were shown on every article detail view no matter wheter the user is the author or not. Though the functionality is blocked 
    for non-authors it confuses users. Hence I added additional ```if``` statement in the article_detail.html to restict the CRUD form to authors only:

    ~~~
    {% if article.author == user.profile %}
        <form method="post">
            <div class="form-group">
            {% csrf_token %}
                <a class="btn btn-secondary btn-sm mt-1 mb-1"
                    href="{% url 'article_update' object.id %}">Update</a>
                <a class="btn btn-danger btn-sm mt-1 mb-1"
                    href="{% url 'article_confirm_delete' object.id %}">Delete</a>
            </div>
        </form>
    {% endif %}
    ~~~

### Code Validators

#### HTML

The entire html code was tested with W3C Markup Validation Service. I used the weblinks to test each page as the validator has difficulties with the 
jinja syntax used in the django templates. In home.html I removed frameborder="0" and the attribut type="text/javascript" from the javascript tag. 
This validation helped me notice in the base.html my footer tag was outside the body which is not good practice.
No other serious issues were found.

#### CSS 

Except for the warnings in the validation, no error found in the css code.

<a  href="/documents/csscheck.png"  target="_blank"><img  src="/documents/csscheck.png" height="80" alt="csscheck"/></a>

#### JavaScript

All pieces of javascript code were validate with Esprima and code is syntactically valid.

#### Python

When checking the code with PEP8 online mostly there were minor issues missing or unecessary whitespaces and no new lines at the end of files. 
I did made the code to stick to best practices as much as possible.

#### Note: Test Some Database issues before 

While taking the next steps for deployement I had to dump the data since I was not using fixtures. After advice from the tutors, Slack ahis this article 
for [Django dumpdata and loaddata](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) and run this command to dump the SQLite data in json file. 
Hence should run:
~~~
python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
~~~
which dumps the db.sqlite3 to a db.json file and then commit and push to heroku and run:
~~~
python3 manage.py loaddata db.json
~~~
It didn't work, probably beaucause I created new superuser for the heroku postgres 
which contradicted with the previous primary keys and got this error in the console 

<a  href="/documents/dbjson.PNG"  target="_blank"><img  src="/documents/dbjson.PNG" height="100" alt="dbjson"/></a>

One of the tutors suggested to dumpdata per each app separately and exclude the profile app to workaround this bug. 
I decided that it may lead to new obstacles and more time consuming. Therefore I manually created the database once again. 
I would suggest to watch out for this as it may take a lot of time and might lead to irreversibly lost data. 
