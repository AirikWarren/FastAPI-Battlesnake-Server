# FastAPI-Battlesnake-Server
An implementation of the *Battlesnake* API using the *FastAPI framework*.

---
# Quickstart 

1. [Initialize a virtual environment](https://docs.python.org/3/library/venv.html) and activate it.
2. Upgrade your pip to the latest version (21.0.1 at the time of writing).
3. Install the dependencies defined in [requirements.txt](https://github.com/AirikWarren/FastAPI-Battlesnake-Server/blob/main/requirements.txt) .
4. Run ```run_dev_server.py``` 
5. Open up web browser of your choice and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) (alternatively you can view those same docs on the server that hosts the [Example Heroku Deployment)](https://battlesnake-fast-api.herokuapp.com/docs).
6. Channel your inner snake charmer and start writing some algorithms!

---
# Deployment to Heroku 

A sane and reasonable default Heroku configuration can be found on the [heroku-deployment](https://github.com/AirikWarren/FastAPI-Battlesnake-Server/tree/heroku-deployment) branch of this repository, of particular note are the ```Procfile``` and ```battlesnake-info.json``` files located in the top level of the branch's directory, which you may use as jumping off points for your own Heroku Battlesnake server.


**Note: *The following pre-requisite knowledge is assumed and beyond the scope of this tutorial* **

- ability to use Git to create repositories and clone other repositories or [refer](https://guides.github.com/activities/hello-world/)
- ability to create and/or posession of a pre-existing Heroku account or [refer](https://docs.railsbridge.org/installfest/create_a_heroku_account)
- ability to create and/or possession of a pre-existing Battlesnakes account or [refer](https://play.battlesnake.com/)


1) fork / clone this repository into a repository of your own. 
2) study and/or copy paste the aforementioned ```Procfile``` and ```battlesnake-info.json``` files into your cloned / forked repo.
3) edit ```battlesnake-info.json``` so that the information it contains accurately reflects you / your snake. Refer to [this page](https://docs.battlesnake.com/references/api#the-battlesnake-api) in the official documentation if you need additional clarity.
4) Navigate to your [Heroku Application Dashboard](https://dashboard.heroku.com/apps) and click on the button towards the top-right of your screen labeled ```New```.
5) Select ```Create New App``` and follow the on-screen dialog to name your Heroku application, (keeping in mind that this name will be used as part of the URL to access your web server!) submit when finished.
6) Locate the ```Deployment``` sub-section on the following page and select ```Github```.
7) Use the search bar in the section located just below that (labeled ```Connect To Github```) and search for the repository that you created earlier.
8) Use the ```Open App``` button near the top right section of the screen to be taken to the root directory of your web server (which should just be the ```battlesnake-info.json``` file you edited earlier. You can also check out your very own copy of the documentation at ```{your-app-name}.herokuapp.com/docs``` while you're there.
9) Almost done! Move over to the [Getting Started](https://docs.battlesnake.com/guides/getting-started) guide on the official Battlesnake docs and complete steps 3 (Register Your Battlesnake) and 4 (Create Your First Game). 
10) train your 🐍 
