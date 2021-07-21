# Lab 6: Build Your Own Monsters

## Intro
The training wheels are starting to come off this week. You will be directly working with our game engine to set up the game and create your own monster types!

Knowing about classes and objects unlocks a whole wide world of how a lot of programming gets done. Now you can be exposed to how we create the Game object and set up attributes to format the running of the game program. Also, you'll be creating your own monster classes and instantiating them into the Game world!

We will get you through the first steps of starting off the game and building your own monsters. However, you will start to have a lot more autonomy on how to tackle the later steps of the lab. Have fun with it, and please don't hesitate to reach out if you need help.


## Set Up
* Click the green 'Code' button on the top right of this section.
* Find 'Download ZIP' option and click it
* Unzip the file and move it over to your 'workspace' folder (or wherever you keep your files)

* Find the folder and open the entire folder in VSCode
    * You can find it in your Files and right click on it. Use the "Open with VSCode" option
    * You can also open VSCode, go to 'File' > 'Open' and then find the lab folder

* With VSCode open, go to the top of your window and find `Terminal`
* Click `Terminal`
* Click `New Terminal`


## Game Explanation
This is a base version of tower defense with 2 tower types. The objective is to take down the monsters before they reach the destination flag.

If a monster reaches your flag, then you will lose a life. Lose all your lives, and you lose the game.

We have 2 magic towers:
* Lightning
    * Cooldown: 2 seconds
    * Attack Radius: 300 pixels
    * Attack Damage: 20
* Rock
    * Cooldown: 5 seconds
    * Attack Radius: 200 pixels
    * Attack Damage: 100

You will be creating your own monsters for your towers to face off against.

## Lab Steps
* All the code you will need to edit is in `lab.py`
* You will also need to edit `run.py` to set up the game.
* Everything inside the `engine/` folder are the inner workings of the game. Feel free to take a look, but you won't need to change anything

### Set up the Game object
Let's start off looking inside of 'run.py'. Notice how we mostly have an empty file. This week, we are trusting you to understand how creating the Game object works and writing the code yourself.

* Before we get started, we need to figure out what arguments our Game object needs to be instantiated
* Take a look inside `engine/game.py` and notice that we have defined our Game class in there
* Look at the `__init__` function and see what it takes
    * Arg 1: background
        * This is the location where we can find the background image. Notice on `line 56` we load up that image and set it to our background. Now we know our first argument to create a Game will be the background image file.
    * Arg 2: lives
        * This might be a new one to you. The `lives=3` is called a default argument. Pretty much, if you don't give it a value, it will default to 3. Now we know our second argument to create a Game will be the number of lives (which will default to 3 if we don't give it)
* First step is to locate where our game background files are.
* Take a look inside of the `assets/background/` folder
    * Notice how we have 4 background files:
        * main_bg_rock.png
        * main_bg_snow.png
        * main_bg_sand.png
        * main_bg.png
* Let's set up a variable with a string that points to one of these files. Put this below `------- Your Code Here -------` 
```python
background_file = 'assets/background/main_bg.png'
```
* Now all we need to do is edit this variable to change our background!
* Next we can set up the Game with the line
```python
game = Game(background_file, lives=1)
```
* Save your changes, and run the game with `python run.py`
* You should see the game window pop up with a green background, and your terminal should say that you won the game! (Because we have no more monsters left)
* Congrats! You just set up your first game with our engine!


However, this game seems a little too friendly right now. We are definitely out of the "beginner" part of this course, and now firmly in the higher levels. Let's make it look like a harder part of the game.
#### On Your Own
* Change the background to use the sand background. The desert seems like a tougher level to beat.
* Change the number of lives to 5. You're going to need the extra lives!

### Add attributes to the Game
Now that we have the Game created, let's start adding stuff into our game world.
* First step will be to set up the finish spots, the area we want to protect. For this week, our finish area is the entire right side of the map.
* Let's add two finish indicators.
```python
game.add_finish((0.97, 0.03,))
game.add_finish((0.97, 0.90,))
```
* Take a look at how this works
    * We have a method inside of the Game class called `add_finish`.
    * It takes in a tuple with two items, an x and y value.
