# AI Apps Exam Project --- AI Trading Card Price Prediction
## Ai Exam Project Description
### Made by Frederik Kruse Christiansen.
#### Full project scope
The full program in execution is supposed to both predict the prices of trading cards based on
previous days and/or weeks worth of price trends, price lows and amount + amount of different
versions.

Along with the project's predictions it is supposed to have a local database with the current
cards plus a history for the cards that have a value above a certain amount.

the model used should be able to handle tools and/or should be a reasoning model, these
requirements are for the ability to more accurately predict trends.

finally there is supposed to be a frontend where you can interact with the model, this while in
testing, might just look like a chatbot, or have dedicated buttons, but most likely i will also make
a figma of a fully complete program, with both its table view and further functionality once i finish
the basics.

#### models that could be used.
the current models i plan to make use of:

Qwen 3.5 for the reasoning. This model is of a higher quality to where it can think and reason
with itself, important for predicting the values of cards, though because of this reasoning, might
have to make a custom model where I tighten what it is supposed to work on.

Qwen 2.5 7b for the tool usage. While this model isn’t a reasoning model i have good
experiences with its ability to use tools, so i would lose the ability to predict/ reason if i used it
but there is a higher likelihood of doing specifically what i need it to without having to make a
custom model of it.

#### the ai part

Ai would pull from a database on what has the highest discrepancy like this item price is set to
500% of the price trend and higher for the lowest price in English, sorting out items with a price
value below 1 EURO

it would also show the top 10-50 outliers in the database, outliers being items like above
solutions, where there is a difference in the current database price, and the price trend/lowest
price

It could also run a prediction on say an item which had a trend of 5 euro, that rose to 8 euro
then rose to 11 euro over three days and predict if it's going to rise, in how many days, or if it's
going to fall in price depending on the amount available.

#### Other Electives and Group Members
#### This project incorporates no other electives and I am alone in making this project.