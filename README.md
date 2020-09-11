# How to install 

###### If you don't have python on your system :

If you don't already have python 3.8 installed, go to https://www.python.org/downloads/
and install it.

###### If you don't have pip on your system :

https://pip.pypa.io/en/stable/installing/

###### If you don't have git on your system :

https://github.com/git-guides/install-git


### Install and create a virtual environment :

Go to the folder where you want to install the game, open a terminal, and install virtualenv using pip :
```
pip install virtualenv
```

then, create a virtual environment : 

```
virtualenv Space_inv
```

then activate the virtual environment :

```
Space_inv/Scripts/activate
```

### Download the Game and install the requirements on the virtual env :

With git on your system, type :

```
git clone https://github.com/Alexmdg/Space_Invaders.git
```

then go in the downloded folder : 

```
cd Space_Invaders
```

and install the requirements :

```
pip install -r "requirements.txt"
```

then, to launch the game :

```
python main.py
```

(Each time you wanna launch the game, don't forget to activate the virtual environment if you've left it)


then, gl hf :)