```
Important Note: When we are using the Game engine, we use decimals to determine position in the window. These decimals are the percentages of the window.
So the tuple (0.0, 0.0,) will be the bottom left hand of the window.
The tuple (1.0, 1.0,) will be the top right hand of the window.
The tuple (0.5, 0.5,) will be the exact center of the window.
```
* We call the game object's `add_finish` method so we can create a finish marker at the xy value pair we gave as the argument.
* Save your file, run the game again and see what happens. Notice how we have the finish flags there now!


Next up, let's start adding some towers! Before we move into this, you must know how our game engine works.
* We don't want to have the towers all pre-setup when the game starts. What would the player do then!
* Instead we want to have SPOTS where specific towers can be created.
* Our game engine will take in locations where it'll generate spots. When the game starts, those spots are clickable, and can have towers spawn into them.

Let's see how our game engine wants to receive the location of these spots.
* Take a look inside `engine/game.py` on line 196.
* Notice we have a method called `add_tower_spots` and takes in a variable called `coords`.
* Notice how we iterate through `coords` right? This must mean that coords is a list of coordinate values.
* Now go back to `run.py` and let's start making a list
```python
tower_spots = [
    (0.5, 0.5,)
]
```
* This will start us off with one tower in the middle of the map.
* We aren't done yet though! We must actually call the `add_tower_spots` method with it!

#### On Your Own
* Call our game object's `add_tower_spots` method with the list we just created.
* Add some more tower spots!
* Run the game, and see where those tower spots ended up. Would you want to change those positions?

### Add monsters to the Game
Now let's go through how to add monsters to our game. We need to first have a Monster class, and then create monster objects, which we will feed into our game object.
* Let's first look where we need to add our monsters into the game.
* Go to `engine/game.py` on line 246
* Look at the `add_monsters` method and notice what it takes in.
* We need a list of monster objects to feed into our game.
* We'll start you off with the FastMonster class.
* Go to `run.py` and start a list:
```python
monsters = [

]
```
* Notice on line 6 in `run.py` we imported a class called `FastMonster` from our lab code.
* Hop into `lab.py` and take a look at what we need to create a single `FastMonster`
    * arg1: x
        * The x position (in percentage of screen width)
    * arg2: y
        * The y position (in percentage of screen height)
    * arg3: spawn_delay
        * The time in seconds it takes for this monster to spawn after the previous one has spawned
* Let's create our first monster in game. Go to `run.py` and **add a single FastMonster** to our `monsters` **list**.
* You can create a FastMonster object by
```python
    FastMonster(0, 0.4, 0)
```
* We want to start on the left side of the screen, so the first argument for x position is 0.
* The monster should start slightly below the center of the screen height, so the second argument is 0.4
* The monster should spawn immediately, so we give it 0 as the third argument.
* **REMEMBER, WE WANT TO ADD THIS MONSTER TO OUR MONSTERS LIST**
* Next, call the `add_monsters` method in our game, so we can add our list of monsters to the game
```python
game.add_monsters(monsters)
```
* Save your file and run `python run.py` to see the results! You should have a single monster moving across the screen.

#### On Your Own
* Add some more fast monsters!

### Create Your Own Monsters
Now that we've got our basic game set up, let's create some more variety in our monsters!

* If you remember from last week, we also had a heavy monster.
* Let's create a new class for this heavy monster!
* Below the FastMonster class, create a new class called `HeavyMonster` with an empty init function.
```python

class HeavyMonster:

    def __init__(self):
        return

```

* Remember that `self` is always needed in a class. This is used to refer to itself as an object.
* Take a look at what was needed to create the FastMonster. Let's add those arguments in:
```python

class HeavyMonster:

    def __init__(self, x, y, spawn_delay):
        return

```
* Right now, this does nothing though!
* For classes, if we receive arguments inside of the `init` function, we must then assign variables to `self` in order for the created object to remember them!
* Take the argument variables in `__init__` and assign them to `self`
```python

class HeavyMonster:

    def __init__(self, x, y, spawn_delay):
        self.x = x
        self.y = y
        self.spawn_delay

```
* IMPORTANT: In order for us to use these variables in the rest of the class, we need to assign them to `self`. Variables assigned to `self` become **attributes** and can be used throughout the class.
* Speaking of attributes, let's define some key ones.
    * `self.assets`: This is the folder where all the monster game assets are. The images that allow us to show the monster sprite and animate it.
    * `self.hp`: This is the amount of health points a monsters has. 
    * `self.speed`: This is the speed in pixels per second of this monster.
    * `self.defeated`: This is a boolean saying whether or not this monster is defeated. If true, then the game engine will start it's defeated animation.

