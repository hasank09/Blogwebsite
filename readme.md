# Personal Blog Website

can be used with local network or deploy on any cloud platform
### Main feature

1.  userid --> '1' in database is the admin with full right <br>
2. rest user are the general user just can post commit on your blog post
3. database are kind of RDM with the help SQL
4. content are shown as per user rights
5. comment are recorded with author detials 

##### default credential 

admin --> user: admin@flask.python.com , pass = python123456
general --> user: user1@flask.python.com , pass = user123456

Password are hashed : `pbkdf2:sha256` and salted <br>
inputs are validated 'email' & etc

you may change default blog post and user details doing following steps:

1. open `blog.db` file in any db browser, I used [this](https://sqlitebrowser.org/)
2. db has three table `blog_post`, `comments` and `users` all are in relationship <u>don't any delete table or `blog_db`</u> <br>. Delete entries starts from `comments` then `blog_post` after that you may delete the user 
3. Now run server and get register with first user which will be admin

perform step-1 
![db1.png](blog_image%2Fdb1.png)

perform step-2 & 3
![db2.png](blog_image%2Fdb2.png)

##### Blog Home Page - without no post shown

![homepage.png](blog_image%2Fhomepage.png)

##### After Login page post are visible 
![login.png](blog_image%2Flogin.png)


##### click on any post

![post-1.png](blog_image%2Fpost-1.png)
