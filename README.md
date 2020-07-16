## Test task: Python Developer 
#### Simple REST API with Django Rest Framework
 #####Implement:
  - used Django Rest Framework
  - JWT token authentication
  - swagger documentations
  - testing models, auth, views, urls
  
#####Models:
1. SimpleUser inheritance AbstractUser
2. Post
3. Like

#### Urls:
1. user signup ```/auth/users/```
2. user login (get JWT token) ```/api/token/```
3. show all posts ```api/post/```
3. post creation ```api/post/create/```
3. post updating ```api/post/<post_slug>/update/```
3. post deleting ```api/post/<post_slug>/delete/```
4. post like ```api/post/<post_slug>/like/```
5. post unlike ```api/post/<post_slug>/unlike/```
6. analytics about how many likes was made for one day ```api/post/date_<YYYY-MM-DD>/```
6. like analytics for range of days ```api/post/date-from_<YYYY-MM-DD>-date-to_<YYYY-MM-DD>/```
7. user activity show when user was login last time and when he made a last request ```user/```



### Running project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
 or 
 ```
 env\Scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

