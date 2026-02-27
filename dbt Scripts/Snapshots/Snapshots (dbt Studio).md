# Snapshots

## Contents

- [Welcome to Snapshots 10min](#welcome-to-snapshots-10min)
  - [Welcome](#welcome-to-snapshots-10min-welcome)
- [Snapshots 45min](#snapshots-45min)
  - [Snapshots](#snapshots-45min-snapshots)
- [Survey and Next Steps 5min](#survey-and-next-steps-5min)
  - [Course Feedback](#survey-and-next-steps-5min-course-feedback)

## Welcome to Snapshots 10min
<a id="welcome-to-snapshots-10min"></a>

### Welcome
<a id="welcome-to-snapshots-10min-welcome"></a>

#### Intro to Snapshots

📣 **Product Name Updates**

Since this course was recorded, some dbt product names or features have changed. While the content remains accurate and useful, you may notice references to outdated terms. Namely dbt Cloud is now dbt, the Cloud IDE is now Studio, and dbt Explorer is now dbt Catalog.

📣** Note regarding trial dbt accounts**

- If you are using a dbt trial account to complete the hands-on portions of this course, and your trial account was created after February 2, 2026, your dbt version might be using the new dbt Fusion engine.
- As of October 13, 2025, the dbt Fusion engine is in a preview phase, meaning it is not generally available, but is stable and production-ready.
- If your dbt account is on Fusion, you may experience some limitations in dbt. Please refer to this page for the current [supported features and limitations](https://docs.getdbt.com/docs/fusion/supported-features).
- If you are unable to use a non-GA product, please follow these steps to turn off the Fusion engine:
- Go to Orchestration -> go into each environment -> click edit -> select "Latest" as your dbt version -> click save

Extracted captions from video: Intro to Snapshots

Welcome. This course will be showing you how to use snapshots in your projects.

Analysts often need to, you know, look back in time at previous data states and immutable tables. And while some data systems are built in a way that makes accessing historical data possible, this is not always the case. dbt provides a mechanism called snapshots, which record changes to a mutable table over time. To be more technical about it, snapshots implement type two slowly changing dimensions over mutable source tables.

These slowly changing dimensions or SCDs identify how a row in a table has changed over time. In this course, you'll practice using snapshots to get a look back at your data's previous state. If you have your own dbt project, feel free to adapt the hands on practice sections to your own data.

Otherwise, you should use the project you built out while taking the dbt fundamentals course.

The practice sections in this course will build off that same project, so we encourage you to use the same repository for your learning.

#### Frequently Asked Questions

## Frequently Asked Questions

**How long does this course take to complete?**

We estimate that this course takes about 1 hour to complete.

**What is the structure of the course?**

The very first video in the course gives a brief overview of the course. I recommend starting there for how to get the most out of the course.

**Do's and don't for Check for Understanding questions**

- **Do** try to answer each question on your own first. This helps the learning stick better than if you just look something up.
- **Do** use [**docs.getdbt.com**](https://docs.getdbt.com/) to help you get unstuck on the quiz. You will have docs during real development, so you can leverage docs here.
- **Do **take the quiz additional times to get a passing score and earn your badge!
- **Don't** get discouraged if you don't pass on the first try - you got this!
- **Don't **screen clip questions / answers and share those with the world. That defeats the purpose of everyone checking their own understanding.

**How much does this course cost?**

A grand total of… $0.

**If I need help loading training data into my data warehouse, where can I reach out?**

Please reach out in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)**** **channel in **[dbt Slack](https://www.getdbt.com/community).** We'd be happy to support you there.

**If I notice a bug or error in one of the lessons, where can I share that?**

First off, we really appreciate you surfacing this for us. Secondly, you can send a quick email over to **[training@dbtlabs.com](mailto:training@dbtlabs.com).** Please include the URL and a screenshot. This will allow us to quickly find out what needs to be fixed.

**Where can I submit feedback on the course content?**

Please feel free to post feedback in the end of [**course survey**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com).  We are quick to respond and love to hear suggestions!

#### Setup

## Getting Set Up

**Need to create a new dbt Cloud free trial account?**

This course assumes that you have completed the [**dbt Fundamentals**](https://learn.getdbt.com/courses/dbt-fundamentals) course covering the topics of models, sources, tests, documentation, and deployment. Please refer to the [**setup instructions**](https://learn.getdbt.com/learn/course/dbt-fundamentals/set-up-dbt-cloud-55min/getting-started?page=1) in the dbt Fundamentals course for any and all questions related to data warehouses and/or dbt Cloud accounts.

The practice sections in this course will build off that same project so we encourage you to use the same [**repository**](https://github.com/dbt-labs/dbt-Fundamentals-finished-project) for your learning. 

**Have your own dbt Cloud project already setup?**

Alternatively, if you have have your own dbt project, feel free to adapt the hands-on practice sections to your own data.

As you learn, be sure to join other learners in #learn-on-demand over in the dbt Community Slack!

## Snapshots 45min
<a id="snapshots-45min"></a>

### Snapshots
<a id="snapshots-45min-snapshots"></a>

#### Learning objectives

## Learning objectives

- Explain the use-cases for snapshots
- Describe snapshot strategies
- Summarize snapshot best practices and adapt them to their use case
- Implement snapshots in a dbt Cloud project

#### How to use snapshots

Want to learn more about snapshots? Check out our [docs!](https://docs.getdbt.com/docs/build/snapshots#what-are-snapshots)

Extracted captions from video: How to use snapshots

So how do we actually configure our snapshots?

We configure snapshots and YAML files.

dbt expects your snapshot YAML files to be located in the snapshots folder by default, But if you fudge around with your dbt project YAML, you can put them in any YAML file.

We'll have to let dbt know what we're snapshotting and how it should detect record changes before we're able to snapshot anything.

So let's take a look at this example.

I'm naming my snapshot, giving it a description, and using this relation tag to reference either the source or the model that I'm snapshotting.

Database refers to the database I'm rendering my snapshot in and schema indicates it's schema.

Because snapshots can't be rebuilt, it's a good idea to put your snapshots in a separate schema so end users know they're special.

From there, you might want to set different privileges on your snapshots compared to your models and maybe even run them as a different user or role. So this way, it'll be very difficult to drop a snapshot unless you're very sure that you want to.

So let's take a look at some of the other keys here.

Unique key should be the primary key column in my model.

Hard delete tells dbt what to do if hard deletes occur. You can invalidate them, ignore them, or add a new record with a dbt is deleted meta fields that lets you know that that record has been deleted.

Snapshot meta fields are customizable, and you can customize them with the snapshot meta column names key, and you can read more about this key and all the keys here in the docs. And finally, strategy. So strategies are required field, and there are two strategies, time stamp and check.

So timestamp uses an updated at column to determine if a row has changed.

This is the recommended strategy since it's much more efficient and it handles schema changes more effectively.

The check strategy compares a list of columns between their current and historical values to determine if a row was changed.

We run snapshots with the dbt snapshot command.

You can select from them using the ref macro, but you can't preview or compile their SQL.

Technically speaking, snapshot tables are created as a clone of the data set with some additional meta fields.

Snapshots need to be run twice in order to actually capture changes.

The first run establishes the meta fields, and then changes are looked for on the second run. This might sound familiar if you've configured incremental models before.

Snapshots are incredibly useful. They can add a bit of complexity if you're snapshotting joined tables downstream because you've added multiple rows of history per ID. So what happens when you have ten snapshots that you want to join together and you want to capture the history of all of those datasets.

If you find a bug and you need to change your modeling code, you can find yourself with inaccurate results and no way of recalculating the correct data.

By contrast, if you snapshot the source data and then build on top of that, you can always recalculate everything from first principles if or when you need to.

It's not like you should never be snapshotting downstream models.

For instance, maybe you have a very important metric, and maybe it's reported to the board of directors or a regulatory agency. You know, the sort of metrics that you want to keep a very careful track of. We'll want to know what's said about that metric and when. A downstream model containing a metric like this that is that's this important is the sort of downstream model that you might want to snapshot.

As a rule of thumb, snapshot your sources. Sometimes snapshot very downstream models if necessary.

So how often should we run our snapshots?

Capturing history can be dependent on how your job is scheduled.

Meaning, for example, let's say we have an order that goes from pending to shipped to delivered, but we only run the DP snapshot command when the records in the source table are in pending or in delivered.

We'll miss the intermediate step when the package was being shipped.

The solution for this is to run your snapshots as often as your source data changes.

#### Using snapshots

Want to learn more about snapshots? Check out our [docs!](https://docs.getdbt.com/docs/build/snapshots#what-are-snapshots)

Extracted captions from video: Using snapshots

Now that we understand the basics of how snapshots work, we're actually going to use them.

I want to write a snapshot for our order source table.

This way, we can keep track of how orders are processed over time.

I've already previewed this table here.

And if we take a look at the columns we have, we'll get a better idea of what strategy we should actually be using.

So we do have a time stamp here. We have this order date column, but it's an ordered at time stamp. It's it's the time the order was placed. So this time won't change when, say, an order status is updated from maybe completed to returned or a turn pending to returned.

The order date column will not change if the status column changes.

So we are going to have to use the check strategy. If we wanted to use the time stamp strategy, we would need some sort of updated at time stamp, which we just don't have. So we're gonna use the less preferred but still useful strategy, the check strategy.

So let me create a new snapshot in our snapshots folder.

I will name it, orders snapshot dot YAML, and let me get coding.

Alright. I'm gonna name it orders snapshot. Pretty self explanatory.

This order source table is from the shuffle shop source.

Again, it's the orders table.

Here, I'm just putting down the schema and database I want these to be put in.

My unique keys, the ID column.

And, again, I'm using the check strategy.

And these columns that I'm going to be checking, they might not be one to one with the column names in our stage orders model, but that's because these are the names of the columns in the actual order source table. We renamed them when we made stage orders.

So when using the check strategy, in general, it's better to be on the safe side regarding how many or or which columns you choose, just because you you're gonna wanna think hard about which ones are gonna be useful and why. The more you pick, you know, the more compute you're gonna be doing every time you snapshot your snapshots. But if something does go, like, wrong, you do wanna make sure that you actually have all the information you need to figure out what's going wrong and why.

Okay. Great. So here is our order snapshot.

You can see that I'm materializing the snapshot in my snapshots schema in my analytics database.

I'm following best practices and building my snapshots in a schema separate from my Analytics schema.

I also have this d b t valid to current key down here. So the time stamp that I provide is when this row becomes invalidated.

So for current records, this is null by default or the value specified in DBT valid to current, which in this case is way in the future. You can learn more about other snapshot meta column names in the docs.

And I've set hard deletes to ignore. So I'm gonna run dbt snapshot.

I actually ran dbt build, but this is going to, also snapshot all of my snapshots.

Dbt build runs tests, builds your models, snapshots your snapshots. So my snapshot table's metadata columns are only actually going to get updated the second time I run my snapshot if there's an update to the data. So I'm going to go to Snowflake and I'm going to update my data.

Currently, the Order ID twenty three has the status 'Return Pending', not returned, But we're going to update that right now.

And now we're going to snapshot our snapshots again.

So while we're here, let's actually take a look at what's going on under the hood.

So what we're actually doing here is we're checking to see where each column we specified is null or different from a different existing value with that unique key.

It's how the check strategy is going to make sure your data is new.

So I'm going to open a new tab here.

Going to actually take a look at our snapshot. So SELECT FROM REF. Now we can reference our snapshot. Here we go. Orders snapshot.

And to make it easier for us to look at, I'll just put order by ID.

Hey. Let's preview this, and we can actually see what our order snapshot looks like. We can see all the great metadata columns you added.

Let's take a look.

We have our loader dot column, our DBT ID that we've been given, updater dot column.

This is when this column was updated at, our valid from, and our valid to columns.

And if we scroll down, we can actually see we have two entries with the ID twenty three, one of them returned and one of them returned pending.

And if we look at our 'Updated At' column, we can see which one of these happened earlier than the other. First, it was returned pending, then we actually returned it.

Alright. I'm back in our 'order snapshot. Yaml' file, and I'm going to change the strategy to timestamp.

Again, just because the timestamp strategy won't actually work with, our orders table doesn't mean we can't still look at the code that's gonna be run under the hood if you are actually using the timestamp strategy.

I'm gonna add this new key here, updated at.

Let's just make it the order date column, and I can delete this check calls here.

Gonna run snapshot again.

I've clicked on 'Details' here. We can see what's actually going on.

So you can see we're kind of filtering on a time stamp value here. We're saying, show me the records that I've got, since the last time I've snapshot of this table. And in Snowflake's case, we're also merging it to the existing snapshots table. So snapshots are a little bit similar to incremental models.

#### Practice

## Practice

*Use what you've learned to complete the following*

Snapshots are difficult to practice without genuine type 2, slowly changing dimension data. For this exercise, use the following code snippets to practice snapshots. **You may need to adjust the Snowflake snippets based on your data warehouse.**

- **(In dbt Cloud)** Create a new snapshot in the folder snapshots with the filename mock_orders.yml with the following code snippet. 

```
snapshots:
  - name: orders_snapshot
    relation: source('jaffle_shop', 'orders')
    config:
      schema: snapshots
      database: analytics
      unique_key: id
      strategy: check
      check_cols: ['id', 'user_id', 'order_date', 'status']
      hard_deletes: ignore
      dbt_valid_to_current: "to_date('9999-12-31')"
```

- **(In dbt Cloud)** Run snapshots by executing dbt snapshot.

- Now we'll simulate new data coming in. In your data warehouse, append/insert the data below to raw.jaffle_shop.orders

```
(100, 100, '2025-02-15', 'shipped', current_timestamp),
(101, 84, '2025-02-15', 'shipped', current_timestamp),
(102, 42, '2025-02-15', 'shipped', current_timestamp),
(103, 101, '2025-02-15', 'shipped', current_timestamp),
(104, 66, '2025-02-15', 'shipped', current_timestamp);
```

Not sure how to append/insert data to existing tables in your warehouse? Check out the docs below for guidance!

- [Snowflake](https://docs.snowflake.com/en/sql-reference/sql/insert)
- [BigQuery](https://cloud.google.com/bigquery/docs/managing-table-data#append-overwrite)
- [DataBricks](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-dml-insert-into)
- [Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c_Examples_of_INSERT_30.html)

- **(In dbt Cloud)** Run snapshots by executing the dbt snapshot command.
- **(In dbt Cloud)** View the snapshot by running this command in a blank worksheet.
select * from {{ ref('orders_snapshot') }}

Note: If you want to start this process over, you will need to drop the snapshot table by running the following in Snowflake. This will force dbt to create a new snapshot table in step 4. (Again, you will need to swap in your development schema for dbt_fmckenna)

```
drop table analytics.dbt_fmckenna_snapshots.orders_snapshot
```

#### Review

## Review 

Analysts often need to "look back in time" at previous data states in their mutable tables. While some source data systems are built in a way that makes accessing historical data possible, this is not always the case. dbt provides a mechanism, **[snapshots](https://docs.getdbt.com/docs/build/snapshots#what-are-snapshots)**, which records changes to a mutable table over time.

Snapshots:

- Are built as a table in the database, usually in a dedicated schema.

- On the first run, build entire table and adds four columns: dbt_scd_id, dbt_updated_at, dbt_valid_from, and dbt_valid_to

- In future runs, dbt will scan the underlying data and append new records based on the configuration that is made.

- This allows you to capture historical data

#### Knowledge Check

## Survey and Next Steps 5min
<a id="survey-and-next-steps-5min"></a>

### Course Feedback
<a id="survey-and-next-steps-5min-course-feedback"></a>

#### Quick survey

# 4 quick questions!

Almost there! As you finish the course, we'd love to hear your feedback on the course in this quick form here: [Open survey in new tab](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com)

#### Congratulations!

# Congratulations!

Thank you for joining all of us from the dbt Labs team!!! You just leveled up your dbt skill set with dbt **snapshots!**

Make sure you hit complete on each of the lessons. Check out the resources below to continue the journey, stay fresh on your skills, and share this with your fellow analytics engineers.

### **Resources**

**dbt Docs: **There is no shame in referencing the docs as an analytics engineer! Use this to continue your journey, copy YML code into your project, or figure out more advanced features.

**Short courses: **We have four courses to continue leveling up:

- [**Jinja, Macros, and Packages:**](https://courses.getdbt.com/courses/jinja-macros-packages) Extend dbt with Jinja/Macros and import packages to speed up modeling and leverage existing macros.
- [**Analyses and Seeds:**](https://courses.getdbt.com/courses/analyses-seeds) Analyses can be used for ad hoc queries in your dbt project and seeds are for importing CSVs into your warehouse with dbt.
- [**Refactoring SQL for Modularity:**](https://courses.getdbt.com/courses/refactoring-sql-for-modularity) Migrating code from a previous tool to dbt? Learn how to migrate legacy code into dbt with modularity in mind.

### **Contribute**

- Support fellow learners and let us know what you thought about the course in **#learn-on-demand**.
- Support other beginners in **#advice-dbt-for-beginners.**

### **Feedback**

- **Bugs:** Help the training team squash bugs in the course by sending them to** [training@dbtlabs.com](mailto:training@dbtlabs.com)** and we will triage them from there.

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

- Course: Snapshots
- Generated (UTC): 2026-02-27 14:16:39Z
- Source slug JSON: response\Snapshots\slug\Snapshots.json
- Source captions dir: response\Snapshots
