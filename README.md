# The Football Report


This website is part of the the Code Institute Full Stack Software Development course. 
It is the fourth project along the learning curve and needed to graduate from the course. The project represents a football newspaper 
site which allows page visitors to read a sample of free articles. I have been inspired to create this website since I write about football myself in my spare time. 
By visiting the website you will be introduced to a landing page with free sample of articels. If a user registers can have full access to the website articles. 
The next level of user experience the user subsription functionality which employs the business and payment logic of the project. 
By subscribing an user can become an author and publish an article with picture. The subscription plan resembles a contribution 
that help the founders of the website to maintain and host the writing platform. The deployed version is available [here](https://the-football-project.herokuapp.com/). 

<h1 align="center">
<a  href="/documnets/desktop_demo.gif"  target="_blank"><img  src="/documents/desktop_demo.gif" width="420" height="240" alt="TFR desktop"/></a>
<a  href="/documnets/mobile_demo.gif"  target="_blank"><img  src="/documents/mobile_demo.gif"  width="140" height="240" alt="TFR mobile"/></a>

</h1>

<hr>

The project is meant for educational usage, although it provides good readings that I personally wrote as part of my hobby.
The payment system module is build with the test version of Stripe and it can be used for testing purposes only. It does not process real payments. 
Tests of the payment can be performed with a card number 4242 4242 4242 4242. Please visit https://stripe.com/docs/testing to find more about the test card details.


## Table of Contents

1. [**Project Goals**](#project-goals)
-  [**User Stories**](#user-stories)
-  [**Design**](#design)
-  [**Wireframes**](#wireframes)

  
2.  [**Features**](#features)
3.  [**Database Schema**](#database)
4.  [**Technologies Used**](#technologies-used)
5.  [**Testing**](#testing)
6.  [**Deployment**](#deployment)
7.  [**Credits**](#credits)
8.  [**Acknowledgements**](#acknowledgements)
9.  [**Disclaimer**](#disclaimer)


# User Experience

## Project Goals

The project purpose is to build a Full Stack webiste to present the complete learning 
outcomes of the course.  The project is submitted for evaluation and entails a pass grade to graduate with 
an universite certified diploma from the Code Institute. The website backend is built with the 
[Django Framework](https://www.youtube.com/watch?v=F5mRW0jo-U4) and 
Python. For the development process the website uses Django's builtin backend SQLite database 

The website represents a football platform for analysis and creative writing 
for authors. Page visitors can read the sample of articles available at the home page. 
To access the full list of articles for free, users have to register which automatically 
creates a profile page. Registered user can extend their experiece by writing 
and publishing their own articles. To publish an article user needs to buy a 
subscription framed as a contribution to keep the website going and 
paying for costs of hosting. The subscription logic uses small amounts to 
support community. To facilitate the e-commerce logic 
I will install Stripe which is payment processing software. 

### Target customers

People who love football as a sport and social event.
People who like to read about football.
People who like writing.
Freelance journalists.


### User Access

This website aims to provide the following:

1. Allow users to visit the page and have access to sampled articles and media without being registered.
2. Non-registered users can view the about page, landing page and pricing page and authnetication pages.
3. Provides users with signup option.
4. After registration users has access to the full webpage content.
5. User have their own profile page with a default picture automatically setup.
6. After log in users are able to pick subscription plan, add it to their shopping cart and submit the payment to become authors and publish their own articles.
7. In the profile page users have access to a shorlist with their own articles and subscripton history
8. After becoming authors, user are provided with option ot update and delete only their own aritcles.

### User Stories

Non-registered users:

1. As a non-logged in user I want to see the landing page media and read the sampled articles in the carousel slider.
2. As a non-logged user I wish to find more about the philosophy behind the website and check what I receive in the pricing plans.
3. As non-logged in user I can either signup or login to the page if I already have an account.

Registered users:

1. Users Have to be able to login and logout from the website
2. After registration users can access own profile page with basic profile info and profile image.
3. After registration can read all the articles published in the reports page.
4. In the articles list user can view the article card with date published, name of the author and image thumbnail.
5. I want articles shown per page to be limited to 3 and rest of the articles list be accessed with a pagination.
6. Each article card in the article list has to provide user with links to view the full article page by clickig either the title or the image.
7. Article detailed page should present with article picture, date published with author info, and the entire text of the article
8. After registration I can choose a subscribtion plan to publish my own articles.
9. After choosing the subscription plan I would like to see the chosen subscription plan in a shooping cart with a option to remove or proceed to checkout page. 
10. If the subscription is removed users can return back to the homepage or to the pricing page.
11. Users can proceed to the checkout page where they should view the subscription plan details.
12. In the checkout page user can submit theire payment details.
13. Users can see double-check the price of the subsription and the amout the credit card will be charged.
14. In the checkout page the user needs to have the button to return to the shopping cart page and adjust it.
15. In the checkout page user can complete the purchase of the subscription plan paying with a valid credit card details 

Subcription Users:

1. After a successfull payment I can view the subscription added to a subscription history column in my profile page
2. After successfull payment users can see the button for publishing articles in their profile page.
3. In the publish article page users can add title, photo and text content to the article.
4. In the publish article users can check their text and add additional content using the rich text editor.
5. If users forget to provide article picture the website provides default picture themed according to the website design.
6. After clicking the publish article button can check and see the article published in the reports page.
7. After publishing the article I can see it also in the list with published articles in my profile page.
8. In the reports page I can access and read both my articles and other user articles.
9.  If I choose to read and article which I authored then I can update and delete the article, but only if I am the author.
10. In the update view of the page I can change the title, picture and text of the article.
11. In the delete view I am asked to confirm the removal or cancel the removal. 



## Design

### Wireframes

Wirefames serve as the blueprints of the website design. Wireframe are added 
thanks to [https://balsamiq.com/](https://balsamiq.com/) tool recommended by 
the Code Institute. The blueprints are in the [documentation](https://github.com/podvistorcheto/football-report/tree/master/documents/wireframes)
folder. Due to limited time available all my blueprints were done on a notebook or just on the go 
and were added after the page was coming through. Some of the page desings were simplified 
in the final design version to utilise space for better user interface on mobile.

### Responsive Design

The website is based on the Bootstrap front-end-framework available at
[getbootstrap.com](https://getbootstrap.com/). 
It is a responsive mobile-first framework that allows to implement key design features and keep them 
responsive on different screen sizes. 
I used Firefox and Chrome as browsers in the development stage and the design 
stacked well eventually after constatly inspecting the devtools. 
The website is responsive on other browsers like Safari, Edge and Opera. 
It stacks well on mobile screens where the navigation bar shrinks to a hamburger dropdown menu.

### Colours

![#757575](https://placehold.it/15/000/000000?text=+) ***#000***<br>
![#a8a9ad](https://placehold.it/15/343a40/000000?text=+) ***#a8a9ad*** <br>
![#fafafa](https://placehold.it/15/f1f1f1/000000?text=+) ***#f1f1f1***  
At the start of the project I used the default pure white background color for the body. 
Later decided to switch to rather very light grey to reduce the lightning of the page and better visual relaxation for the user. 
The styling of the buttons follows the bootstrap4 color convention for danger, success, secondary and info classes.


###  Fonts and Icons

My choice went for the ['Inter'](https://fonts.google.com/specimen/Inter?sidebar.open=true&selection.family=Interstems) ranked first in 
the [Typewolf](https://www.typewolf.com/google-fonts) fonts. 
I presents the page lightly from not heavy for reading.
The icons are from the Font Awesome library [fontawesome.com](https://fontawesome.com/). 
I tried to use as less as icons as possible in the desing because the website 
is focused and meant as writing platform that resembles a newspaper website. 
Using many icons would perceive the design style as more technical than it 
should be for such website types.


## Features

### Implemented Feautures

1. Landing page with image slider and inspirational video message.
2. Login and signup authnetication functionaliy with personlised profile page.
3. CRUD model so user can create, retreive, update and delete their Articles.
4. User with registered profiles can choose a subscription and author articles to get the perks from the CRUD model.
5. Payment system with Stripe.

### Feautures To Implement In the Future

1. A star score rating under each article generated by user votes
2. Social media share buttons for the articles
3. More personalised profile page.

## Database

During the development process the date is stored thanks to the Django builtin SQLite database. In the deployment phase the datebase will be 
imported in Postrgres in Heroku.

### Datebase Schema

Here is my Database pattern. I created this schema thanks to 
this [advisory article](https://www.freecodecamp.org/news/how-to-create-database-schemas-quickly-and-intuitively-with-dbdesigner-2f4adf79a29d/) I used  https://www.dbdesigner.net/ to generate more clear and visual presentation of the datebase logic. 

<a  href="/documnets/db_schema.png"  target="_blank"><img  src="/documents/db_schema.png"  alt="TFR db_schema"/></a>

To explain the database pattern I will simply follow the user logic. First, a profile needs to be created 
in order to add a subscription package to the shooping cart. 
The subscription data model is connected to the package line item with through a Foreign Key as shown with arrows.
Once purchased the package gets attached to the profile through its Foreing Key user. 
Similarly the packaline item get attached to the package via its Foreing Key order. Each order is unique with a number which is 
auto-generated and can be used for additional data modeling if needed.

# Technologies Used

-   [Python](https://www.python.org/) version Python 3.8 is uded to develop the website.

-   [Unsplash API ](https://unsplash.com/) to generate the randomized photo gallery for the home page and the about page. The gallery theme is football.

-   [JQuery](https://jquery.com/) to make the video modal working and other responsive features like the navbar hamburger menu.

-   [CKEditor 5](https://ckeditor.com/ckeditor-5)  The project uses  CKEditor 5 as part of the blog app models.py to make the text field user frienldy.
    
-   [Bootstrap 4](https://getbootstrap.com/)  to enhance website design responsivess on different screens.
    
-   **HTML 5, CSS3 and JavaScript** are used throughout to improve the website frontend and functionality.
    
-   [Google Fonts](https://fonts.google.com/) to style the page text.
    
-   [Django](https://www.djangoproject.com/). The website is build from the  **Django**  framework.

-   [Pillow](https://pypi.org/project/Pillow/) to add image processing capabilities. 

-   [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) that controls the rendering behaviour of the forms accros the entire website.

-   [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) package for handling login, registration. Which can be extended to social account authentication.
    
-   [SQLite](https://www.sqlite.org/)  comes as built in feature in the Django Framework. It is used during the development phase.
    
-   [Postgres](https://www.postgresql.org/).  The project utilizes Postgres relational database to store database for the production phase in Heroku.
    
-   [StackEdit](https://stackedit.io/) used for writing the readme file.
    
-   [Stripe](https://www.stripe.com/)  facilitates the payments direclty from the page.

-   [GitHub](https://github.com/) is used for version control. It is the source code remote repository for the project.

-   [Heroku](https://www.heroku.com) is used to host the project and make it available online with an original url.

-   [Amazon Web Services](https://aws.amazon.com/education/awseducate/) host the website using the S3 bucket feature.

## Testing

Please visit the file [TESTING.md](https://github.com/podvistorcheto/football-report/blob/master/TESTING.md)
in the documentation.

## Deployment

### Local Depoloyment  


This project was programmed in the Gitpod integratred development environment (IDE).
It was deployed locally using Github repository. All versions throughout the programming phase were managed via the Github repository 
after each stage was completed. 

The website is developed in Python version 3.8.6. If you want to clone this repository please make sure you have installed [Python](https://www.python.org/downloads/). 
To clone the repository please take these steps in your IDE: 

1. Clone
~~~
    git clone https://github.com/podvistorcheto/football-report.git
~~~

For troubleshooting and additional reference more details are available in [GitHub Docs](https://docs.github.com/en) for [cloning a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

2. Then you need these installations:
~~~
    pip3 install django
    pip install django-allauth
    pip3 install django-crispy-forms
    pip3 install stripe
    pyhton3 manage.py makemigrations
    python3 manage.py migrate
~~~
3. To fully check the entire list of requirements you can also run:
~~~
    pip3 install -r requirements.txt
~~~
4. At the start make sure you remove the email setup from the ```setting.py``` 
    to send emails in the console, hence set it up to: 
~~~
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
~~~
5. To run the admin panel you have to create a superuser
~~~
    python3 manage.py createsuperuser
~~~
6.  To check the webpage your local machine type in the console:
~~~
    pythnon3 manage.py runserver 
~~~

7. Here is a link to find more details to the documentation on how to integrate [Stripe Payments](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details) in the website

### Heroku deployment

Before start you will need to create [Heroku account](https://signup.heroku.com/) and create new app. 
A detailed explanation is available in [developer.mozilla.org](https://developer.mozilla.org/) what one 
must observe before prepering the website ready to publish  To follow the standard security protocol you must check:

-   `DEBUG`. This should be set as  `False`  in production (`DEBUG = False`). It  prevents the critical security info and debug trace and variable information from being displayed.
-   `SECRET_KEY` - Django recommends to store it in separate environment variable


Under the app settings in Heroku click reveal to check and add the confivigurations variables there: 

SECRET_KEY<br>
STRIPE_PUBLIC_KEY<br>
STRIPE_SECRET_KEY<br>
STRIPE_WH_SECRET 

Required later for the AWS:<br>

USE_AWS `True`<br>
AWS_ACCESS_KEY_ID<br>
AWS_SECRET_ACCESS_KEY

After this you need to provide the heroku app with Postgres database. Heroku works with Postrgress 
which is different from SQLite used in the development. 

 - Then run the following commands in the IDE console:

~~~
    pip3 install dj_database_url
    pip3 install psycopg2-binary
    pip3 freeze > requirements.txt
~~~
- in ```settings.py``` now needs an import:
~~~
    import dj_database_url
~~~
- to connect to the the new database in Heroku need to switch to a new database default in ```settings.py```
~~~
    DATABASES = { 'default' : dj_database_url.parse("type in your heroku database url here")
~~~
- then you need do make the migrations to the new database
~~~
    pyhton3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
~~~
Creating new superuser is required as the Django database is not the new Postgress database which has not taken any data from the SQLite database in Django. 
DATABASE_URL is usually available in the settings of the newly created heroky app.
    
~~~
    DATABASES = { 'default' : dj_database_url.parse(os.environ("DATABASE_URL")
~~~
    
 - install gunicorn as a webserver
~~~
    pip3 install gunicorn
~~~ 
- create a Procfile
~~~
   heroku login -i or heroku login
~~~
  - prevent collecting the static file for deployment to Heroku
~~~
heroku config:set DISABLE_COLLECTSTATIC=1 
~~~
- in ```settings.py``` have to add the heroku app website url to ALLOWED_HOSTS
  
Note that in the heroku app - >  Deploy -> needs to connect connect to deploy to heroku via github. Afther this need to initialise a heroku git remote
~~~
    heroku git:remote -a <type in you heroku-app-name>
    git add .
    git commit -m "some commit"
    git push
~~~
- deploy the app with 
~~~ 
    git push heroku master
~~~

#### Sending emails outside the console in the real-world

As advised by the tutors I set up email service after completing the Heroku Deploymet. 
Here is an useful article how to setup [sending emails with Django](https://medium.com/@royprins/sending-emails-with-django-16f1c54529af) and configuring a SMTP backend. Note, do not commit your email and password to version control for security reasons but add their values in the configuration variables in Heroku instead. 

EMAIL_HOST_PASS<br>
EMAIL_HOST_USER

#### AWS Amazon Web Services

AWS is cloud based service which is used to store the media and static files for the project. 
To host the media and static files the project uses the [Amazon Simple Storage](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html), 
better known as the S3  feature. Here are more details how to user [Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html).



## Credits

### Code

The idea about the project is inspired by my freelance hobby for writing about football and pure passion about football. During the development process I followed the Code Institute video tutorials for the 
[Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project develped by [ckz8780 Chris Z](https://github.com/ckz8780).
I have to give credit to these lessons which helped me to develop the payment logic and system for The Football Project. Additionally, I took extra time to learn more 
about how to develop with python and Django thanks to the video tutorials from [Corey Schaffer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g). 

Through the entire process the Code Institute Slack community helped me with many bugs and obstacles I encountered. 
Addintional thanks again to [ckz8780 Chris Z](https://github.com/ckz8780) who help out with his advice in the Code Institute Slack community, 
specifically with the dumbdata base case.


The pagination for the page was developed with the help of [this tutorial article](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) 
in [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/).

As mentioned above the Database Schema was created after reading this [advisory article](https://www.freecodecamp.org/news/how-to-create-database-schemas-quickly-and-intuitively-with-dbdesigner-2f4adf79a29d/) 
at the [freeCodeCamp](https://www.freecodecamp.org/) website.

The idea to add the ckeditor5 аs rich text editor in the text field for publishing articles comes from this interesting video from [Codemy.com](https://www.youtube.com/watch?v=mF5jzSXb1dc&feature=emb_logo).

The initial version of coding the [toast files](https://github.com/podvistorcheto/football-report/tree/master/templates/includes/toasts) was taken from [mdbootstrap.com](https://mdbootstrap.com/docs/jquery/javascript/notifications/). 
I further re-styled and modified them to achieve the customized design that suits my project.

This readme file is created via the [StackEdit](https://stackedit.io/) tool for markdown files.

### Content & Media

- All text content in the articles published for the project is written by me. The text of the first artice 
    'The Italian Paradox' is actually my first article published [here](https://webcafe.bg/football/478321977-italianskiyat-paradoks.html) in Bulgarian some years ago with a translation and some statistics updates added again by me. 
    I also used the pictures from this same article to use them though the different articles.

- I used [imgur.com](https://i.imgur.com/xjXTE9Z.jpg) for the picture under the overlay background. 

- For the carousel [slider one](https://unsplash.com/photos/eVbwuIvaR5g) and [slide three](https://unsplash.com/photos/qawemGipVPk) I used [Unsplash](https://source.unsplash.com/). The source for the picture in slider two comes this [article](https://thesefootballtimes.co/2019/07/09/how-marcelo-bielsa-turned-athletic-club-into-one-of-europes-most-exciting-machines/).

- The gallery in the home page and the changing picture in the about page are taken and randomized from the simplified source again from [Unsplash](https://source.unsplash.com/).

- [Default picture for the user profile](https://www.siciliaogginotizie.it/2020/01/21/e-partito-con-successo-il-progetto-safe/). 
- [The article detail page default picture](https://www.saltwire.com/sports/local-soccer-players-training-in-bc-192267/).
- Picture from [One night at Anfield](https://www.google.com/imgres?imgurl=https://images.daznservices.com/di/library/GOAL/3f/88/marcos-llorente-liverpool-atletico-madrid-uefa-champions-league_7pzxyjmlina41bgiz6ehzywrt.jpg?t%3D-794606592%26quality%3D100&imgrefurl=https://www.goal.com/de/meldungen/video-highlights-champions-league-liverpool-atletico-madrid/1xpi02zq0r8l21a9m9yikmc6zm&tbnid=w8qyHSyLtU_pEM&vet=1&docid=0Lb3EcDTiexvmM&w=1920&h=1081&source=sh/x/im).
- [Guardiola vs. Mourinho. The rivalry continues](https://www.planetfootball.com/quick-reads/jose-mourinho-and-pep-guardiolas-war-of-words-through-the-years/).
- For the video modal I used a link from the [Tifo Football Channel](https://www.youtube.com/c/TifoFootball/search?query=atalanta). Here is a direct [link](https://www.youtube.com/watch?v=M0fijoZOYbY) to the video itself.

## Acknowledgements

I want to express my gratitude to Igor, Tim, Cormac, Michael, Johan, Samantha, Scott and all the tutors of Code Institute for help and guidance while debugging my code.
Thanks to their support I convincingly added value to my programming skills.

I am also thankful to my mentor Rahul and the folks from the Code Institute Slack community for the guidance and advise provided.

In addition, I would like to thank to Code Institute Student Care for the constant support from day one. 

## Disclaimer

This webisite is developed for educational usage only. The website does not process real payments.