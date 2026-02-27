# Jinja, Macros, and Packages (dbt Studio)

## Contents

- [Welcome 5min](#welcome-5min)
  - [Welcome](#welcome-5min-welcome)
- [Getting started with Jinja 40min](#getting-started-with-jinja-40min)
  - [Jinja basics](#getting-started-with-jinja-40min-jinja-basics)
- [Working with Macros 60min](#working-with-macros-60min)
  - [Macros](#working-with-macros-60min-macros)
- [Packages](#packages)
  - [Installing packages](#packages-installing-packages)
- [Advanced Jinja and Macros](#advanced-jinja-and-macros)
  - [Advanced Jinja and macros](#advanced-jinja-and-macros-advanced-jinja-and-macros)
- [Survey 3min](#survey-3min)
  - [Survey](#survey-3min-survey)

## Welcome 5min
<a id="welcome-5min"></a>

### Welcome
<a id="welcome-5min-welcome"></a>

#### Welcome

## **Welcome to dbt Learn, Jinja, Macros, and Packages! **

****This course assumes that you have learned and completed the dbt Fundamentals course covering the topics of models, sources, tests, documentation, and deployment.

The practice sections in this course will build off that same project so we encourage you to use the same repository for your learning. 

As you learn, be sure to join other learners in #learn-on-demand over in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)** channel in the dbt Community.

**Note: **Some demos in this course use sample datasets from Amazon and Shopify. Please find the CSV files for these datasets in the resource library. 

📣** Note regarding trial dbt accounts**

- If you are using a dbt trial account to complete the hands-on portions of this course, and your trial account was created after February 2, 2026, your dbt version might be using the new dbt Fusion engine.
- As of October 13, 2025, the dbt Fusion engine is in a preview phase, meaning it is not generally available, but is stable and production-ready.
- If your dbt account is on Fusion, you may experience some limitations in dbt. Please refer to this page for the current [supported features and limitations](https://docs.getdbt.com/docs/fusion/supported-features).
- If you are unable to use a non-GA product, please follow these steps to turn off the Fusion engine:
- Go to Orchestration -> go into each environment -> click edit -> select "Latest" as your dbt version -> click save

#### Frequently Asked Questions

## Frequently Asked Questions

**How long does this course take to complete? **

I would estimate that this course would take about two hours to complete. There are 45 minutes of video and I would approximate about one hour of practice for someone who is new to dbt. 

**How much does this course cost? **

A grand total of… $0.

**If I need help with working on dbt Cloud, where can I reach out?**

We have chat support embedded in dbt Cloud. Click on the chat bubble icon in the upper right-hand corner. Reach out with any questions/errors that you have.

**If I need help loading training data into my data warehouse, where can I reach out? **

Please reach out in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)** channel in [**dbt Slack**](https://www.getdbt.com/community). We'd be happy to support you there.**
**

**If I notice a bug or error in one of the lessons, where can I share that? **

Send a quick email to **[training@dbtlabs.com](mailto:training@dbtlabs.com)**. Please include the URL and a screenshot. This will allow me to quickly find out what needs to be fixed. 

**Where can I submit feedback on the course content? **

Please feel free to post feedback in the end of [**course survey**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com). We are quick to respond and love to hear suggestions

## Getting started with Jinja 40min
<a id="getting-started-with-jinja-40min"></a>

### Jinja basics
<a id="getting-started-with-jinja-40min-jinja-basics"></a>

#### Learning objectives

## Learning Objectives

- Explain how Jinja works as a templating language.
- Anticipate the output of a block of Jinja code.
- Refactor a pivot query using Jinja.

#### What is Jinja?

Extracted captions from video: What is Jinja?

So now we're talking about something called Jinja. You may have heard of Jinja before. It's what's called a templating language. What this is going to allow us to do is really level up our SQL writing.

So this is going to bring in functional aspects of programming like we see in Python, Ruby, and JavaScript, and use that in our SQL so that we can work more like software engineers when writing SQL. So, have you ever received an email that said something like hello with like an awkward space and then a comma or something like hello, and then curly braces and the word name, not your actual name. The author of that email was probably using a templating language in some way. Something, another popular templating language is something called liquid.

So given that we've actually seen curly braces like that before and most popular one that we've used so far is the ref function. So what the ref function does, is it allows us, you and I, to both write ref to reference whatever model we want to refer to. But then when you're working in your development environment, it's going to replace that with dbt underscore your first initial, last name. When I run it in my environment, it's going to be dbt_kcoapman, so we can write the same code and we don't have to swap out the schema name manually when we traded the code between you and I.

So it's going to allow us to collaborate better and also just write a faster SQL and more powerful SQL. Ultimately, this is going to this Jinja knowledge that we're about to develop. It's going to help us level up into what's called macros, which is where we really get to leverage Jinja in our dbt project.

#### If Statements in Jinja

Extracted captions from video: If Statements in Jinja

Welcome everyone. In this video, we're going to cover if statements in jinja. So DBT's power comes from a combination of three different programming languages. We've got SQL for defining data transformations, YAML for configuring, documenting and testing those transformations, and finally Jinja for templating and lineage.

Of course, Python is in the background, stitching those three together. But with these few languages, YAML, Jinja, SQL and Python, they're the only ones really that you are expected to to interact with as you get started with dbt. Jinja is a major part of DBT's compilation process, allowing dbt to build and understand relationships between models and tests in your DAG and properly model the relationship between your project files and your warehouse objects. Since dbt relies on and understands Jinja, we as engineers can adopt Jinja into our modeling process to make our code more powerful, more modular and more efficient.

Jinja can be a powerful tool to both speed up the process of developing SQL, as well as enabling more sophisticated dbt operations like environment specific behavior permission controls in your warehouse, and even automated removal of deprecated or stale models from your warehouse. The goal of this course is to learn what Jinja is, how it interacts with its data types, and finally learn about how to build Jinja into your own projects in a scalable way. First, we're going to start with the basics of Jinja. At its core, it's just a Pythonic templating engine.

If you've ever received a marketing email from some company that says something along the lines of hey, first name, here's an offer for you. You've likely already seen a templating engine, or maybe even Jinja itself, out in the wild. If you've ever coded in Python, coding in Jinja is going to feel pretty similar to you. The most basic operations available are setting and interacting with variables, using if, then statements for conditional logic, using for loops to iterate over variables and produce some sort of repeated code, and finally printing variables out into your files.

Let's begin with some basic forms of Jinja syntax. So first we want to use the curly percent. Now this indicates some sort of operation is happening inside of the Jinja context. It will be invisible to the end user after the code is compiled into whatever you are outputting.

The second thing we have is a double curly brackets. This indicates that we are pulling something out of the Jinja context and actually printing it into the file that we're interacting with in order to produce some sort of written, material. Now, the first thing we're going to start with is setting a variable. So we're going to say set and we'll say temperature equal to 80.

Okay. The next thing we're going to start with is an if statement. So we can use our shortcut and go to if. An if statement helps us have a flow of logic.

Kind of like, if it's raining, bring an umbrella. Or else if it's not raining, leave that umbrella at home. So let's dive in. So we set our variable.

And a variable is a container that holds a value. Think back to algebra class. Now, our if statement is going to choose one of two desserts. So we're going to have an if block depend on the value of temperature.

We're going to say if temperature, let's say greater than 70m Then we want to say I want a sorbet. So start with a refreshing lemon sorbet. Else. Because what if it's, equal to or less than 70?

So we have options here. So we need to think through that logic. A decadent. Oops.

If I can spell decadent chocolate cake. And I'm going to start with a sentence up here. So on a day like this, I especially like. And then we'll flow through our if statement.

So let's read through this. So I'm setting a variable named temperature at 80 degrees. On a day like this, I especially like. And if my temperature is greater than 70, and it is, I should get a refreshing lemon sorbet.

Else if it's equal to or, less than, I should get a decadent chocolate cake. So let's compile here and see what we get. On a day like this, I, especially like a refreshing lemon sorbet. Because our temperature is greater than 70 degrees and it satisfied this if statement, we got the first option.

Now what happens if we change that variable? Let's change it to maybe 60 degrees. What do you think the expected behavior would be here if you said I would get the decadent chocolate cake? You are correct.

Let's test this theory. On a day like this, I especially like a decadent chocolate cake. Awesome. So now you've learned how to use an if statement.

In the next video, we'll talk about other concepts in Jinja.

#### For loops and Variables in Jinja

Extracted captions from video: For loops and Variables in Jinja

Welcome back. We just learned about if statements and setting variables in Jinja. Now it's time to learn about for loops. Let's remember the two basic forms of Jinja syntax.

We've got the curly percent, okay? And that indicates that some sort of operation is happening inside of the Jinja context. Now remember, that's invisible to the end user after the code is compiled into whatever you are outputting. And we saw that in the previous example.

The second basic Jinja syntax is a double curly bracket. That means we are pulling something out of the Jinja context and actually printing it into the file that we're interacting with in order to produce some sort of written material. I'm going to bring over some code that I wrote previously, going to post it in a new scratch pad. Now let's just take a look at this.

We can see a, we've got the curly percent, so that's the Jinja context and the double curly percent, meaning I'm pulling something out of that context. Here we have something called a for loop. This iterates over some sort of iterable variable. And if we click on the compile button, dbt will interpret these statements.

So it understands that this is a for loop inside of the Jinja context. It should be printing this variable called J, which is a number within the range 0 to 26. When we compile this Jinja, we end up with a readable query. that, we are selecting each of the numbers.

So let's click compile. We also notice an if statement here. So if not loop last, meaning if this is not the last loop statement. So I'm getting a union all for all of these except the very last.

So we notice that if statement which we remember from the previous video. Let's click Preview. Now when we click Preview we have an execute against our warehouse and run SQL. That actually makes sense.

This is intended to just be a starting place to understand some of the basic syntactical blocks of Jinja. Let's go a step deeper and learn how Jinja interacts with these variable types. Now before we get into the sort of deep end for the for loops and the if statements, let's get familiar with some of the very, very basics and tactical interactions in Jinj. Specifically, we'll set some variables in Jinja just like we learned in the previous video.

So I'm going to open a new scratchpad. Now Jinja, being a Python based engine, supports the use of basic Python data objects, namely simple variables, lists and dictionaries. You can interact with them in much the same way you would expect if you were developing in Python. Dictionary values are accessed by keys.

For example, list values are accessed by the index. So let's start with some of the basics here. So the first thing I'm going to do is start with my curly percents and have a set block. So I'm going to set my first cool string.

Oops, cool underscore string equal to. Wow, cool beans. Okay, oops. And I need just my underscore here.

So in these curly percents, we are actually setting something inside of the Jinja context set is the keyword that we're going to use to actually set that variable. Now, if I want to access coolstring, I would use my double curly percents to access that. Okay, so let's click compile and I got my cool string. Wow, cool string.

Side note here, when we are outputting something, and we hit compile, the limit is 500. So that's it does not execute the code. And that's just to make sure that Studio is performant for you. Okay, so let's add two more variables.

So set my second bool string and let's set that to Oops, equal to. This is Jinja 90 my percent again. And I'm going to set one more. So my curly percent set.

And let's say my fav num, equal to 26. Okay, now I'm going to string these things together. So cool string and then my second cool string, I'll just copy this name. I want to write Jinja 4.

And now I'm going to access my fav num for my favenum, years. Okay, let's think about what this is going to output. Let's click compile. Wow, cool beans.

This is Jinja. I want to write Jinja for 26 years. Yeah, sounds doable. So set inside of the block of the curly percent syntax here.

That's how we set simple variables. We can also do the same thing to set a, a list. So the next thing I'm going to do here is introduce a, third Jinja syntax, which is just the curly pound sign. So let's practice that, curly pound sign.

This indicates a comment. So I need to do now the pound sign curly to close that comment. If we do this and click compile, we should get nothing because it's inside of a comment. So nothing is actually executed or evaluated.

All right, so now we're going to move on to lists. So let's just set a variable named animals. So, and I can even use my, shortcuts. So set.

So set. And I'll set animals equal to. And now I'm going to have a list. So I'm going to start with a lemur, a dingo, a rhino, and a dog.

Okay, so this is bracketed by square brackets with commas in between each of the values. You can see here that this list has four strings. If we want to access each of the values of the list, we're going to use the index, just like we would in Python. So this is my animals list.

And just like in Python, the list starts at index zero. If I access the zeros index of this using the bracket notation, which you'd expect to see the first or zero index value of that list. So if we do this, let's say animals and then I'll say zero. This should give us the first value.

And now let's say index one, which gives us the second list value two and three. Let's click compile to access lists. We start at zero and then we do length minus one to access each of the elements. Here we can see each of my list values were printed out.

Lemur, dingo, rhino, and dog. Now that we have a list, we can practice iterating over that list and producing similar boilerplate code using the for loop that we introduced before. So first I need a loop to access each index in my list. So I'm going to use my shortcut for.

So I've got that. So let's say for animal. Oops. Animal. In animals, let's say my favorite animal is the, And remember the double curlies to access something from my list.

So let's click compile. This for loop indicates that we are going to be iterating over the values inside of an iterable. And in this case, the list is an iterable. A dictionary is also an interval which we will learn about in the next video.

So in this case, for each of the animal in my animals, and each of the four blocks that we write needs to be boxed in by that N4 keyword, which we get when we use that shortcut. That's how Jinja knows to start and end a particular iteration. All right, now that we have that sentence printing My favorite animal is the lemur. My favorite animal is the dingo.

My favorite animal is the rhino. My favorite animal is the dog. So we see the animal with that number index. This is repeated every single time.

And the thing that changes is the value of the animal. A variable inside of a looping iterable. Here we can kind of get some similar code printed multiple times, changing the input based off the contents of that list variable. All right, so we just learned about lists and for loops.

And in our next video we will be combining if statements with for loops, lists and dictionaries.

#### Combined Concepts

Extracted captions from video: Combined Concepts

Hey everyone. Welcome back. We just learned about if statements and for loops in Jinja. So now for my next trick, we're going to combine two of those ideas and get some really powerful code.

These don't just have to be standalone pieces of code. So what I'm going to do is show you an example of this. Okay, I'm going to bring over some code just to save time. This is what we know as a list.

And I'm setting my list called foods. closed in by the brackets. And I have a few values in here, so radish, cucumber, chicken nugget, and avocado. So now we're going to see how we can, use for loops and if statements to put together for some good use.

Okay, so let's start with and I'm going to use my shortcut of, four. So for food in foods. Okay. And I want to do something now based on what the food is.

So we're going to set a new variable. We will call that food type. so let's use my shortcut. So for oops, I mean, if.

So if my food is equal to chicken nugget, I want to do something and I want to set a variable. So I'll say set. I'm just going to indent this. So set food type equal to snack, obviously.

But now what about the situations when it's not a chicken nugget? If you recall, I need my else statement. I'm just going to copy this so else I'm going to set my food type equal to vegetable. So remember, the else statement is if.

My first if is evaluated as false. And remember to end our if, we need the end if block. And just remember to keep your logical blocks at the same indentation level. It just helps us follow along a little bit easier.

And so to end my for loop, I need the end for okay, and now I want to build a sentence so the delicious. And now we want to access food. Oops, is my favorite food type. Okay, so now we have a for loop and inside of that an if loop setting a variable.

And then I have a sentence printing out in that for loop. So for every food in food, I'm going to print a statement And based on that food, I will assign a food type. All right, so let's hit compile. All right.

The delicious radish is my favorite vegetable. The delicious cucumber is my favorite vegetable. We're looking good. The delicious chicken nugget is my favorite snack.

Correct. And the delicious avocado is my favorite vegetable. Awesome. This is exactly what we wanted with the exception of these really large white space white space blocks.

The reason for this is that as Jinja compiles and evaluates each of the blocks that it needs to evaluate in order to generate the code we want, it's going to include lines for every line inside of our Jinja code, even if it's not evaluating into something inside of our file. So, for example, for food in foods, this is a line of code that we wrote, right? And that gives us white space. So the way that we can control white space is by adding these little minus signs next to our percents.

So this will remove it as a line. When we add the minus sign next to the percent, it will remove the line, immediately adjacent to the percent sign. It will eliminate white space before and after these lines. So in this case, the set block is very standalone.

We don't need to use this. We don't need white space for this. So we can remove it here. I'm going to see what we get now.

All right, that's a lot better. So we should see fewer lines at the very top of our file just by adding in those minus signs. If you play around with the minus signs, this can be a good way to control the cleanliness inside of your Jinja code, corresponding to cleanliness inside of whatever code we're generating here, probably SQL. So we've reviewed if loops for loops, variables, and lists.

The next option we will talk about is a dictionary. So I'm going to copy and paste my dictionary just for time's sake. So I'm going to open a scratch pad all, right. So here is a dictionary which is wrapped by the curly percents box in by another curly bracket.

So that tells Jinja it's a dictionary. Each of the variables I'm setting inside of the dictionary has a key which is the first part, and a value, which is the second. So, If I would access, the key called word, I should get the word data. And then when I access the key part of speech, I should get noun.

When I access the definition, I should get the building block of life. So how do I access something from a dictionary? Just going to copy and paste this for time. I still use those double curlies for my Jinja context, but I need to use my brackets and add the key that I'm accessing.

So let's hit compile. We get data. the key is word, and then the value is data. So this looks right.

So now I want to string these together. Okay. So I'm going to just copy this for the sake of time. So I want to say the word is my.

This is my part of, speech. And I want percent. I want, a parentheses there to close that in colon defined as. And let's say definition.

So I should get my data is a noun and it's defined as. The building block of life. Let's click compile. Awesome.

Exactly what we were looking for. So now you can imagine a list of dictionaries can also be very valuable. Hopefully you feel a little bit more comfortable setting variables, interacting with lists, dictionaries for loops, and if statements. In our next videos, we're going to see how we can apply these things in applications of different macros.

#### Pivot with Jinja

Extracted captions from video: Pivot with Jinja

Welcome back everyone. In this video, we're going to focus on taking the Jinja skills that we just learned and apply those in a model so we can write more concise SQL and see how Jinja can be used in our modeling practice. So with that, we're going to start with stg Payments. And I've already previewed my data just to see what it looks like.

So I see here that I have a bunch of payment methods. Credit card, bank transfer, gift card, etc, etc. Well, I might want to take order ID and pivot that out by payment method and grab the amount. So I'm going to start with this basic select statement.

Okay. And I want to filter out any failed payments here. Okay, so let's say where status. Let's say equals success.

Oops. And I need a lowercase there. Okay, let's click preview. Awesome. Great. So I've got all my successful payments.

So the picture we're going to look to build is order ID in the first column and then a column for each amount for each of those payment methods. So for order ID 1, we'd have credit card as 10, coupon as 0, bank transfer as 0, gift card as 0, etc. Etc. So only credit card would have an amount, and the same for each of the other order values.

So if you haven't seen pivoting before, we're going to do it with a case when statement. Some warehouses have a built in pivot function, but this is still a helpful exercise to go through just to see how Jinja can be leveraged to write a pivot function, something that might be useful to your coding practice. So first we're just going to write that pivot in just pure SQL and then we'll refactor it with Jinja. So I'm going to make a new model and I'll just use what I have.

So I'll click save as and I'm going to name it Int. Underscore Orders. Underscore. Underscore, Pivoted.

Oops. Let's make that lowercase pivoted SQL and I'll put that in my Models folder in my intermediate folder. Okay, great. Let's start building out the CTEs that we might want to use.

So our first CTE should be with payments as. I'm going to indent all of this. Okay. And then I'm going to create another CTE for my pivoted data.

Pivoted as. I'm going to select Star from Payments. I'm just building out my CTEs at this point in time. So don't worry about.

We're not trying to actually do the pivot right now. Just setting us up. So select star from pivoted. Okay.

We're just following best practices here by having that import cte, a CTE to do our second transformation, and then finally selecting from that final cte. Okay, so we're going to build all of that pivot logic here in our pivoted cte. So we want to pivot it again on our order id, just as I said before. And we want to have each of our payment methods in our pivot.

So one way to do that is through a sum of a case when, and we're going to do a case when for each payment method. So, okay, I'm going to start with pivoted. So I know I need my, let's say, order id. I'm gonna have some.

I'm gonna just start with doing it for bank transfer first. Okay, so case when payment method, oops, equals bank transfer, Then I want the amount else zero. We can say end, and I'll, have that as bank transfer amount. Okay.

And don't forget your group by. So group by. Let's just say one. Okay, let's click save and let's preview that.

Okay, so I have some values here. Some have zero. That makes sense because some of them might not have, a bank transfer amount. Okay, so now we just pivoted on order id.

And for each order id, we can see the bank transfer amount in the videos. Following this, we're going to keep building this out and actually apply Jinja to our code.

#### For Loops and Case When

Extracted captions from video: For Loops and Case When

hey, everybody. In the previous video, we successfully pivoted out revenue amount for bank transfer. So now I'm going to use that same code that I built and repeat that for my other payment methods. So, let's go back to stg payments, and I have it previewed already.

So let's look at the other payment methods that I have. I have credit card, coupon, gift card. Okay, great. So I want to use those other, payment methods and pivot it out on those.

So let's add a line for each. So credit card, coupon, gift card. Okay, And I'm going to change these one at a time so that you can follow along. Okay, so let's start with coupon.

So I'm just changing case when payment method equals coupon, then amount else zero end. I'm going to change this to coupon amount. Okay, next is credit card, and I'm just going to copy that. So case when payment method, equals credit card, then amount else zero end.

All right, looking good. Now we have gift card pay. Case when payment method equals gift card, then amount else zero and. Okay.

All right, so let's click save. Now let's preview our data and see what it looks like. All right, looking good. So we have our order ID on the leftmost and across the top, we have each of our different payment methods in the amount for that particular payment method for that order.

So that's how we would write this pivot in pure SQL. But now we're going to focus on how we can write that a bit more concisely using Jinja. If you ever notice yourself repeating code just like I've repeated this case statement, it's probably a opportunity, to improve your code and make it a little bit more dry. By dry, we mean if you're repeating it, you can probably build, use some ginger or build a macro for that.

So we are going to use this application. And if we have a very long list of pivots, say we had even more amounts, it would even be more powerful. All. Right.

So let's think, back to the beginning videos and think of some tools we learned, just to make this a little bit more programmatic rather than declaring what we want the sequel to look like. So I'll give you a second to think of the things that we learned. Okay, so the first thing that we're going to start with is setting a list. okay, so after order id, I'm going to create a list to hold my different payment methods.

Okay. So if you remember, I can do a set. Okay, So I can use my double underscore. So let's say set payment methods.

Oops, I can spell equal to, and we're going to have a list. So if you remember, that would be bracketed in. And then in that list, I'm just going to add a list, of each of these as strings. So bank transfer.

Okay. Coupon, credit card, and then gift card. Okay, great. So I've got a list for my payment methods.

Let's just save that. It's a good practice to save as you go along. Now, I want to use this list that I just created, loop through each of those payment methods, and then have a case statement with a sum wrapped around it that uses that list. Let's think about how we can do that.

Give you a second. Okay. Hopefully you have some ideas. Okay, now since we are going to use our Jinja, I'm going to remove these three, sums and case statements.

Because I'm actually going to just use one and use a few other ginger applications like for loops. And we are going to loop through this list and create a statement a, just based on that loop. Okay, so I want to start with a for loop. So, that would be after my list.

So I'm going to do four. Okay, so that's just my. My shortcut I use for a for statement. And I'm going to bring this case statement in here.

Oops. Okay, all right, so I've got a four item in sequence. So I can say four. Let's say payment method in payment methods.

So for each, instance of a value in my list, I'm looping through. Okay, remember, you always need to end that for loop, but if you use a shortcut, it's already there. Okay, so now we can actually use our ginger variable payment method. So what I can do is this needs to be a string, but I can use my jinja for payment method.

Okay, so one payment method equal equals my payment method from the list. Then amount else zero. Okay, looks good. But I also want to add it actually in the column name.

So let's add it here then too. Payment method. Okay. All right. And, looking good. Okay, so because I want to teach you an additional topic.

A really powerful thing that we can use. I'm going to actually make a comma here at order ID and a comma at the end of my sum. Okay. And we'll talk about that a little bit later.

That's just for the example. Okay, so let's talk about what this loop is doing. So the first time we go through this loop, bank transfer is being used. Right?

So case one payment method equals bank transfer, then amount, else zero as bank, transfer amount. Let's collapse this. Okay, so that would be great. Then it goes through for coupon.

Then we have would have coupon amount, then credit card, and then gift card. Okay, so let's, compile this and see what it looks like. Awesome. I've got select order id.

I've got my bank transfer amount, my coupon amount, my credit card amount, and my gift card amount. So we've successfully created that, pivot using a four list, and using Jinja. So I'm going to save this. Okay, we're going to break the video up here because I'm going to teach you a new concept.

In the next video, we will learn about loop last and we will learn how to tidy up the SQL and remove that white space.

#### Using `loop.last`

Extracted captions from video: Using `loop.last`

In the previous video, we were working on stg payments, we were working on pivoting out order ID and the amount for each of the different amounts that we have, bank transfer, coupon, credit card and gift card. So I've compiled that SQL. Let's take a look at it I've got order ID comma, my case 1 for bank transfer comma, my Case 1 for coupon as coupon amount comma, same for credit card, same for gift card. Now, if you read through this carefully, we might see something that might throw an error when we actually run the SQL.

I'll just give you a few seconds to think about it. If you read through, okay, if you caught it, it's this trailing comma. So we actually want the SQL to not have this trailing comma. So we need to find a way to change this that we can go through the for loop and we don't get that comma at the end.

So, one way that we could avoid this is by using leading commas. This could be useful. But, I want to remind you of a useful Jinja variable. So I'm going to keep the trailing commas.

Okay, let's take a moment to think about, Jinja applications that we saw in the earlier videos. There's specifically one that's very useful in this case. If you remember, we were, introduced to loop last. So if we are on any iteration except the last, add the comma, else do not add the comma.

That's just one way of doing it. Okay, so I'm going to, navigate to the docs. Okay, so this is my for loop documentation. Now just a reminder here, our compiled SQL is working, but it's not compiling to exactly what we want.

So this is a ginger problem. So the docs are really going to be helpful here. I'm looking at the for loops because I'm trying to see how I can access, if it's the last part of the loop, if it's the last instance in the loop. So we've got our for loops here.

Great. There's some extra variables that we can actually access inside of a for loop block. So let's take a look at these. We've got loop.index

so that tells us what iteration the loop is on. I see loop first. So it's true if we're on the first iteration and loop last. Okay, I think that this is what we are looking for.

Let's go back to studio. Let's take a look at our code. Okay, so we want to do something about that last comma we had in the compiled code. So we want to use the loop last.

So let's think about our logic. If I want to go through for the first, three objects in our list. So bank transfer, coupon, credit card, I want that comma. But when I'm on gift card or the last instance, I do not.

Okay, so using loop last, let's think about that loop. So the first three times, that would be false. And if I go through the last time, it will be true. So let's use an if statement here.

Okay. Inside of our for loop. So I'm going to remove this comma. I'm going to indent here.

So I'm going to add an if if block. Okay, so if, loop dot last. Okay, then I want my comma. That doesn't seem right.

I want a comma for if I'm not on my loop last. So let's try if, not loop last. Okay, so for each of these first three objects in our list, bank transfer, coupon, credit card, they're not the last. So I'll get a comma.

But on this last, object, gift card, I will not get a comma. Okay, sounds good. Let's click compile and see what we get. Okay, so there's a lot of white space.

Don't worry, we'll fix that up in a moment. But let's check our commas and see what is going on here. So after bank transfer, I've got a comma correct. After coupon amount, I've got a comma correct.

After credit card amount, I've got a comma. And after gift card amount, no comma. Well, it worked. So that sounds great.

Now we were able to do the pivot with Jinja. Instead of copying and pasting, that case statement four times using Jinja, we were able to write this a little bit more concisely, a little bit more dry with using a for loop and an if statement. Now, let's say we get a new payment method to expand this. I can just add it to my list.

Okay, say it was bitcoin. Let's preview that and make sure that it adds to my list. Now, gift card is not the last anymore. But let's just take a look at my SQL.

So now I should have a comma after gift card, but not after bitcoin. All right, looks good. So always when you have that list and you have a for loop, it's going to iterate over the entirety of your, your list. So that's how you use Jinja to refactor a pivot.

A bit, bit more functionally make it a bit easier to update. So now we're just going to focus on the styling, and how to get rid of some of that messy white space. So way that we can do this if you remember from the previous videos, we just want to add, little minus signs next to this. Okay, so that's going to be really helpful.

So maybe for this list I don't want to add a line, right? For this, if statement, I don't want to add a line here. The minus signs remove the white space before and after. Okay, so let's click compile and see what we get.

Oh, wow, that looks nice. So now we've learned how to, make it look a little bit prettier. We've learned how to use a for loop. We've used, learned how to use an if statement and loop last.

It's really helpful to look at the documentation as you're going through this because not everything is going to be on top of mind. There's a lot of documentation in the Jinja docs, so, so a lot of variables that you might not know about. So that's going to be really helpful. Just to say, if you're ever writing some repeated code and you find yourself copying and pasting something, it can be really helpful to consider using Jinja.

This will then build into macros which we're going to cover next, which are ways that you can take the same logic, generalize it, and put it in a separate file that will quickly pull that same logic into other models. So if you have multiple pivot models, maybe you could write one pivot macro and use that macro in all the different models, that you are performing a pivot. So thank you for joining and looking forward to learning in the next videos with you.

#### Practice

## Practice

Using what you've learned in this module, complete the following in your dbt project:

### Try it yourself

Follow the video on refactoring a pivot model with Jinja to build a model called int_orders__pivoted.sql in the models/marts/core directory.

### Extra credit

Find another creative way to use Jinja in your models.

#### Exemplar

# Exemplar

	Code snippet for int_orders__pivoted.sql

	```sql
{%- set payment_methods = ["bank_transfer", "credit_card", "coupon", "gift_card"] -%}

with 
    payments as (
        select * from {{ ref("stg_stripe__payment") }}
        ),
    
    final as (
        select
            order_id,
            {% for payment_method in payment_methods -%}
                sum(
                    case
                        when payment_method = '{{ payment_method }}' then payment_amount else 0
                    end
                ) as {{ payment_method }}_amount
                {%- if not loop.last -%}, {% endif -%}
            {%- endfor %}
        from payments
        group by 1
    )
select * from final
```
****

#### Review

## Review

	### Jinja 

	Jinja a templating language written in the python programming language. Jinja is used in dbt to write functional SQL. For example, we can write a dynamic pivot model using Jinja.

	### Jinja Basics

	The best place to learn about leveraging Jinja is the [Jinja Template Designer documentation](https://jinja.palletsprojects.com/page/templates/).

	There are three Jinja delimiters to be aware of in Jinja.

	

		- {% … %} is used for statements. These perform any function programming such as setting a variable or starting a for loop.

		- {{ … }} is used for expressions. These will print text to the rendered file. In most cases in dbt, this will compile your Jinja to pure SQL.

		- {# … #} is used for comments. This allows us to document our code inline. This will not be rendered in the pure SQL that you create when you run dbt compile or dbt run.

	

	A few helpful features of Jinja include dictionaries, lists, if/else statements, for loops, and macros.

	**Dictionaries** are data structures composed of key-value pairs.

```
{% set person = {
    ‘name’: ‘me’,
    ‘number’: 3
} %}

{{ person.name }}

me

{{ person[‘number’] }}

3
```

	**Lists** are data structures that are ordered and indexed by integers.

```
{% set self = [‘me’, ‘myself’] %}

{{ self[0] }}

me
```

	**If/else statements** are control statements that make it possible to provide instructions for a computer to make decisions based on clear criteria.

```
{% set temperature = 80.0 %}

On a day like this, I especially like

{% if temperature > 70.0 %}

a refreshing mango sorbet.

{% else %}

A decadent chocolate ice cream.

{% endif %}

On a day like this, I especially like

a refreshing mango sorbet
```

	**For loops** make it possible to repeat a code block while passing different values for each iteration through the loop.

```
{% set flavors = [‘chocolate’, ‘vanilla’, ‘strawberry’] %}

{% for flavor in flavors %}

Today I want {{ flavor }} ice cream!

{% endfor %}

Today I want chocolate ice cream!

Today I want vanilla ice cream!

Today I want strawberry ice cream!
```

	**Macros** are a way of writing functions in Jinja. This allows us to write a set of statements once and then reference those statements throughout your code base.

```
{% macro hoyquiero(flavor, dessert = ‘ice cream’) %}

Today I want {{ flavor }} {{ dessert }}!

{% endmacro %}

{{ hoyquiero(flavor = ‘chocolate’) }}

Today I want chocolate ice cream!

{{ hoyquiero(mango, sorbet) }}

Today I want mango sorbet!
```

	### Whitespace Control

	We can control for whitespace by adding a single dash on either side of the Jinja delimiter. This will trim the whitespace between the Jinja delimiter on that side of the expression.

	### Bringing it all Together!

	We saw that we could refactor the following pivot model in pure SQL using Jinja to make it more dynamic to pivot on a list of payment methods.

	**Original SQL:**

```sql
with payments as (
   select * from {{ ref('stg_payments') }}
),
 
final as (
   select
       order_id,
 
       sum(case when payment_method = 'bank_transfer' then amount else 0 end) as bank_transfer_amount,
       sum(case when payment_method = 'credit_card' then amount else 0 end) as credit_card_amount,
       sum(case when payment_method = 'coupon' then amount else 0 end) as coupon_amount,
       sum(case when payment_method = 'gift_card' then amount else 0 end) as gift_card_amount
 
   from payments
```

	**Refactored Jinja + SQL:**

```sql
{%- set payment_methods = ['bank_transfer','credit_card','coupon','gift_card'] -%}
 
with payments as (
   select * from {{ ref('stg_payments') }}
),
 
final as (
   select
       order_id,
       {% for payment_method in payment_methods -%}
 
       sum(case when payment_method = '{{ payment_method }}' then amount else 0 end) 
            as {{ payment_method }}_amount
          
       {%- if not loop.last -%}
         ,
       {% endif -%}
 
       {%- endfor %}
   from payments
```

#### Knowledge check-jinja

## Working with Macros 60min
<a id="working-with-macros-60min"></a>

### Macros
<a id="working-with-macros-60min-macros"></a>

#### Learning objectives

## Learning Objectives

- Explain the role of macros in a dbt project.
- Define macros in the macros folder.
- Add macros to models.
- Write a macro for converting from cents to dollars.
- Write a macro for limiting data in development.
- Negotiate the balance between readability and DRY-ness.

#### What are macros?

Extracted captions from video: What are macros?

Now, we're going to talk about macros. Think about all the SQL that you've written in your work in data. There's probably some places where you've written the same similar logic across multiple models or across multiple SQL files. And this may have been in the form of a pivot or creating a really long table of dates or times, or it may have even been something like remove duplicates or check for duplicates.

This is where macros come in. Macros allow you to write generic logic that is then reusable throughout your project. So what this means is in a single file, you write your macro and then you can have multiple models use that macro in their specific use case. And so if we're working on a team and you write a macro, commit that to our project, I can then leverage that macro in the modeling I'm doing.

And we can reverse that. And I can give you a macro that I've been using as well in a future module. We're going to cover packages and this is where things really get cool. There are packages that you can bring into your project that allow you to just use macros that someone else developed a day ago, a week ago, maybe even a year ago.

So that's ways that we can work really asynchronously to help each other have better tooling and better macros so that we can more quickly develop data products for our organization. So ultimately macros are going to do, they allow us in analytics to work like software engineers do when they build applications.

#### cents_to_dollars macro

Extracted captions from video: cents_to_dollars macro

Welcome back, everyone. In this video, we are going to create our first macro. So we have this model, stg_payments here. We're converting the amount column from cents to dollars.

So you can imagine if we're working with the data source that stores everything in cents, you might end up writing this SQL over and over again and repeating it in a lot of different places. So we have an idea. We're going to abstract it into a macro and replace this logic with a call to that macro instead. It's important to note very quickly that macros are actually a feature of Jinja.

They're similar to a function in Python. If you're looking for documentation on this, there's some docs in the dbt docs. We have documentation on Jinja and macros, but there's also documentation on the Jinja, documents as well. So we can see here what a macro is.

They are comparable with functions and regular programming languages. So to start we need to first create a macro. So we're going to expand the macros folder. Click our three little dots create file.

We're going to name this cents to dollars SQL. now to start a macro, we need the macro tag then you need the name of the macro, cents to dollars and then you need parentheses. Now if we were going to add any input parameters, this is where we would put them. For now, we're going to leave this blank.

Now that we have our start macro tag, we also need an end macro tag. This should seem similar to your end if statements that we have seen in previous videos. going to go back to stg Payments and I'm just going to copy the amount divided by 100. I'm just going to paste it as it is.

And let's click save. now I want to call this macro in stg Payments, right where I have amount divided by 100. So I'm going to do my double curly and cents to dollars. So you can see that the shortcut came up there and I just click tab and it populated my macro call.

Going to click Save. All right, so I want to test to make sure that this looks correct. So I'm going to click compile. All right, we can see here we get exactly what we had before, but we have a new line, right here and we have some extra white space.

If you remember in previous videos, we can get rid of that by actually adding these little minus signs next to our percents. So I'm just going to try this. And let's go back to stg Payments and let's click compile again. All right, looks good.

This is exactly what we had before. Okay, but we have one problem here. Let's go back to cents to dollars in this macro. We hard coded this column named amount.

But what happens if we go into another model and maybe the field is payment amount, it could change. So we want to be able to pass through our column name then I want to actually reference that right here. So I need my double curly column name. Let's click Save.

Okay, let's navigate back to stg payments. Now I want to pass in that column amount. To do that, I need my double quotes and the column name. Now the reason for that is if I don't add the double quotes, it will be looking for a variable called amount.

We want to tell the dbt column compiler that this is actually a column. So let's click save and let's click compile. This looks like exactly what I want. All right, what if this field was maybe called payment amount, Click save and let's click compile.

We can see here. As long as I pass through the correct column name, it will compile. Let's change it back to amount, because I know my column is named amount. Now say I maybe want to round this amount.

Let's go back to my macro and take a look at it. Right now I'm only dividing by 100. Say I want to round this. I'm going to add the rounding function and then I'm going to add two decimal places.

Let's click Save. Let's go back to stg payments. Let's click compile again. Now I have my round function to two decimal places as my amount.

But say we want to be able to have the user input how many decimal places we are rounding for. Well, I can say decimals equal to 2. This means that I can input a value for decimals, but my default will be 2. So if the user doesn't pass anything in, it will default to 2.

Now I want to reference this decimals input value. So I'm going to use my double curlies to do that. Let's click save. All right, so now if I compile, let's think about what my default will be for the number of decimals I'm rounding for.

If you said two, you're correct. Let's click compile and check it out. Awesome. Say I want to Change this to 4.

I would just input that in my macro call just like this. Now let's click Save and compile again just to test that out. Awesome. Now I have a reusable macro.

But to remember what this macro is doing, people need to go into this macro, right? So it's not always clear. So we want to add some documentation so that it's clear for users what our macro is doing. I'm going to go to the macros folder and create a file.

I'm going to name this macros docs YAML. Okay, so to start this off, we're already familiar with YAML files for models and sources, right? And so in those situations we start our YAML files with a sources or a models tag. In this situation we're going to have a macros key And here I can put the name to my macro.

Cents to dollars. Okay, Now I can add a description and let's say a macro that converts dollars to cents and rounds to the user input decimal places or two if none is provided. Okay, and now I can add an arguments tag. Now here's where I want to put what columns or values are being passed into the macro.

So first I have column name and this is a type. We can add the type. This would be a string. Then I want to add a description.

Let's say the name of the column you want to convert. And now I'm going to add, another column and that was decimals type, integer description, let's say number of decimal places defaults to two and let's click save. This will be really helpful for when users might want to use a macro. But they don't want to go sort through, look through the code.

They can come to the documentation so they can very clearly read through in user friendly language what our macro is doing. Let's navigate back to this macro. Now macros are really useful for when you're repeating code in a bunch of places and you can make a function to just reuse that code. That way, if you ever have to make changes, instead of changing it in 5, 10, 15 places, we're only changing it in one.

So that's the benefit of a macro. Now the downfall, as I had mentioned, is people have to go into the code to understand it, maybe the documentation. It's not always clear what a macro is without actually navigating to the macros folder. Would I use this macro in my project?

Probably not. But this is really good for getting used to macros. There's some other really powerful examples that we will go through later, such as, fixing permissions for our warehouses in Snowflake. We're also going to look at macros.

We've looked at one that helps us union together, different columns. So these are some really awesome practicalities of macros. And I hope that you now understand what a macro is, and I hope you navigate to the documentation to read more about it.

#### DRY code vs. readability

Extracted captions from video: DRY code vs. readability

Great, you just learned about macros and you have this new superpower to add to your analytics toolkit, and you should. Macros are huge. They help you do things way faster in DBT with these though, there's an important trade-off to consider macros. Ultimately allow us to write dry code dry sending forward.

Don't repeat yourself. Very common in other programming languages like Python, Ruby, Java script, what have you. So with this, we can be tempted to take our 200 line file abstract away, 50 lines to one macro, another 25 lines to another macro. And then what ends up happening is a lot of our model is a lot of macros that are not very human readable.

I've seen some out in the wild where a single model is just a macro and there's some trade-offs here. Right? So that is very dry code. Definitely gets a 10 and a 10 on that scale but it's not very human readable.

When someone opens that model, it's hard to know what's really going on there. So as you work on your dbt project, think about like the sliding scale between dry code and human readability. You want to be somewhere in the middle so that when I push things into our project or you push things into our project, we can read each other's work and we can continue working on that in a productive way. Shouldn't have to spend 30 minutes to understand a model.

We want that to be quick so we can get in there, fix things, adjust things, improve things as needed. So really important to consider as you write more code is make sure you're writing code so that it's maintainable over time, because you're inevitably going to need to come back in a week in a month in a year to edit that model that you're working on today. So all this is to say macros are incredible, but just be careful with how much you use them throughout your project.

#### Practice

## Practice

Using what you've learned in this module, complete the following in your dbt project:

### Try it Yourself

Follow the video on the cents_to_dollars macro:

- Build a macro called cents_to_dollars.sql
- Leverage this macro in your model stg_payments.sql
- Check out the limit data in dev macro video and implement this in your project.*

### Extra Credit

Find another creative way to use a Macro in your project.

*Note: The default target name set up for each dbt Cloud project is default. To make the example in the video work for you, you have two choices.

- Change the code in the macro to if target.name == 'default'.
- Change the target name of your project to dev. Click on your profile image in the top right-hand corner and select Profile. On the left-hand navigation menu under Credentials, click on the name of your project. Then click on the Edit button. For the Target Name field, change default to dev.
- Read more in the docs here: [https://docs.getdbt.com/docs/dbt-cloud/using-dbt-cloud/cloud-setting-a-custom-target-name#dbt-cloud-ide](https://docs.getdbt.com/docs/dbt-cloud/using-dbt-cloud/cloud-setting-a-custom-target-name#dbt-cloud-ide)
- Shout out to @Leo Folsom for suggesting this be part of the practice section with clear directions on how to update target names!

#### Exemplar

# Exemplar

	macros/cents_to_dollars.sql

	{% macro cents_to_dollars(column_name, decimal_places=2) -%}
    round( 1.0 * {{ column_name }} / 100, {{ decimal_places }})
{%- endmacro %}

	Refactored stg_payments.sql

```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    -- amount is stored in cents, convert it to dollars
    {{ cents_to_dollars('amount', 4) }} as amount,
    created as created_at
from {{ source('stripe','payment') }}
```

#### Review

# Review

	## Macros

	**Macros** are functions that are written in Jinja. This allows us to write generic logic once, and then reference that logic throughout our project.

	Consider the case where we have three models that use the same logic. We could copy paste the logic between those three models. If we want to change that logic, we need to make the change in three different places.

	Macros allow us to write that logic once in one place and then reference that logic in those three models. If we want to change the logic, we make that change in the definition of the macro and this is automatically used in those three models.

	## DRY Code

	Macros allow us to write DRY (Don’t Repeat Yourself) code in our dbt project. This allows us to take one model file that was 200 lines of code and compress it down to 50 lines of code. We can do this by abstracting away the logic into macros.

	## Tradeoff

	As you work through your dbt project, it is important to balance the readability/maintainability of your code with how concise your code (or DRY) your code is. Always remember that you are not the only one using this code, so be mindful and intentional about where you use macros.

	## Macro Example: Cents to Dollars

	**Original Model:**

```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    -- amount stored in cents, convert to dollars
    amount / 100 as amount,
    created as created_at
from {{ source(‘stripe’, ‘payment’) }}
```

	**New Macro:**

```
{% macro cents_to_dollars(column_name, decimal_places=2) -%}
round( 1.0 * {{ column_name }} / 100, {{ decimal_places }})
{%- endmacro %}
```

	**Refactored Model:**

```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    -- amount stored in cents, convert to dollars
    {{ cents_to_dollars(‘payment_amount’) }} as amount
    created as created_at
from {{ source(‘stripe’, ‘payment’) }}
```

#### Knowledge check-macros

## Packages
<a id="packages"></a>

### Installing packages
<a id="packages-installing-packages"></a>

#### Learning objectives

# Learning objectives

- Explain the role of packages in a dbt project.
- Install a package from [hub.getdbt.com](https://hub.getdbt.com/).
- Use models and macros from a package.

#### What are packages?

Extracted captions from video: What are packages?

So now we're going to talk about packages. You're inevitably going to ask yourself while working in dbt, like someone's definitely written this, right. Or someone's figured this out, and you're probably right. This is where packages come in.

Packages are a way to import models in macros into your dbt project so that you can leverage them in your own project. So from a modeling perspective, there's a lot of common sources that other people are using like Facebook ads. Snowplow or Stripe data. Someone's already modeled these at a really high level.

So you can import a package for those sources and then instantly model those in your own dbt project. Also from a macro perspective are really popular packages, dbt utils, and there's a lot of individual macros that you can use to level up your project. One of my favorite is a date spine, and that allows you to create a really long table of dates with whatever difference you configure between each of the dates. Instead of having to manually write that up in a CSV or manually control that you just write it with a macro.

So there's a lot of great packages out there and you can find a bunch of them on hub.getdbt.com. That's managed by Fishtown Analytics, and that's the way, has all the directions there for how to bring in packages to your project. but you can also import them from GitHub directly. And in this module, we're going to cover how to bring in a package, but then also how to use models in a package and how to use macros in a package.

#### Installing packages

Extracted captions from video: Installing packages

All right, welcome back, everyone. Let's install some packages. Now, the way we add packages to our project is always by using a file called the packages YML that we create in our dbt project directory. Now, in order to learn about what packages are available for us to install and use, we can check out the hub site hub.getdbt

uh.com if we navigate to this site, we see tons of useful packages like dbt Utils, CodeGen, dbt Project Evaluator, and more. These packages are created by dbt and other members of the community, which are totally open source and completely available for you to install and use in your project. Now, if we navigate to any of these packages pages by clicking on them, we can see a code snippet that I would copy and paste into my packages YML with the most recent version, let's add a few useful packages together.

We'll start with dbt utils. Now, this package has a wide variety of macros that we can reuse in our project. There's a bunch of additional generic tests we can use and even macros that generate SQL for us. If we stay at the top of the page and copy this code, we can bring it into our dbt project YAML or our packages YAML.

So we want to copy and paste it there. Let's go back and navigate back to the Hub and Let's also add CodeGen. CodeGen is really useful for generating SQL code for our staging layer or maybe generating a YAML file to fill out documentation and tests. So let's copy and paste the most recent version.

Go back to our packages YAML. Now, there's a couple of ways to specify packages in the YAML file. So this, what we have here is called the package or hub site mechanism for installing packages. It's equally possible to go straight to the source.

So instead of using the package syntax that you see here, I could actually reference it via git. Now that's using SSH or HTTPs, as long as I have access to it from the GitHub account which I'm developing here. Let's change dbt codegen to use the HTTPs. So let's navigate back to the Hub and let's click on this little GitHub icon and it should take us to the GitHub, account for CodeGen.

So in this little green code button, I'm going to navigate to HTTPs and copy this link. Let's go back to our project and remove this reference and paste it here. Now, instead of version I need revision here, I can name the branch I want to use. Let's navigate back to the codegen GitHub and see we want to use the main branch.

I need to save this. There's one more option. The last option, is if we want to install local subdirectories as projects, this can be any relative path relative from the dbt project YAML relative to the packages YAML that we're writing in. In this case, you can see here that I have a project called Subproject and it has a dbt project YAML.

Okay, so here I want to label local and the name of the folder. So sub project and let's click save. Now this is nice if you have projects that are doing slightly different things, but you still want to version control them all together in one repo. This can also be a nice way to test out project inheritance if you yourself are developing packages.

So now, once we've saved this and added all the packages that we need, I'm going to come down to the command bar and run dbt deps. This stands for dbt Dependencies. This will go through the packages YAML file, validate all the code that I've entered, clone and install all of the dependencies I need in order to run my project. Great.

Now we're actually ready to use these packages. So move on to the next video for more.

#### Packages with macros

Extracted captions from video: Packages with macros

Today we're going to spend some time looking at packages with macros in them. The most famous and most widely used example is dbt utils. So first things first, we need to make sure that this package is in our packages YAML. So let's copy this code in case we need it.

Let's go back to Studio and let's go to our packages. YML. And I see, I already have it in here, so I'm good to go. So the next step.

Is running dbt deps. It's installing packages. That we have defined in our packages YAML and we are good to go. All right, so let's navigate to the dbt utils package GitHub.

Page. So we'll go back to the package, hun. I will click this link, okay? And then I want to find a very useful macro called the Date Spine macro.

So I'm going to go to macros. Going to, expand SQL and I'm going to navigate to date spine. Okay, so this macro is going to create a table full of rows of dates within a range defined by a start and end date. We can see that in our input for the macro.

Okay, so I want to actually use this macro. So if I go back to the package hub and I find the date spine code, here it is. I can click on this and it will give me some boilerplate code that I can use. So I'm going to copy this, going to create a new model file named datespine.

SQL. I'm going to paste this code in here. I'm going to save it. Let's click preview and see what that data looks like.

Okay, all of the logic that's being applied here and that's creating this table of days for me, is defined inside the dbt utils package. Now, the only thing I've done is define that that package is a dependency in my packages YML file. To look a bit into the magic here, we can click compile. Let's compile the SQL and we can see that it's running some pretty tricky code.

Just take a look. This is the most performant way to generate a series of numbers and dates on databases where Union all Union all Union all doesn't perform super well. This complexity has been abstracted away from us. We get to just benefit from the output instead of checking the macros folder in our own projects to see the source code for this, we would actually need to come to the open source package, in this case dbt utils.

Find the macro like we did before and take a look. So this is everything that's going on in it. We can see that this macro calls some other macros we can see get intervals between. We can see.

Generate series and so on, so on. So let's navigate back to studio. And I've already created a model called Customers Daily Summary. So I'm going to click preview and just take a look at this data.

We can see here that it's one row per customer per order date and then it's the number of orders that they had on that day. When we have this kind of group table or a many to many mapping table, we have the need for a primary key. In this table. The primary key is a combination of customer ID and order order date.

Well, there's a handy dandy dbt utils function for that called generate surrogate key. So let's navigate to the package hub and generate surrogate key is right here. And this is the. The context to, Actually call this macro.

So let's copy that, bring it into our model, and paste it as. Primary key. It takes a list of columns and splits. A unique hash that will always be the same when those columns are the same.

All right, so let's. Edit this to include. Customer ID and order date, and I'm going to remove these brackets. Okay, so let's click preview.

Let's see what this data looks like. Let's see what this macro generates for us. And here we go. Totally unique identifier for each row.

Something that we could feed maybe into a unique test or used to filter on these rows later. So now let's compile the SQL and take a look at what's going on behind the scenes. Okay. And in this case, we see the Snowflake MD5 function combined with a couple of casts, some concats.

Okay. One of the nice things about packages like dbt utils is that they are defined in such a way to work across databases. An example of this is the concat function. So we have a default and then we have a implementation for each of the databases that we would be working on, for example, BigQuery or Snowflake.

And this is what surrogate key is actually using. So this means that you can write dbtutils generatesurrogatekey and run it on Snowflake or redshift or bigQuery, etc. Etc. And it'll just work.

Could we write this logic ourselves and define this in our macros folder and get the Jinja right? Probably we could do that, but there's no sense in doing it when there's already some open source code that does the thing we need to do. All right, in the next video we'll talk about packages with models.

#### Packages with models

Extracted captions from video: Packages with models

we just talked about packages with macros. But packages are not just limited to macros that you can reuse in your project. They can have all sorts of things like models, seeds, analyses, etc. In this case, we are going to try installing a package that has Models, specifically models about Snowflake spending.

Now, this is a package that GitLab created. This is on the dbt Hub site. And if you click this GitLab link, it will take you to the GitLab page. Let's go back to the hub and copy and paste this code to bring it into our packages.

YAML, you can see here I already have it, so I'm going to hit save. Now let's run a dbt deps, make sure that our package is installed. Awesome. We're good to go.

Now, there are frequently with packages that have models in them a couple of extra steps that you need to do because maybe those models select from or depend on certain sources. That's certainly true, of packages like Snowplow, Facebook ads, a lot of fivetran packages which will build on top of common data sources. Let's go back to the dbt package hub and scroll down a little bit. You want to make sure you read the readme first when you're getting started.

Now it's telling us to do a few things. I already read through this readme and one of the things we need to do is create a CSV called Snowflake Contract rates. Now if you search for this in the GitLab hub for this package, you will find this. And then you just need to open a seed and paste these values in there.

Now, to seed this, we need to run dbt seed. So these are all prerequisites that we need. Right. And we are good.

All right, now I'm going to run a dbt build. I'm just going to exclude one model because it's long running. Oh wow, look, I have all these new Snowflake models. Snowflake Query History Snowflake Warehouse Metering Snowflake Contract Rates Snowflake Warehouse Metering xf.

Now, where's the code defining these models? It's not in our own models folder. We can see here, not in there. It's actually inside dbt modules Snowflake Spend.

We can see these models in here. It's inside the package. If we wanted to, we could go find the source code for those models in that, GitLab page that we just saw. These models will show up in our data warehouse when we run them.

And they will also show up in our generated documentation site. So to do that, my dbt build is still running. I'm going to cancel that. What's the command we need to run for that local doc site?

Does anyone remember? Okay, so let's run a dbt docs generate. It's running. We're looking good.

Taking a second to build up our dock site. Awesome. We're good to go. So now we can click this little docs button to take us to our generated doc site.

All right, now we can see here that we have Snowflake Spend project. So let's open that. Let's look at the models. Let's take a look.

Let's look at our dag. We can see that these models even show up in our dag. So that's really awesome. Now because these models don't actually exist in our project, if we wanted to configure them, we would need to do all of that configuration in the dbt project YAML.

So let's navigate back to our dbt project YAML. And this is also on the GitHub page or dbt hub page. So Snowflake Spend enabled. True.

So I've already got that in here. I'm just going to uncomment it and then I can save it. One last thing. If you want to run or test only the models from a certain package, you can type the name of that package.

Or if you'd like to be extra explicit as I do, I like to say package colon and then the name. So I'm going to run a, dbt build dash dash select right package Snowflake Spend and let's try that. Awesome. We're good to go.

So now you just learned about packages with models. If you want to learn more, navigate to the dbt package hub.

#### Practice

## Practice

Using what you've learned in this module, complete the following in your dbt project:

### Try it yourself

Follow the video called Packages with Macros to:

- Add the dbt_utils package to your project.
- Use the date_spine macro to build a data spine model in your project called all_dates. This model should list every day in the year 2020.
- Use a config block to materialize all_dates as a table. (The default materialization will be a view)

### Extra credit

Find another creative way to use a Macros from the dbt_utils package.

#### Exemplar

# Exemplar

	**packages.yml**** in the root directory of your project**

```
packages:
  - package: dbt-labs/dbt_utils
    version: 0.7.1
```

	**models/all_dates.sql**

```
{{ config (
    materialized="table"
)}}

{{ dbt_utils.date_spine(
    datepart="day",
    start_date="cast('2020-01-01' as date)",
    end_date="cast('2021-01-01' as date)"
   )
}}
```

#### Review

# Review

	## Packages

	**Packages** are a tool for importing models and macros into your dbt Project. These may have been written in by a coworker or someone else in the dbt community that you have never met. Fishtown Analytics maintains a site called [hub.getdbt.com](https://hub.getdbt.com/) for sharing open-source packages that you can install in your project. Packages can also be imported directly from GitHub, GitLab, or another site or from a subfolder in your dbt project.

	## Installing Packages

	

		- Packages are configured in the root of your dbt project in a file called packages.yml.

		- You can adjust the version to be compatible with your working version of dbt. Read the packages documentation to determine the version to use.

		- Packages are then installed with the command dbt deps.

	

	**Example: Adding dbt_utils and snowflake_spend to your dbt project**

	**packages.yml**

```
packages:
  - package: dbt-labs/dbt_utils
    version: 0.7.1
  - package: gitlabhq/snowflake_spend
    version: 1.2.0
```

	dbt deps

	## Using Macros from a Package

	

		- After importing a package, your dbt project now has access to all the macros from that package.

		- The documentation of that particular package is the best place to learn how to use those packages.

		- When you want to reference a macro in a package, you must reference that package and then select the particular macro. (e.g. dbt_utils.date_spine)

	

	**Example - The following snippet will reference the dbt_utils package and use the date_spine macro.**

```
{{ dbt_utils.date_spine(
    datepart=”day”
    start_date=”to_date(‘01/01/2016’, ‘mm/dd/yyyy’)”,
    end_date=”dateadd(week, 1, current_date)”
    )
}}
```

	## Using Models from a Package

	

		- After importing a package, your dbt project now has access to all the models from that package.

		- The documentation of that particular packages is the best place to learn how to use those packages.

		- Those models will then become part of your dbt project. They will be build when you run dbt run and can be viewed in documentation as part of your DAG and text-based documentation as well.

	

	**Example - The following DAG below shows all of the snowflake_spend model in gray**

#### Knowledge check-packages

## Advanced Jinja and Macros
<a id="advanced-jinja-and-macros"></a>

### Advanced Jinja and macros
<a id="advanced-jinja-and-macros-advanced-jinja-and-macros"></a>

#### Learning objectives

## Learning objectives

- Build a macro to grant permissions using the run_query macro, log macro, and target variable
- Build a macro to union tables by a common prefix using the execute variable, agate file types, and get_relations_by_prefix macro
- Build a macro to clean up stale models in the target schema using the information schema

#### Resources:

For this chapter, we have organized all the code in a public GitHub repository.  Code snippets will be included below each video.  If you prefer viewing code in GitHub, checkout the repository here: [dbt-learn-jinja repository](https://github.com/dbt-labs/dbt-learn-jinja)

#### grant_select macro

#### grant_select macro code:

```
{% macro grant_select(schema=target.schema, role=target.role) %}

  {% set sql %}
  grant usage on schema {{ schema }} to role {{ role }};
  grant select on all tables in schema {{ schema }} to role {{ role }};
  grant select on all views in schema {{ schema }} to role {{ role }};
  {% endset %}

  {{ log('Granting select on all tables and views in schema ' ~ target.schema ~ ' to role ' ~ role, info=True) }}
  {% do run_query(sql) %}
  {{ log('Privileges granted', info=True) }}

{% endmacro %}
```

	#### Resources:

	

		- [grant select macro code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/grant_select.sql)

		- [run_query macro documentation](https://docs.getdbt.com/reference/dbt-jinja-functions/run_query)

		- l[og macro documentation](https://docs.getdbt.com/reference/dbt-jinja-functions/log)

		- [target variable documentation](https://docs.getdbt.com/reference/dbt-jinja-functions/target)

Extracted captions from video: grant_select macro

In the previous videos, we saw how Jinja and macros can be very useful to enhance our SQL writing, making it more dynamic and less repetitive. We can also write macros that actually execute SQL against our Warehouse in a programmatic fashion. There are a number of dbt specific Jinja functions that I'll go over in a moment that allow us both to send SQL down to the Warehouse, execute it, and optionally return that data from the Warehouse and use it within our code. For the next couple of videos, we're going to go over a handful of these specific functions and learn how to write these higher level macros.

To illustrate this example, let's create a macro that grants the select privilege on all tables and views in a specified schema within our Warehouse. In this case, this is going to be a snowflake specific example, but permission granting is something that happens in all data warehouses. So to start, I'm going to create a new file inside of our macros folder. Let's name it GrantSelect SQL.

And I'm going to start by using the keyboard shortcut for macros to give us our end macro tag and Begin macro tag. And let's name this Grant Select. Let's click Save. As I mentioned a moment ago, DB comes with a lot of specialized Jinja functions built out.

To help with some of these use cases, I'm going to go over to the documentation site here. This is where I start most of the time that I'm developing with these functions. And underneath the reference tab, underneath Jinja Reference, there's a page called dbt Jinja functions. We can see that here we scroll down, we can see a ton of specific functions built for higher level macro writing.

Now, to start this exercise, we're going to call attention to the Run query. Okay, let's scroll down. Let's take a look. This, as it says in the documentation, is a convenient way to run queries and fetch the results.

It is a wrapper around the statement block right here, which is more flexible but also more complicated to use. So let's see if we can use this together inside of a macro. Let's go back to Studio. Okay, so the first thing that we need to do is actually define the SQL statement that we want to run.

So we need our curly percent sign and let's say set our variable, so set SQL and we need our end set. This operates the same as a single line set statement that we saw in our Jinja Basics video. But here I'm able to write multi Line string definitions, which is helpful because we want to do a few things at once here. Now, the first thing we need is a grant usage on schema and we're going to pass this in.

So we need our double, curlies schema and we're going to add this to our list of arguments. So whatever schema is passed, we want to grant the usage privilege on that schema. Now we want to grant that to the role, whichever role we want to specify here as well. So two double curlies, role, oops two and semicolon.

And let's add rule to our arguments as well. Okay, so this is step one. Step two will be to grant the select privilege on all tables in this schema that we pass to the role and then one last statement for all the views. Okay, so let's do that.

So grant select on all, tables in schema Schema to oops. And I forgot role up here to roll. Roll. Okay, so we have one statement for the tables.

I'm just going to copy that oops. And I got an extra curly oops. Okay, and let's change this to Awesome. So I'm granting usage for a schema to a role.

Oops. I'm also missing a double curlies here. I'm also granting select on all tables in schema to a role and for views in schema to the role as well. All right, looking good.

Now we're actually going to implement using that Run query Jinja function. What we're going to do is wrap this in a do, which is a jinja call that will execute some sort of code. It will not print anything, but it will do whatever sort of operation we're going to define. Oops.

So our curly percents do and let's say run query. We want to run our SQL. Okay, since this really isn't code that I'm going to want to put inside of a model, that's something that's going to be run on its own. At the moment, this macro is going to require a schema and a role to be specified to do anything useful.

Otherwise, we're going to end up with empty space templated into each of these query statements. So one thing that I want to do is specify here is the target variable. This target variable is a specialized dbt jinja function that contains information about how dbt is currently connected to your warehouse. For those of you on the cli, this will correspond to the keys and values you specified in your profile.

So let's go back to the dbt Jinja Functions and let's find target. For those of you on dbt Studio, we set these inside of your individual user profile for development or inside, of an environment configuration for prod or staging or any other environments that you have. And this is where you set some of these values for the name of the target that you're building towards. And you can see for each of these adapters there are additional pieces of information that get written to this target variable.

It's basically just a dictionary with keys and values that correspond to how dbt is connected to your warehouse. So I'm going to go back to Studio, I'm going to open a scratch pad, and I'm going to just, say target oops and I can't spell today target dot name. Just to see what we've got, let's also print target rule and let's print target schema oops and let's click, compile. All right, so now we see the values that are specified here when we hit compile.

So the name of this target is my default target, which is specified in my profile. Again, the role that I'm using specified is transformer. And then the schema, for all my tables and views is dbt. And then your first initial last name.

Now, the reason I bring this up is because this exact macro is going to be useful to be executed after a dbt run, and it's going to have to be specific to each user who's executing a dbt run here. So let's go back to our grant select macro and we need to give the schema a default. So let's say target schema and for the role we want to do target role and let's save that. So what we can do is specify these as the default arguments so that anytime a user executes this without specifying any additional arguments, what they're going to get is the usage of the schema that they're building to and the select privilege on all of the tables and views that are building into that schema.

So if I run this right now without any additional arguments, we should see grant all these privileges to the role transformer on the schema DBTJ bushby's. Now, because we're not going to actually use this code inside of the context of a model, I just want to call this macro independent of anything else. So what we can do is a dbt run operation. So I'm going to type dbt run dash operation and then the name of my macro.

This is a specialized command that allows us to call a single macro and execute whatever code is written inside of that macro without having to do a full dbt run. So what I'm going to do here is just run this command. Oops. And I need to say not grant macro, say grant.

Select. So dbt run operation space and then the name of your macro. Awesome. Let's open up the logs.

So we don't see anything here, but if we open up the details, we should be able to see macro Grant select running Grant select on all tables in schema dbtj bushby's to role transformer Grant select on all views in schema dbt JBushby's to role transformer. But what if we wanted to know what was happening without having to go to these full details here? That brings me to another additional function. So let's go back to the Jinja functions.

Now this one is called log. Let's scroll down a little bit. So logging is a very useful way to kind of see under the hood as things are running inside of a dbt project, especially as you start to develop more and more complex macros. It looks kind of like a simple print statement, so we can specify some sort of string and any additional arguments.

A tilde in Jinj is concatenation. So let's see if we can use this to get a little bit more context into exactly what our macro is doing here. So let me go back to my macro. So before we actually execute the query, I want to log something.

So let's say, oops, I need double curlies, log, parentheses, single quote, and let's say granting select on all tables and views in schema. And now I want to concatenate. So I need that tilde. And let's say target schema.

And I also want to say what role I'm concatenating to. So let's do tilde single quotes to role tilde role. So I'm going to save this. The second argument of the log function is info.

If I specify info is true, just like this, I'm going to get the message out in the actual terminal output as well as the detailed logs. If this is false, which is the default, it's only going to go to the rich logs. So then after I print this sort of summary statement, we're going to execute the query. And now finally, we'll log some sort of a success statement right after this.

So let's say log proves granted and let's say info equals true. All right, so let's do that. Let's run that run operation again and let's take a look at the logs. Awesome.

Let's go back and let's take a look here. We can see here that my logs, the log statements that I had said printed out in our detailed logs. That's really helpful. Now we have a macro that can dynamically generate permissions for any user who is building to their target schema and their target role.

We have a little bit of an understanding of how to make the visibility into this macro a little bit cleaner and easier and also how to execute a query against our warehouse. But now, before we wrap up, let's document this macro. So in our macros folder, let's go to our docs YAML. Now we can remember here that to start out our documentation for macros, we need that macros block.

Now I'm going to add a name tag. I'm going to say grant select and I need my description. And let's say a macro oops that grants select privs on schema on let's say target oops.schema to target role unless otherwise specified.

Okay, and now we know we need the arguments tag. And now a name tag. And let's say schema type string. Let's say description schema we want to grant privson by default is our target schema.

Okay, now I'm going to add another argument and this will be role and the type is a string again. And let's say my description role we want to grant proofs to by default is our target role. Awesome. So we just created a macro that helps us, grant select to views and tables in our default schema.

Our target schema to target role we learned how to log to the output statement and we also learned how to document our macro. Hopefully this is useful and you can use this in your current dbt project.

#### union_tables_by_prefix macro

#### union_tables_by_prefix macro code:

```sql
{%- macro union_tables_by_prefix(database, schema, prefix) -%}

  {%- set tables = dbt_utils.get_relations_by_prefix(database=database, schema=schema, prefix=prefix) -%}

  {% for table in tables %}

      {%- if not loop.first -%}
      union all 
      {%- endif %}
        
      select * from {{ table.database }}.{{ table.schema }}.{{ table.name }}
      
  {% endfor -%}
  
{%- endmacro -%}
```

	#### union_tables_by_orders_prefix model code:

```
{{ union_tables_by_prefix(

      database='raw',
      schema='dbt_learn_jinja', 
      prefix='orders__'
        
      )
      
  }}
```

	#### Resources:

	

		- [union_tables_by_prefix macro code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/union_tables_by_prefix.sql)

		- [execute variable documentation](https://docs.getdbt.com/reference/dbt-jinja-functions/execute)

		- [agate file types documentation](https://agate.readthedocs.io/en/latest/api/table.html)

		- [get_relations_by_prefix documentation](https://github.com/dbt-labs/dbt-utils#get_relations_by_prefix-source)

Extracted captions from video: union_tables_by_prefix macro

In the previous video, we learned how to execute SQL against our warehouse using Jinja. We've already seen how this can be a really useful tool for doing simple things like managing permissions on objects. But we could probably also imagine how this could be a very useful tool to actually use the results of a query to build out our SQL code dynamically. To explore this, we're going to put a very simple example together that's going to execute a SQL query, returning the results to our Jinja context, and then use those results to template a very simple SQL query.

So to start, I'm going to create a new macro. We will call this template example, SQL. I'm also going to create a model file as well. We can just name this example.

So to start in our macro backup template example, we need our macro block, so we can just use the shortcut. Let's make sure the name is the same template example and let's click save. We don't have any arguments just yet. We'll get to that later.

So to start, I'm going to create a set block so we can use our shortcut again. And let's have our end set as well. Going to just add some extra lines so it's a little bit easier to read. Okay, so just like last time around, we want to define a query that I want to run against the warehouse.

So I'm going to call this query This is just going to be a very simple example. So we will do select true as, boolean, since we actually want to run this query and then use the results in a template in a SQL query, which I'm going to write in just a moment. We can use a specialized variable called execute. And I'm going to jump over to that documentation.

We can see Execute is a Jinja variable. Scroll down a little bit. Right here we're using it. This is the Jinja documentation.

So what exactly is Execute mode? When dbt is an execute mode, the Jinja variable returns true. So under the hood, when you execute a dbt compile or dbt run, there's basically two phases of compiling your project that dbt is going through. The first thing is to build the sort of structure of the project inside of a manifest, the relationship between each of the files.

No SQL is run during that phase, so execute is equal false. The second is when it actually compiles the code within each of those models. And in some cases, SQL is run during that phase. So the variable execute equals true.

Since we're going to tell dbt to run a SQL query before it compiles. We want to make sure that we do that when the execute variable returns true and SQL is able to be run. So in contrast to last time when we were running a SQL query just as an operation, we're going to need to specifically specify a new if block here for if execute. So let's go back to Studio.

Going to need a new if block. So I'm going to use my shortcut. So if execute, then what we want to actually do is run the query. And in contrast to last time, we're going to do a set result equal to the results of the run query and I'll show you how to do that.

So let's, we need a. Oops, let's use our shortcut set. So I will set results equal to. And I will do run query and I'm going to run my query.

I'm going to jump back over to the documentation for run query. Let's remind ourselves that the RunQuery macro is a wrapper. It runs queries and fetches the results and returns a table object. So if we follow this documentation right here, we will be taken to the Agate documentation, which is the class that dbt uses to manage the results of the run query macro.

We can see here that there are some properties such as columns, and rows in addition to somewhere on here there's a values method that we can use on either of these properties. So if those of you out there have ever used data frames in Python before, this is a very similar data object. We can assess the results of this query as a table. And so since this is just a single column that I'm returning with one single value, I'm going to say we are going to use the dot columns methodology.

So let's go back to Studio and in the run query we need to say the dot columns and I also want to grab the value. So let's say values. We'll use the values methodology here. Okay, great.

Let's save. The reason why I'm using the zero here is because we want the first value location, the zero index. We're just trying to grab the first value here. I'm also going to add a log here just for best practices.

And if you remember from the last video, we need info equals true. So let's say log SQL results base and my concatenate results info equals true so that it outputs. So we want to take the results of a query which we just got by doing the run query and actually put it in some other SQL statement that is going to become the code that is run when the model actually is executed against the warehouse. So we're going to do select results.

So we're going to use the gingivalue as is real. Oops. From a real table. This obviously is not a real example.

Let's just go ahead and save this. Just notice here that we don't have white space controls, so we probably will not see a perfectly rendered result here. Let's go to our model and let's call the template example macro and let's compile. We can see here we get the results from our query.

Great. So now we are able to run a query against the warehouse, execute that query, get the results inside of a Jinja context, pull those out, and some sort of dynamic way to create a new SQL statement inside of our model. Let's do this one more time, but with a slightly more real example. So I'm going to save this model just for later.

I'm going to jump over to a SQL statement that I have prepared. We have a new schema called dbt Learn Jinja and we're getting some order information here. We have a table from Shopify, a table from Amazon. so let's check out our Amazon orders.

We've got two here. Let's check out our Shopify orders. See, we have two here as well. We want to be able to dynamically grab any table inside of the schema that starts with orders, underscore, underscore and union them together.

So we have a complete picture of all of the new orders coming into this new schema in our RAW database. One thing that I'm not going to do in this example is declare sources. You absolutely should, as I'm sure you've learned in previous sections. But for this use case of doing something a little bit more real, a little bit more dynamic, I'm not going to declare sources for each of these.

So let's create a new macro. So, and let's call this Union Tables by prefix. Okay, the first thing that I'm going to do is actually go over to the dbt Packages hub, pull this from another screen. Okay.

We're going to be looking at dbt utils. I highly recommend everyone installs this in their project. There's tons of useful macros inside of this package. There's one in particular here that I'm going to Call attention to and it is called Get Relations by Prefix.

If you click on the documentation here, you can see that this is going to return a list of relations that match a particular schema in prefix combo. If you pass this argument of the schema and some sort of prefix, it's going to return a list of relations that match those. So what's a relation? Let's hop over to the dbt classes documentation here.

We can see here that a relation is an object that dbt understands. It's one of the API objects inside of dbt that is used to interpolate schema and table names into SQL code with appropriate quoting. This is how dbt is able to understand the relationship between a file and in your project and an object in your warehouse. So what this macro returns, if we go Back to the GitHub, is a list of these relations and we can use relation.database,

relation.schema, relation.identifier or relation.name to get some information about where this relation lives. So effectively this is returning a nice usable variable that represents a table in our warehouse.

So I want a dictionary of these values of relations in my schema that I want to union together. The first thing that I'm going to do here is go back to Studio, I need to start my macro. Let's name it Union Tables by prefix. All right, we're ready to go.

So the first thing that I'm going to do is have my set block. Okay. I'm going to, set the set tables. So tables equal to the results of, the dbt utils get relations by prefix macro.

So dbt utils dot get relations by prefix. The good news for us is that this macro actually takes into account that execute variable that we talked about earlier. So we don't really need to worry about it ourselves. The logic underneath here will do the actual execute wrapping that we need and we'll be able to run this query as our models compile here.

So if we go back to the documentation, this macro takes a few inputs. We can see schema, prefix and database. So we'll need to add those to our list of arguments. We'll need database, we will need schema and we will need prefix.

We also need to add this to our macro call. So database equals database, schema equals schema, and prefix equals prefix. So now we have a list of relation objects. So you may have already thought that for when we have a List of things, oftentimes we are going to loop over that list.

So maybe for table in our list of tables or relation objects, we want to union them all together. As you may have thought already, when we have a list of things, oftentimes we're going to loop over that list. So. So four.

So we'll have a four. So for table in tables, then we want to union them together. So I need an if. So we'll use our shortcut and we'll do if not loop.

First we're going to add our union. That'll only happen on runs that are not the first. Okay, so after our if we will do a select star from, table database table dot schema, I'm going to, add my spaces so it's a little bit easier for you to read. Table dot name.

This is coming from our relation object and I want it to look a little bit nicer on the front end. So I'm going to add some white space controls. we can come back later and fix these. Let's create a model file.

Name it Union Tables Dot SQL. Okay, and I want to call that macro. I'm going to say Union Tables by prefix. And I need my database.

And that's going to equal raw. My schema, is going to equal dbt. Learn Jinja. And my prefix is equal to orders.

Let's save this. Let's compile and look at the code we get. All right, so we've got select star from our, Amazon orders. Union All.

Select all from our Shopify orders. And that's exactly what we were intending to do. Let's preview this and make sure the SQL runs. Okay, great.

We've got all four of our orders here, and the amounts and the order dates we need all together. So for those of you who have been around the block a couple of times, you may have noticed that this is an opportunity here for me to actually use the other macro in dbt utils. The union relations macro does exactly this and it takes care of any mismatch in columns. It's an excellent macro to use.

There's a lot of great shortcuts available in packages, so I would highly encourage you to look around and look for prior work before getting in too deep into macro writing. Well, now we know how to execute a query against our warehouse, return those results to Jinja context, use those results in some useful way, and end up with a model file that does some sort of dynamic behavior here.

#### clean_stale_macro

#### clean_stale_models macro code:

```sql
{#  
    -- let's develop a macro that 
    1. queries the information schema of a database
    2. finds objects that are > 1 week old (no longer maintained)
    3. generates automated drop statements
    4. has the ability to execute those drop statements

#}

{% macro clean_stale_models(database=target.database, schema=target.schema, days=7, dry_run=True) %}
    
    {% set get_drop_commands_query %}
        select
            case 
                when table_type = 'VIEW'
                    then table_type
                else 
                    'TABLE'
            end as drop_type, 
            'DROP ' || drop_type || ' {{ database | upper }}.' || table_schema || '.' || table_name || ';'
        from {{ database }}.information_schema.tables 
        where table_schema = upper('{{ schema }}')
        and last_altered <= current_date - {{ days }} 
    {% endset %}

    {{ log('\nGenerating cleanup queries...\n', info=True) }}
    {% set drop_queries = run_query(get_drop_commands_query).columns[1].values() %}

    {% for query in drop_queries %}
        {% if dry_run %}
            {{ log(query, info=True) }}
        {% else %}
            {{ log('Dropping object with command: ' ~ query, info=True) }}
            {% do run_query(query) %} 
        {% endif %}       
    {% endfor %}
    
{% endmacro %} 
```

	#### Resources:

	

		- [clean_stale_models macro code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/clean_stale_models.sql)

		- **Discourse:** [Clean your warehouse of old and deprecated models](https://discourse.getdbt.com/t/clean-your-warehouse-of-old-and-deprecated-models/1547)

#### generate_schema_name macro

Extracted captions from video: generate_schema_name macro

So far we have learned a lot about different applications of macros. One very common usage of macros is customizing databases and schemas. Let's think back to our dbt Fundamentals course. We know that our repository tells dbt what to write.

But how does dbt know where to write? By default, if you set our target database in schema, you are correct. Our target database and schema are defined in our connection for development. This is defined in our individual profile connection.

So we go to our name, we go to our profile and let's navigate to credentials and the project we are working on. And then we can see here we have our target database analytics. And my target schema is right here as well. DBTFirstInitial Last Name.

The concept of target database and schema means the default location for dbt to write. What if we wanted to customize this behavior? Let's start with customizing our schema. Let's quick hop into our project.

Okay, so let's pause for a moment and think where can we provide dbt a custom schema name at the folder level? If you said our dbt project YAML, you are correct. Let's scroll down. We can see here I have my models, my project name and then different, folders.

Let's open up my models folder. Here I have staging. Let's start with Jaffle Shop stg Customers. Let's build this and see where it builds to.

Going to expand this window. Okay, we can see here that this built to my schema DBTJ Bushbuys stg Customers. Let's navigate back to that dbt project YAML. If we wanted to customize this at the folder level, I would just add the folder name.

So staging and then I need a plus schema to tell dbt that's the configuration I want to change. I want to write to staging. Here I'm telling dbt for a specific folder where I want to write to using the configuration key of plus schema. Now if I wanted to do this at the model level, I could add a config block at the top of my model.

Let's see how that's done. Let's hop back into stg customers. Going to add a new line at the top of my stg Customers. I'm going to add a config block.

Now a config block is for telling dbt model specific configurations. So let's say schema and let's say staging. I'm going to save that using the dbt Project YAML. We tell dbt what schema our table should write to at the folder level.

But if we add it at the model level, we are overriding that behavior. dbt is taking the most granular setting and prioritizes that so we can go from project level configurations to folder level configurations and the highest level model level configurations. Let's see how this changed the behavior of where dbt is writing my staging models. Just going to remove that and we're just going to use the settings from the dbt project YAML.

Okay, let's go back to stg Customers and let's build Expand this. This wrote to dbtjbushpee's staging. But wait a second. I thought if I added a custom schema that it would write just to that schema.

So staging stg customers. Not exactly behind the scenes. DBTS macros handling custom databases and schemas. Let's take a look at the macro handling this scenario.

I'm going to scroll down a little bit. Let's try to understand this code together. As we learned earlier, the target schema is our default. We can see that in the first line.

Next we see an if statement, which we learned in an earlier video that this is a logical block. So let's hop through this logic. If there is no custom schema, use the default schema, which we're setting here as the target schema. Else.

So if there is a custom schema, use default schema, which we know is our target from above. Underscore custom schema. So this is a little bit different than just the custom schema. What if we want to override this default behavior for custom schemas?

We can simply add this macro to our dbt project to tell it exactly what we want to do. The way we do that is by copying and pasting this code. Let's go back to our project and let's add this macro in the macros folder. So create file.

And this is generate schema name SQL and I can paste this here. Okay, so now that we have the macro, let's practice customizing it. Let's say I want to write to just staging and not the default schema. Underscore staging.

Well, I can change this line here. We can change it to just custom schema name. So let's backspace this. Let's save this.

All right, let's test this out. We'll hop back to stg Customers and click Build. Let's expand our command window. We'll wait for it to build.

Awesome. Aha. Awesome. We can see here it wrote to staging stg customers exactly what we wanted.

Our customization worked. We can also do the same exercise using custom databases. Follow the link below in the docs to learn more.

#### Customizing schema by environment

Extracted captions from video: Customizing schema by environment

In the previous video, we learned how to add custom schemas and configure the behavior of our generator. Schema name macro. Great job. You are becoming a Jinja pro.

But my boss came back to me and we want to only write to the custom schema in production, not in development. This way my developers can all have their own schema in dev, but in prod, my staging objects are separated out. In other words, we want to write all of our objects to a different schema, per environment. For example, when we are in studio, we want to write to dbtfirstinitial last name.

So for me, that would be dbtjbushpease. But when we are in our production environment, we want to write that staging folder to the schema, stag staging. How can we have a dynamic schema name per environment? Hint, hint.

This may be an application for environment variables. With environment variables, we can have an object that stores different values depending on what environment we are in. So let's navigate to those docs we see here. By the definition, environment variables can be used to customize the behavior of a dbt project depending on where the environment is running.

Where means the environment. So we are going to use an application of these to customize this behavior even further. So let's navigate back to Studio and let's go to our orchestration. We'll go to environments.

We will go to environment variables. Okay, so for environment variables, we're going to start by naming one, creating one called dbtenvnven. Now, you can see here that we can hold a different value per environment. Let's make our development value dev and, our prod one prod.

We will come back to this environment variable later. Let's click save. And now it will require you to restart all of the IDE sessions. That's okay.

Now, before we dive in too deep, we're going to review what we did in the previous video. We modify the Generate schema name macro. All right, let's hop back to Studio. We need to restart the ide.

If you're following along, you should have to do the same thing. Awesome. So let's hop into our generate schema name macro. So in the last video, we customized this to say if we do not have a custom schema Use our default schema, else use my custom schema.

But because of my boss's request, I need to edit this to add a consideration for my environment. The perfect application for this is for environment variables. Let's go to the docs So let's use dbtenvname. This doc tells us how we can use the, environment variables Jinja function.

So we're going to add this to our code. We can see it right here. Let's scroll down a little bit. Here you can see the precedence of the different ways you can set environment variables.

So feel free to follow the link to the docs and read more about that. Okay, so we're going to add a line, to use our environment variable. Just going to copy this for the simplicity of time. Okay, so from the docs we saw that environment variable was in double curly brackets.

Now, because we are in the Jinja context, we don't need those. So we can just use the environment variables function on its own. So I'm setting a variable env to the value of my environment variable depending on what environment I am in. Okay, let's pause.

Let's think about what logic we are going to use. Well, my schema is compiling to my custom schema even in dev, as we saw in the previous video. But I still want developers to be able to use their personal target schema set up in their profiles connection. Okay, so maybe I can say, well, if I'm in production, then I want my custom schema and if there's a custom schema, let's think.

If I don't have a custom schema or my environment is equal to dev. So does this work? Let's think if I do not have a custom schema or I am in dev, use the default schema, else it would mean I have a custom schema or I'm in prod. Use the custom schema.

All right, we're on the right track. But what if I have a staging environment? Maybe I could say or the environment is not equal to prod, because if I have another environment that we set up later, it would not catch that. Great, this makes sense.

Let's take a moment to look at this code. How can we confirm that this macro override is going to work as intended. Well, let's navigate back to our staging customers model and see if our schema, is our personal schema still? Let's click build.

I'm going to expand this. All right, let's see where built. Awesome. We know this works in dev.

I'm, still building to my custom target schema, dbtfirstinitiallastname. How can I test if this is working in prod? If you said that I need to commit these, changes and merge back to main and also run a job in production. You are right.

So I'm going to skip ahead. I'm going to do all of that and skip ahead. So just bear with me for a moment. Okay, we're back.

I merged all those changes back into main, so now I'm going to navigate to my, environments. Going to go to prod. I'm going to look at my jobs. I have a daily run, so I'm going to use that.

Let's run now. Okay, so I skipped over the boring part waiting for the job to run. We see that it ran successfully, so let's look for our stg customers model. Awesome.

It built to the staging schema, so our modification of the generate schema name macro worked. Now you can add using environment variables in Jinja to your dbt tool belt. How cool.

#### Practice

# Practice

In this practice section, we will focus on replicating the instructor/s grant_select and clean_stale_models macro in your environment. We have provided you with some code skeleton below to get started.  You can always check out the exemplar on the next page or go back to the previous lessons to work along with the instructor.

#### grant_select macro

- Create a new file in the macros directory titled 'grant_select.sql'
- Copy the code below and adjust it based on your environment to grant select to your role or user (depending on your data platform).  You will need to reference the [target variable documentation.](https://docs.getdbt.com/reference/dbt-jinja-functions/target)

```
{% macro grant_select(...) %}

    {% set sql %}
        ...
    {% endset %}

    {{ log(..., info=True) }}
    {% do run_query(sql) %}
    {{ log(..., info=True) }}

{% endmacro %}
```
#### clean_stale_models macro

- Create a new file in the macros directory titled 'clean_stale_models.sql'
- Copy the code below and adjust it based on your environment to drop any database objects that are older than 7 days by default.

```sql
{% macro clean_stale_models(database=target.database, schema=target.schema, days=7, dry_run=True) %}

    {% set get_drop_commands_query %}
        select
         case 
            when table_type = ...
```

#### Exemplar

# Exemplar

	Use the following code snippets to assist you in the previous exercise and check your work. Disclaimer, for the sake of brevity, these solutions are in a Snowflake environment. 

	#### grant_select macro

```
{% macro grant_select(schema=target.schema, role=target.role) %}

    {% set sql %}
        grant usage on schema {{ schema }} to role {{ role }};
        grant select on all tables in schema {{ schema }} to role {{ role }};
        grant select on all views in schema {{ schema }} to role {{ role }};
    {% endset %}

    {{ log('Granting select on all tables and views in schema ' ~ target.schema ~ ' to role ' ~ role, info=True) }}
    {% do run_query(sql) %}
    {{ log('Privileges granted', info=True) }}

{% endmacro %}
```

	#### clean_stale_models macro

```sql
{% macro clean_stale_models(database=target.database, schema=target.schema, days=7, dry_run=True) %}
    
    {% set get_drop_commands_query %}
        select
            case 
                when table_type = 'VIEW'
                    then table_type
                else 
                    'TABLE'
            end as drop_type, 
            'DROP ' || drop_type || ' {{ database | upper }}.' || table_schema || '.' || table_name || ';'
        from {{ database }}.information_schema.tables 
        where table_schema = upper('{{ schema }}')
        and last_altered <= current_date - {{ days }} 
    {% endset %}

    {{ log('\nGenerating cleanup queries...\n', info=True) }}
    {% set drop_queries = run_query(get_drop_commands_query).columns[1].values() %}

    {% for query in drop_queries %}
        {% if dry_run %}
            {{ log(query, info=True) }}
        {% else %}
            {{ log('Dropping object with command: ' ~ query, info=True) }}
            {% do run_query(query) %} 
        {% endif %}       
    {% endfor %}
    
{% endmacro %} 
```

#### Review

## Review

Check out the quick summary of this chapter of the course below. You can also reference the instructor's work in the GitHub repository here: [dbt-learn-jinja repository](https://github.com/dbt-labs/dbt-learn-jinja)

## Grant permissions macro

**([view code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/grant_select.sql))**

We can run queries against the database when calling a macro. In the instructor's example, we walked through how to use a macro to execute multiple permissions statements in a parameterized way. We leveraged the following dbt specific Jinja functions to do so:

**run_query (**[**documentation**](https://docs.getdbt.com/reference/dbt-jinja-functions/run_query)**)**

The run_query macro provides a convenient way to run queries and fetch their results. It is a wrapper around the [statement block](https://docs.getdbt.com/reference/dbt-jinja-functions/statement-blocks), which is more flexible, but also more complicated to use.

**log (**[**documentation**](https://docs.getdbt.com/reference/dbt-jinja-functions/log)**)**

The log macro is used to log a line of text to the logs in dbt. We can add the key default=True to also log the same text to the command line interface.

**target (**[**documentation**](https://docs.getdbt.com/reference/dbt-jinja-functions/target)**)**

Target contains information about your connection to the warehouse. The variables accessible within the target variable for all adapters include profile_name, name, schema, type, and threads. Check out the documentation for adapter specific variables

## Union by prefix macro

**([view code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/union_tables_by_prefix.sql))**

We can also use the results of a query to template the SQL we are writing in a model file. In the instructor's example, we walked through the use of the execute variable, agate file types, and the get_relations_by_prefix macro

**execute (**[**documentation**](https://docs.getdbt.com/reference/dbt-jinja-functions/execute)**)**

The execute variable is a boolean variable that is true when dbt compiles each node of your project. This can be helpful to wrap around a block of text that you want to *only* run in the execution phase. Check out the docs linked above for a concrete example and additional context.

**agate file types (**[**documentation**](https://agate.readthedocs.io/en/latest/api/table.html)**)**

When executing the run_query macro, the results of the query are stored in a file type called agate. If you are familiar with pandas in python, this works in a very similar fashion. Check out the documentation linked above for interacting with agate types.

**get_relations_by_prefix (**[**documentation**](https://github.com/dbt-labs/dbt-utils#get_relations_by_prefix-source)**)**

The get_relations_by_prefix macro can be imported into your project through the dbt_utils package. This works by parsing through the dbt project and looking for relations with a similar prefix. These relations are returned in the form of a list. Check out the documentation linked above for additional ways to leverage this macro.

## Clean stale models macro

**([view code in GitHub](https://github.com/dbt-labs/dbt-learn-jinja/blob/main/macros/clean_stale_models.sql))**

The instructor walks through an example of using all the tools in the previous lesson to clean up his development schema for any stale models that haven’t been altered in the past 7 days. This macro was built using the information schema in Snowflake and this can be replicated on other data platforms using the respective information schemas. Read more about the origin of this macro in the Discourse post below:

**Discourse:** [Clean your warehouse of old and deprecated models](https://discourse.getdbt.com/t/clean-your-warehouse-of-old-and-deprecated-models/1547)

#### Knowledge check-adv jinja

## Survey 3min
<a id="survey-3min"></a>

### Survey
<a id="survey-3min-survey"></a>

#### Quick survey

## 4 Quick questions!

Almost there! As you finish the course, we'd love to hear your feedback on the course in this quick survey here: [Open survey in new tab](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com)

#### Congratulations!

## Congratulations!

Thank you for joining all of us from the dbt Labs team!!! You just leveled up your dbt skill set with **Jinja, Macros, and Packages!**

Make sure you hit complete on each of the lessons.  Check out the resources below to continue the journey, stay fresh on your skills, and share this with your fellow analytics engineers.

### **Resources**

**dbt Docs: **There is no shame in referencing the docs as an analytics engineer! Use this to continue your journey, copy YML code into your project, or figure out more advanced features.

**Short courses: **We have three courses to continue leveling up:

- [**Advanced Materializations:**](https://courses.getdbt.com/courses/advanced-materializations) So far you have learned about tables and views. This course will teach you about ephemeral models, incremental models, and snapshots.
- [**Analyses and Seeds:**](https://courses.getdbt.com/courses/analyses-seeds) Analyses can be used for ad hoc queries in your dbt project and seeds are for importing CSVs into your warehouse with dbt.
- [**Refactoring SQL for Modularity:**](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) Migrating code from a previous tool to dbt? Learn how to migrate legacy code into dbt with modularity in mind.

### **Contribute**

- Support fellow learners and let us know what you thought about the course in [**#learn-on-demand**](https://getdbt.slack.com/archives/C01DU491K1A).
- Support other beginners in [**#advice-dbt-help**](https://getdbt.slack.com/archives/CBSQTAPLG)

### **Feedback**

- **Bugs:** Help the training team squash bugs in the course by sending them to [training@dbtlabs.com](mailto:training@dbtlabs.com) and we will triage them from there.

Congratulations and thank you again! See you in dbt Slack! 

- The dbt Labs team

#### Get dbt certified!

By completing this course, you are one step closer to achieving your dbt Cloud certification! To continue your progress, explore the next course in our certification path and apply your new skills in real-world scenarios. Stay committed, keep learning, and join our community of experts to share your experiences and gain insights.

### The dbt Certified Developer Path

The courses on the path are:

- dbt fundamentals 
- Refactoring SQL for Modularity
- Jinja, Macros, and Packages
- Advanced Materializations
- Analyses and Seeds
- Advanced Testing
- Advanced Deployment
- Exposures
- dbt Mesh

Enroll in the next course today. Then visit [dbt-certification](https://www.getdbt.com/dbt-certification) and download the study guide to begin planning your path.  🚀🚀

---

### Metadata

- Course: Jinja, Macros, and Packages (dbt Studio)
- Generated (UTC): 2026-02-27 11:53:52Z
- Source slug JSON: response\Jinja Macros and Packages\slug\Jinja Macros and Packages.json
- Source captions dir: response\Jinja Macros and Packages
