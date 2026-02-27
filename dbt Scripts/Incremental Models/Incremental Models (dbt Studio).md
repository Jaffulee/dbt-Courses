# Incremental Models

## Contents

- [Welcome to Incremental Models 10min](#welcome-to-incremental-models-10min)
  - [Welcome](#welcome-to-incremental-models-10min-welcome)
- [Configuring Incremental Models 30min](#configuring-incremental-models-30min)
  - [Configuring Incremental Models](#configuring-incremental-models-30min-configuring-incremental-models)
- [Incremental Strategy 30min](#incremental-strategy-30min)
  - [Incremental Strategy](#incremental-strategy-30min-incremental-strategy)
- [Specific use cases 15min](#specific-use-cases-15min)
  - [Specific use cases](#specific-use-cases-15min-specific-use-cases)
- [Survey and next steps 5min](#survey-and-next-steps-5min)
  - [Course Feedback](#survey-and-next-steps-5min-course-feedback)

## Welcome to Incremental Models 10min
<a id="welcome-to-incremental-models-10min"></a>

### Welcome
<a id="welcome-to-incremental-models-10min-welcome"></a>

#### Course Overview

Welcome! This course will be showing you how to use incremental models in dbt Cloud. Incremental models are a great way to reduce build time and compute when working with extremely large tables. 

You will: 

- Configure models as incremental
- Learn about and utilize incremental strategies
- Learn about incremental models best practices

If you have your own dbt project, feel free to adapt the hands-on practice sections to your own data. Otherwise, you should **use the project you built out while taking the [dbt Fundamentals course](https://learn.getdbt.com/learn/course/dbt-fundamentals)**. The practice sections in this course will build off that same project so we encourage you to use the same repository for your learning.

📣 **Product Name Updates**

Since this course was recorded, some dbt product names or features have changed. While the content remains accurate and useful, you may notice references to outdated terms. Namely dbt Cloud is now dbt, the Cloud IDE is now Studio, and dbt Explorer is now dbt Catalog.

📣** Note regarding trial dbt accounts**

- If you are using a dbt trial account to complete the hands-on portions of this course, and your trial account was created after February 2, 2026, your dbt version might be using the new dbt Fusion engine.
- As of October 13, 2025, the dbt Fusion engine is in a preview phase, meaning it is not generally available, but is stable and production-ready.
- If your dbt account is on Fusion, you may experience some limitations in dbt. Please refer to this page for the current [supported features and limitations](https://docs.getdbt.com/docs/fusion/supported-features).
- If you are unable to use a non-GA product, please follow these steps to turn off the Fusion engine:
- Go to Orchestration -> go into each environment -> click edit -> select "Latest" as your dbt version -> click save

Extracted captions from video: Course Overview

Welcome. This course will be showing you how to create incremental models in your dbt projects. Incremental models in dbt are a materialization strategy designed to efficiently update your data warehouse tables by only transforming and loading new or changed data since your last run. Instead of processing your entire data set every single time, incremental models update only these new rows, significantly reducing the time and resources required for your data transformations.

In this course, you'll materialize models as incremental, learn about and implement incremental strategies, be able to use incremental models with the CI/CD workflow, and learn how to configure incremental models for various use cases. If you have your own dbt project, feel free to adapt the hands on practice sections to your own data. Otherwise, you should use the project you built out while taking in the dbt fundamentals course. The practice sections in this course will build off that same project, so we encourage you to use the same repository for your learning.

#### Frequently Asked Questions

## Frequently Asked Questions

**How long does this course take to complete?**

We estimate that this course takes about 1.5 hours to complete.

**What is the structure of the course?**

The first video in the course gives a brief overview of the course. We recommend starting there for how to get the most out of the course.

**What are the prerequisites for the course?**

You are expected to have prior experience with SQL and dbt. If you are new to dbt, complete [**d****bt Fundamentals On Demand**](https://www.learn.getdbt.com/learn/course/dbt-fundamentals) or the [**Zero to dbt workshop**](https://www.getdbt.com/resources/webinars/zero-to-dbt-workshop) before engaging in this course. The hands-on lab in this course uses the Jaffle Shop data used in dbt fundamentals. 

**Do's and don't for Knowledge Checks questions**

- **Do** try to answer each question on your own first. This helps the learning stick better than if you just look something up.

- **Do** use [**docs.getdbt.com**](https://docs.getdbt.com/) to help you get unstuck on the quiz. You will have docs during real development, so you can leverage docs here.

- **Do **take the quiz additional times to get a passing score!

- **Don't** get discouraged if you don't pass on the first try - you got this!

**If I need help with the course, where can I reach out?**

Please reach out in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)** channel in **[dbt Slack](https://www.getdbt.com/community).** We'd be happy to support you there.

**If I notice a bug or error in one of the lessons, where can I share that?**

First off, we really appreciate you surfacing this for us. Secondly, you can send a quick email over to **[training@dbtlabs.com](mailto:training@dbtlabs.com).** Please include the URL and a screenshot. This will allow us to quickly find out what needs to be fixed.

**Where can I submit feedback on the course content?**

Please feel free to post feedback in the end of [**course survey**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com).  We are quick to respond and love to hear suggestions!

#### Intro to Incremental Models

Extracted captions from video: Intro to Incremental Models

Do you have any really large tables in your warehouse? I'm talking huge tables with over a million rows. Maybe something a little bit like this. So how do we add new data to this table?

Do we just append it? Are there any frequent edits or schema changes? Rebuilding some giant table over and over again, especially if all you're doing is just appending some new rows is a huge waste of time and compute. So how are we going to materialize this table to avoid rebuilding this whole table every single time that we want to make sure our data is fresh.

So let's look at some of the materializations in dbt. If we materialize our model as a table or a view, we're still going to have to rebuild the model every single time we want to make sure it contains fresh data. And ephemeral models don't even exist in our data platform. And we couldn't even query them if we wanted to.

But what if we could only build the new data that's recently arrived? If we use the incremental materialization for this model, we are going to be able to do just that. Let's take a quick look at this graph showing the build times of an incremental model. We ran this model on Monday like normal, but on Tuesday we've materialized it as an incremental because we found this model takes too long to build.

So on Tuesday and Wednesday, we are only building the new data that's coming in. We've already built the data from Monday, so there's no point in wasting compute, rebuilding data that hasn't changed. And on Wednesday we don't bother rebuilding the data that we've had on Monday and Tuesday. We're only building the data that's coming in on Wednesday.

And on Thursday we're doing a full refresh. Rebuilding the whole model again and we can just look at the difference. This full refresh would take forever, and we can tell that just appending the data is going to take much less time. Here's a real example of the kind of time you can save by materializing your models as incrementals.

We have one table at the bottom. We have the build time of this table without materializing as an incremental. And then up top we have materialized it as an incremental. I mean, it took almost an entire day to build and here it's only taking like two hours.

The materialization time is so much shorter. Before we materialize a model as an incremental though, we need to learn how to configure incremental models. We're going to get you set up. And then I'll show you all the different ways that you can configure incremental models.

#### Setup

## Setup

#### Do you need to create a new dbt Cloud free trial account?

This course assumes that you completed the dbt Fundamentals course covering the topics of models, sources, tests, documentation, and deployment. Please refer to the setup instructions in the dbt Fundamentals course for any and all questions related to data warehouses and/or dbt Cloud accounts.

The practice sections in this course will build off that same project so we encourage you to use the same repository for your learning. 

#### 

#### Do you have your own dbt Cloud project already setup?

If you have have your own dbt project, feel free to adapt the hands-on practice sections to your own data.

As you learn, be sure to join other learners in #learn-on-demand over in the dbt Community Slack!

## Configuring Incremental Models 30min
<a id="configuring-incremental-models-30min"></a>

### Configuring Incremental Models
<a id="configuring-incremental-models-30min-configuring-incremental-models"></a>

#### Learning objectives

## Learning objectives

- Explain use cases for incremental models
- Identify the 3 required configurations for incremental models
- Identify and explain the 4 required conditions for a model to be built incrementally.

#### How to configure incremental models

Want to learn more about incremental models? Check out our [docs](https://docs.getdbt.com/docs/build/incremental-models)!

Extracted captions from video: How to configure incremental models

Let's say that a model of ours was taking a really long time to build. We want to materialize it as an incremental model so that it takes less time to build. And this way we won't have to rebuild all of our old records each time, only the new ones. So how do we actually configure an incremental model?

Well, these config logs might look a little familiar. This is how we tell dbt to add only new rows instead of just completely rebuilding our model. And our incremental config looks just like our table in view configs. This can't be all we're doing though.

Because we want to keep old records. And then when we're rebuilding our table, we only want to actually build our new records without actually rebuilding all of the old ones. So how does dbt actually know which rows are new? And what do we mean when we say we want to add new records?

So let's start with which rows are new. We'll have to compare the source data to the already transformed data somehow. There's a couple macros that are going to help us out with this. Let's take a look at this code block.

It looks like we're configuring our model as an incremental. So great. And now we're going to select everything from our model fct_marketing_web_analysis where our updated_at column is greater than or equal to {{this}}. So what's this {{this}} here.

So this encased in curly brackets represents the currently existing database object mapped to this model. This is how we'll be able to tell which rows are new. So what this code is actually doing is selecting from and then building new rows after the most recent updated_at time stamp from the currently existing version of the model in your warehouse. Okay, so we know which records are new now.

Are we done yet? Well, we're not quite done yet. The is_incremental() macro powers incremental materializations. It will return true if all of the following conditions are met.

The model must already exist in the database. We don't want to materialize something incrementally if it's the first time we're building it. The full-refresh flag is not passed. A full-refresh flag added to a dbt command ensures that incremental models are configured as tables.

Sometimes we'll actually want to rebuild our entire incremental model. And during those times, we will add a full-refresh flag to override the is_incremental macro. And the running model is configured with materialized=’incremental’. Pretty self-explanatory.

We need it to be configured as an incremental model to be treated as incremental model. So to tell dbt which rows it should transform on an incremental run, we wrap valid SQL that filters for these rows in the is_incremental() macro. So what does this actually look like in practice? Let's take a look.

We're saying that if this model exists already in the data warehouse and we're not passing a full-refresh flag, and this model is configured as an incremental model, then we are going to select everything from this model where the updated_at date is more recent than the more recent date on the last run. If is_incremental() returns false, then we will build this whole model like usual.

#### Configuring incremental models

Want to learn more about incremental models? Check out our [docs](https://docs.getdbt.com/docs/build/incremental-models)!

**Note**: The `=` in the if_incremental configuration could cause duplicate records. Check out the next section to learn how to handle duplicates!

Extracted captions from video: Configuring incremental models

So I'm in my fact orders model. I have previewed my model, and I have also ordered by order date descending. So I'm looking at my most recent orders at the top of this, table. They're from twenty eighteen, pretty old data, but I've had some new data come in quite recently, and I haven't built this model since. I've had five new orders come in, and I want to build only these new rows without building the rest of my model.

So I'll start by actually configuring fact orders as an incremental model.

And let me use this keyboard shortcut if I do double underscore incremental config incremental.

So great.

Configured as an incremental model. Now I just need to add my, is incremental and this macros. So I'm actually making sure that I'm only selecting my new rows.

Another double underscore incremental.

If I click if incremental, I get this generic is incremental macro, this macro over here.

I'm gonna change event time to be order date because I want this to be my order date column, and I want this to be greater than or equal to.

Again, so the order date column will be my time stamp column. And right now what this is saying is that if this model is an incremental model that I would like to build incrementally, and the order value of a row in my, table is more recent than that of my last production build, then we can build those rows.

I've put my is incremental config all the way at the end. But depending on your data platform, you may be able to save on compute by filtering at the CTE level instead.

So I'm going to save this and I'm gonna build it.

And I'm gonna preview it.

Oh, now I'm going to save it.

Now I'm gonna build it.

And now I'm gonna preview it.

There we go. And here's my new data. Here are my five new orders. They are much more recent dates on these, twenty twenty five, not twenty eighteen. You know, it's been a rough seven years of sales at the Jaffle Shop, but we're back in business now.

#### Practice

## Practice

*Using what you’ve learned, complete the following in your dbt project*

1. Add the necessary configs to the fct_orders model to materialize it as an incremental model. Use the model's most recent timestamp in your where clause.

#### Exemplar

## Exemplar

Use this page to check your work.

models/marts/fct_orders.sql

```sql
{{
    config(
        materialized='incremental'
    )
}}
with orders as  (
    select * from {{ ref ('stg_jaffle_shop__orders' )}}
),

payments as (
    select * from {{ ref ('stg_stripe__payment') }}
),

order_payments as (
    select
        order_id,
        sum (case when status = 'success' then amount end) as amount

    from payments
    group by 1
),

 final as (

    select
        orders.order_id,
        orders.customer_id,
        orders.order_date,
        coalesce (order_payments.amount, 0) as amount

    from orders
    left join order_payments using (order_id)
)

select * from final

{% if is_incremental() %}
where
order_date >= (select max(order_date) from {{this}})
{% endif %}
```

#### Review

## Review 

An **incremental model** only processes **new or changed data**, instead of rebuilding the entire table every time. They are the ideal materialization for extremely large datasets. 

#### The Incremental Materialization: 

The incremental materialization is included in the model you'd like to materialize as incremental. 

{{ config(materialized='incremental') }}

#### Writing incremental logic with {{this}} and is_incremental

-  {{this}}  represents the currently existing database object mapped to this model.

- We’re selecting from (and then building) new rows after the most recent updated_at timestamp from the currently-existing version of the model in your warehouse. 
 

- The is_incremental() macro powers incremental materializations. It will return True if all of the following conditions are met:
- The model must already exist in the database
- The full-refresh flag is not passed 
- The running model is configured with materialized='incremental'

- To tell dbt which rows it should transform on an incremental run, wrap valid SQL that filters for these rows in the is_incremental() macro.

```sql
{{
    config(
        materialized='incremental'
    )
}}

select * from {{ ref('example_model') }}
{% if is_incremental() %}
where 
updated_at >= (select max(updated_at) from {{this}} 
{% endif %}
```

#### Knowledge Check

## Incremental Strategy 30min
<a id="incremental-strategy-30min"></a>

### Incremental Strategy
<a id="incremental-strategy-30min-incremental-strategy"></a>

#### Learning objectives

## Learning objectives

- Explain a potential strategy for accommodating late-arriving data in incremental models, and the trade-offs that late-arriving data introduce.
- Explain each of the 5 incremental strategies and a potential use case for each.

#### Trade-offs and tactics

Extracted captions from video: Trade-offs and tactics

When we work with incremental models, we define a cutoff time for what constitutes new data. In the example we gave, we defined that as whatever data is after the most recent collected timestamp from the currently existing version of our model. Incremental runs of our model will find new records and append them to the currently existing version of the model, and it'll make updates too, if we configure it to do so. Here are a few things we should be wondering as we build our incremental workflow.

So what if our data shows up to the warehouse late? We could do an incremental run and so there's data with a collected timestamp before the cutoff we set. So our data gets loaded in late. Well, we could try widening our cutoff window to grab the late data.

If we look at this code block, we can see that we're now widening the cutoff window to include three days before our most recent updated_at. But if we do that, we're going to end up with duplicate records. Some of our data will be counted twice. So how do we deal with duplicate records?

We want dbt to replace existing rows that were updated and insert new ones into the overlap window. So what info do we need to have in order to know if there are duplicate records? Well, we can use a primary key aka something unique. We'll include this unique_key config here so that we won't have any duplicates of the unique key.

So what does this behavior look like in the logs? So up here we can see that the developer set the cutoff as X days before the most recent updated_at date. And in this other section of the logs we see that the merge statement that dbt is running to update the rows that already exist and to add new rows that didn't already exist. Obviously, this behavior is going to be warehouse specific.

And here's a summarized version of what dbt is doing under the hood. It's creating a temporary table of new records. And it's reconciling the existing table with a temporary table by using one of our incremental strategies. Here's just three examples; we could be merging.

This is upserting new field values on a row. We could be deleting and inserting. So deleting a row and inserting a new row in its place. Or we could be inserting and overwriting.

So replacing entire partitions. So this behavior will depend on your incremental strategy. And it'll depend on your database. So what if our data arrives really late?

What if that X day cutoff window isn't large enough and we get data regularly arriving like 2 x days late? What should we do? So instincts might tell us to just make the cutoff window bigger. But wouldn't that drastically increase our compute?

The whole point of incremental models is to reduce our compute. So how do we find the ideal cutoff date? We can perform an analysis on the arrival time of our data. We can figure out our organization's tolerance for correctness.

And we can set a cutoff date based on these two inputs. And once a week, we can perform a full-refresh to get the ‘true’ table. Incremental models will fundamentally introduce trade offs, but most incremental models are approximately correct. Something to consider as well is that incremental models introduce a level of code complexity and decrease the readability of code.

But if you prioritize correctness or readability, you can negate the performance gains you wanted to get from materializing your model as incremental in the first place. So how do we decide which models should be incremental? Good candidates are immutable event streams. Long but skinny tables.

Tables that only append new data, few updates. And if there are any updates, these tables will have a reliable updated_at field. Bad candidates for incremental models have small data sets. The data might change constantly.

Maybe you're always adding new columns or renaming columns or your data updates in unpredictable ways, or your transformations perform comparisons or calculations that require other rows. If you're not sure if you want to materialize a model as an incremental, we recommend you start by materializing your model as a view. If that takes too long to query, you can try making it a table. And if your table takes too long to build, now it's time to make it incremental.

#### Incremental strategies overview

Extracted captions from video: Incremental strategies overview

Incremental strategies are how dbt adds and updates data on incremental runs. You'll pick a strategy based on your data platform, your data volume, and the reliability of your unique key. Dbt offers the following strategies; append, merge, delete and insert, insert_overwrite, and microbatch.

#### Incremental Strategies: Append

Learn more about the append strategy and other incremental strategies on our [docs](https://docs.getdbt.com/docs/build/incremental-strategy)! The append strategy is supported by the following data platform adapters:

- dbt-postgres

- dbt-redshift								

- dbt-spark					

- dbt-databricks					

- dbt-snowflake					

- dbt-trino					

- dbt-fabric					

- dbt-athena

Extracted captions from video: Incremental Strategies: Append

The first incremental strategy we'll look at is the append strategy. The append strategy adds new rows to the target table only. Does not check for duplicates. Does not check for updates.

And it's best to use the strategy if you have a truly immutable event stream. The SQL the strategy uses is insert into to just append new rows to your table. The benefits of using this strategy is that, you know, it's just simple and straightforward. Doesn't drive up compute costs or time because you don't need to scan your final table.

However, if you expect there to be duplicates in your data, or if you need to update any other rows for any other reason, this is not the best strategy to use, because again, you can only append to your table. So now I'm going to switch over to the IDE. You see, I'm in my fct_orders model and I have configured my incremental fct_orders model to use the incremental strategy “append”. So I'm going to run my model.

And then we can look at the logs together. Okay great. It has run successfully. So let's take a look at the details here.

Let's scroll down. It lets us know what's going on under the hood. Down here we see that insert into state that we were talking about where we're inserting or appending new rows into our table.

#### Incremental Strategies: Merge

Learn more about the merge strategy and other incremental strategies on our [docs](https://docs.getdbt.com/docs/build/incremental-strategy)! The merge strategy is supported by the following data platform adapters:

- dbt-postgres

- dbt-redshift					

- dbt-bigquery					

- dbt-spark					

- dbt-databricks					

- dbt-snowflake					

- dbt-trino										

- dbt-athena

Extracted captions from video: Incremental Strategies: Merge

The merge strategy updates records that already exist using a primary key. It'll insert new records based on that primary key. It will run a full table scan, which can cause performance issues at scale. You should use the merge strategy if you have models that are getting new data added, but they could also be updating existing records.

This is a good way to address the duplicate records issue that something like “append” doesn't address. The merge strategy is best for tables with a smaller number of updates each run. SQL used in the strategy is merge into with matching on the primary key. the benefits of using the merge strategy are that it can address the issue of duplicate records, and you can use this method even without a timestamp column.

It can be inconvenient to use the merge strategy when tables are very large, since you have to scan through the whole table. This drives up processing time and compute costs, although this can be mitigated through partitioning or using clustering methods on the incremental model. Let's go over to my project and check out the merge strategy in action. So I've configured my incremental strategy as “merge” and my unique_key is order_id.

So I will go ahead and build this model. Let's take a look at our logs now. Great, our incremental model ran successfully. When I click on details...

Here we're making our temporary model. I scroll down...

Here you can see that merge into statement I was mentioning before. And because I set my unique_key to be order_id, I don't have to worry about any duplicate records.

#### Incremental Strategies: delete+insert

Learn more about the delete + insert strategy and other incremental strategies on our [docs](https://docs.getdbt.com/docs/build/incremental-strategy)! The delete + insert strategy is supported by the following data platform adapters:

- dbt-postgres

- dbt-redshift									

- dbt-snowflake					

- dbt-trino									

- dbt-athena

Extracted captions from video: Incremental Strategies: delete+insert

The delete and insert strategy grabs all selected records, deletes old versions of those records if they exist in the target table. And it inserts new records and the new version of those deleted records based on primary key. The delete and insert strategy typically requires a full table scan unless you use clever partitioning. You should use the delete and insert method if your models are getting new data and updates to old rows, but the data platform doesn't support merge.

It's best to use delete and insert if there is a significant number of updates each run. The SQL used in this method is delete from and then insert into with matching on primary key. Benefits of the delete and insert strategies; it addresses the duplicate records issue, but it can be convenient to use when tables are very, very large since, again, you typically need to scan the whole table unless, again, you are using very clever partitioning. This can drive up processing time and compute costs.

Let's take a look at the delete and insert strategy in action. Here I've configured the incremental strategy to be delete and insert, and I configured my unique_key. I'm going to build this model. And we can look at the logs together.

Great! The model built successfully. So let's take a look at our logs. Let me click the details button.

You can see it's starting off how we usually start off our incremental models. And if I keep scrolling...

Here we see our delete from statement and our insert into statement. And we can tell that we're matching on ORDER_ID.

#### Incremental Strategies: insert_overwrite

Learn more about the insert_overwrite strategy and other incremental strategies on our [docs](https://docs.getdbt.com/docs/build/incremental-strategy)! The insert_overwrite strategy is supported by the following data platform adapters:		

- dbt-bigquery					

- dbt-spark					

- dbt-databricks										

- Dbt-athena

Learn more about partitioning incremental models with BigQuery in our [docs](https://docs.getdbt.com/reference/resource-configs/bigquery-configs#using-table-partitioning-and-clustering)!

Extracted captions from video: Incremental Strategies: insert_overwrite

The insert_overwrite strategy replaces entire partitions in a destination table. This doesn't require scanning the entire source table; it will only scan partitions that you configure. You should use this strategy if models that are partitioned are getting new data and updates to all rows, but merge is too slow and costly. Insert_overwrite is more complex, and it's most useful on BigQuery since it's much more efficient than merge on BigQuery.

The SQL used for this strategy depends on your data warehouse. BigQuery creates a temporary table, declares partitions to replace, and then merges into. In other data warehouses you'll ‘delete from’, and then ‘insert into’. Partitioning your data prevents you from scanning your entire table like you might be doing if you're using the merge or delete and insert strategies.

However, the insert_overwrite strategy can be complex to set up, and if it's not set up correctly, you can risk generating duplicates. Let's see how I've configured the insert_overwrite strategy in my incremental model fct_orders. I’ve materialized this model as an incremental. I've selected the insert_overwrite incremental strategy.

Let me fix that indentation there...

And you can see I am partitioning by my order_date field. And I'm listing the data_type and the granularity I'd like to partition by. For more information on how to partition properly, you can check our docs, which will show you how to set up incremental models with BigQuery. I'm going to hit the build button.

And because I'm using snowflake, my logs will differ from what you'll see if you're using BigQuery. If I scroll down...

We can see that I have this insert overwrite statement here. And my incremental model built successfully.

#### Incremental Strategies: Microbatch

Learn more about the microbatch strategy on our [docs](https://docs.getdbt.com/docs/build/incremental-microbatch#what-is-microbatch-in-dbt)! 

Learn more about the microbatch strategy and other incremental strategies on our [docs](https://docs.getdbt.com/docs/build/incremental-strategy)! The microbatch strategy is supported by the following data platform adapters:

- dbt-postgres

- dbt-redshift					

- dbt-bigquery					

- dbt-spark					

- dbt-databricks					

dbt-snowflake

Extracted captions from video: Incremental Strategies: Microbatch

Our newest strategy is the microbatch strategy. This differs from other strategies in two key ways. This strategy doesn't require an is_incremental clause, and the strategy does require an event time timestamp. The microbatch strategy divides data into atomic time bound units.

For example, day or week, splits big models into multiple time bound queries, which we call batches. Then dbt takes those queries and inserts them into your target table. Dbt processes the most current batch by default. Processing data in batches, as opposed to reprocessing an entire dataset each time, can save you a lot of time.

You can use what's called a lookback config to process more batches immediately prior to your current batch. So basically you'll define your batch or unit of time that dbt will use to process new data additions to your table. Dbt will process the current batch and whatever is configured in your lookback window during each run. You should configure your microbatch model with the full refresh as false as well.

You should use the microbatch strategy if you have very large time series datasets or time series datasets with regular updates. The SQL used in the microbatch strategy is a time bound ‘select’ query to construct each batch. And then to insert each batch dbt will use insert/overwrite or delete + insert depending on your data platform. One of the benefits of the microbatch strategy is that there's no need for an is_incremental block.

It's a bit more simple to set up. But you still need to be careful about skipping runs on accident, which can lead to holes in your data, so you still need to be careful and intentional when configuring a model as an incremental model using the microbatch strategy. So here I am in the IDE. I'm in my model fct_orders, which I have configured as an incremental model that uses the microbatch strategy.

So again, when dbt runs a model using the microbatch strategy, it will split the processing into multiple queries or batches based on the event_time and batch_size that we've configured. My event_time is set to order_date. This is how dbt knows which column to go to to make batches with, so it's using my order_date column. And my batch_size is ‘day’.

So each batch is going to be a day. You could choose a larger or smaller batch time if you'd like. So I'm going to go ahead and run this model. And now that it's run successfully, we can take a look at the logs and what dbt is doing under the hood.

So even just looking at the summary, we can see where dbt is creating all of my batches. I select details here...

And I scroll down...

Here we can see our delete from and insert into queries here. Again microbatch uses the most efficient mechanism that’s available for each adapter for batch replacement. So the SQL that's here is going to depend on your warehouse. I'm using snowflake, so we're deleting and inserting.

What's really cool about the microbatch strategy is that each batch corresponds to a bounded time period. While other incremental strategies only categorize data by whether it's old or new. The microbatch strategy categorizes data by which batch it's in. So each batch is a unit of data that can be built or replaced on its own, which means that you can run specific batches separately if you really want to.

Or if you want to, you can retry failed batches. If I wanted to run only specific batches. I might use a command like this: dbt run --select fct_orders. And then I can choose my event-time-start and my event-time-end.

#### Practice

## Practice 

*Using what you’ve learned, complete the following in your dbt project*

1*. *Configure an incremental strategy for fct_orders. Choose an incremental strategy that your warehouse supports. *
*

2. Run the fct_orders model.

3. The jaffle shop has some new data coming in! Append the rows below to the orders, customers, and payments source tables in your data warehouse.

Append/insert the data below to raw.jaffle_shop.orders

```
(100, 100, '2025-02-15', 'shipped', current_timestamp),
(101, 84, '2025-02-15', 'shipped', current_timestamp),
(102, 42, '2025-02-15', 'shipped', current_timestamp),
(103, 101, '2025-02-15', 'shipped', current_timestamp),
(104, 66, '2025-02-15', 'shipped', current_timestamp);
```
Append/insert the rows below to raw.jaffle_shop.customers

```
(101, 'Michelle', 'B.'),
(102, 'Faith', 'L.');
```
Append/insert the data below to raw.stripe.payment

```
(121, 100, 'bank_transfer', 'success', 1000, '2025-02-14', current_timestamp),
(122, 101, 'credit_card', 'fail', 400, '2025-02-14', current_timestamp),
(123, 102, 'credit_card', 'success', 1900, '2025-02-14', current_timestamp),
(124, 103, 'credit_card', 'success', 1000,  '2025-02-15', current_timestamp),
(125, 104, 'coupon', 'success', 100, '2025-02-15', current_timestamp);
```
Not sure how to append/insert data to existing tables in your warehouse? Check out the docs below for guidance!

- [Snowflake](https://docs.snowflake.com/en/sql-reference/sql/insert)
- [BigQuery](https://cloud.google.com/bigquery/docs/managing-table-data#append-overwrite)
- [DataBricks](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into)
- [Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c_Examples_of_INSERT_30.html)

4. Run fct_orders again. Look at your logs to see your incremental strategy in action! Then, preview your incremental model to see your new data.

#### Exemplar

## Exemplar

Use this page to check your work.

models/marts/fct_orders.sql

```sql
{{
  config(
    materialized = 'incremental',
    unique_key = 'order_id',
    incremental_strategy = 'merge',
  )
}}

with orders as  (
    select * from {{ ref ('stg_jaffle_shop__orders' )}}
),

payments as (
    select * from {{ ref ('stg_stripe__payment') }}
),

order_payments as (
    select
        order_id,
        sum (case when payment_status = 'success' then payment_amount end) as amount

    from payments
    group by 1
),

 final as (

    select
        orders.order_id,
        orders.customer_id,
        orders.order_date,
        coalesce (order_payments.amount, 0) as amount

    from orders
    left join order_payments using (order_id)
)

select * from final

{% if is_incremental() %}
where
order_date >= (select max(order_date) from {{this}})
{% endif %}
```

#### Review

## Review

### Tradeoffs and Tactics

Incremental models introduce tradeoffs.

- Most incremental models are “approximately correct” 

- They introduce a level of code complexity (i.e. how easy it is for someone to understand your code) 

- Prioritizing correctness can negate performance gains from incrementality.

**
How do I choose which models to materialize as incrementals?** 
Good candidates:

- Immutable event streams: tall and skinny tables, append-only, no updates

- If there are any updates, a reliable updated_at field

Not-so-good candidates:

- A small table

- Data changes constantly: new columns, renamed columns, etc.

- Data is updated in unpredictable ways

- Transformations perform comparisons or calculations that require other rows

### Incremental Strategies

[Incremental strategies](https://docs.getdbt.com/docs/build/incremental-strategy) for materializations optimize performance by defining how to handle new and changed data.

There are various strategies to implement the concept of incremental materializations. The value of each strategy depends on:

- The volume of data.
- The reliability of your unique_key.
- The support of certain features in your data platform.

Data platform adapterappendmergedelete+insertinsert_overwritemicrobatch[dbt-postgres](https://docs.getdbt.com/reference/resource-configs/postgres-configs#incremental-materialization-strategies)✅✅✅✅[dbt-redshift](https://docs.getdbt.com/reference/resource-configs/redshift-configs#incremental-materialization-strategies)✅✅✅✅[dbt-bigquery](https://docs.getdbt.com/reference/resource-configs/bigquery-configs#merge-behavior-incremental-models)✅✅✅[dbt-spark](https://docs.getdbt.com/reference/resource-configs/spark-configs#incremental-models)✅✅✅✅[dbt-databricks](https://docs.getdbt.com/reference/resource-configs/databricks-configs#incremental-models)✅✅✅✅[dbt-snowflake](https://docs.getdbt.com/reference/resource-configs/snowflake-configs#merge-behavior-incremental-models)✅✅✅✅✅[dbt-trino](https://docs.getdbt.com/reference/resource-configs/trino-configs#incremental)✅✅✅[dbt-fabric](https://docs.getdbt.com/reference/resource-configs/fabric-configs#incremental)✅✅[dbt-athena](https://docs.getdbt.com/reference/resource-configs/athena-configs#incremental-models)✅✅✅[dbt-teradata](https://docs.getdbt.com/reference/resource-configs/teradata-configs#valid_history-incremental-materialization-strategy)✅✅✅✅
#### Append:

- **Adds** new rows to target table **only**

- Does not check for duplicates

- Does not check for updates

- **Best used for: ** Truly immutable event streams

- **SQL used: insert into** to add new rows

#### Merge:

- Updates records that already exist using primary key 

- Inserts new records based on primary key

- Runs full table scan (can cause performance issues at scale)

- **Best used for**:

- Models that are getting new data added, BUT they could also be updating existing records. This is a good way to address the duplicate records issue that something like append doesn't address.

- Best for tables with a small number of updates each run.

- **SQL Used: **merge into with matching on primary key

#### Delete+insert

- Grabs all selected records, deletes old version of those records if they exist in the target table.

- Inserts new records *and* the new version of the records deleted above  based on primary key

- Requires full table scan (unless you configure incremental predicates)

- **Best used for: **Models are getting new data and updates to old rows, but the data platform does not support MERGE.

- **SQL used:** delete from and then insert  into with matching on primary key

#### Insert_overwrite

- Replaces entire partitions in a destination table.

- Does not require scanning entire source table–will only scan the partitions you configure. 

- **Much more efficient than merge on BigQuery. **

- **Best used for: **Models *that are partitioned* getting new data and updates to old rows, but *merge* is too slow and costly. insert_overwrite is more complex, &  most useful on BigQuery.

- **SQL used:** 

- In BigQuery: creates temp table, declares partitions to replace, then merge into. 

- In other databases: DELETE FROM then INSERT INTO

#### Microbatch

- Divides data into atomic, time-bound units (ex: day) 

- Splits large models into multiple time-bounded queries: batches! dbt takes those queries and inserts them into your target table.

- **Best used for**: 
- Very large time-series data sets

- Time series with regular updates.

- **SQL used**: 
- Time-bound SELECT query to construct batch. 

- To insert batch, dbt will use insert/overwrite or delete + insert depending on data platform.

#### Knowledge check

## Specific use cases 15min
<a id="specific-use-cases-15min"></a>

### Specific use cases
<a id="specific-use-cases-15min-specific-use-cases"></a>

#### Learning Objectives

## Learning objectives

In this section, we’ll be looking at some edge cases that might arise while you’re using incremental models. We’ll show you how to address issues like

- Using incremental models with CI jobs

- Dealing with schema changes

#### Dealing with Schema Changes

Learn more on our [docs](https://docs.getdbt.com/docs/build/incremental-models#what-if-the-columns-of-my-incremental-model-change) site!

Extracted captions from video: Dealing with Schema Changes

Incremental models can be configured to include an optional on_schema_change parameters so that you have additional control over your incremental models and columns change. These options enable dbt to continue running incremental models even when there are recent schema changes, letting you do fewer full refreshes and save costs on queries. We configure the on_schema_change parameter like this in our incremental config block. We add a new key called on_schema_change.

And we can set it equal to a couple different potential values. Setting on_schema_change equal to ‘ignore’ is the default behavior. If you add a column to this incremental model and run a dbt run, this column will not appear in your target table. If you remove a column from your incremental model and run a dbt run, your run will fail.

The ‘fail’ key triggers an error message when the source and target schemas diverge. ‘Append_new_columns’ will append new columns to the existing table, who would’ve guessed. Note that this setting does not remove columns from the existing table that are not present in the new data. And ‘sync_all_columns’ will add any new columns to the existing table and remove any columns that are now missing.

Note that this is inclusive of data type changes. On BigQuery, changing column types requires a full table scan, so be mindful of trade offs when implementing this. So here I am in the IDE. Here I'm in my fct_orders model, which I have configured as an incremental.

And I have set on_schema_change to be ‘fail’. So I'm going to do something that will change my schema. Let's say I'll rename this column to customer_ids. Let’s save and I'll go ahead and run this model.

And let's take a look at what happens. Looks like this has failed. Let's take a look at why. It's because we set on_schema_change to ‘fail’.

And here it is suggesting we switch it to something else or remedy the error or some other way.

#### Using incremental models with CI jobs

Learn more about CI and incremental models on our [docs site](https://docs.getdbt.com/best-practices/clone-incremental-models)!

Extracted captions from video: Using incremental models with CI jobs

Let's say you've configured a slim CI job in dbt Cloud. This job is configured to defer to my production environment like so. It's also configured to run a dbt build, but with a

state:modified flag, so that all of my modified models and all models downstream of my modified models have been run and tested. And the CI job will also trigger whenever my team opens a pull request. It's triggered by a pull request. The setup ensures that I'm not introducing breaking changes into my merge, and I don't have to rebuild my entire dbt project.

This setup helps me save time and compute costs. But because my CI job is building modified models into a PR specific schema, on the first execution of dbt build with that state:modified flag, the modified incremental model will build in its entirety. This is because it doesn't yet exist in the PR specific schema and is_incremental will be false. We're basically running a full refresh every single time we try to submit a pull request.

This isn't ideal for a few reasons. Typically, incremental models are our largest datasets. It will be slow and expensive for these to build in their entirety, and there could be situations where a full refresh of an incremental model will pass successfully in our CI job, but an incremental build of that same table would fail in production once the PR is merged into main. For example, there could be schema drift where the on_schema_change config is set to fail.

We can avoid these issues by zero copy cloning the relevant preexisting incremental models into our PR specific schema as the first step of our CI job, using the dbt clone command. This way, incremental models already exist in the PR specific schema when we first execute command dbt build with our state:modified flag, so is_incremental will be true. So the first and only step of our CI job can remain the same. But before that, we're going to introduce a new command, this dbt clone command, which will clone all the preexisting incremental models that have been modified or are downstream of another model that has been modified.

This state:old is here because we want new incremental models to run in the full refresh, because they don't exist in Prod yet, and they're brand new. If you don't specify this, then you'll get an error message. And then, of course, we want to use this classic command to build all of our models that have been modified and their downstream dependencies. Because you cloned your incremental models, these models will be selected in your dbt build, and your dbt build will run in incremental mode, not full refresh mode.

#### Review

## Review

### Dealing with schema changes

Incremental models can be configured to include an optional on_schema_change parameter to enable additional control when incremental model columns change. These options enable dbt to continue running incremental models in the presence of schema changes, resulting in fewer --full-refresh scenarios and saving query costs.

The possible values for on_schema_change are:

- ignore: Default behavior (see below).
- fail: Triggers an error message when the source and target schemas diverge
- append_new_columns: Append new columns to the existing table. Note that this setting does *not* remove columns from the existing table that are not present in the new data.
- sync_all_columns: Adds any new columns to the existing table, and removes any columns that are now missing. Note that this is *inclusive* of data type changes. On BigQuery, changing column types requires a full table scan; be mindful of the trade-offs when implementing.

Read more on our [docs](https://docs.getdbt.com/docs/build/incremental-models#what-if-the-columns-of-my-incremental-model-change)! 

### Configuring CI jobs when your project has incremental models

Because your CI job is building modified models into a PR-specific schema, on the first execution of dbt build --select state:modified+, the modified incremental model will be built in its entirety *because it does not yet exist in the PR-specific schema* and [is_incremental will be false](https://docs.getdbt.com/docs/build/incremental-models#understand-the-is_incremental-macro). You're running in full-refresh mode: This wastes time and compute.

You'll have two commands for your dbt Cloud CI check to execute:

1. Clone all of the pre-existing incremental models that have been modified or are downstream of another model that has been modified:

```
dbt clone --select state:modified+,config.materialized:incremental,state:old
```
2. Build all of the models that have been modified and their downstream dependencies:

```
dbt build --select state:modified+
```
Because of your first clone step, the incremental models selected in your dbt build on the second step will run in incremental mode.

#### Knowlege Check

## Survey and next steps 5min
<a id="survey-and-next-steps-5min"></a>

### Course Feedback
<a id="survey-and-next-steps-5min-course-feedback"></a>

#### Quick survey

# 4 quick questions!

Almost there! As you finish the course, we'd love to hear your feedback on the course in this quick form here: [**Open survey in new tab**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com)

#### Congratulations!

# Congratulations!

Thank you for joining all of us from the dbt Labs team!!! You just leveled up your dbt skill set with **ephemeral models, incremental models, and snapshots!**

Make sure you hit complete on each of the lessons. Check out the resources below to continue the journey, stay fresh on your skills, and share this with your fellow analytics engineers.

### **Resources**

**dbt Docs: **There is no shame in referencing the docs as an analytics engineer! Use this to continue your journey, copy YML code into your project, or figure out more advanced features.

**Short courses: **We have four courses to continue leveling up:

- [**Jinja, Macros, and Packages:**](https://courses.getdbt.com/courses/jinja-macros-packages) Extend dbt with Jinja/Macros and import packages to speed up modeling and leverage existing macros.
- [**Analyses and Seeds:**](https://courses.getdbt.com/courses/analyses-seeds) Analyses can be used for ad hoc queries in your dbt project and seeds are for importing CSVs into your warehouse with dbt.
- [**Refactoring SQL for Modularity:**](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) Migrating code from a previous tool to dbt? Learn how to migrate legacy code into dbt with modularity in mind.

### **Contribute**

- Support other beginners in ****[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)**.**

### **Feedback**

- **Bugs:** Help the training team squash bugs in the course by sending them to [**training@dbtlabs.com**](mailto:training@dbtlabs.com) and we will triage them from there.

Congratulations and thank you again! See you in dbt Slack!

- The dbt Labs team

#### Get dbt Certified!

By completing this course, you are one step closer to achieving your dbt certification! To continue your progress, explore the next course in our certification path and apply your new skills in real-world scenarios. Stay committed, keep learning, and join our community of experts to share your experiences and gain insights.

### The dbt Certified Developer Path

The courses on the path are:

- dbt fundamentals
- Refactoring SQL for Modularity
- Jinja, Macros, and Packages
- Materialization Fundamentals
- Snapshots
- Incremental Models
- Analyses and Seeds
- Advanced Testing
- Advanced Deployment

Enroll in the next course today. Then visit [**dbt-certification**](https://www.getdbt.com/dbt-certification) and download the study guide to begin planning your path. 🚀🚀

---

### Metadata

- Course: Incremental Models
- Generated (UTC): 2026-02-27 12:10:17Z
- Source slug JSON: response\Incremental Models\slug\Incremental Models.json
- Source captions dir: response\Incremental Models
