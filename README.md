# Project 3
This repository contains the code for project 3 of *CS50's Web Programming with Python and JavaScript* implementing the *Pizza* django application.

## Filestructure

According to the specifications of Django this repository contains one main directory for the whole *Pizza* Django Project as well as one directory for each of the two Django Apps: *Orders* and *Users*

### Pizza

There have been only very minor changes to the files in this directory relative to their default contents when they created by the Django `startproject` command.

Those changes include

* *settings.py*: Some additional lines in the end to enable using some additional Features such as *Crispy Forms*.

* *urls.py*: Urlpatterns to include the urls specified in users and orders module.

### Orders

The Orders Application contains the whole logic for the implementation of both the Menu as well as the ordering process. In fact it contains everything except the User Registration / Log In functionality.

In the templates directory one can find the main layout template which is then extended by the templates for the Menu / Index page (index.html), the Shopping Cart page (cart.html), the Adding Item page (add.html) and the Order overview (orderlist.html).

In have chosen to create the following models:

* *MenuItem*: This is one Item of the Menu like a Small Regular Cheese Pizza (each size is a different MenuItem)
* *Topping*: Toppings that can be added to a pizza.
* *Extras*: Extras that can be added to a product. (Currently only Extra Cheese for all Subs and Onions etc. for Steak+Cheese Sub). Which Extras can be added to which product is controlled through a Many to Many relationship.
* *OrderItem*: Item that has been configured and added to an Order. Contains a ForeignKey reference to the MenuItem as well as many to many relationships describing which Toppings or Extras have been added.
* *Order*: One Order contains of all the Order Items that have been added to this order and is assigned to a status (Open (Shopping Cart), Pending, Completed, Canceled)

To enable a user to customize and add an OrderItem I have used a django ModelForm based on the OrderItem Model.

### Users

For the log in part I completely rely on the built in log in view, whereas for the registration I have slightly customize the view using a slightly modified version of the built in UserCreationForm that adds first and last name.
To improve the aesthetics of the forms I format them using *Crispy* Forms in my templates.

## Usage

To see a quick walkthrough of the project check this [Video](https://youtu.be/j41qNQd8erI).

## Personal Touch / View and Cancel Orders

My Personal Touch was adding an additional page for the user where he can see all his Pending, Completed and Canceled Orders as well as being able to cancel his pending orders in case he changes his mind.