* We can define these in the `__init__` function. Remember, this function is run in order to create a new monster object, so we can initialize our attribute values there.
```python

class HeavyMonster:

    def __init__(self, x, y, spawn_delay):
        self.x = x
        self.y = y
        self.spawn_delay = spawn_delay
        self.assets = monster_1_folder

        self.hp = 140
        self.speed = 35

        self.defeated = False
```
* Notice we set `self.assets` to the variable at the top of the file. The `monster_1_folder` should be the folder with all the HeavyMonster assets.


* Now we have a final attribute to define, which is interesting. We call it the `path`. This is the path the monster must travel, defined by xy values.
* For now we will give you a function to add into the HeavyMonster class that will generate a path for us (simply go from left to right).
* IMPORTANT: Remember that adding a function to a class turns that function into a **method** for that class.
```python

class HeavyMonster:

    def __init__(self, x, y, spawn_delay):
        self.x = x
        self.y = y
        self.spawn_delay = spawn_delay
        self.assets = monster_1_folder

        self.hp = 140
        self.speed = 35

        self.defeated = False


    def build_path(self):
        # Only goes right
        i = self.x
        path = []
        while i < 1.0:
            i += 1
            path.append((i, self.y,))
        return path
```

* Also we must define `self.path` in our init function
```python
    def __init__(self, x, y, spawn_delay):
        ...
        self.path = self.build_path()
```

#### On Your Own
* Finally, let's figure out how our monster receives damage!
* Add a new method called `take_damage` to our HeavyMonster class.
* This method should have two arguments:
    * `self`: Every method in a class must start with self
    * `damage`: The amount of damage a tower deals to our monster
* Use these two arguments to change the HP attribute of our monster.
* Hint, you can change the `self.hp` attribute in order to do this.
* If our monster's hp is lower than 0, set its defeated attribute to True!

### Adding New Monsters into the Game
* If you create a new class in `lab.py`, before we can use it, we must import it into our `run.py` file.
* In `run.py` on line 6, see the line
```python
from lab import FastMonster
```

* Change that to say:
```python
from lab import FastMonster, HeavyMonster
```

Notice how we used a comma and added a new Class to import. Now we can start using that class inside of `run.py`
* Change your monsters list to also include a HeavyMonster. (Just add it at the end of the list, don't replace the other monsters you already added)
```python
monsters = [
    FastMonster(0, 0.4, 0),
    HeavyMonster(0, 0.3, 2)
]
```

* Save your file and run the game again, and you should see the HeavyMonster show up!
* Play the game and see if your heavy monster plays normally. Check if it gets damaged and can walk across the screen.

### Final Step
* It's a bit boring to have the monsters show up in the same exact spot!
* Change all of your Monsters to start at a random y position (the second argument in the constructor)
* Hint: use `get_random()` as the argument for y

### On Your Own
We've set up the game from scratch and added some monsters. Now let's set you off on your own!


There are 3 tasks for you to complete.
* Create the Speed Monster!
    * Create a new class called SpeedMonster
    * Set hp to 100 and speed to 15
    * The SpeedMonster has one special property
        * Everytime it takes damage, it gains 30 speed!
    * Implement the `take_damage` method to do this
* Create the Shield Monster!
    * Create a new class called ShieldMonster
    * Set hp to 50 and speed to 40
    * The ShieldMonster has two special properties
        * It ignores the first damage it takes
        * It ignores 10 percent of all damage!
    * Implement the `take_damage` method to do this
* Create a larger game!
    * Use iteration to create much more monsters than you can manually

These are fun challenges, and put a new twist to our game. Good luck, and reach out to me if you need any help!
