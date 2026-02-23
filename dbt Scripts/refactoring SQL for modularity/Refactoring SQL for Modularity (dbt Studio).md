# Refactoring SQL for Modularity (dbt Studio)

## Contents

- [Welcome 10min](#welcome-10min)
  - [Introduction](#welcome-10min-introduction)
- [Learn the refactoring process 120min](#learn-the-refactoring-process-120min)
  - [The refactoring process](#learn-the-refactoring-process-120min-the-refactoring-process)
  - [Centralizing Logic](#learn-the-refactoring-process-120min-centralizing-logic)
  - [CTEs or Intermediate Models](#learn-the-refactoring-process-120min-ctes-or-intermediate-models)
  - [Final Refactor](#learn-the-refactoring-process-120min-final-refactor)
  - [Auditing](#learn-the-refactoring-process-120min-auditing)
  - [User-Defined Functions](#learn-the-refactoring-process-120min-user-defined-functions)
- [Closing](#closing)
  - [Wrap up](#closing-wrap-up)

## Welcome 10min
<a id="welcome-10min"></a>

### Introduction
<a id="welcome-10min-introduction"></a>

#### Welcome to the refactoring course

[**Join the dbt Community Slack**](https://www.getdbt.com/community/)

Learn with fellow analytics engineers and work through the course together in the** #learn-on-demand** channel.

📣** Note regarding trial dbt accounts**

- If you are using a dbt trial account to complete the hands-on portions of this course, and your trial account was created after February 2, 2026, your dbt version might be using the new dbt Fusion engine.
- As of October 13, 2025, the dbt Fusion engine is in a preview phase, meaning it is not generally available, but is stable and production-ready.
- If your dbt account is on Fusion, you may experience some limitations in dbt. Please refer to this page for the current [supported features and limitations](https://docs.getdbt.com/docs/fusion/supported-features).
- If you are unable to use a non-GA product, please follow these steps to turn off the Fusion engine:
- Go to Orchestration -> go into each environment -> click edit -> select "Latest" as your dbt version -> click save

Extracted captions from video: Welcome to the refactoring course

Hi everyone. Welcome to the dbt Labs refactoring course. My name is Jessica Stayton. I'll be teaching the course.

I'm a data engineering resident architect here at dbt Labs. And a common question that we're asked after people finish dbt Fundamentals is how can I apply the basic dbt concepts and best practices to my existing code, particularly when migrating to the platform. This process is what we refer to as refactoring. So perhaps you have a new or existing dbt project and you need to move code that lives elsewhere into your dbt project.

Or you might be looking at your existing models and just decide, wow, these are insane and I wish they were a little bit more modular. Whatever the case, you want to refactor them using dbt best practices. And this course will teach you how to do that in an organized way. So there's two tracks that you can code along with.

One's using the dbt platform with the Studio IDE and the other is in VS code. Either way, I'll walk you through the process of refactoring the SQL code using our best practices and insights here at dbt Labs. So code along with me. I highly encourage it.

The more hands on you can get, the more comfortable you're going to be. So let's walk through what we're going to cover. First, migrating our code into the dbt project, and then we'll use dbt sources to change out our hard coded references. Next we'll talk about refactoring strategies to consider, which will help us set up for success when we're auditing and validating our, refactoring refactored versions.

And then we'll talk about CTE groupings, formatting, cosmetic cleanups. And after that we'll get into the actual refactoring itself. So that's where we're going to be moving around a lot of logic dividing things up into models. And there's a lot of different models that we'll talk about.

So our staging models, intermediate, our final marts. One common question is whether we want to use CTEs or intermediate models for certain parts of code. And we'll cover that too. We'll wrap up and then we'll talk about and walk through how we can audit our refactored versions against our original, model results so that we can deprecate our old code with confidence.

As a bonus, then we'll also explore migrating UDFs to dbt as well. So I'll see you in the next session. Hope you enjoy this course.

#### Prerequisites

# Prerequisites

Before engaging with this course, we highly recommend that you have experience with the following SQL and dbt concepts.

**SQL prerequisites:**

- Joins
- Case when
- Window functions
- Subqueries
- Aggregations
- CTEs

**dbt Prerequisites:**

- Models
- The ref function
- Configuring and selecting from sources
- How to use a package in dbt
- Modularity and Reusability Concepts*

If you are unfamiliar with these dbt prerequisites, check out [dbt Fundamentals](https://courses.getdbt.com/courses/fundamentals) first and then come back to learn how to refactor sql!  You will be able to build on your project from dbt Fundamentals in this course!

#### Frequently Asked Questions

## Frequently Asked Questions

**How long does this course take to complete? **

The course takes about 4 hours to complete. There are about 90 minutes of video and approximately 2.5 hours of practice for someone who is new to refactoring. 

**If I need help with working on dbt, where can I reach out?**

We have chat support embedded in dbt. Click on the chat bubble icon in the upper right-hand corner. Reach out with any questions/errors that you have.

**If I need help loading training data into my data warehouse, where can I reach out? **

Please reach out in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)** channel in [**dbt Slack**](https://www.getdbt.com/community). We'd be happy to support you there.

**If I notice a bug or error in one of the lessons, where can I share that? **

First off, I really appreciate you surfacing this for us. Secondly, you can send a quick email over to** [training@dbtlabs.com](mailto:training@dbtlabs.com).**  Please include the URL and a screenshot. This will allow us to quickly find out what needs to be fixed. 

**Where can I submit feedback on the course content? **

Please feel free to post feedback in the end of [**course survey**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com). We are quick to respond and love to hear suggestions!

#### Set up a practice project

## Set up a practice project

For this course, you should use a dedicated project for training rather than try to replicate this in your company’s primary project. You will also need access to a data warehouse and a git repository.  We recommend BigQuery because they have a generous free tier and a Github repository because of how simple it is to get started.

- If you have already completed the dbt Fundamentals course, you can advance through the next three lessons to get to **3. Create a `customer_orders` model with the query below** 
- If you haven’t completed dbt Fundamentals, you will need to a) create a project in dbt platform with connections to your warehouse and repository, b) get the training data set into your warehouse of choice and c) ensure that you have the right permissions to operate on that data.

## 2. Create a project in dbt platform with a connection to your warehouse and repository

Check out [chapter 3](https://learn.getdbt.com/learn/course/dbt-fundamentals/set-up-dbt-60min/getting-started?page=1)in dbt Fundamentals for directions on how to set up your data platform and repo with dbt. 

##

## Learn the refactoring process 120min
<a id="learn-the-refactoring-process-120min"></a>

### The refactoring process
<a id="learn-the-refactoring-process-120min-the-refactoring-process"></a>

#### Learning Objectives

## Learning Objectives

- Identify and explain the importance of SQL refactoring, specifically in the context of improving model maintainability.
- Analyze existing SQL scripts and identifying areas where cosmetic cleanups and CTE groupings can improve readability and maintainability.

#### Migrating legacy code

Extracted captions from video: Migrating legacy code

All right, folks, so at this stage we should have our dbt project set up. Our, Snowflake platform set up with the training data loaded in. And the first step in refactoring your legacy code is to actually migrate your legacy code. So in dbt you can see, this project is empty.

My folders exist, but they are empty. So I'm going to migrate that code over. That's step one. What I'm going to do is hop over here into Snowflake.

I already have a, model that I want to refactor, so I'm going to hover over it on definition. Just copy that definition. Let's hop over here. And now in my models directory, I've got mine, a subdirectory called Demo here, because that's where I'm, I'm doing this demo.

I'm just going to create a folder. I'm going to call it Legacy. Cool. And then in there I'm going to create a file and let's call it Customer Orders.

I'm actually going to give it the suffix Legacy as well. Cool. All right, it's been created. Open it up.

Paste her in. Now we're going to just delete the stuff that we don't need. So we don't need this metadata, at the bottom. And dbt will create this, create or replace DDL for you, specific to your adapter that you're using.

So I'm going to take that out as well. All right, Save can also press Command S or Control S for Windows. That should save it. Now let's do a quick run.

Make sure we have this correct. You can click here and click Run Model or we can just do it manually. dbt run at the bottom -s And the name of my model is Customer Orders Legacy. Click Enter.

We should watch it build. Shouldn't take long because it's just a view. Here it goes. All right, success.

That's great. If I come over into Snowflake, let me refresh. There it is. Customer Orders Legacy.

You'll see it has that same Create or Replace and all that lovely definition. All right, now, important thing to keep in mind, a lot of the times you might be moving from one database to another. So for instance, you could be migrating from, MySQL to Snowflake. And in those instances the process of migrating might be a little bit longer for you because you'll have to translate the flavor of SQL.

So in our case here it was pretty straightforward because we're using Snowflake before and after refactoring. So anyway, that's a wrap for migrating our code into dbt So simple copy paste to start. We're not really going to change anything quite yet, but next step, we'll look at how we can implement sources and remove any hard coded references.

#### Implementing sources

Extracted captions from video: Implementing sources

We've migrated our code over and so now the next step is to implement some dbt sources and get rid of these hard coded table references it's pretty critical that we do that at this stage now, especially if we're going to be migrating over multiple scripts. If we can do that now, it's gonna save us time in the long run when we're trying to figure out identify our different components, down the line for additional scripts. So for instance, this one here, we see the database, the schema name and the table name. That's a fully qualified reference.

Right. Let's just see how many from the raw database are being called here. And that's six. So we got six that we got to replace.

Okay, I see Jaffle Shop orders, and there's another Jaffle Shop orders just above it was the customers one, so that's two. Another customers. So we still have two. And then our raw Stripe payment.

So we have three different sources. Let's check out the last one. Yeah. All right, three sources, two from Jaffle Shop, one one from Stripe.

Let's go ahead and make those. All right, so in staging, that's where I'm going to have these live. I'm going to create a folder called Jaffle Shop, and then I'm going to create another folder called Stripe. All right, here we go.

In Jaffle Shop, I'll create a file called Sources YAML. And in Stripe, I'm going to do the same. Now there is a pretty cool. If you're familiar with using dbt packages at this point, you can generate your sources YAML, using a code gen package, the dbt code gen package, they have a macro that you can call, called generate source.

And it'll do this for you, but we're going to just do it by hand here. So we're using version 2. This is for Stripe. Here's my sources.

If I hit tab, it'll start auto filling this in for me. Name was Stripe. Then I have a database that was raw. And then I had tables.

The first one was named Payment. So that's my Stripe source right here. Raw Stripe payment. Raw Stripe payment looks good.

Save. And then I'm going to come here, copy, come here, paste. I don't want to do the same thing twice. But this source is called Jaffle Shop.

It's from Raw. And I had one called Customers, and then I had another one called Orders. I hit Save all Right, this looks good. I've got my two sources.

Now we're just going to go replace those in our legacy SQL file. Okay, So I had six to replace. Here's my first one. Raw Jaffle Shop orders.

I'm going to hit underscore, Underscore type source. That's going to. When I hit tab, blam. Auto template that macro for me so I don't even have to worry about it.

This was the Jaffle Shop and the orders source. All right, so there's one. I'll hit save and if I come here and update my graph. Yeah, there it is.

Great. All right, love to see it. We're going to do the same thing down here. Double underscore source tab.

This one is also Jaffleshot. And this one was customers save. If I update my graph. Blam.

Love to see it. Now I've got two sources. All right, these were called a couple of times, so I'm just going to go through and replace those. Here's another orders.

Here's another customers. Looks good. All right, everything's compiled. We had four that we've replaced, so there's two left.

Another double underscore source tab. This is stripe. And that table was called payment. You can see it Auto fill in for me.

It's nice. Love it. Okay, one more. Last one right here. I'm just going to copy paste it.

Why do more work when less work is, well, it's better. All right, we save. Can update that graph and look at that. All right, that's it for removing, all those hard coded references.

#### Choosing a refactoring strategy

Extracted captions from video: Choosing a refactoring strategy

Next step in refactoring this legacy code is to choose how we're going to do it. So our refactoring strategy, there's not really a lot of hands on work here, but we still need to consider how we'd like to proceed. Right now, I've been working on my own feature branch with the legacy code. You can see my branch here.

Demo jstaten. I haven't pushed anything to remote yet. It's not running in production, so if I keep working out of the same file, I won't have anything to refer to when it's time to do an audit. So if you have your code migrated, pushed and merged, you can create a branch off of main and start refactoring on top of the model.

But the other way to go, which is the way that I prefer, is just right alongside the model. So what that means is that you would copy and paste that model and place it somewhere into your project, preferably where you'd like it to exist post refactoring. So for us, that's gonna be in the marts folder, because that's a downstream model meant for BI. So this would be the model that we refactor.

Let's go ahead and do that. I'm gonna copy this and then in my marts directory I'm gonna create a new file. This is a fact model, so we'll just call it fact customer orders. I'll paste it in there.

So this is where I'm going to be performing my refactoring work. So I'll always have a, reference to the legacy if something goes wrong or if I need to revert something. But most importantly, I'll always have the reference to the legacy so I can audit. So with that done, I'm ready to start refactoring.

#### Cosmetic Cleanups

Extracted captions from video: Cosmetic Cleanups

We have migrated our code over. We've removed our hard coded sources and implemented some dbt sources. Right here. And now we're going to deal with some cleanups just to make this a little bit more readable and easier to follow.

Legibility is pretty important. We want developers coming after us to be able to understand what they're reading, what they're doing, and also, we don't want to get lost while we're refactoring. So there's a couple of things here. Number one.

I want to get rid of having to scroll here. This is bad for me, so I'm just going to, Right click. You see this toggle? Word wrap.

All right. Marginally better. Next. This is a small thing. But we have some standards that I'd like to enforce.

We have mostly lowercase. But then we have some uppercase as well. So with dbt. The best practice is to have everything be lowercase for things like Snowflake, which is the data platform that we're using.

It's actually the opposite everything. Best practices uppercase. But don't worry. The. Adapter is going to compile that, To meet the best practices of the target platform that it's building in.

So what I'm going to do is go to the command palette and we're just going to transform this to lowercase to get rid of those keywords and those different. Table functions that were just not quite doing what we wanted them to do. So now everything is lowercase. So next, I want to give myself some space for readability.

I'm just going to start putting in some spaces here, so I have some groupings that make a little bit better sense for me. All right, so there's one select here and another select here. This is generally okay, but these case wins, I think, is when it starts to get a little difficult to read. So, what I'm going to do is break these apart by our.

Our keywords there. So Case when, not in, then end and then bring that closing parens back as that. All right, so this to me is a lot easier to read than what it used to be. So let's do that for all of these.

Case, when, not in, then end at the bottom as K. This one, I'd like to actually break that one up a little bit too, just because we have multiple things going on. There. Colorless.

Same here with this. Colorless. Break that up. And then we have a case when as well.

Case when. Then end. That's the end of that count. And that's the end of the coalesce.

Okay. Oh, that looks better to me. Can see some stuff starting to go a little bit better. I'm going to leave that min as is though the sum.

Let's break this one up too. Case when, not n. Then we have an else also. And then an end.

Okay. That looks nice. Follow it a little bit more easily. And this one's nice and long.

Great. Love it. We'll actually refactor these when we get there as well. Right now we just want to see what we're even working with.

There's another else. There's the end that divided by the nullif count is, When. End. It's the end of the count.

It's the end of the null if. Okay. Okay, this looks good. Let's bring that select up.

Bring that one up. B. So join on Left outer. Join on where? Group I. Okay.

The rest of this looks pretty good, so we'll go ahead and save. Okay, now I want to point something else out as well, which you might have noticed. I'm actually going to go ahead and undo all of this really quickly, just because I want you to see something that we have that's just built in. So starting with our gross, we'll go ahead and untoggle that too.

Right, Our gross monster model. We have this nice format button. We can go ahead and click that and see what that did. It essentially did what we just did manually for us, breaking it apart to be a little bit more legible.

So either way you go, that's going to be very helpful. Moving forward.

#### CTE Groupings

Extracted captions from video: CTE Groupings

we've done some basic cosmetic cleanup after migrating our model over into dbt and importing our sources. So the next thing is splitting this up into some CTE groupings. So there's a proper order for our CTE groupings. First you want to have your imports.

Then you want to follow those up with your logicals. Your, your final CTE comes next. That final CTE is just going to be pretty much like this main, select statement. And then your final select statement at the very end is just going to be a select star from that last CTE.

So with your import CTEs, you generally want these to be at the top of your model. That's best practice. It's best practice just within a lot of different programming languages, like in Python projects, to have your imports at the top of the file. First off, because it's cleaner.

Having, them at the top allows you to see for you as the developer, but also for any developer coming after you, what are all of the models that are being referenced within this single model file? That's going to be super helpful for larger projects. It's going to prevent a lot of guesswork, a lot of scrolling through to try to make sure, you know, what all we're referring to here. Of course, having this lineage at the bottom is also helpful for that same thing.

So for fct customer orders, we know we're referring to these three, and so those are going to be the three that we have as import CT's at the top. So the keyword to kick off a CTE is with. So we're going to start with that. And I've got Jaffle Shop customers and Jaffle Shop orders and stripe payment.

These are all coming directly from the source. So what I'm going to do is prefix my CTE with the word raw. So raw customers as. And then we'll have raw orders as, and then we'll have RAW payments as.

Okay, so within these, CTEs, these import ones, we're just pulling everything over. So this is going to be a select star from. I've already got my source listed off here. And this one is customers, this one was.

Orders, and this one is a select star from. So Jaffle Shop, we're doing stripe instead. Not strip stripe. And instead of orders, we're doing payment.

Okay, so we've got our first three import CTEs. And I want to point out something since I'm doing this demo, with the new fusion engine, you can see here that just by splitting them into CTEs, we've got something that's popped up for us, this Preview CTE option. So that's going to allow you, with just a quick click, to preview what your CTE would return for you. So I can see here, this is the data for RAW customers.

When dealing with things like transformations or renamings or even column reorderings, having the functionality to quickly preview your CTE rather than having to build and then switch over to your data platform, it's going to be very helpful. All right, so I've got my imports. Next is to move on to our logicals. So with our logical CTEs, what I want to do is break apart these different subqueries that I'm seeing, get rid of subqueries in general, and have those be pulled into a ct.

So when I'm saying subquery, let me just clarify really quickly, I'm referring to like within our main select statement, we have these joins that have a select statement within them. Right. Same with here, join and then a select statement. Here's another subquery, another select within a select and then one there.

So we're going to have at least what I found looked like four. So this one's a bit complex, this long one. So what we're going to do is just start with this first one. We're going to preserve the order of these, but also the logic of these.

For now, we're not going to worry too much about refactoring what's within these CTEs yet. So I'm actually just going to cut this and paste it up here. It's going to be customers as, there, there's my next cte. I also want to make sure that I'm replacing the references as I go.

So. So I'm not making more work for myself. So this CTE is actually going to be pulling from our RAW customers that we created earlier. Let's go through and just fix those as well.

So this is coming from RAW Orders. Those orders won't worry about renaming here. K. This one here is also from RAW Orders.

I think that means we might need to rename a couple pieces up here too. This looks okay. Yeah, this looks good. A.

From, RAW customers left join RAW Payments and here also RAW payments. That one's getting renamed to C. Renamed to payments. Okay, I think I've cut everything.

Do you have a RAW Orders there that needs to get renamed RAW orders. Let's just do a quick orders dot. Let's See? Looks good, Looks good.

It's going to be A RAW orders just above it as well. RAW orders in. Oh, I ruined this one actually, since we're renaming There, there, that looks good. All right, so back to pulling into CTEs.

We've done one that leaves us with this huge one within this join, but let's start smaller because this huge join with customer order history. If we come up and see where it starts there, it actually is a subquery that has more nested subqueries within it. So what I'm gonna do is start smaller before we tackle the main one. Let's cut this one out from A, so it's called A.

I wanna preserve that alias for now just to make it easier on myself. A as we'll paste that up there, comma, because we're not done yet. Scroll down. Okay, from A join, here's another nested subquery.

Get rid of that. Come up. Okay, it's going to be B as paste. All right, now we can look at this main one join subquery.

From A join B. Where does this end? Where does it end? Customer order history there.

All right, since it's joining customer order history as there. All right, I think we are looking good. Our, last thing we want to move up, this is our final select. That's what's left.

So we've got our main, select with those columns from RAW orders, renaming it to Orders join customers, which is the CTE we defined above. Joining there looks good. Joining customer order history, which we defined above. Looks good.

Left outer join, RAW payments. I think this looks good. I do think now we can take that out. Take that out, take that out.

Since we're aliasing it to just orders. Okay. And this is going to be our final select or sorry, our final cte. Now you should give it a more descriptive name, something that is good for your project.

But for the purposes of our demo, this will be fine. I'm going to just cut this out final as paste. We do not have a comma separating our final CTE from our final select. And that should do it.

All right, we're going to do a quick save and, let's do a run and see what this looks like. So I can do a run here, run model, or I can do a run here. Let's see what happens. Fingers crossed.

All right. Looks good. We didn't break anything. So with that all done, we've split up our model.

Into more modular sections. It's going to be easier to test, it's going to be easier to edit, We're going to be able to comment out anything that is irrelevant. And right off the bat, I saw one. We've got this CTE that's doing the exact same thing as this cte, for instance.

So with that done, we'll be able to next centralize some of this logic into staging models.

#### Practice - Migrate Legacy Code

## Migrate Legacy Code

1. In your dbt project, under your models folder, create a subfolder called legacy.

2. Within the legacy folder, create a file called customer_orders_legacy.sql

3. Paste the following query in the customer_orders.sql file:

```sql
WITH paid_orders as (select Orders.ID as order_id,
        Orders.USER_ID    as customer_id,
        Orders.ORDER_DATE AS order_placed_at,
            Orders.STATUS AS order_status,
        p.total_amount_paid,
        p.payment_finalized_date,
        C.FIRST_NAME    as customer_first_name,
            C.LAST_NAME as customer_last_name
    FROM raw.jaffle_shop.orders as Orders
    left join (select ORDERID as order_id, max(CREATED) as payment_finalized_date, sum(AMOUNT) / 100.0 as total_amount_paid
from raw.stripe.payment
where STATUS <> 'fail'
group by 1) p ON orders.ID = p.order_id
left join raw.jaffle_shop.customers C on orders.USER_ID = C.ID ),

customer_orders 
    as (select C.ID as customer_id
        , min(ORDER_DATE) as first_order_date
        , max(ORDER_DATE) as most_recent_order_date
        , count(ORDERS.ID) AS number_of_orders
    from raw.jaffle_shop.customers C 
    left join raw.jaffle_shop.orders as Orders
    on orders.USER_ID = C.ID 
    group by 1)

select
    p.*,
    ROW_NUMBER() OVER (ORDER BY p.order_id) as transaction_seq,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY p.order_id) as customer_sales_seq,
    CASE WHEN c.first_order_date = p.order_placed_at
    THEN 'new'
    ELSE 'return' END as nvsr,
    x.clv_bad as customer_lifetime_value,
    c.first_order_date as fdos
    FROM paid_orders p
    left join customer_orders as c USING (customer_id)
    LEFT OUTER JOIN 
    (
            select
            p.order_id,
            sum(t2.total_amount_paid) as clv_bad
        from paid_orders p
        left join paid_orders t2 on p.customer_id = t2.customer_id and p.order_id >= t2.order_id
        group by 1
        order by p.order_id
    ) x on x.order_id = p.order_id
    ORDER BY order_id
```
4. Conduct a dbt run -s customer_orders_legacy to ensure your model is built in the warehouse. You should see this model under {your development schema}.customer_orders (i.e, dbt_jstayton.customer_orders_legacy)

5. In your dbt project, under your models folder, create a subfolder called marts.

6. Within the legacy folder, create a file called fct_customer_orders.sql

Paste the following query in the fct_customer_orders.sql file:

```sql
WITH paid_orders as (select Orders.ID as order_id,
        Orders.USER_ID    as customer_id,
        Orders.ORDER_DATE AS order_placed_at,
            Orders.STATUS AS order_status,
        p.total_amount_paid,
        p.payment_finalized_date,
        C.FIRST_NAME    as customer_first_name,
            C.LAST_NAME as customer_last_name
    FROM raw.jaffle_shop.orders as Orders
    left join (select ORDERID as order_id, max(CREATED) as payment_finalized_date, sum(AMOUNT) / 100.0 as total_amount_paid
from raw.stripe.payment
where STATUS <> 'fail'
group by 1) p ON orders.ID = p.order_id
left join raw.jaffle_shop.customers C on orders.USER_ID = C.ID ),

customer_orders 
    as (select C.ID as customer_id
        , min(ORDER_DATE) as first_order_date
        , max(ORDER_DATE) as most_recent_order_date
        , count(ORDERS.ID) AS number_of_orders
    from raw.jaffle_shop.customers C 
    left join raw.jaffle_shop.orders as Orders
    on orders.USER_ID = C.ID 
    group by 1)

select
    p.*,
    ROW_NUMBER() OVER (ORDER BY p.order_id) as transaction_seq,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY p.order_id) as customer_sales_seq,
    CASE WHEN c.first_order_date = p.order_placed_at
    THEN 'new'
    ELSE 'return' END as nvsr,
    x.clv_bad as customer_lifetime_value,
    c.first_order_date as fdos
    FROM paid_orders p
    left join customer_orders as c USING (customer_id)
    LEFT OUTER JOIN 
    (
            select
            p.order_id,
            sum(t2.total_amount_paid) as clv_bad
        from paid_orders p
        left join paid_orders t2 on p.customer_id = t2.customer_id and p.order_id >= t2.order_id
        group by 1
        order by p.order_id
    ) x on x.order_id = p.order_id
    ORDER BY order_id
```
7. Conduct a dbt run -s fct_customer_orders to ensure your model is built in the warehouse. You should see this model under {your development schema}.fct_customer_orders (i.e, dbt_jstayton.fct_customer_orders)

#### Practice - Implementing Sources

## Implementing sources

1. Create a subfolder under your models folder called staging.

2. Under your models > staging folder, create two subfolders - one for each source schema that our original query pulls from. These subfolders are stripe and jaffle_shop.

3. Create a file under models > staging > jaffle_shop called sources.yml.

4. Create a file under models > staging > stripe called sources.yml.

5. [Declare configurations for the corresponding source](https://docs.getdbt.com/docs/building-a-dbt-project/using-sources#declaring-a-source) in each file:

**models/staging/jaffle_shop/sources.yml
**

```
version: 2

sources:
  - name: jaffle_shop
    database: raw
    tables:
      - name: customers
      - name: orders
```
**models/staging/stripe/sources.yml
**

```
version: 2

sources:
  - name: stripe
    database: raw
    tables:
      - name: payment
```
6. Now that your sources are configured, open your fct_customer_orders.sql file and replace any hardcoded references (i.e, raw.jaffle_shop.customers) with a [source function](https://docs.getdbt.com/docs/building-a-dbt-project/using-sources#selecting-from-a-source), referencing the sources you have set up.

**Note** If you are using BigQuery, your database is not `raw`, it is `dbt-tutorial`

#### Practice CTE Groupings and cosmetic cleanup

## CTE Groupings and cosmetic cleanup

This section is heavy on best practices, specifically [our own best practices](https://github.com/dbt-labs/corp/blob/master/dbt_style_guide.md) - we encourage you to create and follow your own!

**Import CTEs at the top**

1. The cosmetic cleanups in this video are listed below. Use this guideline to refactor the cosmetics of your fct_customer_orders model:

- Add whitespacing
- No lines over 80 characters
- Lowercased keywords

2. CTE restructuring

Refactor your code to follow this structure:

```
    -- with statement
    -- import CTEs
    -- logical CTEs
    -- final CTE
    -- simple select statement
```
    a. Add a with statement to the top of your fct_customer_orders model

    b. Add **import CTEs** after the with statement for each source table that the query uses. Ensure that subsequent from statements after the import CTEs reference the named CTEs rather than the {{ source() }}. We will focus on additional restructuring in the next section.

```sql
with 

-- Import CTEs

customers as (

  select * from {{ source('jaffle_shop', 'customers') }}

),

orders as (

  select * from {{ source('jaffle_shop', 'orders') }}

),

payments as (

  select * from {{ source('stripe', 'payment') }}

),

-- Logical CTEs
-- Final CTE
-- Simple Select Statment

paid_orders as (
    select orders.id as order_id,
        orders.user_id as customer_id,
        orders.order_date as order_placed_at,
        orders.status as order_status,
        p.total_amount_paid,
        p.payment_finalized_date,
        c.first_name as customer_first_name,
        c.last_name as customer_last_name
    from orders
    left join (
        select 
            orderid as order_id,
            max(created) as payment_finalized_date,
            sum(amount) / 100.0 as total_amount_paid
        from payments
        where status <> 'fail'
        group by 1
    ) p on orders.id = p.order_id
    left join customers as c on orders.user_id = c.id ),

customer_orders as (
    select 
        c.id as customer_id
        , min(order_date) as first_order_date
        , max(order_date) as most_recent_order_date
        , count(orders.id) as number_of_orders
    from customers as c 
    left join orders on orders.user_id = c.id 
    group by 1
)

select
    p.*,
    row_number() over (order by p.order_id) as transaction_seq,
    row_number() over (partition by customer_id order by p.order_id) as customer_sales_seq,
    case when c.first_order_date = p.order_placed_at
    then 'new'
    else 'return' end as nvsr,
    x.clv_bad as customer_lifetime_value,
    c.first_order_date as fdos
from paid_orders p
left join customer_orders as c using (customer_id)
left outer join 
(
    select
        p.order_id,
        sum(t2.total_amount_paid) as clv_bad
    from paid_orders p
    left join paid_orders t2 on p.customer_id = t2.customer_id and p.order_id >= t2.order_id
    group by 1
    order by p.order_id
) x on x.order_id = p.order_id
order by order_id
```
**Pull out intermediates and simple subqueries**

1. Move any simple subqueries into their own CTEs, and then reference those CTEs instead of the subquery.

2. Wrap the ultimate remaining select statement in a CTE and call this CTE final.

3. Add a simple select statement at the end: select * from final.

**Remove join in favor of window functions + some cosmetic cleanup**

1. This is specific to this query, but one of the subqueries and fields (customer_lifetime_value) would be better written as a window function to avoid an unnecessary extra self join. You could have made it one step better by making it a CTE rather than a subquery, but we are going to go 2 steps and just rewrite that bit of logic as a window.

2. Add comments for case-when or window functions to help out future you

**Use fully qualified table names and references**

At this point, I do some cleanup to make it easier to read, mostly fully qualifying column names and removing single letter aliases or other potentially confusing bits 

**Simplify with window functions (FIX)**

1. This is specific to this query, but I noticed one of the final columns was using a CTE to aggregate: min(orders.order_date) as first_order_date which could be simplified with a first_value window function. Here we are practicing continuous improvement - always looking for ways to make your code more terse or performant.

2. Remove the customer_orders CTE and join in the final CTE:

 followed by 

3. Change the transformation logic for the following two columns: nvsr & fdos

### Centralizing Logic
<a id="learn-the-refactoring-process-120min-centralizing-logic"></a>

#### Intro to Centralizing Logic

Extracted captions from video: Intro to Centralizing Logic

we just spent some time cosmetically cleaning up, formatting our code, moving our different subqueries and the main select into CTEs and having that final select to kind of wrap it all up at the end. So what we did was essentially just organize our code so we could read it a little bit more easily from top down. Understand the flow really of what we're trying to say and what we're querying. Our next step in this process is to centralize our transformations and then split them up up into models.

when we're talking about centralizing transformations we're also honing in and really looking at the code within our CTEs and doing some optimizations. And when you're optimizing queries so that they're performing best with your data platform, whether you're working with things like Snowflake or Bigquery or Redshift, what have you, what you want to do is move any transformations or filtering logic or joining earlier in the process so that your downstream processes are more efficient. So that way you're dealing with less data, you're handling less complex logic. Your queries in general are going to compute a bit faster and be more performant.

So we've got different types of models that we can split these transformations into with varying naming conventions depending on your project architecture. Generally your staging models are going to host these transformations. So intermediate models are optional. But consider using intermediate models when you have transformation logic that's within a model cte, but then the SQL starts getting a little bit long, maybe a little bit too complex too.

An intermediate model is a great place to host that kind of logic. Your mart models are your final layer. They're ready for consumption. You might have noticed also that we named our customer orders model Fact customer orders.

So fact models store quantitative metrics and events. So things like sales or payments and then dimension models, those dims, they store descriptive context for those facts. So things like product details for customer information. So fact and dim models are also consumer ready insights.

They're usually also combined into additional mart models for further deeper analysis. Now how do we identify these different parts? What should be a staging model, what if anything should be an intermediate model and then what's going to be our final mart model? So, so we'll take a look moving forward at our fact customer orders model that we are currently in the process of refactoring and we'll start by pulling out and separating that staging model logic, and then we'll proceed from there with any downstream models.

#### Customers Staging CTE

Extracted captions from video: Customers Staging CTE

All right, so looking at our model, we can actually identify, our staging models by identifying our sources. Right? The sources, are just our dependencies. So that means that for this model, fact customer orders to run.

It, depends on these three sources that we have identified. So, so our, staging models are aiming to transform just the source itself. So looking at, the customer cte, we're doing a transformation here on just raw customers. And that tells me that's going to be a good staging model.

Whenever we're talking about, like a mart model, one of our marts, that's going to be typically indicated by some type of join logic. So when you're combining data from multiple models, to create some kind of analytical insights, you can think of staging models as a place where you would create the building blocks for analysis. So you're taking your raw data, transforming it to meet your needs, whether that's casting a data type, renaming a column, combining a lot of different fields into one, like we had with the concatenation here, flattening extracting fields. And then that cleaned data can be used by developers to build any number of models downstream without having to perform the exact same cleanup on the data in multiple places.

So now that we have an idea of, like how we're going to split this up, let's go ahead and dive in. So our import CTEs are just selecting from our sources. I'm going to leave those for now and then take a look at our logical CTEs. So to start, I'm actually going to split up the logical CTE section into two.

I'm going to have my staging. So this, to me again looks like, it could be a candidate for a staging model. We're transforming just one source here also. We'll talk about B in a second.

But with customer order history, this is where it starts to get a little tricky, where we've got some joins going on. So to me, this one looks like it's a great candidate for marts. So I'm going to label that, marts. Okay, so let's start small with customers here, right?

So in the customers cte, we have that first transformation. We're concatenating first name with last name to create a field called Name. All right. We can actually see that same transformation happening here in B.

So we can get rid of B as redundant. Just delete it. I'm going to do that now. But we need to be careful.

By deleting B, that means we also need to delete any reference to B and just replace it with customers above. So here where we see B dot, I'm going to replace with customers dot. So that top one, I want to click through them instead of just replacing all. I don't trust myself.

So we'll replace the first one, second, third, fourth. Okay. B ID looks good. B ID name.

Get a last name, first name. All right, so no more reference to B except for specifically right here. Join customers there. All right, we save it compiles.

We see no errors. Looks good. All right, let's see what other transformations that occur with customers that maybe we'd be able to pull up into our staging model. So in addition to this here, this concatenation.

Okay, so I see some renamings here. I think this would be good to pull earlier into the staging model. Let's actually double check and see especially if this, renaming happens twice. So in our final cte.

Yeah. All right, so I think those are good candidates to rename those. So instead of ID as customer id, get rid of that star. And then we had name as full name.

So let's go ahead and make that change up here. Why name it here and then rename it later? Last name and given name. Okay, Looks good.

I think I'm going to put full name here, comma. Yes. All right, so generally also within your staging models, instead of seeing the select star, we want to go ahead and explicitly name out our, columns. It's going to make it easier for developers and analysts so they don't have to go through and like query your information schema if you don't know, how to get those.

There's actually right here going to create a new file and let me just run, a query really quickly so you can see select column name from. I know it's in the RAW database and columns is what I want. I want the table name to be customers and the table schema to be. Let's give that single quotes too.

And the table schema is jaffle shop. And if I run that. Yeah, we have last name, ID, first name. Okay, so we've pulled in all of the columns into our cte.

Since we've, we've pulled the renaming here, I want to make sure we didn't break anything. As you can see, we've got an error because we need to make sure we are pulling the correct settings here. Not called last name anymore. We've done the renaming earlier.

Okay. And let's just make sure we've got everything. Renamed customers, customer ID. And then this is also going to be customer ID Full name, surname and given name.

I think that's the, I want to do it here, too. Given name and surname. This is customer ID. Okay, let's see.

I'm still getting an error. Surname. We want to make sure we're explicit there. Customers surname and customers given name.

All right, we have no more errors, so I'm going to go ahead and run this, make sure we don't have anything wrong. Okay. dbt ran succeeded. Great.

#### Orders Staging CTE

Extracted captions from video: Orders Staging CTE

We've got our staging, CTE now just going to become our staging model, for customers. We're going to do the same thing with orders here. So step one, it's named A right now. That's not good.

Let's name it Orders. Let's be explicit. Which means that I'm also going to have to go through and rename every, instance that I see a, A status. It's going to now become orders status, A dot status.

And actually let's do a, A dot. We're going to call it order of stat. So get rid of that one. Get rid of that one.

That one, that one, that one. Yep, yep, yep, yep. All right, that looks better. Make sure I got all of the A's though, from A there.

Orders and. Okay, looks good. Click save. It'll compile. Looks good. We're all great. So just like we did before, this here row over partition by this is just giving us a numbering for things.

So I want to make sure I have all of my column names. Specifically, I'm going to go back into the query that I had. This is against my snowflake information schema. That's going to give me information on my columns.

Right? So now I'm going to do the same thing I did here for orders command enter. That'll send that command from dbt to my data platform. And then I can see.

All right, these are all of my columns. We'll copy those over. Let's just start dealing with those now. Orders as instead of star here, we want to make sure we have id, user id, order date, and we can keep that underscore ETL loaded at, even though we're not using it.

And then status is also one that we need. I'll have status at the end. Okay, looks good. Let's go through now and see if there's any renaming that we need to do here.

Order date is first. Order date. That's fine. This is fine. Yeah. Orders ID as order id, User ID is customer id.

So let's do those renames at least. Order count, and then status will rename to order status. Okay, so let's pull those transformations up here. ID as order id, user ID as customer id, order date, status as order status.

All right, I think that's probably going to be it for us. But before we save, let's go ahead and clean that up. Orders, dot, order, status, order date, I'm going to do the same thing here for that looks good. Orders that.

Status. Orders, status. I should have done another control f or a command f to replace them, but I'm already too late. Into the game now, Order IDs.

Orders that. Order ID. Orders that. Customer ID. Orders. Order ID. Looks better. Order status. And here.

Orders, order ID, customer ID and order status. This becomes customer ID. This becomes customer ID, and this becomes order ID. I think that should do it.

Cool. Click save. Oh, we have an error. Our error is here. Oh, because I don't have a comma there.

See? Another error down here. Orders, customer id. Oh, because we're joining RAW orders. Okay. These joint orders get sort of that.

Yeah, no more references to the RAW here. All right, that looks good. And once again, we can do a quick dbt run, make sure. Oh, I don't want to do a whole run.

Oh, that's fine. Yeah, Looks good. Okay, you can also, Again, preview your CTEs. Make sure that everything looks how you would like it to.

So I'm going to go ahead and preview that I just built so I can see the user order sequence id, Customer id. Everything's renamed how I like it. Okay, looks good.

#### Payments Staging CTE

Extracted captions from video: Payments Staging CTE

We made our customers staging cte. We've made our orders staging cte. So you guessed it, we're going to make our payments staging cte. So let's go ahead and fill this in.

And I'm going to have a select. We'll fill this part in later from, and we're going to have it be raw payments. Okay, so what's going to go here? Well, let's figure out what all of our column names are.

So this is the payment table from the stripe source. Let's just run this really quick. Great. I'm going to copy these over.

Just remember it's best practice even if we're not using them. Our staging models should have all of the, all of the columns listed out explicitly because another model might use these columns, even if it's not this specific one. The fact customer orders. All right, so I pulled them over.

We're going to transform these to lowercase with the command palette just so that we're consistent. And I'm going to do some ordering here for the columns. But you should follow the, the business requirements, that you have outlined. For the most part.

It's generally, a good practice to have your, timestamp, columns. Anything that's around it, like dthe loaded at batched at created at those should come at the end and IDs should come at the top. So with that done, let's figure out how we're going to rename these. So I saw below here that we had, so this here C Amount.

That C is the alias for payments. So we know we're going to be, working with amount and we're also renaming that as order value dollars. But I'm going to rename this to something a little bit more clear for our case. So status or, sorry, amount is going to be called payment amount ID here.

Payment id Order id. Let's just be, let's just be consistent here. For orders we have the underscore. So I'm going to clean this one up as well.

So order ID as order underscore id. Payment method will do the same thing. Payment underscore method status. Be very clear here because we also have an order status.

Status here is referring specifically to payment status badged at. I think we can leave that one. We left that for orders as well. And then created, I'm just going to be explicit as payment created at.

Okay, now we're going to have to do some renaming so we'll see an error here. But before I go through and fix those, I just want to see if there's any other transformation logic or cleanup that we can move from our marts section into the staging section. And remember that in here, our customer order history, CTE that payments has been aliased to C. So I see this, transformation with amount, and I see that's happening a couple of times.

So what I'm actually going to do is take this logic up here, Amount as payment amount. And then what we're going to do is replace this logic so we're not performing it multiple times. That's a little better. And I think we've probably got more errors coming up here.

Refer to our payments cte. And here it's not going to be C, status, but C payment status. See what else needs to get changed. Come up here.

Okay. Need to have a comma after our CTE all. Right. Next we have an error.

Payment amount. This looks good to me. Payment amount. Okay. Order id need to have that fixed.

And then down here, let's make those changes. So we're going to be referring to our sort of raw payments. We're just going to join payments, and we have to do these. So payments amount as order value dollars.

So this part's going to be a little tricky here, and we should follow this specifically when we're auditing, because we're going to have a problem. So an order can have, multiple payments just because of the different payment methods that could be assigned to it. So calling it down here is going to fan out the results. So we'll fix this logic when we're refactoring our marts area.

But I do want to call this out as something to pay attention to. Okay. Anyway, so this is called payment amount. And then Payments.

Payment helps to spell it. Right. Status. Then we can take out that renaming. Okay. And payment stat, order underscore ID and payments payment status.

I think that's everything, but let's double check. Looks like we're good. Let's do a quick run. Make sure this runs successfully.

And it succeeded. All right, so we've created our staging CTEs with the transformations and cleanups for customers, orders and payments. So our next step is going to be pulling these out into their own staging models.

#### Building Staging Models

Extracted captions from video: Building Staging Models

All right, staging CTE is done. Time to pull them out into their own staging models. So first thing I'm going to do is create those files. So under Jaffle Shop, we've got the two have stg customers, and we'll have looks good stg orders.

Then under Stripe, we'll have stg payments. Okay. For each of those, we're going to follow a pretty standard format. So I'm going to pull the logic where I'm calling, the source.

So that's not going to exist in our fact model anymore. And then we're gonna have the transformation, let's call it Transformed as that's where we're gonna put the staging CTE logic that we did. And then we'll have a select star from Transformed, bring it all together. And the same basic model is what we're gonna follow in all three.

So I'm just gonna go ahead and copy and paste. So we have that template for orders, and replace this with orders for payments, Stripe and payments. And following that template, I'm just going to call them RAW instead of raw, customers, raw orders. So with RAW as the logic to pull from the source, Transformed as the logic.

Let me get rid of this file, too, from our, staging cte. Copy this over for customers. Looks good. Now we're referring to raw.

So I'm going to get rid of that Raw customers and select star from Transformed. Save this should be okay. Oh, need a from. You all probably caught that before I did.

Okay, let's go ahead and pull this logic over customers. Here's orders, And then here's payments. Oh, it's the payment. Okay, so this all looks good to me.

One thing that we can do also, I showed you how we, ran a query against our snowflake information schema to get all of our column names. But when you have your CTEs pull in from the source, you can also preview the CTE and see the column names, too. Id, first name, last name, same with orders can preview this, and we'll see id, user id, order, date, status, and the ETL loaded at, and then with the one column that we added. So that's another way that you can verify that you are, in fact pulling in all of the columns that you need.

And then here I can see that my transformations, are matching how I want them to look. This looks good to me. Okay, so we've created our staging models, and now what we need to do is replace, we can get rid of the CTEs, the staging CTEs and replace these import CTEs. Instead of calling from the source, we're going to be refing our staging models.

So let's start here. Can delete this nice big chunk of code. It's nice. Love to clean things up a bit.

And we'll just say with customers as like star from. We'll do a double underscore ref tab and this is going to be stg customers and click save. And then this is going to be the same thing. Instead of orders, we're going to have or raw orders in the source.

Double underscore ref tab. stg orders, click save. Instead of raw payments, we'll have payments as double underscore ref tab and stg paint. All right, so that looks like it compiled correctly.

All we need to do is test to make sure we're good. So we'll do a quick dbt run dash s to select our model. I want to build everything that's upstream of it too. So that's including the three staging models we just did.

So I'm going to have this little plus, in front of my model and that's just going to let dbt know we're building fact customer orders and its upstream dependencies. Hit enter and we'll watch this go. You can see it building my three staging models and then my orders model my fact customer orders. So we did it.

We've got our staging models done. One fun thing. We can see our lineage. We're starting to get there.

Everything's looking nice. And next up, we'll start tackling these marts models, refactoring these. So this is where like the meat of refactoring is going to come in, where we're tackle some of the logic, make it a little cleaner, a little more efficient. It's going to be a bit more of a, heavy lifting than when we did the staging models.

So See you in the next one.

#### Practice - Centralizing Logic

## Centralizing Logic

**Move 1:1 transformations to CTEs**

1. Ignoring the import CTEs, identify where the staging CTEs are. These CTEs don't conduct any joins - notate above this section of CTEs with a comment that says -- staging.

2. Identify where the marts CTEs are. These CTEs conduct joins - notate above this section of CTEs with a comment that says -- marts.

3. Remove any redundant CTEs that conduct the same transformations on the same data sets. Replace all references to any removed CTEs with the proper references.

4. In the marts area, look at each field and identify the transformations that answer Yes to both of these questions:

- Can this transformation be done using one data set?
- Is this transformation done on a field whose value is not due to a join?
- For example: case when data_set.status is null looks like it can be done using one data set, but if the status is null because the row wasn't joined with other data, then doing this earlier than where the join occurs will result in incorrect calculations.

Move these transformations to the appropriate CTE under the -- staging section of code. Ensure that when you move these, you are:

- Removing redundant transformations
- Re-referencing the CTE and field names correctly
- Giving good names to fields that don't have a good name established

5. There was not a subquery that operated only on the payments table. Create a new CTE under the -- staging area that selects from the payments CTE, and continue moving transformations that belong to payment data following the rules in step 4.

**Move transformations to staging models**

Once you're done with the above, It's time to split out the code under -- staging and create models!

1. Under staging > jaffle_shop create files called stg_customers.sql and stg_orders.sql.

2. Under staging > stripe create a file called stg_payments.sql.

3. Starting with stg_customers.sql, cut from the fct_customer_orders.sql and paste the CTE that operates only on the customers data.

You then need to structure your code as we did in fct_customer_orders.sql:

```sql
with

source as (

    select * from {{ source('jaffle_shop', 'customers') }}

),

transformed as (

    select 

        id as customer_id,
        last_name as surname,
        first_name as givenname,
        first_name || '' || last_name as full_name

    from source

)

select * from transformed
```
Do the same with stg_orders.sql and stg_payments.sql.

4. Back in fct_customer_orders.sql, ensure you've moved all of your -- staging CTEs into staging models and remove the code, if you haven't already. Change your **import CTE**s to use the {{ ref() }} function to refer to your new staging models instead of the source. Ensure everything is referenced correctly in subsequent CTEs.

5. Finally, run dbt run -s +fct_customer_orders to ensure your models build successfully.

#### Practice - Create staging models

## Create staging models

Your import files at the top of fct_customer_orders.sql are pulling directly from the source raw data, but we want that to happen it its own model, so future marts can reference those source files as well. We would like to create staging models to handle this import of the source and renaming potentially problematic fields in one place, so all future models can benefit from this.

1. Create files under models > staging > jaffle_shop called stg_customers.sql & stg_orders.sql. Here we are using the syntax stg___.sql .

2. Create a file under models > staging > stripe called stg_payments.

3. Paste the following into each file, keeping in mind: 

  a. Change id fields to _id 

  b. Make potentially clashing fields more specific, i.e. status becomes order_status 

  c. Rounding or simple transformations that you always want to happen in the future should be done here, i.e. we never want a dollar amount in cents, so we change amount to round(amount / 100.0, 2) as payment_amount

**models/staging/jaffle_shop/stg_customers.sql**

```sql
with 

source as (

  select * from {{ source('jaffle_shop', 'customers') }}

),

transformed as (

  select 

    id as customer_id,
    last_name as customer_last_name,
    first_name as customer_first_name,
    first_name || ' ' || last_name as full_name

  from source

)

select * from transformed
```
**models/staging/jaffle_shop/stg_orders.sql**

```sql
with 

source as (

    select * from {{ source('jaffle_shop', 'orders') }}

),

transformed as (

  select

    id as order_id,
    user_id as customer_id,
    order_date as order_placed_at,
    status as order_status,

    case 
        when status not in ('returned','return_pending') 
        then order_date 
    end as valid_order_date

  from source

)

select * from transformed
```
**models/staging/stripe/stg_payments.sql**

```sql
with 

source as (

    select * from {{ source('stripe', 'payment') }}

),

transformed as (

  select

    id as payment_id,
    orderid as order_id,
    created as payment_created_at,
    status as payment_status,
    round(amount / 100.0, 2) as payment_amount

  from source

)

select * from transformed
```
## Exemplar: Update references to point to staging models

Now that you have moved some simple transformation logic back to the staging models, it's time to persist that transformation into fct_customer_orders.sql by:

1. Referencing the new staging models using the {{ ref('') }} function

2. Changing any column reference from the original column names to the new column names (i.e. id instead of customer_id)

This looks like a lot of line changes, but it is fairly straightforward.

Paste this into your file if you want it to match perfectly with mine:

**models/marts/fct_customer_orders.sql**

```sql
with

-- Import CTEs

customers as (

  select * from {{ ref('stg_customers') }}

),

orders as (

  select * from {{ ref('stg_orders') }}

),

payments as (

  select * from {{ ref('stg_payments') }}

),

-- Logical CTEs

completed_payments as (

  select 
    order_id,
    max(payment_created_at) as payment_finalized_date,
    sum(payment_amount) as total_amount_paid
  from payments
  where payment_status <> 'fail'
  group by 1

),

paid_orders as (

  select 
    orders.order_id,
    orders.customer_id,
    orders.order_placed_at,
    orders.order_status,

    completed_payments.total_amount_paid,
    completed_payments.payment_finalized_date,

    customers.customer_first_name,
    customers.customer_last_name
  from orders
  left join completed_payments on orders.order_id = completed_payments.order_id
  left join customers on orders.customer_id = customers.customer_id

),

-- Final CTE

final as (

  select
    order_id,
    customer_id,
    order_placed_at,
    order_status,
    total_amount_paid,
    payment_finalized_date,
    customer_first_name,
    customer_last_name,

    -- sales transaction sequence
    row_number() over (order by order_id) as transaction_seq,

    -- customer sales sequence
    row_number() over (partition by customer_id order by order_id) as customer_sales_seq,

    -- new vs returning customer
    case  
      when (
      rank() over (
      partition by customer_id
      order by order_placed_at, order_id
      ) = 1
    ) then 'new'
    else 'return' end as nvsr,

    -- customer lifetime value
    sum(total_amount_paid) over (
      partition by customer_id
      order by order_placed_at
      ) as customer_lifetime_value,

    -- first day of sale
    first_value(order_placed_at) over (
      partition by customer_id
      order by order_placed_at
      ) as fdos

    from paid_orders
        
)

-- Simple Select Statement

select * from final
order by order_id
```
##

### CTEs or Intermediate Models
<a id="learn-the-refactoring-process-120min-ctes-or-intermediate-models"></a>

#### Order Totals CTE

Extracted captions from video: Order Totals CTE

we're going to be, focusing on any additional CTEs that we might need to make our code a little bit more modular, a little bit more legible, and then possibly splitting those out into intermediate models, wherever that's applicable. So let's go ahead and dive in, specifically with this first CTE and just try to figure out what it's doing. So the customer order history, this looks like it is aggregating our order information up to the customer level. Right?

And it's joining in, as we saw down here, payments, and then it's aggregating that payment information up to the order level. So you're joining on the order id. So in our final cte, we are joining in those aggregations from customer order history, and we're joining those to orders. Okay, so this is telling me that we want a final result that's at the level of orders, but we've got this competing grain going on here with customers.

So I think I want to split this out so that we have components that are just a little bit more easily understood. we also have this payment amount is order value dollars. And we took a note of that that we're going to want to pay attention to this specifically. I don't think this is aggregated correctly.

So this is going to be a really good spot for just starting to build out an additional component. So we'll focus on orders and payments. So let's scroll back up here just between our imports with our staging models and our marts. And I'm going to designate, a little working area for myself here, just so that I know where I'll be altering code for now.

let's, call this CTE order totals. All right? And we're going to do a select from, payments, so I know that I can aggregate our payments up to the orders level just using this stg payments model, because we did join here on our order id. So that's where we'll start here.

It's just by getting that, aggregation. So I'm going to bring in order id, because I know we're going to need that the payment status. And then, we're going to sum our Payment amount, And call it order value dollars, our final cte. So we'll go ahead and give it that name here.

All right, now something to pay attention to here is that we have this payment status. And then every column that we add to this id, that we want to aggregate on, we need to be aware of all of those values that could exist within our payment status because this could fan out our data. So, I know we have two statuses available for payment status and we can actually check that by coming here and doing a select, distinct payment status from And then we'll have our ref stg payments. And if I run this, we'll actually see those two distinct statuses.

Don't Either. There we go. We see success and we see fail. So I know that there's two.

All right, so in our original, code here, we know that that's kind of accounted for. We have a filter down here, for where payment status equals fail. We're actually repeating that filter, if I believe. Yeah, right here in the final one where payment status does not equal fail.

So we can actually move that filter up and centralize it in the process. So what I'm going to do cut that. You don't need to filter twice. We can be more efficient.

I'm going to go ahead and just put it here up in the staging area and we can also remove it from here. So sometimes you do still. need to filter in the CTE that you're working in. But since we have a.

Where, orders.order status but also an. And this is telling me that either of those can be filtered beforehand. So that's what we're going to do.

We're going to cut that. Right. Okay, so now we're already dealing with a pre filtered data set when we get down to our order totals. So that is helpful.

We've got our one order totals, CTE that we've created. And then in the next video we'll talk about how we can join that back in to orders.

#### Order Values Joined

Extracted captions from video: Order Values Joined

we've got our order total cte, and y' all might have caught this, since I'm performing an aggregation, I actually need to also do a group by. We're going to be grouping by our order ID and our payment status, also separating out our CTEs with commas, having those two fixes, and we should be, yep, compiling green. All right, so the next thing I want to do is, take a look at these, order status filter that was down here as well. Here where orders.order

status not in pending. So I looked into this. Pending is not even an option for an order status. I can show you that here.

So let's look at order status from stg orders. Let's just run that real quick and you can see what I'm talking about. Select distinct is going to just select each, distinct value that a row could have for this column. And so we don't even have pending as an option.

So this filter that we had down here is doing nothing for us. So before you remove any kind of filters from your CTEs, make sure that you double check with someone on your team who would be very familiar with that model and the data before you get rid of it. But for our case, we can go ahead and get rid of it, and we will so delete that. All right, and now the next step here, is to join in, our aggregation here and with our orders.

And I'm going to just call that order values, order values joined as. We're going to perform a select, And what I want to do, so I want to preserve all of the order information because our final data set, if you recall, is at the level of orders. So we're going to select, orders dot star. But then we're joining in our, order totals above.

And I want to take in my payment status and I want to also take in my, order value dollars, that aggregation. So we're going to pull that in from orders. We're going to, join specifically, we're going to do left join on order totals, and we're going to join that on orders. Order ID equals order totals dot order id.

All right, this looks good to me. Let's do a save. Oh, we have a comma to separate our CTEs. Okay, so now we have all of our orders with their aggregated payment information.

And that's great. That's exactly what we want.

#### Centralizing Case When Logic

Extracted captions from video: Centralizing Case When Logic

one of the next things that I would like to take a look at are these, case whens that we've got. So running aggregations on a case when it's a little bit messy. So what I want to do is move this logic, we can even see we have the same logic repeated. So it's a really good candidate to move out into an earlier model, especially since we can see here, both of these fields are available in our stg orders model.

So I think that's going to be a good place to put it. So I'm just going to copy that over. Let's go to our stg orders model and let's put it in. So I've got order date, order status, and I'm just going to paste it in right here, Clean it up a little.

We need to give it a name. Let's call it, valid order date. All right, give that a save. And we need a comma.

Give it another save. All right, so this is the name of the field that we just used to replace that logic. And let's go make those replacements, clean things up a bit. So I'm going to just delete and replace.

Looks good to me. Much nicer, easier to follow. Beautiful. Right, we'll look at this, later.

So it would be great if we could reuse that logic here. The valid order date logic that we just wrote. So what I'd like to do is just that. So you definitely want to double check with your team, whoever is closest to the legacy model, closest to the data itself.

But for our case here, we could do this. So let's do it. So I'm going to just rewrite this logic to be using the logic that we just created. So instead of calling orders, order status, we're going to refer back to our valid order date.

We're going to say when it's not null. Yeah, as non returned order count. And we can actually just use that same logic here as well and also here and here. All right, that looks good to me.

Okay, so I'm seeing we've got an error, so I'd like to know. Here it is. It is just called status actually here. So far we have not renamed it as of yet.

Status not in. And this should be good now. Okay. All right, so next we'll do some cleanup here.

Instead of the payment amount, we should be able to, to pull in. I don't think we even need to join on the payments table anymore since we've got our order totals and our order values joined. So we'll do some cleanup, and I think we'll pull some of this logic into an intermediate model. See you in the next one.

#### Int Orders and Cleanup

Extracted captions from video: Int Orders and Cleanup

we've got these two CTEs, performing aggregations for us to fix that order value dollars. We've pulled out some of the case when logic and moved it into our staging our stg orders model. So that's cleaned this up a bit and we've been able to reuse that logic pretty much across the board here. So the next step, I actually want to, split these two CTEs into an intermediate model.

And what we're going to do is call it, int Orders, since we are at the orders grain here. So under our models in our marts, I'm actually going to create a new folder. We're going to call it intermediate, and then I'm going to create a file in there int orders SQL. All right, now everything that I need for these two CTEs, we can go ahead and just cut them.

This whole working area over, do all of that pasted into here. And we're going to need a little bit more. So I need suck star from our order values joined. Okay, I need to have my imports now.

So both of these payments was the, the first one. And that's going to be referring to our ref. So that's double underscore ref tab. That's our stg paints model.

And then from here we were joining, into orders. So I need to make sure that I have that as well. That's one of our dependencies for this intermediate model. So orders as.

And that's going to be another select star from, double underscore ref tab stg orders. Let's click save. Make sure this looks good. Oh, we need a comma to separate our CTE and remove that comma.

All right, I can check out my lineage. This looks nice. It's combining those two together to perform that aggregation of payments at the orders level. And now we can do a little bit of cleanup.

So over here I don't need to be pulling in my staging models anymore. And I think that's an important distinction. I do want to have this, now in my intermediate model. So I'm just moving that payment status filter into the intermediate model so that I can go ahead and get rid of this.

So orders is going to be refing instead of stg orders. It's going to be reffing now in orders. Let's. And let's click save.

All right, we're going to see some errors mainly because we still have references to the old payments import CTE that we had. So we need to go swap those out. So anywhere where we See this? See payment amount.

So that's actually going to be referring now to our orders order value dollars. So let's go ahead and copy that and we'll fix that here. And we don't need this at all anymore. This left join onto payments that was done now earlier within our intermediate model.

Okay, let's click save. I think we're still going to have some things that we need to clean up. Yeah, down here. Same here.

So orders dot order value dollars. We still need to make sure we pay attention to that when we're auditing. And this is now orders paymentstatus. We can get rid of this join into payments as well.

Let's click save. All right, great. So our last join is on the customers model here. Since that's just the one join that's left, I think it should be fine to stay in our, fact customer orders.

It's letting us know that now we are combining, our aggregated payment and orders information to our customers and providing that fact view for us. So I think that's fine. Let's go ahead and give this a run. We'll do a dbt run s for select the plus to make sure that we're building any upstream dependencies like this int orders model, but also the staging orders model that we edited.

And then we'll select fact customer orders. Let's give it a run. And fingers crossed, it works. You can see build, build, build, build, build.

You love to see it. Love it when it works. All right, so we've done some pretty good cleanup here. And let's take a look at our lineage.

So let me go ahead and even update this graph a little bit more. So now we can see the flow from our original sources, to our cleaned up staging models, to our aggregated int orders, all the way here to our fact customer orders. And the good part about this lineage is now all of these models that we have built will also be available to any other models that might need to reference that same cleaned up or aggregated data set.

#### Practice - CTEs or Intermediate Models

## CTEs or Intermediate Models

**Continue to reorganize code**

1. Move the filter for payment_status found in the customer_order_history and final CTEs to the import CTE for payments, so we are working on a limited data set before our calculations and transformations.

2. Remove the filter on order_status - this doesn't actually filter out anything.

3. In fct_customer_orders, create a new CTE above the customer_order_history CTE. Call this CTE order_totals. From the payments table, get the order_id, payment_status, and the total amount of the order - the final result of this CTE should be at the order_id grain.

4. Under the order_totals CTE, create a new CTE called order_values_joined and join orders data set with the previous CTE to get a new result set of all orders with associated payment status and total information.

5. In the final CTE, since payments information will be included with orders in future work, remove the join to the payments table and rereference any fields from payments. to orders.. Do the same with customer_order_history's reference to payments data.

6. In the customer_order_history CTE, copy the case when orders.order_status not in ('returned', 'pending') then order_date end statement and move this logic into the staging model stg_jaffle_shop__orders as valid_order_date.

7. Back in fct_customer_orders, reference the orders.valid_order_date anywhere the case when statement is written.

8. The case when orders.order_status != 'returned' then 1 end was a piece of logic that was supposed to be changed to the new logic on not in ('returned', 'pending'). Replace this with the new field from step 6.

9. Places where there is the order status logic, but assigning a different value for the then clause can simply use orders.valid_order_date is not null

**
**

**Moving logic to intermediate models**

Lastly, some of the logic in your fct_customer_orders.sql we might want to reuse in later marts, such as paid_orders and completed_payments, so let's create an intermediate model with that logic which we can then reference in our fact model.

1. Under your marts folder, add a new file: marts/intermediate/int_orders.sql. This will add a new subfolder and file at the same time

2. Paste this into the int_orders.sql file:

**models/marts/intermediate/int_orders.sql**

```sql
with 

orders as (

  select * from {{ ref('stg_orders') }}

),

payments as (

  select * from {{ ref('stg_payments') }}

),

completed_payments as (

  select 
    order_id,
    max(payment_created_at) as payment_finalized_date,
    sum(payment_amount) as total_amount_paid
  from payments
  where payment_status <> 'fail'
  group by 1

),

paid_orders as (

  select 
    orders.order_id,
    orders.customer_id,
    orders.order_placed_at,
    orders.order_status,
    completed_payments.total_amount_paid,
    completed_payments.payment_finalized_date
  from orders
 left join completed_payments on orders.order_id = completed_payments.order_id
)

select * from paid_orders
```
3. Remove that same logic from fct_customer_orders.sql

4. Remove helper comments we added for the course (i.e. - Import CTEs)

5. In the final file, be more explicit with ordering of window function subclause. This fixes a future potential bug where if there are multiple orders placed on the same day for one customer ID, this would cause indeterminate ordering.

This is what you should end up with as the final file:

**models/marts/fct_customer_orders.sql**

```sql
with 

customers as (

  select * from {{ ref('stg_customers') }}

),

paid_orders as (

  select * from {{ ref('int_orders') }}

),

final as (

  select
    paid_orders.order_id,
    paid_orders.customer_id,
    paid_orders.order_placed_at,
    paid_orders.order_status,
    paid_orders.total_amount_paid,
    paid_orders.payment_finalized_date,
    customers.customer_first_name,
    customers.customer_last_name,

    -- sales transaction sequence
    row_number() over (order by paid_orders.order_placed_at, paid_orders.order_id) as transaction_seq,

    -- customer sales sequence
    row_number() over (
        partition by paid_orders.customer_id
        order by paid_orders.order_placed_at, paid_orders.order_id
        ) as customer_sales_seq,

    -- new vs returning customer
    case 
      when (
      rank() over (
        partition by paid_orders.customer_id
        order by paid_orders.order_placed_at, paid_orders.order_id
        ) = 1
      ) then 'new'
    else 'return' end as nvsr,

    -- customer lifetime value
    sum(paid_orders.total_amount_paid) over (
      partition by paid_orders.customer_id
      order by paid_orders.order_placed_at, paid_orders.order_id
      ) as customer_lifetime_value,

    -- first day of sale
    first_value(paid_orders.order_placed_at) over (
      partition by paid_orders.customer_id
      order by paid_orders.order_placed_at, paid_orders.order_id
      ) as fdos
    from paid_orders
    left join customers on paid_orders.customer_id = customers.customer_id
)

select * from final
```

### Final Refactor
<a id="learn-the-refactoring-process-120min-final-refactor"></a>

#### Customer Orders CTE

Extracted captions from video: Customer Orders CTE

we've split up our legacy code into some CTEs and into staging models and then an intermediate model. So our final step in refactoring is our marts CTEs. So we've got two our customer order history and our final CTE down here. And our goal here is to make these both just more understandable, more legible.

So that, not only is it easier for us to follow and read, but also for our team and for any future onboarding developer or analyst. So like I said, we've got customer order history and we've got the final one. So the final step that's actually happening here is joining in on our customer, information. So I think that this step can be done in maybe one, maybe two CTEs.

So that's going to be our goal when we're cleaning up the rest of this model. So let's start there, pulling in this join on customers just a little earlier in the process. we'll call this CTE up here and make my working area again and we'll call this cte. Just to be very clear, customer orders.

Since we're pulling in our customer information. So it'll be a select from orders and it'll be in inner join on orders. Customer ID equals customer customer id. All right, so to recap just really quickly there, we're going to do an inner join here because we want, only data from customers in orders that can be matched.

So meaning we only want orders that have a customer and we only want customers that have an order. So we're going to pull in everything from orders. Right? And then we're going to just start adding in our customer information.

So we have customers and we have full name, we have customers. Spell it correctly. Let's do given name and customers surname. Okay, so we've got those three values and then we'll start doing our customer level aggregations.

Okay, so now we can look down here at customer order history and what I'm going to do is just copy that. I'm actually going to switch the order of these since I see that's how they are in customer order history as well. I'm actually just going to copy all of these aggregations over and then we'll start tweaking them as needed. Okay, so copy and paste.

All right, so how are we going to do our aggregations now? So I think the best way is to use a window function. So over, partition by. So that's what I'm going to Add in here.

So we have min order date, and we'll have an over. And we need partition by customer ID as first order date. Okay, looks good. So the, the window function here, the over partition by is performing a calculation for us across a window or a group of rows, but kind of similar to group by.

But unlike groupby, it's not going to collapse those rows so it's going to keep all of our original rows and then it's just going to add the calculation as a new colum. So the window function here allows us to get that group level total, again similar to a group by. But we're stamping that total back into the individual rows. So I'm going to just copy this and put it in wherever I see it needed.

So here as well, and here as well. Okay, so that takes care of those three and then this next one. And just really quick too. We could have done these customer level aggregations back in int orders too.

Just to be very clear about that. But having them here is more by design, right? So for like an analyst, the aggregations make a little bit more sense for specifically when you are joining in the customer information. So if like another analyst is onboarding and they're going to be looking for where these aggregations are performed, they would probably start to look here where we're joining in customers.

So I think leaving it here is the best design choice. So we're adding this over partition by to aggregate by customers throughout. Now another call out too, since we do have this repeated logic, right, we're adding in this over partition by customer ID in multiple places. That is something that you could template out with Jinja in dbt.

But I think Jinja's best saved for things that are a little bit more difficult or complex than this. So we'll leave this here as is. Anyone coming in and inheriting this project will understand the SQL. Whereas Jinja can be a little trickier to understand.

But again there's always a trade off. So like if this logic needs to change, that means you'd have to change it in every place that you have it outlined here. Whereas if you do template it out with Jinja, then you would only need to change it in that one spot. So this is a design choice that you're making by doing it like this.

Let's take a look at this here. So this one is giving us like the sequence, right? But I think for our purpose it's easier to do a count star and then our same over partition by that we're doing as order count. So let me show you what that's going to look like.

We can double check, you know, when we're auditing and see if we still need to have the coalesce. I don't think we do. So let's just take a look at what this is going to look like instead. Of coalesce we'll do count star and then our over partition by customer id, as order count.

Okay, so this is giving us essentially the same thing here. I'm gonna drop this if we need to. After we audit, we can go back and add that coalesce.

#### Customer Level Aggregations

Extracted captions from video: Customer Level Aggregations

Okay, right where we left off, here with these coalesces. So I think we can make this one a little bit simpler too. Instead of doing a coalesce we'll do a sum. Coalesce in this case when we'll do a sum NVL2.

So that's going to mean when our orders valid order date is not null, then it will return the first input, otherwise it will return the second input and then that will be summed as our non returned order count here. So let me just show you what that will look like. I'm going to comment this piece out. That's what we're refactoring.

And so this is what I mean by that. So sum and NVL2 again it's just doing something similar here. This is our what we're going to put in our orders valid order date and if it is not null that'll return this. Otherwise it'll return this.

Okay, so our valid order date comma and we want it to be either a one if it's not null or a zero if it is and we'll sum those. So that looks good to me. Now the next piece is that we need to have our just like above, we're doing this at the customer level. So we need to have our over partition by here as well.

So over partition by customer id that looks good as and it's named non returned ordered count. Okay so these two are returning the same thing for us. But I think that this version is a little bit easier to understand and easier to read. And then also anytime you're performing any kind of aggregation on a case when statement it's a little less performant.

So performing it this way is going to be a little bit more efficient for us. So let me get rid of this and we're going to do the same thing for pretty much all of these. So that was our non returned order count. Let's take a look at this one the total lifetime value.

So I want this to be same. I comment that out. So sum in BL2 and this is another valid order date. But this time we're doing order order value dollars or zero.

Okay and similarly I need my over partition by I'm just going to copy paste and then as this is our total lifetime value. So a little cleaner to read a little easier to understand. Delete that. Okay, now this is where it gets interesting.

So what we have here is something I kind of want to tackle in a second. But I want to split this out, I think, into its own cte. So we're essentially doing our, total lifetime value here and dividing it by our non returned order count to get our non returned order value as an average. So instead of performing those two, aggregations separately again, I want to just reuse what we built up here, in a different CTE that we can then just kind of join together.

So I'm going to take this and pull it out. We'll put it down here for now and we'll be handling that in just a moment. Okay, so let's take a look here. Our, array aggregation.

So this one just needs another over partition by. Okay. Okay, I think this looks good, but I want it to be like that. Okay.

Our order ID, customer ID as order IDs. Okay, so this looks good.

#### Implementing an Intermediate Model

Extracted captions from video: Implementing an Intermediate Model

So I pulled this piece of logic into its own separate cte. Again, just because I don't want to have to restate this logic one more time. To recap, this is essentially what we did above our total lifetime value divided by our non returned order count. So what I'm going to do is have a select, star and then instead of having this all typed out like this, we are going to just copy paste total lifetime value divided by our non returned order count.

As. And then we had named this as average non returned order value. Okay. So that gives us the same piece without having to restate that logic again.

Right. And then this is coming from customer orders. Okay. So I feel better about that.

That was pretty simple. The next thing I want to do is clean up a little bit and make these a little bit more legible, or at least a little bit more explicit with what they, what they are. So what I mean by that is in this CTE we're joining in our customer information. So I want to be very clear that that's what we're dealing with here, that this is the first order date.

It's specifically the customer first order date. This is the customer first non returned order date. So I want to give these names even though they're longer, I want them to be as explicit as possible. And then just so that we're not breaking any dashboards, these are customer order IDs.

We're not breaking any dashboards or anything that will be dependent upon this model. We'll have them renamed as needed in our final CTE as well. Okay. Then this is going to be Customer Total lifetime value, Customer non returned order count as Customer Average Non returned order value.

Okay. So I feel better about that. Let's give this CTE a name as well. We're going to call it, Customer Average Value as.

Let's call it Customer Average order value. Okay, just being very clear here. Now we don't need this customer order history CTE anymore. We've done our aggregations above.

We pulled that logic out earlier. We also pulled the join out earlier. So we can safely get rid of this. Okay.

And then let's clean this up. So we'll be pulling this all from our customer average order value. Let's change that name as well. Values.

We're pulling order id, customer id, surname, given name. Okay. Order value, dollars, order status, payment status. All of that's coming from orders.

Couple of things. I think these ones are the ones we need to rename. So this is going to be customer first order date as, first order date, customer order count, order count, customer total lifetime value as total lifetime value. And the rest should be good to go.

Okay, and then we have our select star from final. All right, so I think we're cleaned up. What I'm going to do now. Let's get rid of some of these notes.

Got our, mart CTEs, our final select and the select star from final. Okay, let's, give this a save and see. All right, I see some errors that we need to take care of. Let's see where they are.

Inner join on. Yeah. Okay. Inner join customers on, orders. Customer ID equals customer customer id.

Okay, that looks good. And then back up here. Oh, this is going to be an ambiguous column name. Yeah, so we want to do orders.

Customer id. Be very explicit there. Save. All right,

#### Final Cleanup

Extracted captions from video: Final Cleanup

All right. So, couple of things. Number one, we had moved our division logic, into its own cte. we actually ended up getting this error division by zero.

Now, when I go to run this model, I want you to pay attention to something. This is going to succeed. And the reason for that is because this column, even though we're creating it here, it's not a part of our final. Right.

We're not including that down here at all. So there's a couple of things that I want to do. Number one, we're going to flag this as something we, need to have a safe divide by zero. So I'm going to flag that as potentially something that we can fix.

But in the meantime, since we're pulling out some and creating some columns here that we're not even using in our final, but we might use them in another model, downstream, we want to have this information available. So on second thought, I think this is a good case to take it out into an intermediate model. So what I'm going to do is just like we had with our int orders, I'm going to create an int Customers. Since this is at the customers grain, I'm going to cut this from here and add that file here.

Int customers. So this still has all of our customer aggregations in one centralized area that, our analysts will be able to view pretty easily for us. So we have our customer average order values as that and then our final as select star from customer average order values. Okay, let's give that a save.

Oh, right. Don't need that comma there. From our final cte. All right, so this looks good.

And that means in our import area, we need to have a. With, customer orders as select star from. In our double underscore ref tab int Customers. That model there.

Let's give that a save with the comma. There's our import, our final. Rename that. Okay.

And then our final select. So we've extrapolated that logic out, and now we have a place where we have all of these aggregations performed. And while we don't need them for our fact customer orders model, we have them available for another model that might want them. Let's take a look at our lineage reset update can see stg customers and int orders.

Let's actually go back three. And we can see customers, payments and orders. These both combine then into int Customers. And then we have our fact customer orders.

Okay. So we've created a nice lineage to follow. We've got our columns renamed. We have the column highlighted to audit.

We've made a note here of, something that we're going to want to check out again. And I think I have a perfect use case for how we can fix this. So this all looks good to me. And what's left, then, is to do the auditing.

And it's equally as important as refactoring. Right. We want to run an audit, make sure that our data matches across the legacy and the refactored. So data integrity, data validation, those are crucial.

Refactoring is pointless if we're not actually getting the data that we need.

#### Practice - Final Refactor

## Final Refactor

We're going to clean up our fct_customer_orders model to polish it up a bit.

1. Create a new CTE called customer_orders above the customer_order_history CTE.

2. In the customer_orders CTE, select from orders and inner join customers.

3. Within the select statement of the customer_orders CTE select orders.*, then copy all fields and aggregations from the customer_order_history CTE and paste after.

4. Turn all of the aggregated fields into window functions, partitioning by orders.customer_id. Extra cleanup:

- order_count can be made more inherent as count(*) over (partition by orders.customer_id)
- non_returned_order_count can be simplified to sum(nvl2(orders.valid_order_date, 1, 0)) over(partition by orders.customer_id)
- total_lifetime_value can be simplified to sum(nvl2(orders.valid_order_date, orders.order_value_dollars, 0)) over(partition by orders.customer_id)
- Create a new CTE called add_avg_order_values and select * from the customer_orders CTE and add the calculation for total_lifetime_value / non_returned_order_count as avg_non_returned_order_value. Remove the avg_non_returned_order_value field from the customer_orders CTE.

5. Remove the customer_order_history CTE - all of this should be covered in our new CTEs.

6. Keep the final CTE in place for auditing purposes - go through the fields and ensure the correct columns are referenced and named back to the legacy version's final field names. This is for auditing purposes, and can be removed later.

7. Conduct a dbt run -s +fct_customer_orders to ensure your models build successfully.

#### Knowledge check

### Auditing
<a id="learn-the-refactoring-process-120min-auditing"></a>

#### Audit Helper Package

Extracted captions from video: Audit Helper Package

Okay, we did it everyone. We're in the home stretch. So we have wrapped up, our final fact model, refactored our legacy code. It's more legible, it's more performant.

But the big kicker is, is it accurate? Do our results match our legacy results? And if we do have changes, are they expected? So for example, we will expect to see one mismatch when we audit in our legacy.

If you recall, we were fanning out this order value dollars, that order amount, the payment amount. So it was really just grabbing the payment amount in general. So we fixed that aggregation up in our int orders model. So we do expect to see that fix and you'll see what we mean when we get there.

So let's audit. How can we do that? There's a couple of ways. Row count comparisons and minus queries are generally like the first step.

You can run those manually, there's no problem with that. You can do that in like a snowflake worksheet, and then you can export those to a spreadsheet. Do your own little comparison checks, verify that the changes are expected. But I don't know about you, I don't really like doing manual testing of anything.

And what's great about dbt is that we already have some pretty fantastic pre made tools that handle things just like that. So we don't need to manually audit everything and manually verify everything. So for example, we're going to try out the dbt Audit Helper package. So that's over here, the first step we need to do.

You can get these at the hub.getdbt.com this one you can see is created by dbt Labs and it's also maintained mostly by dbt Labs as well. So we need to include this in our packages YAML file. So we'll just copy paste that come back over to Studio and if you don't have a packages YAML, you can create one just right in the root of your project.

I already have one and you can see I already have my package, over here as well. But you'll copy paste that in save and run a dbt deps and that's going to install the package for you, making those macros available for us. So this package has definitely gotten a couple of makeovers since it first came out. Notice that the legacy macros are still here.

These two main ones compare queries and compare relations. But I'd like to actually start off by running some of the ones that we see up here. So compare row counts first off, is a good place to start. That's your cheapest, fastest check.

It's simply going to compare the total number of rows between two tables that you give it. So the legacy one and then the refactored one. And it'll tell you if one has more or fewer rows than the other. It's a very simple check.

And you should definitely run it. If there's a row count discrepancy, then you know that there is either an issue somewhere or at least something that you need to highlight in your audit report. So you can take a look over here at what that macro does in the docs by clicking on it. And you can see, the code that you can use like as a template.

So I'm going to copy that over into Studio. I'm going to create a new file up here. Not a file that's going to live in my project, just a file like a working area. So you click over here.

I'm going to paste that in here. Okay. May create some separation. And just for my own sake, I want to have this be pretty legible so that I and others know what I'm doing.

So this is going to be my compare row counts. Then I'll have another section down here. So other than the row count comparison, I also would recommend doing this one. Compare all columns.

It's sort of the replacement for this legacy one, the compare relations. It performs a very deep comparison of the data itself. It's going to join your tables on a primary key and, and then check, every column, for any mismatched values. So let's take a look at that and you can see what it would return as well.

Perfect match, null, null, missing, missing any number of conflicting values. And I can see what this will look like here. And I'm going to copy that over as well. Okay, this one is compare column values.

All right, so I've got the package installed. I've made my little file. I'm going to do a, just a basic dbt run to make sure everything that I've got is up to date within my project. Can say customers, orders, payments, my legacy, my int orders, my int customers and my fact customer orders.

Okay. Everything built. And now we're going to go into running some checks. So, I'll see you in the next one where we start running these audits.

#### Running Audits

Extracted captions from video: Running Audits

All right, so we've got everything set up. We've installed our package and now let's get into it. So we're doing a comparison between the old and the new. So our database for our old one is Target Database, our schema.

I have it built in my own schema. That is dbt_jstayton and the name of that one is, right here. Customer Orders Legacy. Okay.

Our dbt relation is Fact Customer Orders. And what I want to do is get that row count. So if I highlight it, I'm on a Mac, so I'm going to hit Command and return. If you're on Windows or a PC, it'll be Control Enter, and you'll see dbt Send that, to your data platform and load the results.

Now we can see a couple of things. The relation, that's our legacy and the one that we built. The total number of records is different, which does mean we need to dig a little bit deeper. I'm going to make a note of that here.

Our legacy count is 113 and our refactored is 99. Now, if you recall, again, we did have our order value dollars, when it was just calling in the payment amount, that was fanning out the results. Right. So we do expect to see some discrepancies, but we want to make sure that those are the only discrepancies that we see.

Right. So let's take a look at the deeper dive here at the compare column values. So I'm going to have the same thing. This is our target database.

My old schema is dbt_jstayton, and this is our, Customer Orders Legacy, just like we had above. And this one is Fact Customer Orders. Our primary key, since this is doing a comparison matching on our primary key, is going to be order id. So that works for us.

We don't have to change anything there. And then there is one important thing that I want to, point out here. So above, these row counts are stored as metadata in our data platform in Snowflake. So this above check runs very quickly.

However, since we're comparing the actual row values across columns here, we need to wrap this statement where we're actually doing that comparison in the Jinja if execute. Okay, so this block tells dbt, to run the code inside of it here during the execution phase. So that's when dbt is going to take its compiled SQL and then actually run that compiled SQL against your data platform. So we want it to run during execution, not during that initial parse.

So the parse is when dbt reads your project files. So the yamls, the SQLs, and it builds the whole dependency graph and figures out the relationship between your models. So we want this to actually be executed and not just compiled. Otherwise we won't get what we want to see.

So now I'm going to highlight this, and same thing. I'm on a mac. So it's command return. It might be, control enter.

If you're on a PC, you can see it takes a little bit longer for this one here. All right, so we see some perfect matches. This looks good so far. So in the next video, we'll dig into, this status here, what we have returned.

And we'll figure out how we can read this result.

#### Reading Audits

Extracted captions from video: Reading Audits

All right, to recap really quick, when I ran my row count audit comparison, I did see that my legacy had 113 and my refactored had 99. So again, this could be a red flag, but we're going to table that for now and check out our column values. Right. So if I look here, this actually looks pretty.

Okay, we have a lot of perfect matches except for here, our order value dollars. So remember before, again, we were fanning out those payment amounts, whereas now we've got them fixed and we have them aggregated at the customer and the orders level. So we can verify this by actually checking out the compiled code and digging a little bit deeper. So I want to get this, and let's look at the compiled code.

All right, what I'm going to do is copy this over. This is pretty long. I'm going to copy this over into another file and we can just kind of tweak it a little bit. This is the compiled, test essentially that dbt sent over and ran for us a pretty long SQL query.

So what I'm going to do is get rid of this final CTE at the bottom, since I want to see the results individually and I know that the changes that we are seeing are specific to the order value dollars column. So that's what I want to filter for. So instead of this, I'm going to have a select star from, and our main. You'll see here.

Yeah, this is just a big old subquery that's combining all of the union subqueries. Right. To get all that information per column. So I'm going to select star from main and I want to filter where our column name.

Let me take a look up here a little more. Yeah, where column name equals order value dollar. And perfect match. We came back over here to our results.

Perfect, match equals false. Okay, so I'm going to run all of this. Let's see what happens. Okay, so this is going to return specifically, those 25 results from the first one, our first comparison, where we have those mismatched primary key values.

So I am expecting to see again that the order value dollars was fanned out. So I think we're going to have multiple order IDs in the legacy that are going to correspond to a single order ID in, our refactored version. So let's just verify that. Can see we've got conflicting values.

They're not missing from each other, so we haven't created a new thing. And we have multiple primary keys and in some cases, just a single one. Like I see just 1 77, just 1 9. So I'm wondering if those are where the value was zero for that payment amount and that just, didn't get included in our refactored version.

And then we got some where we have three right there with 25. Okay, so let's double check that.

#### Final Audit

Extracted captions from video: Final Audit

So what I'm going to do is with legacy as and I want to select my order ID and my order value dollars, from if this is customer orders legacy, okay. And refactored as, we're going to do the same thing, our order ID and our order value dollars from, when I need to select. And I want this one to be fact customer orders. Okay?

And now, this is where it's going to get a little tricky because I want to be able to see, everything from both. So I'm going to do a select, and I want to make sure that I have a null value if it doesn't exist in the other. So I'm going to do a coalesce and we're going to call this the legacy order ID and the refactored order ID as order id, we're going to have the same thing except for order value dollars. Okay.

And then I want to know whether or not it exists in legacy or exists in the refactored. So we'll have a legacy, order ID is not null as in legacy and a leg, refactored order id, we need that to be a dot is not null as in refactored. Okay? This is from our legacy.

We're going to do a full outer join because we want those null values too refactored on our legacy order ID equals refactor order ID and our legacy dot, order value dollars equals refactored order value dollars where specifically and legacy is not equal and refactored. And we'll Order by order ID just to make it a little simpler for us. Okay, So I think that's fairly easy to read. I think that's going to give us what we want to.

So let's go ahead and run this and see what we get. Okay, perfect. So we can see in legacy and we can see in refactored. This one for example, is false.

That's what I thought. So this order ID that was a 9. We only saw one order ID of 9. It does not have any value in dollars to it, but it does exist in the legacy.

It's tracked there and it's not in our refactored. So this is fine. Over here, let's look at order ID of 13 in Legacy. In legacy.

Both of these are true, this is false. And this one's false. And this is true. So we had our fanned out data and now our aggregated data.

So we had an order of 5 and an order of 14 and those do add up to equal 19. So now, we have correctly summed that payment amount per order ID at the customer level. So this is an expected change that we want to. We see.

That we want to see. It's welcome. Actually. Let's check this one. Order ID of 18.

Okay? These two are in our legacy model and not in our refactored. And this one is. So we had an eight and a five.

And those do add up to 13, so that's good too. And here with 25. Okay. Oop, we had another one there.

So we had three in our legacy and only one in the refactored. So 20 plus 22 plus 16 does equal 58, so that's a welcome change as well. For 49, we had six and nine. That does equal 15 looks good.

So I'm not going to go down this whole list. But this is how you could dig in to see those specific, numbers. So this all, to me looks good. This is expected.

And not just expected, but actually a welcome change. We have fewer rows in our refactored table because we were fanning out the results in our legacy table. So we had multiple order IDs in the legacy table, whereas we aggregated those together in a refactor. So our audit looks good.

Our changes are not just expected. Again, they are welcome. We have proof of it. We can download our proof as CSVs so that we can share this with our team.

So, yeah, this all looks very good to me. There's one more piece that I want to, check out in addition to our audits that we've performed. And remember, you can perform more audits as well. But for our purpose, I think we've covered everything that we need.

There is one more piece that needs to be addressed. And it was this piece down here where we potentially are dividing by zero. So what I want to do is take a moment to, investigate a new functionality that we have in dbt where we can create and manage UDFs straight from dbt. This could easily be a macro, but we'll talk about this in the next video.

All right, thank you.

#### Practice - Audting

## Auditing

1. In your project, in the root folder, create a file packages.yml

Paste the following into the packages.yml file:

```
# packages.yml 

packages:
  - package: dbt-labs/audit_helper
    version: 0.12.2
```
2. Run dbt deps in the command line

3. Create a blank file as a scratchpad.

Paste the following into the scratchpad:

```
{% set old_etl_relation=ref('customer_orders') %} 

{% set dbt_relation=ref('fct_customer_orders') %}  {{ 

audit_helper.compare_relations(
        a_relation=old_etl_relation,
        b_relation=dbt_relation,
        primary_key="order_id"
    ) }}
```
11. Hit the Preview button or click `command + return` on a mac and `control + enter` on a PC

### User-Defined Functions
<a id="learn-the-refactoring-process-120min-user-defined-functions"></a>

#### Intro to UDFs

Extracted captions from video: Intro to UDFs

all right, so models aren't the only thing you might want to bring into dbt and Refactor. For instance, now dbt supports natively our user defined functions. These are similar to macros, they promote code reuse. But they are different from macros as they are objects that are built within your data platform.

So you can reuse that same logic in tools that are outside of dbt and not just within dbt. So things like your BI tools, your data science notebooks, and etc. Right. So these are particularly useful for sharing logic across multiple tools where you're standardizing, some complex business logic and calculations, or even improving different performances for compute intensive operations.

So these are compiled and optimized specifically by your data platform's query engine, but now you can have them version controlled with custom logic within your dbt project. So let's quickly walk through what that is is going to look like for us here. So say I have this udf. It already exists in my data platform, which is Snowflake here.

I have this essentially little template that's defining this for me. It includes the schema where this is built, the database where this is built, the name of the UDF itself. And then here we have the arguments that this UDF accepts, a first name and an id, and then the data types that it needs, a varchar and a number, it returns a varchar. And it is in the language of SQL, right?

This part itself within these single quotes is the actual logic of the udf. Right? So this is defining the udf. Essentially what, what's needed about the udf.

And this is the logic that the UDF performs on those different parameters that you pass into it. So when we are defining that out in dbt, you're going to use two different files. You'll have the SQL file. Let me make this a little larger there.

You'll have a SQL file in your functions directory and that's going to contain the logic itself, right? So for this one it's going to contain this logic and then you'll also have a YAML file that has the different configurations and properties, the return type. So, so within your functions directory you'll have the function schema and you'll just fill in these different values for it. So the name of it description, that's optional.

This is optional too, a schema or a database. Otherwise it's just going to build it in your default ones. The arguments that it takes the name of them and the data type. Definitely recommend passing those in as long as as well as a description, if it's not very obvious and then the return value of it.

This schema file that you have for your function is going to essentially help build out this template for it. And then the SQL file as you can see is just the actual computation that that UDF is performing.

#### Creating a UDF

Extracted captions from video: Creating a UDF

we had already identified this section here. When I try to preview my int customers model I get an error with divide by zero, meaning that in here we are, we have some customer non returned order counts that could be zero and when we're trying to divide by zero we get an error. Right. This did not break our fact customer orders model since we're not pulling this column in, but it's going to break anything that might rely on this data, downstream that we build out.

So it's good to fix this now. So this could be handled with a macro and that's totally fine if you want to do that. But we also might want to say have this kind of safe division logic available for our BI analysts. So what I'm gonna do is create a UDF within my project that I can call here but also have available in Snowflake, for anyone else even outside of a dbt project to use.

So like we showed last time, we need to do a couple of things. We need to create our functions directory, we need to create a SQL file to hold the logic and we need to create a YAML file to hold like the configurations for it. So off the root I'm going to create a file and call it functions or a folder and then within there I'm going to create we'll call it Safe Divide SQL SQL and then we're also going to create a schema YAML file and that's going to hold these two pieces for us. So in here in the SQL is going to go the logic, but in the YAML is going to go the configuration.

So I'm going to start there actually. And that's going to help me figure out what I want this to look like. So I'm going to copy over the sample YAML that they gave us and we'll customize it from here. So I'm going to call this Safe Divide.

It's going to be the name of my function. It is going to safely divide a numerator, not a number eight ride a denominator where that value might be zero. I want it to just build in my target database and schema. So I'm going to remove this.

But if you want it to live somewhere specifically please do configure that. So my arguments, I'm going to have a numer, not a numerator, a numerator, it's going to be a number. I think that's pretty self explanatory. So we're actually going to just take that out.

I also need a denominator and that's going to be a data type of number as well. The return value is required. This is also going to be a number. Okay, so I've got my schema.

So now let's write out the logic. So I think this is a good use case for a case when. So that's what I'm going to have here. Case So when my denominator equals zero, then let's have it return a null and then otherwise we'll do our numerator divided by our denominator and we will end.

That should do it for me. Okay, double check for spelling. Okay. Looks good. Can see it already kind of building here.

So let's come here and put it in to our file. I look down here, this is how we call it. We're going to have our little jinja curly brackets function, the name of our function and then the two values that are going to go in. Okay.

Function. It's called safe divide. And then we're going to have our customer total lifetime value as the numerator. Our customer non returned order count as the denominator and then as customer average non returned order value.

Okay, let's hit save. Now. I want to make sure that my UDF, builds. So I want to do this dbt build resource type function just to be extra sure we're selecting our functions.

Go ahead and run that. Good. So it's successfully built. And now let's just do a preview of this table and see if we get the same error.

No we don't. Let's see what it returned for us. If I scroll all the way over to customer average non returned order value. Let's go up and there we're handling it.

We've got a null and another null. Everything else looks good. Okay, so we have successfully created a UDF and implemented it within our dbt project. That udf, different from a macro is now built over here in Snowflake Forest as well.

I can see here there's safe divide. If I look at the definition, let me copy that over and I can see create or replace. It created it here. The numerator, the denominator SQL and here's the logic that it ran.

Okay, this looks good.

#### Importing a UDF

Extracted captions from video: Importing a UDF

All right, what we want to do next is take a UDF that exists in our data platform for us demoing that's in Snowflake and we want to figure out how we can import that into our dbt project. So I'm going to take this one as an example. Create email. This one's already been created.

It exists in my UDF Snowflake schema, but it's not available within my dbt project for me to use. So let's look at the definition and figure out how we can port that over. Okay, so we've got our name and our arguments and their data types and the data type it returns and then the logic as well. So I'm going to come into studio and just add that to my functions schema YAML file and then create a new SQL file to go with it as well.

So this one is called Create Email. And what does it do? It looks like it takes the first name and the customer ID and generates a company name. Okay, generates a company email with a customer name and id.

We have the first name which is a varchar. Can just verify that first name varchar. It's an ID is the second argument which is a number ID number and we can be explicit here if we want to. But I think this is the default value also and it returns a varchar.

All right, going to save that and let's go ahead and create our file here. Create email SQL. What I'm going to do is take this, we're going to copy it over here and I want these to be single quotes. All right, so we've got the same logic and I'm going to run my command here, the Build select resource type function and make sure we're building that correctly.

Okay, so it should have built it in my dbt schema. That's my default one. If I refresh I can see it's right there and I just want to do a comparison to make sure that it built as expected. Does my definition match?

Yeah, looks identical. The only thing that's different is that this one exists in my UDF schema. Those are my pre built UDFs. And now this one, is in my dbt project version, controlled and maintained there, but available to the wider audience that has access to Snowflake.

Okay, everything else looks great.

## Closing
<a id="closing"></a>

### Wrap up
<a id="closing-wrap-up"></a>

#### Refactoring SQL for Modularity - One Pager

[Refactoring SQL for Modularity - One Pager (PDF)](https://ti-pdf-uploads.s3.amazonaws.com/e377e1ac-b0cf-4bfb-9046-e286a6603eaa/eizq7ysv8qjm-C4-L7-RefactoringSQLforModularityOnePager.pdf)

The above link may not work due to insufficient permissions via accessing content in an s3 bucket. In this case, please access the content directly via the course itself.

#### Quick Survey

## 4 Quick Questions!

Almost there! As you finish the course, we'd love to hear your feedback on the course in this survey here: [Open survey in new tab](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com)

#### Congratulations

## Congratulations!

Thank you for joining all of us from the dbt Labs team!!! You just leveled up your dbt skill set with refactoring best practices!

Make sure you hit complete on each of the lessons.  Check out the resources below to continue the journey, stay fresh on your skills, and share this with your fellow analytics engineers.

### **Resources**

**dbt Docs: **There is no shame in referencing the docs as an analytics engineer! Use this to continue your journey, copy YML code into your project, or figure out more advanced features.

**Short courses: **We have four courses to continue leveling up:

- **Jinja, Macros, and Packages:** Extend dbt with Jinja/Macros and import packages to speed up modeling and leverage existing macros.
- **Materializations Fundamentals, Incremental Models, and Snapshots:** So far you have learned about tables and views. This course will teach you about ephemeral models, incremental models, and snapshots.
- **Analyses and Seeds:** Analyses can be used for ad hoc queries in your dbt project and seeds are for importing CSVs into your warehouse with dbt.

### **Contribute**

- Support fellow learners and let us know what you thought about the course in **#learn-on-demand**.
- Support other beginners in **#advice-dbt-for-beginners.**

### **Feedback**

- **Bugs:** Help the training team squash bugs in the course by sending them to [training@dbtlabs.com](mailto:training@dbtlabs.com) and we will triage them from there.

Congratulations and thank you again! See you in dbt Slack! 

- The dbt Labs team

#### Get dbt Certified

By completing this course, you are one step closer to achieving your dbt certification! To continue your progress, explore the next course in our certification path and apply your new skills in real-world scenarios. Stay committed, keep learning, and join our community of experts to share your experiences and gain insights.

### The dbt Certified Developer Path

The courses on the path are:

- dbt fundamentals 
- Refactoring SQL for Modularity
- Jinja, Macros, and Packages
- Materializations Fundamentals
- Incremental Models
- Snapshots
- Analyses and Seeds
- Advanced Testing
- Advanced Deployment
- Exposures
- dbt mesh

Enroll in the next course today. Then visit [dbt-certification](https://www.getdbt.com/dbt-certification) and download the study guide to begin planning your path.  🚀🚀

---

### Metadata

- Course: Refactoring SQL for Modularity (dbt Studio)
- Generated (UTC): 2026-02-23 17:49:37Z
- Source slug JSON: response\refactoring SQL for modularity\slug\refactoring SQL for modularity.json
- Source captions dir: response\refactoring SQL for modularity
