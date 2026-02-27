# dbt Fundamentals (dbt Studio)

## Contents

- [Welcome to dbt Fundamentals 5min](#welcome-to-dbt-fundamentals-5min)
  - [Welcome](#welcome-to-dbt-fundamentals-5min-welcome)
- [Analytics Development Lifecycle 30min](#analytics-development-lifecycle-30min)
  - [dbt and the ADLC](#analytics-development-lifecycle-30min-dbt-and-the-adlc)
- [Set Up dbt 60min](#set-up-dbt-60min)
  - [Getting Started](#set-up-dbt-60min-getting-started)
- [Models 60min](#models-60min)
  - [Building your First Model](#models-60min-building-your-first-model)
- [Sources 60min](#sources-60min)
  - [Understanding Sources](#sources-60min-understanding-sources)
- [Data Tests 60min](#data-tests-60min)
  - [Building Tests](#data-tests-60min-building-tests)
- [Documentation 40min](#documentation-40min)
  - [Documentation Basics](#documentation-40min-documentation-basics)
- [Deployment 30min](#deployment-30min)
  - [Understanding Deployment](#deployment-30min-understanding-deployment)
- [Survey and Next Steps 5min](#survey-and-next-steps-5min)
  - [Course Feedback](#survey-and-next-steps-5min-course-feedback)

## Welcome to dbt Fundamentals 5min
<a id="welcome-to-dbt-fundamentals-5min"></a>

### Welcome
<a id="welcome-to-dbt-fundamentals-5min-welcome"></a>

#### Course overview

📣** Note regarding trial dbt accounts**

- If you are using a dbt trial account to complete the hands-on portions of this course, and your trial account was created after February 2, 2026, your dbt version might be using the new dbt Fusion engine.
- As of October 13, 2025, the dbt Fusion engine is in a preview phase, meaning it is not generally available, but is stable and production-ready.
- If your dbt account is on Fusion, you may experience some limitations in dbt. Please refer to this page for the current [supported features and limitations](https://docs.getdbt.com/docs/fusion/supported-features).
- If you are unable to use a non-GA product, please follow these steps to turn off the Fusion engine:
- Go to Orchestration -> go into each environment -> click edit -> select "Latest" as your dbt version -> click save

#### Frequently Asked Questions

## Frequently Asked Questions

**How long does this course take to complete? **

We estimate that this course takes about six hours to complete. There are three hours of video and approximately two hours of practice for someone who is new to dbt. 

**What is the structure of the course? **

The very first video in the course gives a brief overview of the course. We recommend starting there for how to get the most out of the course. 

**How do I earn the dbt Fundamentals badge? **

To receive the dbt Fundamentals badge, you should watch all the video lessons, practice with the exercises, and complete the Check for Understandings with 100% accuracy.  Don't worry - you have unlimited attempts for each Check for Understanding.  Note: You need to click "mark as complete" for each lesson to be marked complete.  

**Do's and don't for Check for Understanding questions**

- **Do** try to answer each question on your own first. This helps the learning stick better than if you just look something up.
- **Do** use [**docs.getdbt.com**](https://docs.getdbt.com/) to help you get unstuck on the quiz. You will have docs during real development, so you can leverage docs here.
- **Do **take the quiz additional times to get a passing score and earn your badge!
- **Don't** get discouraged if you don't pass on the first try - you got this!
- **Don't **screen clip questions / answers and share those with the world. That defeats the purpose of everyone checking their own understanding.

**How much does this course cost? **

A grand total of… $0.

 If you set up a trial account for the course, you can keep your dbt trial account if you switch to a Developer plan.

**If I need help loading training data into my data warehouse, where can I reach out? **

Please reach out in the **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)** channel in [**dbt Slack**](https://www.getdbt.com/community). We'd be happy to support you there.

**If I notice a bug or error in one of the lessons, where can I share that? **

First off, we really appreciate you surfacing this for us. Secondly, you can send a quick email over to **[training@dbtlabs.com](mailto:training@dbtlabs.com).** Please include the URL and a screenshot. This will allow us to quickly find what needs to be fixed. 

**Where can I submit feedback on the course content? **

Please feel free to post feedback in the end of [**course survey**](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com). We are quick to respond and love to hear suggestions!

## Analytics Development Lifecycle 30min
<a id="analytics-development-lifecycle-30min"></a>

### dbt and the ADLC
<a id="analytics-development-lifecycle-30min-dbt-and-the-adlc"></a>

#### Learning Objectives

## Learning Objectives

- Explain the analytics development lifecycle.
- Explain the roles on a data team.
- Explain how dbt fits into the modern data stack.
- Understand the structure of a dbt project.

#### ELT vs ETL

# ELT vs ETL

The battle between ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) is one of the most important conversations in modern data management. As data continues to expand in volume and complexity, organizations must decide which approach is best suited to their analytics needs.

When comparing ETL vs ELT, the key difference lies in when and where the data transformation occurs. With ETL, data is transformed before loading, while in ELT, data is transformed after loading into the data warehouse.

In this article, we will explore ETL vs ELT, breaking down their differences, processes, and strengths to help you decide which is best for your data strategy.

## What is ETL?

ETL stands for **Extract, Transform, Load.** This method prepares data for analysis by extracting it from various sources, transforming it into a structured format, and loading it into a target system.

In ETL workflows, most meaningful data transformation occurs outside this primary pipeline in a downstream business intelligence (BI) platform.

### The ETL process

- **Extract**: Data is pulled from various sources, often in unstructured or semi-structured formats.
- **Transform**: The data undergoes a transformation process, cleaning, formatting, and structuring it for analysis.
- **Load**: Once transformed, the data is loaded into a target system, typically a data warehouse, where it becomes available for querying and reporting.

## What is ELT?

ELT stands for **Extract, Load, Transform** and has gained popularity in cloud-native environments. In this approach, data is extracted and loaded into a data warehouse first, allowing the data to be transformed using the warehouse’s computing power.

ELT has emerged as a paradigm for how to manage information flows in a modern data warehouse. This represents a fundamental shift from how data previously was handled when ETL was the data workflow most companies implemented.

### The ELT process

- **Extract**: Data is collected from various sources, just as in ETL.
- **Load**: The raw data is loaded into a data warehouse without any transformations.
- **Transform**: After the data is stored, transformations are performed within the warehouse, leveraging its computational power.

## Making the case for ELT

ELT aligns with the scalability and flexibility of modern data stacks, enabling organizations to work with large datasets more efficiently. While there are many benefits to using ELT over ETL, below are the primary benefits.

**Leverage cloud infrastructure**

ELT takes advantage of the massive processing power of cloud-native data warehouses like Snowflake, BigQuery, and Redshift. By loading raw data into the warehouse first, ELT enables these systems to handle transformations at scale, which is particularly valuable when working with large volumes of data.

**Faster data availability**

With ELT, raw data is loaded into the warehouse immediately, making it accessible for analysis more quickly. This reduces the delay often seen in ETL processes, where data must be transformed before it’s available for querying​.

**Cost efficiency**

ELT reduces the need for expensive on-premises hardware or complex ETL tools. Instead, it capitalizes on the inherent processing capabilities of cloud data warehouses, optimizing both performance and cost. In modern data stacks, offloading transformation tasks to cloud services can lead to significant cost savings​.

**Flexible, iterative transformation**

ELT allows for more flexible data transformations. Since the raw data is already in the warehouse, analysts and data engineers can transform data iteratively, applying changes and optimizations without having to reload or reprocess the entire dataset. This flexibility makes it easier to adapt to evolving business needs and ensures that teams can always work with the latest data​.

**Data democratization**

By loading raw data into the warehouse first, ELT supports a more self-service data model. Analysts and data teams can access and transform data as needed without being bottlenecked by upstream ETL processes. This democratization fosters greater agility and collaboration across teams​.

## How dbt fits into the ELT workflow

dbt plays a crucial role in the ELT process by serving as the transformation layer within the data warehouse. While ELT relies on loading raw data into the warehouse, dbt empowers teams to manage and automate their transformations, ensuring the data is clean and analytics-ready.

**dbt features include:**

- **Version-controlled transformations**: dbt enables version control for all transformations, making it easy to track changes and collaborate across teams. This ensures data transformations are organized and consistent​.
- **Automation and scheduling**: With dbt, you can automate transformation processes, ensuring that the most up-to-date data is always available for analysis. This fits perfectly within an ELT workflow, where transformation happens after the data is already in the warehouse​.
- **Comprehensive testing**: dbt offers built-in testing capabilities to validate transformations, ensuring data quality and integrity throughout the ELT process​.

At dbt Labs, we advocate for a strong focus on data transformations, especially in analytics-driven workflows where clean and structured data is crucial for making informed decisions.

#### Building data you can trust with dbt

#### The ADLC

Extracted captions from video: The ADLC

At dbt Labs, we use a framework called the Analytics Development Lifecycle, or ADLC to describe how data work actually happens From the moment you identify a business question to the moment you deliver trusted insights and beyond. There are eight phases in this life cycle, and they loop continuously, just like software development. let's go through each. Everything starts with a plan.

Maybe someone on the business side asks what's driving churn? Or a data leader decides it's time to rebuild your core models. The planning phase is where teams scope out the work, clarify priorities and get shared expectations. Whether it's in a jira board, a Notion doc, or a GitHub issue, this stg is all about intentionality.

You want to work on the right things at the right time. Next comes development. In this phase, you write code to transform raw data into something useful. With dbt that's typically SQL models, along with documentation and metadata that describes the logic behind them.

dbt focuses on a modular structure so you can build on top of each model and each other's work with confidence. As you build, you're also testing. In dbt tests are baked right into the code base. You can write simple tests like checking for nulls or custom ones to validate unique business logic.

Testing ensures that your data is trustworthy before it reaches production. and they can help your team catch issues early on. Then it's time to deploy. This is where changes go live.

In dbt you can configure automated deployment workflows tied to your git repository so your code that has been reviewed and tested can safely deploy into production without any manual steps. This helps build confidence across teams. Your stakeholders know the numbers they're using are grounded in a reliable process. Once the code is live, it needs to run consistently.

The operate phase is where you manage production pipelines. In dbt this often means scheduling jobs, monitoring run times and setting up alerts for when things go wrong. Operations are about reliability. Can your pipelines run at 3:00am?

Without you watching them? that's the goal. After pipelines run, we observe them. This is about tracking what happened.

Did all of the models complete? Did the tests pass? Were there any anomalies in the data? Observability tools like dbt's run history logs, test alerts and more help data teams stay proactive and avoid surprises.

With trusted data in production, your teammates can start discovering what's there. This is where data consumers explore models, understand the logic and find answers. Thanks to dbt's documentation, metadata and lineage, people can trace metrics back to their source and build trust in the data. This phase is especially powerful when combined with tools like dbt Catalog.

Finally, we analyze. This might happen in a BI tool or in a notebook or the dbt semantic layer, maybe even a conversation between a data analyst and a stakeholder. This is where your work delivers value. When someone can make a better decision because of the work you've done.

And often the questions that, surface during analysis lead you right back to, you guessed it, planning. So that's the analytics, development, life cycle, plan, develop, test, deploy, operate, observe, discover, analyze and, and then back to plan. And the best part, with dbt you're not just building data models. You're managing a full modern development life cycle.

And you're doing it in a way that scales across people, across tools and across time.

#### dbt - the data control plane

Extracted captions from video: dbt - the data control plane

Let's dive into how you actually coordinate all this work across people, tools and systems. This is where dbt becomes more than a modeling tool. It becomes your data control plane. Now, what is a data control plane?

If you're not familiar with the term, a control plane is a concept borrowed from software infrastructure. Think of it like air traffic control for your data workflows. In this scenario, planes, these are your data pipelines. Pilots are your developers.

The destination is trusted insights and the control tower, which is dbt. The control plane doesn't move the data itself. Instead it orchestrates, governs and observes everything that does. It gives your team visibility into what's running, what's changed and what's breaking.

So you can take fast action and keep improving over time. dbt takes this idea and applies it to analytics. Whether you're building SQL models, defining metrics, running tests or deploying pipelines, dbt helps manage every part of the lifecycle. In development, this happens in a version controlled space.

As your team builds and ships analytics, dbt coordinates six key activities. Just like a control plane orchestrates flight operations. First, we start with design. With dbt mesh teams define ownership and modularize projects.

It's like designing flight paths so no two planes collide. Discover; the dbt catalog makes your model sources and documentation searchable. Like having a live map of all the flights and gates. Align; Use the dbt semantic layer to define metrics once and use them everywhere.

That's like ensuring all the departments use the same flight schedule and definitions. Build; developers use the dbt Studio, dbt Canvas or VS Code extension to write and test code; your hangar, your maintenance crew, your cockpit. Deploy; dbt's CI workflows and scheduler. Make sure only production ready code takes off.

No rogue flights here, just tested approved deployments. And lastly, observe; With tests, alerts and lineage tracking. dbt monitors everything in flight. If something's off course, you'll know it before it becomes a problem.

#### Review

## Review

### **Traditional Data Teams**

- Data engineers are responsible for maintaining data infrastructure and the ETL process for creating tables and views.
- Data analysts focus on querying tables and views to drive business insights for stakeholders.

### **ETL and ELT**

- ETL (extract transform load) is the process of creating new database objects by extracting data from multiple data sources, transforming it on a local or third party machine, and loading the transformed data into a data warehouse.
- ELT (extract load transform) is a more recent process of creating new database objects by first extracting and loading raw data into a data warehouse and then transforming that data directly in the warehouse.
- The new ELT process is made possible by the introduction of cloud-based data warehouse technologies.

### **dbt**

- dbt empowers data teams to leverage software engineering principles for transforming data.
- The focus of this course is to build your analytics engineering mindset and dbt skills to give you more leverage in your work.

**The Analytics Development Lifecycle (ADLC)**

- 
Provides a structured process for building, testing, reviewing, and deploying analytics.

- 
Encourages iteration and collaboration so teams can confidently move from idea to production.

- 
Aligns data work with software engineering best practices—version control, testing, and continuous improvement.

**dbt as the Data Control Plane**

- 
dbt orchestrates and governs the ADLC across your data ecosystem.

- 
It ensures consistency in how data is developed, tested, documented, and deployed.

- 
By serving as the “control plane,” dbt integrates with the modern data stack to enforce trust, scalability, and readiness for AI-driven use cases.

#### Knowledge check - dbt and the ADLC

## Set Up dbt 60min
<a id="set-up-dbt-60min"></a>

### Getting Started
<a id="set-up-dbt-60min-getting-started"></a>

#### Learning Objectives

## Learning Objectives

- Load training data into your data platform
- Set up your warehouse and repository connections.
- Navigate the dbt platform.
- Complete a simple development workflow in dbt Studio.

#### dbt platform Overview

#### Set Up dbt for First Time

## Set Up dbt for the First Time

Welcome! As a new learner, getting hands-on experience with dbt is crucial. While you can watch the videos and go through the lessons, we strongly encourage you to complete the practice exercises for deeper learning.

You’ll need access to a dbt account, a data platform and a Git provider to complete the steps in this course. If you are setting this up as an individual, you can create a [free dbt trial account](https://www.getdbt.com/signup) at any time. While the trial is 14 days, you can change your plan to the free "developer" plan at any time in your account settings under billing. This will give you access to dbt Studio for one developer.

Note the instructor in this course is on an Enterprise plan, so some of the features and capabilities will not be available in the trial account such as dbt Copilot and some dbt Catalog functions. If you'd like access to these features, [contact our sales team](https://www.getdbt.com/contact). 

Your data platform must be compatible with dbt. If you don’t have one set up, we’ll guide you through setting up and loading sample data into the most common dbt-compatible platforms. 

Choose ONE data platform to set up and **watch the TWO corresponding videos for that data platform**. While you only need to watch those two videos in their entirety, simply click through the other data platform specific videos in order for the course completion percentage to reach 100%. 

**Note:** We use Snowflake as the data platform for the demo videos in this course.

If you prefer local development, check out the [dbt Fundamentals course with the dbt VS Code Extension](https://learn.getdbt.com/learn/course/dbt-fundamentals-vs-code) instead!

## 

## Why is Practice Important?

Setting up your own data platform and connecting it to dbt will reinforce your learning and build confidence to apply dbt in real-world scenarios.  

⚠️ **Note: **Besides our Quickstart Guides and demo videos, refer to the official documentation for your chosen platform. You’ll need skills like using docs and debugging errors as you go through this learning journey.

After you connect dbt to your data platform, return to the course to continue building your first model. Good luck, and remember, the more you practice, the more you'll master dbt.

🗓️ **Review trial account terms and pricing for new data platforms carefully. Monitor and record trial period and deadlines.  🗓️**

#### Set up a trial Snowflake account

- [Snowflake trial link](https://signup.snowflake.com/?utm_source=google&utm_medium=paidsearch&utm_campaign=na-us-en-brand-trial-exact&utm_content=go-eta-evg-ss-free-trial&utm_term=c-g-snowflake%20trial%20account-e&_bt=579123129595&_bk=snowflake%20trial%20account&_bm=e&_bn=g&_bg=136172947348&gclsrc=aw.ds&gad_source=1&gad_campaignid=14738821097&gbraid=0AAAAADCzRJV_BNGfVtL7dHxrXFuyWyAxa&gclid=CjwKCAjw2brFBhBOEiwAVJX5GHqZ8tWCr2tBG9SynV8OWJtTqJaHnyaU-NioZF3AFQAUiGneTrgvJhoCAocQAvD_BwE)

**Snowflake Code snippets**

```sql
create warehouse transforming; 

create database raw; 

create database analytics; 

create schema raw.jaffle_shop; 

create schema raw.stripe;

_________________________________________________________________________

create table raw.jaffle_shop.customers 
( id integer,
  first_name varchar,
  last_name varchar
);

_________________________________________________________________________

copy into raw.jaffle_shop.customers (id, first_name, last_name)
from 's3://dbt-tutorial-public/jaffle_shop_customers.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
    );

_________________________________________________________________________

create table raw.jaffle_shop.orders
( id integer,
  user_id integer,
  order_date date,
  status varchar,
  _etl_loaded_at timestamp default current_timestamp
);
_________________________________________________________________________

copy into raw.jaffle_shop.orders (id, user_id, order_date, status)
from 's3://dbt-tutorial-public/jaffle_shop_orders.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
    );

_________________________________________________________________________

create table raw.stripe.payment 
( id integer,
  orderid integer,
  paymentmethod varchar,
  status varchar,
  amount integer,
  created date,
  _batched_at timestamp default current_timestamp
);
_________________________________________________________________________

copy into raw.stripe.payment (id, orderid, paymentmethod, status, amount, created)
from 's3://dbt-tutorial-public/stripe_payments.csv'
file_format = (
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1
    );

_________________________________________________________________________

select * from raw.jaffle_shop.customers; 

select * from raw.jaffle_shop.orders; 

select * from raw.stripe.payment;
```

**Note**: Snowflake has changed their Account Identifier format for some regions. You may need to include two components of your Snowflake URL in your connection settings. For example, this account's ID is `CMVGRNF-FKA50167`

Extracted captions from video: Set up a trial Snowflake account

Here I'm signing up for a Snowflake trial account. So I'm going to add my information here. So go ahead and enter your corresponding information. Then I need to add in my company name and my job title and, and select which cloud provider I would like.

I'm going to use AWS as my cloud provider. Select the region that is appropriate for your location and we'll agree to the terms and services. Next we'll complete this security piece. I'll select SQL and I'll skip the rest of that.

Great. So I'm going to check my inbox and verify my email. Next I'll create my username and my password. Excellent.

So now I have created my Snowflake trial account. The next piece is to add data to our account. So over here I'll go into my catalog and my database explorer and I have some Snowflake data already in here. Pre populated, but we are going to add some additional data to our Snowflake account.

So here at the top I'm going to click Create and click SQL Worksheet. And here I'm going to create some databases and schema. In my project. I've copied these SQL statements from the dbt fundamentals page and we are going to execute all of these.

First we'll create a warehouse. A warehouse is the overall container where our data is going to live. Our database here raw is where kind of the individual folders will live and the schema are those folders themselves. So we'll go ahead and execute these.

It's important to note that because I've created a trial account, I am an account admin in my Snowflake account, so I'm able to perform these. If you're using an existing Snowflake account, make sure that you have the appropriate permissions to create these different aspects in your account. The next piece is I need to create the actual tables that I'm going to use for my data sets. So here I'm going to create a table in my RAW database, my Jaffle Shop schema called Customers.

Perfect. Now that we've created the table, we want to put data into the table. so There is an S3 bucket that has all of our data for this particular table. And so we'll copy that into our customers table.

Excellent. Now I'm going to just do a select star from that specific table to make sure that this was loaded correctly. Perfect. That was successful.

We need two additional tables in our Snowflake account, one for orders. So I'll go ahead and paste in my SQL here to create the table first. And I ran into an issue here because I didn't have a semicolon at the end. So.

So we need to separate these queries from each other. So the semicolon Will do that separation. I just want to execute this piece. I could also highlight it to indicate which SQL I want it to run.

Great. Now we will copy in again that copy into this table from our S3 bucket. We'll execute a similar query, select star from and we'll copy in our table. Perfect.

That looks great. And then we have one more table that we want to create and this time it's going to be in our stripe schema. So stripe payment here. And then we will copy from our S3 bucket.

Excellent. Let's go ahead and execute our select statement here to make sure that our data is looking correct. And that looks good to me. So the last piece that I need here in my Snowflake account is I need my account, number.

There's a few different places that I can find that, but the easiest is finding it in our URL. So here in our URL we have this RvB and that is going to be our account number. I also could click my initials down below and we see the account information here as well. So this is information I'm going to need for dbt in the next section.

#### Set up dbt with Snowflake

**Note**: Snowflake has changed their Account Identifier format for some regions. You may need to include two components of your Snowflake URL in your connection settings. For example, this account's ID is `CMVGRNF-FKA50167` in some cases you may also need to include the region.

Extracted captions from video: Set up dbt with Snowflake

So here I am on dbt Labs main website, getdbt.com I need to create a new dbt account. So let's click Try dbt here. I'll go ahead and fill out all of my information here and then create my account.

Excellent. I have created my account. I've verified my email. I've selected multi factor authentication method and I have completed the survey.

So here in my dbt account I need to create a dbt project. So this is the first page that I am prompted with. The name of my project currently is Analytics. I'm going to rename this to Jaffle Shop and click Continue.

The next piece is a connection. This is a new dbt account. I need to establish a new connection to my data platform. So I'll go ahead and click Add new connection.

Here we have various data platforms that you can connect to. Each need different information in order to connect. So click the connection that is correct for your data platform that you are using and fill in the appropriate information for that account. Here I'll demo a Snowflake connection I'll fill out the account information here, add my target database and add my warehouse.

I'll click save. Great. And now I have a connection set up. I'll go back to my main page here.

Now I see Snowflake as an option to connect to my dbt project. So I'll select that. And now I am prompted to add in my development credentials. We have a few different authentication methods available for our development credentials.

Either username, password or a key pair here. In our trial account we don't have an SSO option, but that is an option that we could enable if I had an enterprise account, I'll enter my credentials here and my target schema. The schema that my tables that I build in dbt will be created in. This is going to be automatically defaulted to dbt underscore my first initial last name We have this development schema, here unique to the specific user so that when we are developing, we can develop in a specific location that's not going to be overriding what's in production or overriding anyone else on my team.

So we'll keep this as a unique schema. Excellent. So I'll click save here and then the next section is setting up a repository. So we have a few different options.

We could connect to a specific git repository here. With a native integration we could set up a Managed repository. Or we could clone a Git repo. If we aren't using one of these here, let's use a managed repository.

This is a repository that dbt Labs manages. I won't have access to this repository, but it's a place that will store my code and I can use Git best practices in my dbt project. So we'll go ahead and name our repo here. Just Jaffle Shop.

Excellent. So our project is ready. We can start developing in dbt Studio. So I'll click here.

The first piece I need to accomplish is initializing my dbt project. We'll click this. And what this is going to do is going to clone a repository that is our starter repository that dbt Labs has created, and it's going to have all of these folders that are necessary for my dbt project. We'll have an example folder here with a few different dbt models as well as a configuration file.

We'll go ahead and commit to a branch here. Our commit message can be initial commit. Excellent. Here I am, now officially set up with my dbt account and I've successfully accessed dbt Studio.

The next piece we want to dive into is making sure our connection to our data platform is correct. So we'll execute the command dbt run. What this is going to do is it's going to take any models in my models directory here, any SQL files that I have, and it's going to create those as data objects in my target schema. So we'll go ahead and execute our command here and we'll let this run.

my command failed here. So we'll take a look at our summary of this execution and we see that there is this error indicating that we don't have sufficient privileges to operate on my schema. I know this is not completely accurate because when I log into Snowflake, I'm able to operate on this specific schema. So there must be something off with my connection details.

So let's go into our account and go into account settings, and we'll go to Connections and pop back into this connection that we just established. So I know all of this information is correct. Let's check out the optional settings that we have here. Here for Snowflake, there's specific roles that our users have, and I didn't enter this information previously when I was setting this up.

So I'll enter the role, which is my default role in Snowflake, which is Transformer. So I'll go ahead and save this. And now pop back into Studio and I'll execute dbt run, once more. Great.

Okay, so these were successful. So I've executed my dbt run model here. My first dbt model. This was built as a table in my development schema.

So our connection to our data platform has been successful.

#### Set up a trial BigQuery account

Extracted captions from video: Set up a trial BigQuery account

Here I'm at cloud.google.com and I'm going to create a BigQuery account here under Products. We'll go into BigQuery and we'll click Get Started for free. I need to fill out some account information.

here I've added my contact information and my credit card information. This is a free trial, but they do require that you enter your payment information. But rest assured, the trial is still free. So after you are done using your account, that's always good practice to either delete it or make sure that you aren't going to get charged in the future.

We filled out our beginning survey here and We're in our BigQuery project called my first project. I'm actually going to add a new project here and we're going to name this, something that's specific to what we are doing here. So we'll name this Jaffle Shop since that's the data set we're going to use. and then our location here.

And so we'll select our project here. And now we are in our Jaffle Shop project. The next piece we'll go to is analyze and manage data specifically here for BigQuery. We'll click into this and we can see our project here and there are some resources already inside.

We are going to click create new SQL query. And here we're going to paste in the SQL statements that are in the dbt fundamentals section for BigQuery. And we're selecting from this dbt tutorial jaffle shop. This is going to be an embedded data set.

So we don't need to add this data. We can already query it. We're just making sure that we can in fact query it. So we'll go ahead and execute each of these and we see that those were successful.

So that looks good. We can even view the results of these data sets to make sure that those look the way that we might expect them to. And I do see ID first name, last name here for my customers table and for my orders table. I have id, user ID order state status, ETL loaded at.

That looks great. And then stripe payment here we have our corresponding fields. So all of these I can query appropriately. And these are the data sets that we're going to use in our dbt project.

Next, we need to create a service account. This is how we're going to authenticate into dbt and build our datasets into BigQuery. So over here we're going to go into I Am Admin and then go into service accounts. Here we're going to create service account and enter in the name.

Here we'll do something like dbt Jaffle Shop. And we'll do service account for dbt project and continue. We'll select a role here. We'll select the owner role here.

For full permissions, we'll click Continue and then we'll leave the grants blank here. We don't need to fill that out. So we'll click Done. And so now we have our service account created here.

Next we'll click into our service account here and we'll go into keys and we'll add a key, create a new one. And we want this to be a JSON type. We'll click Create and then save that file to our computer. And then this JSON file is what we need to authenticate into our dbt project.

#### Set up dbt with BigQuery

Extracted captions from video: Set up dbt with BigQuery

So here I am on dbt Labs main website getdbt.com I need to create a new dbt account. So let's click Try dbt here. I'll go ahead and fill out all of my information here and then create my account.

I've successfully set up my dbt account. I've verified my email, created multifactor authentication for my dbt account and completed the surveys. So now I am prompted to create a dbt project within my dbt account. So we'll go ahead and name our dbt project Jaffle Shop.

And then we need to select a connection to our data platform. I don't have any connections set up yet, so we'll go ahead and add a new connection. Here we are shown the different data platforms that dbt can connect to. And let's go ahead and connect to BigQuery.

Here we have a few different options. We can connect to, two different adapters. We recommend the BigQuery adapter, so we'll leave that here. And then I need to upload a JSON file from BigQuery, which I have already downloaded and I need to just upload that file.

Excellent. So I've uploaded my JSON file here for the service account for, for my BigQuery account. We'll go ahead and save this. And now go back to my main page here and we see BigQuery as a connection option.

So we'll select that. And our, JSON file is showing up here for our service account. So there's nothing that we need to do here. There is this default data set that is created for us and this is unique to me as a developer.

So dbt_bhipple this will be the target dataset or the target schema for our data objects that we build with dbt. So our tables, our views, those are the things that will get created in BigQuery. So we'll go ahead and test our connection here. And we are good to go.

So we'll click save. The last step is to connect our git repository. We have a few different options for how we might do that. One is connect to one of the Git repos using our native integration.

So GitHub, or GitLab And I have the option to a Manage repository. And this is going to be a git repo that dbt Labs manages. I am able to create branches and commit, but I won't be able to actually view the repository or if I'm using a different application I could click git clone and use the ssh clone for this specific repository, we'll use managed for now. and we'll use jaffle shop dbt as our repository name.

Excellent. So I have successfully connected BigQuery and my managed repository to my dbt project. So let's start developing in dbt Studio. I need to initialize my dbt project so so we'll click this here and what this is going to do is it's going to clone a starter repository that dbt Labs has set up for my dbt project.

This adds various folders that I need for my project here. And we have in our models directory some SQL files which are my dbt models that are going to create data objects in my data platform. we'll want to commit to our branch here and this is our initial commit. So we'll commit our changes and then we'll execute the command dbt run.

What this is going to do is take any SQL files that I have in my models directory and it's going to build those as data objects in my data platform. So we'll execute our command here. And we have successfully built our two dbt models here in my target data set in BigQuery.

#### Set up a trial Databricks account

Extracted captions from video: Set up a trial Databricks account

Here I am at databricks.com and I'm going to create my databricks account. So here I'll click Try databricks and we'll do start your trial for free use Express setup. We can sign up with our email here.

I've entered my email address and now I'm going to enter the name of my account. I'm going to use the name of my organization, select my country. And here we are in our databricks account. Next we'll go to SQL Warehouses and here we will create a SQL warehouse.

We'll name this Jaffle Shop. We'll keep this as extra small. We'll click Create. And now I need to upload my data to my SQL Warehouse.

I've downloaded the three CSV files with the datasets that we're going to use in our dbt project. Jaffle Shop customers, Jaffle Shop orders and Stripe payment. So here we'll go ahead and click new. We'll click create or modify data set And we'll import our CVSs one at a time here.

Here we've selected create new table. The name of this table is just going to be customers. And then our schema, we're going to create a new one and call this Jaffle Shop. We'll create that.

And we'll click Create table. Excellent. So we've created one table. We'll go ahead and click new once more and we'll do add or upload data Create Modify table.

here we'll upload our orders CSV Call this orders. And we'll use the Jaffle Shop schema here. Excellent. And then we'll do one more table and we'll call this payment and we'll create one new schema since this is a different source system called Stripe.

And then create table. Excellent. now we have our Jaffle Shop and our Stripe schema with our payment and orders and customers tables. Next we're going to rename our catalog here.

It's called workspace. But this is going to contain our raw data so I'm going to rename our catalog to raw. So I'll click into our workspace here and do, rename and we'll name this raw. So now we have our raw data in our raw catalog here.

But we want to create a target catalog in databricks that we can use for our dbt transformed data. So we'll go ahead and click the plus button here and we'll click create a catalog and we'll call this analytics. The type here we can choose how we want this to show up. And this is really just going to contain tables and views and other data objects.

We'll stick with standard here. We'll go ahead and click our checkbox here to use default storage. And our catalog has been created. So here, this is where our dbt transformed data will live.

This will be our target catalog or in future videos we'll call this all our target database. The next piece now we need is our user token. So I'll go to my user at the top here and I'll go into settings and I'll go into developer and we'll go into access tokens. We'll click manage.

We'll generate a new token and we'll indicate that this is for dbt. We'll generate it. This token here will not be shown again. So I need to make sure I copy this and I'm going to use this in my next phase where I set up my dbt account and add that token to my dbt project credentials.

The next piece that we need for our account setup is our server host name. At the top here in our URL, this beginning piece here where we have our account number essentially and cloud.databricks.com, this is going to be our server host name. We'll need that for dbt as well.

The last piece that we need for dbt is our HTTP path. So let's go back to our SQL warehouses down here. We'll click into our Jaffle Shop warehouse and then in our url at the top we have this last piece here that starts with SQL warehouses and then some number information. This is going to be our http path.

for dbt so in our connection settings we'll need this beginning piece here our server host name and then the last piece here we'll need for our http path.

#### Set up dbt with Databricks

Extracted captions from video: Set up dbt with Databricks

So here I am on dbt Labs' main website, getdbt.com I need to create a new dbt account so let's click try dbt here. We'll go ahead and fill out all my information here and then create my account I successfully created my dbt account. I have completed the email verification, I've added Multi Factor Authentication, and I've completed the survey.

So here I am prompted to create a dbt project. Here we'll name our project Drafl Shop. Click continue. And then we need to establish a connection.

This is a connection to my data platform. We don't have any connections already established, so let's go ahead and add a new connection. Here I have options to select a data platform and these are the ones that are integrated with our dbt cloud platform. Let's go ahead and select Databricks and I'll, enter the appropriate information for my databricks account.

Then we'll go ahead and click Save and we'll pop back to our dbt project. And now we see Databricks as a connection option. The next piece is a token for my specific databricks user. So I've created a token in my Databricks account.

So we'll go ahead and paste in our token here. And then our schema that we have established is the default schema that dbt has created for me. And this is unique to my specific user. So dbt_bhipple, this is specific to my developer.

I want a unique location where I can build my data objects without overwriting anything that's in production or overriding another developer. So we'll keep this as a unique schema, for my user. Let's go ahead and test our connection. Great.

We'll go ahead and save this. And the last step is to connect a Git repository. We have a few different options. We could select a native integration, either GitHub or GitLab for our starter dbt account.

Or we could use a managed repository that dbt Labs manages. Or we could clone using Git Clone here. If it's a different repository than one of these, we'll click Manage. And this is going to be the managed repository that dbt Labs creates for us.

So let's name this dbt Jaffle Shop, click Create. And this is going to allow us to have a repository where our code is stored. We'll be able to create branches, but we just won't have access to that repository, which is okay for our project here. So let's go ahead and start developing in dbt Studio here.

We're prompted to initialize our dbt project. We'll go ahead and click this button here. And what this is going to allow us to do is have all of these folders that are required for my dbt project already added to my git repository by clicking that initialize and then committing to our branch. So let's go ahead and write initial commit as our commit message.

These folders here we'll use throughout, but the main one will be our models. This has some example models. In it we see these two SQL files. These are my models.

These are going to be data objects that are built in my data platform. To test our data platform connection and make sure we are set up correctly, let's execute the command dbt run. This is going to take any SQL files that I have in my models directory and build those as data objects in my data platform in my target schema. We'll execute our command here.

And we see that was a successful run. So if I look at my details I can confirm that this model, my first dbt model, was created as a table in my developer schema. So we have successfully established our dbt project with a connection to databricks and we have built a few models to start.

#### Quickstart Guides for other data platforms

## Quickstart Guides for other data platforms

- [Quickstart for dbt Cloud and Redshift](https://docs.getdbt.com/docs/get-started/getting-started/getting-set-up/setting-up-redshift)

- [Quickstart for dbt Cloud and Microsoft Fabric](https://docs.getdbt.com/guides/microsoft-fabric?step=9)

- [Quickstart for dbt Cloud and Azure Synapse](https://docs.getdbt.com/guides/azure-synapse-analytics?step=1)

- [Quickstart for dbt Cloud and Starburst Galaxy](https://docs.getdbt.com/guides/starburst-galaxy?step=1)

- [Quickstart for dbt Cloud and Teradata](https://docs.getdbt.com/guides/teradata?step=1)

#### Info dbt for Administrators

### Setting Up dbt for Administrators

If you are the one setting up your organization’s dbt account for the first time, check out our mini courses for dbt Administrators.

- [dbt and Snowflake for Admins](https://learn.getdbt.com/learn/course/dbt-cloud-and-snowflake-for-admins/dbt-and-snowflake-for-admins-5min/introduction)

- [dbt and Databricks for Admins](https://learn.getdbt.com/learn/course/dbt-cloud-and-databricks-for-admins/welcome-5min/introduction)

- [dbt and Redshift for Admins](https://learn.getdbt.com/learn/course/dbt-cloud-and-redshift-for-developers/dbt-cloud-and-redshift-5min/introduction)

- [dbt and BigQuery for Admins](https://learn.getdbt.com/learn/course/dbt-cloud-and-bigquery-for-admins/dbt-and-bigquery-for-admins-5min/introduction)

If you’re going to learn dbt on your organization’s existing dbt account, find setup instructions in the next lesson. You don’t need to follow these instructions but scroll to the end of the page to be sure it is marked complete. You need to complete each page in the course to earn your badge.

#### Access Your Company's dbt Account

## Access Your Company's dbt Account

Your organization’s dbt implementation is integrated with at least one data platform and a git provider. Follow these instructions if you are joining an existing dbt account that has already been setup by your company’s dbt administrator. 

### Setting Up dbt for Developers

You will need your organization’s sign in method, and you will need the right roles, permissions, and credentials in multiple systems to carry out your work in dbt. Use one of our mini courses for developers to set up your individual account:

- [dbt and Snowflake for developers](https://learn.getdbt.com/courses/dbt-cloud-and-snowflake-for-developers)

- [dbt and Databricks for developers](https://learn.getdbt.com/courses/dbt-cloud-and-databricks-for-developers)

- [dbt and Redshift for developers](https://learn.getdbt.com/courses/dbt-cloud-and-redshift-for-developers)

- [dbt Cloud and BigQuery for developers](https://learn.getdbt.com/courses/dbt-cloud-and-bigquery-for-developers)

⚠️  **Note**: The data for BQ is in a public dataset so keep in mind you just need to use these statements:

```sql
select * from `dbt-tutorial.jaffle_shop.customers`
select * from `dbt-tutorial.jaffle_shop.orders`
select * from `dbt-tutorial.stripe.payment`
```

#### Knowledge check-Set up dbt

## Models 60min
<a id="models-60min"></a>

### Building your First Model
<a id="models-60min-building-your-first-model"></a>

#### Learning objectives

## Learning Objectives

- Explain what models are in a dbt project.
- Build your first dbt model.
- Explain how to apply modularity to analytics with dbt.
- Modularize your project with the ref function.
- Review a brief history of modeling paradigms.
- Identify common naming conventions for tables.
- Reorganize your project with subfolders.

#### What are Models?

# Definitions

****D****ata object**: **any entity that can be queried or manipulated within your data platform. This includes tables, views, and other database objects that store and organize data.****

**Table: **a structured set of data held in a database, consisting of rows and columns. Each column represents a different attribute of the data, and each row corresponds to a single record. Tables are fundamental components in databases and are used to store and organize data efficiently.

**V****iew**: a database object that stores a SQL query rather than the data itself. When you query a view, the database runs the stored SQL query and returns the results.

#### Build Your First Model

```sql
with customers as (

    select
        id as customer_id,
        first_name,
        last_name

    from raw.jaffle_shop.customers

),

orders as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from raw.jaffle_shop.orders

),

customer_orders as (

    select
        customer_id,

        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders

    from orders

    group by 1

),

final as (

    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders

    from customers

    left join customer_orders using (customer_id)

)

select * from final
```

#### What is Modularity?

## Modularity

Read the docs with dbt's viewpoint on [modularity](https://docs.getdbt.com/community/resources/viewpoint#modularity)

#### Modularity and the Ref Macro

**Note: **The dbt Fusion Engine is in Preview as of October 2025. If you are interested in using Fusion and are a dbt Enterprise customer, please reach out to your dbt sales team to discuss getting Fusion enabled on your account.

#### Troubleshooting dbt run

Extracted captions from video: Troubleshooting dbt run

Let's go ahead and run our models here. So we have customers, we have stg customers stg orders. Down here I'm going to do dbt run and again that's going to look in my whole models directory, pull up all my models and execute all of those. We see here our two staging models executed and then our customers model did.

This is the order of execution. The other benefit of having that ref macro in there is because dbt knows that customers depends on stg jaffle Shop customers and stg jaffle Shop orders. It knows that it needs to build these two objects before it builds the customer's model. If I hadn't built these two and I just tried to maybe click the build button, I would actually get an error because dbt would try to resolve these references to the upstream dependencies.

If I click compile here, it's going to show me what this will resolve to. It would look for our model in this location, but I hadn't built those yet in Snowflake. I built them as SQL files but they didn't exist yet. So that's going to cause an issue if I don't have that.

Let's actually demonstrate that now. So I'm going to go in here and I'm actually going to just drop my tables here. Actually I think they're views, analytics dot. Great.

Okay, let's drop that. Excellent. Okay, so these two views do not exist anymore. So popping back over here, let's say I either that build button back, either click the build button or I did my selection syntax.

They're both going to give me essentially the same thing. So here we'll run customers and we get a failure as expected. So here we see the references resolving to those dedicated locations. So we need to make sure that everything executes before this particular model is built.

So if I go ahead and build, I'll click this drop down arrow next to the build button here. And so you'll notice there are several different commands that we can execute. There's build model, build model downstream, build model upstream, build model upstream and downstream. And then there's run.

There is a difference between build and run. We won't get to that in this section. We'll see that when we get to testing, so stay tuned. But as of right now, build and run will do the same thing in our project, it'll execute our models.

Materialize those in Snowflake. Here I'm going to do run model upstream and that will execute this model as well as anything that is upstream from this particular model. So you'll notice that the syntax that this is using here. Note the difference between these two.

We have basically the same exact syntax. The only Exception is this + sign in front of customers that is going to indicate okay, build customers as well as anything upstream. If I wanted to build something downstream, I would just add a plus sign to the end of customers. However, I don't have any downstream objects, so that's not going to do anything for me here.

So we see dbt built the order of models correctly based on our dependencies.

#### Data Modeling Frameworks

## Data Modeling Frameworks

- [Building a Kimball dimensional model with dbt](https://docs.getdbt.com/blog/kimball-dimensional-model)
- [Data Vault 2.0 with dbt](https://docs.getdbt.com/blog/data-vault-with-dbt-cloud)
- [Medallion Architecture with dbt](https://tsaiprabhanj.medium.com/medallion-architecture-with-dbt-a40050743be3) 
- [Normalized vs Denormalized](https://medium.com/analytics-vidhya/database-normalization-vs-denormalization-a42d211dd891)

#### Naming Conventions

## Naming conventions

Want to learn more about naming conventions? Visit the dbt developer blog and explore the blog post about [Stakeholder-friendly model names: Model naming conventions that give context](https://docs.getdbt.com/blog/stakeholder-friendly-model-names)

#

#### Reorganize Your Project

#### Materialization Strategies

Extracted captions from video: Materialization Strategies

The last thing that I'm going to do to clean up my project is follow best practices when it comes to materialization strategy So let's go ahead and pop into our dbt project YAML file and all the way at the bottom of our file here we have the section for models and then our project here. The name of our project on line 5 corresponds to this name. And we want this to be something specific. Pretty much it should be the name of the project that we have over here in the ui.

So I'm actually going to just put that name here so that these two match. Excellent. There's a comment indicating that this applies to all the files under Models slash example. This was our folder that we had previously but we just deleted.

So we are going to remove our comment here because we removed that folder and then we have this folder here but again we've removed it. So let's change this to a folder that we do have now staging. So this is saying for all of the models in my staging folder in my dbt Fundamentals on Demand project in my models directory, I want those to be materialized. In this case a view staging models as a best practice should be views.

these are connected to our sources and we're constantly getting new records in our sources. So it doesn't make sense to store the records in a table in our data platform. But keeping this as a view allows us to materialize this object in our data platform but be updated every time we execute this so that we get the most up to date version of our data. The next folder that I want to add is our marts folder.

So, so we've added marts and then similarly we have materialized and marts typically are tables. So we'll put table here. The reason for that being is marts are typically our most downstream tables and these are the ones that are getting queried by our BI tool. So if I did have this as a view.

That means every time that someone executes a query from my BI tool, this is going to execute the view. However, if I have this materialized as a table, then I don't need to execute the view. The data object already exists with the appropriate transform data. So we'll keep that as table here.

You'll notice these plus signs here. These are to indicate that this is a property, not a folder. You can have additional nested folders here. If I had a folder within staging, that would populate here.

So this is going to be, the materialization strategy at the folder level. The next piece to note is the folders within each of these directories. One of the best practices is to split out the subfolders in staging connected to a specific source. Right now I only have one source system in my project, Jaffle Shop.

So we're going to add a folder here called Jaffle Shop and slide those files into there. Perfect. In our marts layer here, instead of matching this to our source system, typically we match this to whatever team or business entity is consuming those particular objects. These are my customers.

So a lot of teams might be consuming this specific table. So right now we'll leave this at a high level marts folder. But note, for your project, you might want to put this in a subfolder that is specific to who might be consuming that particular model. We'll go ahead and commit here.

So we have changed. Oh, we are getting a message here. We have one unsaved file. Let's go back.

Excellent. Okay, so here at the top, our dbt project YAML file has this little blue dot next to it that's indicating that this model is or this file has not been saved. Let's go ahead and save that. Now we will commit and indicate that we have changed the materialization strategy at the folder level in our dbt project YAML file and added a subfolder jaffle shop to our staging folder.

Great. So we have successfully cleaned up our project. We have our materialization strategy in place. We have our marts and our staging high level folders within our models directory.

We've renamed our dim Customers model and and we've added a subfolder jaffle shop. Our last piece here is. Let's just run this to make sure that everything is working the way that we expect it to. Noting that I did change the name of this model here, so we'll do dim customers now instead.

Perfect. because we've changed the name of a model here from customers to dim customers. dbt is still going to have that customers object in here. And the reason for that being is even though they're the same query, dbt recognizes these as two different data objects.

So it's not going to drop that customer's view since it is technically a different object. The next step in refactoring our query here is to talk a little bit more about the source that we are pulling from and getting a better picture of our source in our specific lineage here. So go ahead and hop to the next section on sources.

#### Practice

## Practice

	Complete the exercise in this section in your dbt project. Remember to make adjustments for the data platform you are using and refer to [Quickstarts](https://docs.getdbt.com/quickstarts) and [docs](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections) if you encounter issues. Debug issues and consult the documentation for dbt and your data platform as part of the practice exercise. **REMINDER: **BigQuery users, your database name is not *raw*, it is dbt-tutorial. 

	### Quick Project Polishing

	

		- In your dbt_project.yml file, change the name of your project (at the top of the project AND underneath the 'models' heading further down)

	

	### Staging Models

	

		- Create a staging/jaffle_shop directory in your models folder.

		- Create a stg_jaffle_shop__customers.sql model for raw.jaffle_shop.customers

	

```sql
select
    id as customer_id,
    first_name,
    last_name

from raw.jaffle_shop.customers
```

	

		- Create a stg_jaffle_shop__orders.sql model for raw.jaffle_shop.orders

	

```sql
select
    id as order_id,
    user_id as customer_id,
    order_date,
    status

from raw.jaffle_shop.orders
```

	### Mart Models

	

		- Create a marts/marketing directory in your models folder.

		- Create a dim_customers.sql model

	

```sql
with customers as (

     select * from {{ ref('stg_jaffle_shop__customers') }}

),

orders as ( 

    select * from {{ ref('stg_jaffle_shop__orders') }}

),

customer_orders as (

    select
        customer_id,

        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders

    from orders

    group by 1

),

final as (

    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce (customer_orders.number_of_orders, 0) 
        as number_of_orders

    from customers

    left join customer_orders using (customer_id)

)

select * from final
```

	### Configure your materializations

	

		- In your dbt_project.yml file, configure the staging directory to be materialized as views.

	

```
models:
  jaffle_shop:
    staging:
      +materialized: view
```

	

		- In your dbt_project.yml file, configure the marts directory to be materialized as tables.

	

```
models:
  jaffle_shop:
  ...
    marts:
      +materialized: table
```

	### Building a fct_orders Model

	***This part is designed to be an open ended exercise - see the exemplar on the next page to check your work.***

	

		- Use a statement tab or Snowflake to inspect raw.stripe.payment

		- Create a stg_stripe__payments.sql model in models/staging/stripe

		- Create a fct_orders.sql (not stg_orders) model with the following fields.  Place this in the marts/financedirectory.

			

				- order_id

				- customer_id

				- amount (hint: this has to come from payments)

			

		

	

	### Refactor your dim_customers Model

	

		- Add a new field called lifetime_value to the dim_customersmodel:

			

				- lifetime_value: the total amount a customer has spent at jaffle_shop

				- Hint: The sum of lifetime_value is $1,672

#### Exemplar

## Exemplar

	### Self-check stg_stripe_payments, fct_orders, dim_customers

	*Use this page to check your work on these three models.*

	**staging/stripe/stg_stripe__payments.sql**

```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,

    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount,
    created as created_at

from raw.stripe.payment 
```

	**marts/finance/fct_orders.sql**

```sql
with orders as  (
    select * from {{ ref ('stg_jaffle_shop__orders' )}}
),

payments as (
    select * from {{ ref ('stg_stripe__payments') }}
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
```

	**marts/marketing/dim_customers.sql** 

	*Note: This is different from the original dim_customers.sql - you may refactor fct_orders in the process.

```sql
with customers as (
    select * from {{ ref ('stg_jaffle_shop__customers')}}
),
orders as (
    select * from {{ ref ('fct_orders')}}
),
customer_orders as (
    select
        customer_id,
        min (order_date) as first_order_date,
        max (order_date) as most_recent_order_date,
        count(order_id) as number_of_orders,
        sum(amount) as lifetime_value
    from orders
    group by 1
),
 final as (
    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce (customer_orders.number_of_orders, 0) as number_of_orders,
        customer_orders.lifetime_value
    from customers
    left join customer_orders using (customer_id)
)
select * from final
```

#### Resources & Review

## Resources

- [List of dbt commands](https://docs.getdbt.com/category/list-of-commands) (docs)
- [dbt node selection syntax](https://docs.getdbt.com/reference/node-selection/syntax) (docs)
- [Introduction to sql](https://learn.getdbt.com/courses/introduction-to-sql) (dbt course)
- [Anatomy of a SQL query](https://medium.com/@lomso.dzingwa/the-anatomy-of-a-sql-query-189dd0664851) (article)
- [Advanced SQL](https://medium.com/@datainsights17/subqueries-and-ctes-in-sql-aa1ff4b17686)(article)
- [Version Control basics](https://docs.getdbt.com/docs/cloud/git/version-control-basics) (docs)

## Review

	### Models

	

		- Models are .sql files that live in the models folder.

		- Models are simply written as select statements - there is no DDL/DML that needs to be written around this. This allows the developer to focus on the logic.

		- In dbt Studio, the Preview button will run this select statement against your data warehouse. The results shown here are equivalent to what this model will return once it is materialized.

		- After constructing a model, dbt run in the command line will actually materialize the models into the data warehouse. The default materialization is a view.

		- The materialization can be configured as a table with the following configuration block at the top of the model file:

	

```
{{ config(
materialized='table'
) }}
```

	

		- The same applies for configuring a model as a view:

	

```
{{ config(
materialized='view'
) }}
```

	

		- 

			When dbt run is executing, dbt is wrapping the select statement in the correct DDL/DML to build that model as a table/view. If that model already exists in the data warehouse, dbt will automatically drop that table or view before building the new database object. *Note: If you are on BigQuery, you may need to run dbt run --full-refresh for this to take effect.

		

		- 

			The DDL/DML that is being run to build each model can be viewed in the logs through the dbt interface or the target folder.

		

	

	

	

### Modularity

	

		- We could build each of our final models in a single model as we did with dim_customers, however with dbt we can create our final data products using modularity.

		- **Modularity** is the degree to which a system's components may be separated and recombined, often with the benefit of flexibility and variety in use.

		- This allows us to build data artifacts in logical steps.

		- For example, we can stage the raw customers and orders data to shape it into what we want it to look like. Then we can build a model that references both of these to build the final dim_customers model.

		- Thinking modularly is how software engineers build applications. Models can be leveraged to apply this modular thinking to analytics engineering.

	

	### ref Macro

	

		- Models *can* be written to reference the underlying tables and views that were building the data warehouse (e.g. analytics.dbt_jsmith.stg_jaffle_shop_customers). This hard codes the table names and makes it difficult to share code between developers.

		- The ref function allows us to build dependencies between models in a flexible way that can be shared in a common code base. The ref function compiles to the name of the database object as it has been created on the most recent execution of dbt run *in the particular development environment.* This is determined by the environment configuration that was set up when the project was created.

		- Example: {{ ref('stg_jaffle_shop_customers') }} compiles to analytics.dbt_jsmith.stg_jaffle_shop_customers.

		- The ref function also builds a lineage graph like the one shown below. dbt is able to determine dependencies between models and takes those into account to build models in the correct order.

### Modeling History

	

		- There have been multiple modeling paradigms since the advent of database technology. Many of these are classified as normalized modeling.

		- Normalized modeling techniques were designed when storage was expensive and computational power was not as affordable as it is today.

		- With a modern cloud-based data warehouse, we can approach analytics differently in an *agile* or *ad hoc* modeling technique. This is often referred to as denormalized modeling.

		- dbt can build your data warehouse into any of these schemas. dbt is a tool for *how* to build these rather than enforcing *what* to build.

	

	### Naming Conventions 

	In working on this project, we established some conventions for naming our models.

	

		- **Sources** (src) refer to the raw table data that have been built in the warehouse through a loading process. (We will cover configuring Sources in the Sources module)

		- **Staging** (stg) refers to models that are built directly on top of sources. These have a one-to-one relationship with sources tables. These are used for very light transformations that shape the data into what you want it to be. These models are used to clean and standardize the data before transforming data downstream. Note: These are typically materialized as views.

		- **Intermediate** (int) refers to any models that exist between final fact and dimension tables. These should be built on staging models rather than directly on sources to leverage the data cleaning that was done in staging.

		- **Fact** (fct) refers to any data that represents something that occurred or is occurring. Examples include sessions, transactions, orders, stories, votes. These are typically skinny, long tables.

		- **Dimension** (dim) refers to data that represents a person, place or thing. Examples include customers, products, candidates, buildings, employees.

		- Note: The Fact and Dimension convention is based on previous normalized modeling techniques.

	

	### Reorganize Project

	

		- When dbt run is executed, dbt will automatically run every model in the models directory.

		- The subfolder structure within the models directory can be leveraged for organizing the project as the data team sees fit.

		- This can then be leveraged to select certain folders with dbt run and the model selector.

		- Example: If dbt run -s staging will run all models that exist in models/staging. (Note: This can also be applied for dbt test as well which will be covered later.)

		- The following framework can be a starting part for designing your own model organization:

		- **Marts** folder: All intermediate, fact, and dimension models can be stored here. Further subfolders can be used to separate data by business function (e.g. marketing, finance)

		- **Staging** folder: All staging models and source configurations can be stored here. Further subfolders can be used to separate data by data source (e.g. Stripe, Segment, Salesforce). (We will cover configuring Sources in the Sources module)

	

	

	

	

Want to learn more about jinja and macros? Check out our free online course on[Jinja, Macros, and Packages](https://learn.getdbt.com/courses/jinja-macros-and-packages)!

#### Knowledge check-Models

## Sources 60min
<a id="sources-60min"></a>

### Understanding Sources
<a id="sources-60min-understanding-sources"></a>

#### Learning Objectives

## Learning Objectives

- Explain the purpose of sources in dbt.
- Configure and select from sources in your data platform.
- View sources in the lineage graph.
- Check the last time sources were updated and raise warnings if stale.

#### What are Sources?

Extracted captions from video: What are Sources?

All of this learning is making me hungry. I think we should make some banana bread. I know in order to do that we first need to gather all of our ingredients together. Then I'm going to prepare some of those, such as peeling the bananas.

Combine those ingredients in two bowls, one for dry, one for wet. Then I'm going to mix those two bowls together and finally bake it for the final and delicious product. Similar to baking, the analytics workflow relies on each modular step to create an elegant final product. Instead of gathering ingredients, we will start with our sources, which is just raw data from our tables that we are loaded into our data platform or warehouse.

These sources will then be combined with other layers in our project to "bake" our final models. What we know is in order to reference our database objects, we use a direct string such as raw.stripe.payments. While this is correct, what happens if a change is made to the raw data such as a name or a schema change? Now, anywhere that raw.stripe.payments

is referenced, it will need to be updated with new information. If you are using that source multiple times, that's hours of manual tedious work that can be better spent on other tasks. I'm sure you'd enjoy catching up on Netflix shows while completing this tedious work, but your time could be spent doing something much more valuable for your team instead. Let sources in dbt lend you a hand.

Sources allow you to document the raw tables that live in your data warehouse in a YAML file. These are set by referencing the database they are in, the schema and the string of their name. You can even add aliases in that YAML file. Once your YAML file is configured with your sources, instead of writing something like raw.stripe.payments

in your models, you can use what is called the source function or also known as the source macro. This works a lot like the ref function that is used in other models. What this looks like is we might pass something like {{source(‘stripe’, ‘payments’) }} into that source function to look like this, which creates a direct reference to the YAML file we already created. When it gets compiled, dbt will look at the source YAML file and then replace the source function back to the hard code we are familiar with of raw.stripe.payments

in the data warehouse. Returning back to the situation where a small change is made, you can go straight to the YAML file and make the change in one spot and it will tweak everything downstream and that's going to get your models up and running again smoothly and quickly. The other large benefit of sources is that they will now show up in your lineage. Without sources, you will just have lots of blue nodes in your DAG, identifying all the models that you have.

By configuring your sources, you will have aqua nodes on the furthest left side that show the full orchestration of your data transformation all the way from raw data to your final fact and dim models. In summary, sources help build a better banana bread. Configuring your sources is like adding a recipe card that explicitly lists every ingredient. That way you can see exactly what's powering your final product and easily swap out an ingredient if needed.

#### Introduction to YML

Extracted captions from video: Introduction to YML

dbt relies on two primary file types, SQL and YAML. You'll write SQL models to transform your data. You can also use Python models, but if you want to do that, go ahead and check out our advanced course on Python models in dbt. The other core file type is YAML Y-A-M-L These files are essential for configuring dbt and many other applications configuration because they are a simple, readable way to set up your project configurations, model properties and tests.

Before we dive into building a dbt project, we'll first want to get familiar with YAML. So what is YAML? YAML is a human readable data format used for configuration. Think of it as a simple text based way to structure information using nothing but lists and key-value pairs.

It's easy for humans to read and for computers to parse. Let's look at our Docs site. This article is about how we style our YAML. Because YAML is so particular about how it is written, it's really important that we use some kind of a guide or template in order to inform how we write these.

I'm going to look at the example here and break down some of these best practices. Here's an example YAML. What you can see here is that things are stored in a key-value pairs format. So you'll see everything in yellow on the left hand side is the key, and then on the right in white is going to be our value.

The key on the left, the key's on the left, followed by a colon and a space. And then we're going to go ahead and put in that value. For example, we can see name right here. That is going to be our key and event_id is our value.

Indentation is also everything in a YAML file. It's what creates the hierarchy and shows how information is grouped. You'll use spaces never tabs to nest your data. Every item at the same level of indentation belongs to the same group.

So what you can see here is that name. So underneath models we have the name of our model, which is Events. And if we were to follow this straight down the side here, we'll see that everything is nested within the model named Events. The next thing we see in our hierarchy is the columns.

Underneath columns we're going to have all of this information. So the name of the columns we're looking at is event_id, event_time and user_id. Then nested underneath the column event_id, we get a description and some data tests. Similarly with event_time we'll get the same information there.

Under user_id we also get data tests, but these are a little different. So we get the relationships test with the things nested underneath that. This is all you need to know to get started. By understanding these simple rules, you'll be able to confidently navigate and write dbt YAML files catch you in the next video.

#### Configure Sources

#### Reference: Code Snippets

*reminder: those using bigquery should use `dbt-tutorial` as their database instead of `raw`*

	**models/staging/jaffle_shop/_src_jaffle_shop.yml**

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers
      - name: orders
```

	**models/staging/jaffle_shop/stg_jaffle_shop__customers.sql**

```sql
select 
    id as customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop', 'customers') }}
```

	**models/staging/jaffle_shop/stg_jaffle_shop__orders.sql**

```sql
select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from {{ source('jaffle_shop', 'orders') }}
```

#### References Sources in Staging Models

Extracted captions from video: References Sources in Staging Models

Once we have set up our source files and see aqua colored nodes appear in our lineage, it's time to connect those sources to our staging models so we have a complete data map. This is a crucial part of creating a modular dbt project. Remember, sources and staging models should have a one-to-one relationship. So each source should only feed into one staging model.

Referencing sources is similar to using the ref function. We use the source function, which is a macro written with Jinja. You can tell it's Jinja by the {{ curly braces }}. So let's go into our staging models and replace the hard coded path with the source function.

I'm going to start with orders because I already have that one open. In place of this hard coded piece here, I'm going to replace it with the source function. I'm going to press delete. And the shortcut for this is source within the model.

This shortcut will fill out this formula for us, asking for specific information. For our stg_jaffle_shop_orders model, we want this to reference our orders source. So that source name is jaffle_shop. And when I press 'J' it automatically knows because that YAML file has already been configured.

I can type this out or press enter to finish typing. The object name is going to be that table name. This is going to be orders. Once I have that typed, I can press save.

We should see this update our lineage below. But sometimes it takes a minute to think about it. And there we go. We can see down below in our lineage we've got our dim_customers, stg_jaffle_shop_orders and this aqua node now appears with our source.

So now what I want to do is now that I see the lineage worked, I want to see what this SQL compiles to. So I'm just going to press this button here, compile. Once it loads, it'll show us it'll actually replace this source macro here with that hard coded path that we're familiar with from before. So this below in the compiled section is what's being sent to your data warehouse.

This source function here is what helps us see the full data map. Let's do the same thing in our customer staging model. So again, we want to replace this hard code here with the source macro. So I'm going to delete that and again go underscore, underscore source.

And the source name again is jaffle_shop. And this is our customer staging model, so I want this to relate back to our customers table and press save. This source macro, this source function here, is so powerful because if a schema name or a table name changes in your database, you only have to update it in one place: your source YAML file. So if something were to change here, you would only need to change it in one place here.

This prevents broken models and saves you a ton of time. This is an essential part of building a maintainable dbt project. In the source YAML file you'll also see that this lineage is also built out fully from source all the way through. So now's a good time to do a couple of things.

One, run our first dbt command with our sources involved, and two, commit and sync our changes. I'm going to write dbt run just to make sure that all of this is materialized in my data warehouse. So you'll see that everything ran successfully, our staging models and our dim_customers. I'm also going to go ahead and commit and sync these changes as well.

"referenced sources in staging models" Commit changes While writing this YAML file by hand is fine for small projects, it's not realistic for most. Be sure to check out the videos on automatically generating staging models and using the codegen package to generate source files. Use this as an opportunity to generate the stg_payments model that hasn't been written yet as well. Thanks so much for watching and I'll catch you in the next video.

#### Source Freshness

*Note: Since the data you loaded into your data warehouse for this course is static, you might not see the same results if you follow the workflow here. Bookmark this lesson for when you want to try this in the future in your own dbt project.*

	#### Reference: Code Snippets

	**models/staging/jaffle_shop/_src_jaffle_shop.yml**

	

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers 
      - name: orders
        config:
          freshness:
            warn_after:
              count: 12
              period: hour
            error_after: 
              count: 1
              period: day
          loaded_at_field: _etl_loaded_at
```

#### Using the Codegen package

Extracted captions from video: Using the Codegen package

As nice as it would be to only have, a handful of sources to configure in our YAML files, that just isn't realistic. You likely have hundreds, if not thousands of raw tables in your data warehouse that you want to reference in your dbt projects. Instead of configuring all these sources by hand like we have in our demo project, here in this video, we will demonstrate a faster way using the codegen package to automate this process. This is an optional but highly recommended step to make your life easier.

I'm going to start off in a new branch that doesn't have any edits made in it yet. You can also create a new branch to follow along and compare the changes in this branch to any steps you have been completing for dbt Fundamentals. I already have one prepared, so I'm just going to switch over to that branch. In this branch you'll see that I only have my marts folder here with the dim_customers model in it.

I don't have anything else in here yet. The first thing I'm going to do is get the codegen package. So I'm going to go to the dbt package hub. This is going to be hub.getdbt.com.

Once you're on this site here, there's lots of packages that you can install. Our, most popular packages are here at the top, but you can scroll down and there's plenty more to choose from. The one that we're going to look at to help us get all of our sources inputted without doing this by hand is the codegen package. When I click on that, this is going to tell me everything I need to know about how to install it and how to use it.

So the first thing I need to make sure is that I have the correct dbt version. After that I need to create a packages.yml file and input this into it. So I'm going to copy this and create a packages.yml

file. Back in Studio, I'm going to create a new file by clicking that button there, the plus sign up here, or adding it on the side over here. I'm going to paste this into my YAML and press save as. This is going to be called packages.yml .

This YAML file does not need to go in a folder, it just needs to be in your project, so the same directory as your dbt_project.yml file. Now that this is saved, let's go back and see what it says to do next. It says to run this dbt command, run dbt deps, or dependencies, to install the package.

Now that I have this here, we're going to run that command: dbt deps - Enter. Perfect. Our package is installed. Now that the package is installed, we can use a new macro from the codegen package to generate our source YAML.

Let's go look at what those are in this package. These are the things that are created. We have access to being able to use these as a macro in dbt. Now that we have installed this package, the one that we want to use is to generate_source (source).

Here's all the information that we need to know. We can continue to look at all of the information about this, depending on where you might be installing your packages from or how you might want to use them. For this demo here I'm going to use for multiple arguments. I want to pull all of my sources in that I can.

I'm going to copy this and open a scratch pad using the plus sign here. So just a new file and I'm going to paste this in here. Luckily for us, all of our documentation is also going to be our demo project. So our schema name in fact is jaffle_shop Shop and our database name is raw and I want it to pull everything for me.

I don't need to save, all I need to do is press compile. Now that that is run, you can see that this is all of the sources and tables that I have in my data warehouse that has the schema name jaffle_shop. I can copy this and put this into a new into a new YAML file. I'm going to save as.

And now this gets to be my source file. _src_jaffle_shop.yml. And just like that I, I have my source file all created. Nothing done by hand.

I like to store these also within the model layer. So I'm going to put this in my models folder and also create a staging folder for my sources. So this folder name is going to be staging. And then again within my staging folder I like to have the sources.

This one's going to be jaffle_shop. I now can move that into that file there, that folder and that is now created. I also hinted in another video that we have another source. So if I go back to this now, our schema name is going to be Stripe.

I'm going to change that from jaffle_shop to stripe and press compile. And there's that payment table I alluded to in previous videos. Again, I can copy this and paste this into a brand new YAML file and save _src_stripe.yml in my staging folder.

I should add a new folder called stripe. And then drag and drop that into there. Now we have successfully used the codegen package in order to create and configure our sources. At this point we should definitely commit and sync our changes.

Using a package is a massive time saver, especially when you're working with dozens or hundreds of tables. I highly suggest you check out our package hub for even more things that you can do. Thanks so much for watching.

#### Generate staging models

Extracted captions from video: Generate staging models

Once you have your sources configured, the next step, is to connect them to your staging models. But what if you don't already have your staging models created? If you have hundreds or thousands of sources, that's just as many staging models to build. I'm already irritated thinking about how tedious that task is going to be.

Luckily, dbt has an optional but incredibly powerful time saving feature, the Generate Model button. As you can see, I am in our _src_jaffle_shop.yml file. The source YAML file I am using was created using the codegen package from a previous video.

So there are more sources here than in our base dbt Fundamentals demo project. Notice that above each table name the words Generate model appear and it's actually a button. Go ahead and click it, you know you want to 😉. Clicking this button will do two things.

It will create a new staging model file for you and it will pre populate the file that was with the correct source function, automatically referencing the source and table that you clicked on. It's important that while this model is generating, you do not leave the page. So I'm going to click on the one right above customers. So this is an active button.

When I click on it, you'll see it says generating model for source. Stay on this page until it's done. Great, it worked. So what you'll see here is it actually provides an import CTE here at the top that is already selecting from the correct source.

So it's actually referencing our customers table from our Jaffle Shop source. It also automatically gave it a name that we like for our naming conventions. stg_jaffle_shop__customers . This is telling us this is a staging model from the Jaffle Shop source.

And the name of this is our Customers model. It also pulls in all of your column names. Here we can press Save. This will automatically be put in your jaffle_shop folder here on the side here we can go back to our source file and continue to press Generate model on each of these to create all of our staging models.

This is a huge time saver. There's no need to manually create the file or type out the source function. Continue to repeat this as many times until all of your models are created. Once everything is saved, you will see a complete and connected lineage in your DAG from raw data all the way to your staging models.

Don't forget to commit and sync too before you're done. Using the codegen package together with the Generate model button makes building out the foundational layers of your dbt project fast and efficient. This is the best way to get a jump start on your project. That's all for now.

Catch you in the next video.

#### Cleaning up Staging Models

Extracted captions from video: Cleaning up Staging Models

With our lineage established, with our sources set up and our staging models referencing those sources, we can now refine our staging models by cleaning and standardizing the data. This is going to ensure that every downstream model is built on consistent and high quality inputs, and benefits from these improvements. Some rules of thumb for what we do at the staging layer here - really the quick and fast way to say it is - if I had control over how my data was loaded, what would I want it to look like? So the things we're going to be focusing on are renaming columns, filtering rows, typecasting, basic computations, and basic date transformations.

We can also use our style guide that is found on the dbt doc site (docs.getdbt.com) to look at some of those suggestions for what else we could do within our models to ensure consistency, and clarity. Some of the cleanups we'll be able to do in our demo are focusing on the primary key renaming, where we get to have the object in front of id. So instead of it just saying id, we can actually say what kind of id that is.

So let's head back into Studio and let's do some cleanups here. I'm looking at the customer staging model. We can see here it just says id, but if I look back at my orders model as well, it also says id. I'd really like to make this more clear.

So for id in my customer staging model, that's write as customer_id. And then first_name, last_name, that seems okay to me. Let's press save. Now in our orders model, similarly to what we did before, this is id.

We want this as order_id and instead of user_id, we really want to be clear about who the user is. And in this case it's going to be our customer. So let's also rename this to as customer_id. I like order_date and then status.

Let's also say what status this is. This is going to be our order_status. Also, just to highlight, when we create these staging models, we have a CTE called renamed. So this is where all of those renames are happening.

Some other best practices is we'll use snake case, which you can see here how it's written there. So instead of dots or camel case where we're using upper and lowercase letters. This ensures consistency across the board as well. The best practice is the one that you can agree to.

So by doing these types of cleanups at the staging layer like renaming and standardizing, typecasting, etc. make our staging models reliable and easier to use, so downstream models can now confidently reference customer_id, order_id and order_status knowing they're well defined. This small investment up front creates a huge time saving and data clarity for every transformation that follows. It's important here to mention that these renames and these cleanups will happen to everything downstream.

Our source YAML file that we created earlier will not be impacted by this, so in that source YAML file you'll still need to use these column names that come directly from your raw source.

#### Practice

# Practice

	Using the resources in this module, complete the following in your dbt project. **Reminder: **those using BigQuery should use `dbt-tutorial` as their database instead of `raw`. 

	## Configure sources

	

		- Configure a source for the tables raw.jaffle_shop.customers and raw.jaffle_shop.orders in a file called src_jaffle_shop.yml.

	

	**models/staging/jaffle_shop/src_jaffle_shop.yml**

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers
      - name: orders
```

	

		- Extra credit: Configure a source for the table raw.stripe.payment in a file called _src_stripe.yml. Raw Stripe data was loaded during setup in section 3.

	

	## Refactor staging models

	

		- Refactor stg_jaffle_shop__customers.sql using the source function.

	

	**models/staging/jaffle_shop/stg_jaffle_shop__customers.sql**

```sql
select 
    id as customer_id,
    first_name,
    last_name
from {{ source('jaffle_shop', 'customers') }}
```

	

		- Refactor stg_jaffle_shop__orders.sql using the source function.

	

	**models/staging/jaffle_shop/stg_jaffle_shop__orders.sql**

```sql
select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from {{ source('jaffle_shop', 'orders') }}
```

	

		- Extra credit: Refactor stg_stripe__payment.sql using the source function.

	

	## Extra credit

	

		- Configure your Stripe payments data to check for source freshness.

		- Run dbt source freshness.

	

	You can configure your _src_stripe.yml file as below:

```
sources:
  - name: stripe
    database: raw
    schema: stripe
    tables:
      - name: payment
        config:
          loaded_at_field: _batched_at
          freshness:
            warn_after: {count: 12, period: hour}
            error_after: {count: 24, period: hour}
```

#### Exemplar

## Exemplar

	### Self-check _src_stripe.yml and stg_stripe__payment.sql

	### *Use this page to check your work.*

	**models/staging/stripe/_src_stripe.yml**

```
sources:
  - name: stripe
    database: raw
    schema: stripe
    tables:
      - name: payment
```

	**models/staging/stripe/stg_stripe__payment.sql**

```sql
select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    -- amount is stored in cents, convert it to dollars
    amount / 100 as amount,
    created as created_at
from {{ source('stripe', 'payment') }}
```

#### Review

## Review

	### Sources

	

		- Sources represent the raw data that is loaded into the data warehouse.

		- We *can* reference tables in our models with an explicit table name (raw.jaffle_shop.customers).

		- However, setting up Sources in dbt and referring to them with the sourcefunction enables a few important tools.

			

				- Multiple tables from a single source can be configured in one place.

				- Sources are easily identified as green nodes in the Lineage Graph.

				- You can use dbt source freshness to check the freshness of raw tables.

			

		

	

	### Configuring sources

	

		- Sources are configured in YML files in the models directory.

		- The following code block configures the table raw.jaffle_shop.customers and raw.jaffle_shop.orders:

	

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers
      - name: orders
```

	

		- View the full documentation for configuring sources on the [source properties](https://docs.getdbt.com/reference/source-properties) page of the docs.

	

	### Source function

	

		- The ref function is used to build dependencies between models.

		- Similarly, the source function is used to build the dependency of one model to a source.

		- Given the source configuration above, the snippet {{ source('jaffle_shop','customers') }} in a model file will compile to raw.jaffle_shop.customers.

		- The Lineage Graph will represent the sources in green.

	

	

	### Source freshness

	

		- Freshness thresholds can be set in the YML file where sources are configured. For each table, the keys loaded_at_field and freshness must be configured.

	

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers 
      - name: orders
        freshness:
          warn_after:
            count: 12
            period: hour
          error_after: 
            count: 1
            period: day
        loaded_at_field: _etl_loaded_at
```

	

		- A threshold can be configured for giving a warning and an error with the keys warn_after and error_after.

		- The freshness of sources can then be determined with the command dbt source freshness.

#### Knowledge check-Sources

## Data Tests 60min
<a id="data-tests-60min"></a>

### Building Tests
<a id="data-tests-60min-building-tests"></a>

#### Learning Objectives

## Learning Objectives

- Explain why data testing is crucial for analytics.
- Explain the role of data testing in analytics engineering.
- Configure and run generic tests in dbt.
- Write, configure, and run singular tests in dbt.

#### Why Data Testing?

#### What is Data Testing?

#### Generic Tests: unique & not null

#### Reference: Code Snippets

	**models/staging/jaffle_shop/_stg_jaffle_shop.yml**

	*Note: this is a .yml file rather than a .sql file*

```
models:
  - name: stg_jaffle_shop__customers
    columns:
      - name: customer_id
        data_tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
```

#### Generic Tests: accepted values

#### Reference: Code Snippets

**models/staging/jaffle_shop/_stg_jaffle_shop.yml**

*Note: this is a .yml file rather than a .sql file*

```
models:
  - name: stg_jaffle_shop__customers
    columns:
      - name: customer_id
        data_tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
      - name: status
        data_tests:
          - accepted_values:
              arguments:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
                  - return_pending
```

Extracted captions from video: Generic Tests: accepted values

So we've been able to learn how to write tests on our primary keys that, unique and not null. Another powerful test is the Accepted Values test. For my orders table, I actually do have a column that I would like to have an accepted values test on. So that column name is order status.

I need my name key first and then you'll see that red squiggly goes away. So I got excited, started to write my column name. But I need to remember to write that name key first before the column name. Let's double check that I've done that.

Right. Status as order status. I like that. Let's preview this, table as well to see what's happening.

So when an order is placed, I'm expecting a few certain values to be true in the order styles column. You can see a couple here returned completed, but keep scrolling down, that might be all I see. Return pending depending on the amount of rows that came back. So I'm testing to make sure that only a certain certain values are coming through.

So under this column name I'm going to write data test again because this is a new column and I want the accepted values test. When I press Enter, it'll say values. What do you want to be listed in there? I have a list already off to the side here, so I'm going to go ahead and include those.

And as you can tell, YAML indentation. Horrible. So I'm going to press option and shift on my Mac and just keep moving those until they're all in line. And there we have it.

There is our accepted values test on the order status column. If this test fails on, the accepted values, that means that dbt found a value that isn't in my list of accepted values. So I have five things values listed here. But if it finds something else, it's going to shoot out an error and say, hey, we found something else.

You might want to take a look. So before I go ahead and dive in, I want to test something here, too. I think I might have a syntax error here where I need to have a space between my hyphen and my values. That's run dbt test to check these values against our data.

So again, down in that command line at the bottom right dbt test, we'll see the other tests run as well. That not null and unique that we had before. And we also get this accepted values that passed. So that means that these are the only five values in that column.

Optionally, I also could have run dbt test on only this orders model instead of that customer's model. I added this new test in and I might only be interested in how this one runs. So that's going to look like this dbt test select. And now we get to decide what model specifically we would like to test.

This is going to be our stg. Jaffle Shop orders. You can hand, you can type this out here. You could copy and paste it from our YAML or again, you can use those three dots on the side there to copy the name of this model.

So this will now only run the test that we have for this model specifically. So you'll see that the primary key tests that we have on our customers table are not running this one.

#### Generic Tests: Relationships

#### Reference: Code Snippets

**models/staging/jaffle_shop/_stg_jaffle_shop.yml**

*Note: this is a .yml file rather than a .sql file*

```
models:
  - name: stg_jaffle_shop__customers
    columns:
      - name: customer_id
        data_tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
      - name: status
        data_tests:
          - accepted_values:
              arguments:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
                  - return_pending
      - name: customer_id
        data_tests:
          - relationships:
              arguments:
                to: ref('stg_jaffle_shop__customers')
                field: customer_id
```

Extracted captions from video: Generic Tests: Relationships

There's one more test, the relationships test. This is one of the most powerful generic tests. It's the relationships test. It's like a matchmaker for our data.

Who doesn't love a good rom-com? It ensures that every record in one table has, has a matching record in another table, preventing what we call "orphaned data", data that's lost and doesn't belong anywhere. In this Jaffle Shop example, we know that for every order that we have, it should belong to a specific customer. So the relationships test, is going to confirm that link.

It checks that every customer_id in our stg_jaffle_shop__orders model actually exists in the customer_id column for our stg_jaffle_shop__customers model. So let's write this code as well. So we're looking at a new column in the orders model. So let's add this column.

All right, start with name and customer_id. Data tests. And this one's going to be a relationships test. When I press enter on the relationships test, you see that it automatically asks for the field from the foreign key to a reference.

So the key that we're looking for here is customer_id. And the ref that we're looking for is our stg_jaffle_shop__customers. I already have this up here. I'm going to copy and paste.

And just right in between those quotations there, we're going to add that information in. So this field specifies the column we're testing our relationships test on. Then we have data tests in here, and it's the relationships test. That's the name of the generic test.

This is the field that we want to make sure is in, our customers table and also our orders table. And this is the reference, the internal reference in dbt that we're using to connect these two tables together. By using the relationships test, we're building a safety net that makes sure our data models are connected correctly, which is a huge step towards ensuring data quality for our customers. Let's press save.

I'm now very eager to see what the results of this are. Now that I've configured all of our tests, I want to run these. So we're going to use the dbt command line and we're going to type 'dbt test'. dbt will now run all those tests that we just configured in the output.

You'll see if each test passed or failed. If a test fails, dbt provides details about what went wrong, which helps you pinpoint the data issue. Let's open one of these up, such as the not_null test, and look at the details here. So what you'll notice is that dbt runs a SQL query in the background for each test.

What you can see here is that for this not_null test it's actually looking for when the customer_id is null, then it's counting these and it'll say they're going to count these as failure. So if dbt runs its test and finds rows that are against your test, that is when it will fail. So in this case, it's looking for anything that is not zero. Zero is good.

Anything other than zero, that's bad. So it's going to trigger a failure or an error in your test. Now feels like a great time to commit and sync: added data tests. That seems good.

And that's it. By adding a few lines of YAML you've created an automated quality control checklist for your data. And for those of you who want even more testing power, there's a community contributed packages like dbt_expectations that offer a huge library of pre built tests. It's a great way to expand your toolkit.

Check out the dbt Hub website (hub.getdbt.com) for those packages. See you in the next video.

#### Singular Tests

#### Reference: Code Snippets

	**tests/assert_positive_total_for_payments.sql**

	*Note how this is a .sql file in the tests directory*

```sql
-- Refunds have a negative amount, so the total amount should always be >= 0.
-- Therefore return records where this isn't true to make the test fail.
select
    order_id,
    sum(amount) as total_amount
from {{ ref('stg_stripe__payments') }}
group by 1
having total_amount < 0
```

	**dbt Commands**

	

		- Execute dbt test to run all **generic** and **singular** tests in your project.

		- Execute dbt test --select test_type:generic to run only **generic**** **tests in your project.

		- Execute dbt test --select test_type:singular to run only **singular**** **tests in your project.

#### Testing Sources

#### Reference: Code Snippets

	**models/staging/jaffle_shop/_src_jaffle_shop.yml**

```
sources:
  - name: jaffle_shop
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers
        columns:
          - name: id
            description: primary key
            data_tests:
              - unique
              - not_null        
      - name: orders
        config:
          freshness:
            warn_after:
              count: 12
              period: hour
            error_after:
              count: 1
              period: day
          loaded_at_field: _etl_loaded_at
```

#### Data Testing Best Practices

Extracted captions from video: Data Testing Best Practices

A common question we get is when should I test my sources and when should I test my models? It's a great question, and there's a simple but important distinction. Think of your data pipeline like a recipe - thinking back to that banana bread before. Your sources are the raw ingredients, the flour, sugar, butter.

Your models are, the transformed ingredients, like the dough, the cake batter, the final cake itself. So when do you test your sources? You should test your sources to validate the quality of your raw ingredients or raw data. These tests should be simple and focused on the basics.

Are the primary keys unique and not null? Do foreign keys have a valid relationship with a parent table? Are the loaded_at time stamps being populated correctly? Testing sources is an excellent first line of defense.

It gives you confidence that the raw data coming from your ingestion tool is exactly what you expect. If the source test fails, it points to an issue with your data ingestion, not your dbt code. So when do you test your models? Then you should test your models to validate your transformations.

These tests check the integrity of your dbt code and the business logic that you have applied. For models. You can use all types of tests, from simple, unique and not_null checks to more complex singular tests that enforce specific business rules. For example, you might create a singular test on a final model to ensure that a customer's lifetime value is never a negative number.

This is a check on your transformation logic, not the raw data itself. Here's a simple rule to test sources for data integrity and test models for transformation integrity. By using this approach, you'll have a clear, logical testing framework that ensures the quality of your data every step of the way. This is just the start of what's possible with testing.

If you want to learn how to create your own custom generic tests or explore a whole world of testing packages, check out the resources on dbt Lab's website or at the Hub Happy testing!

#### Using dbt Copilot to Generate Data Tests

Extracted captions from video: Using dbt Copilot to Generate Data Tests

So far we've been writing all of our data tests by hand. Now that you've mastered the basics, I want to show you how a tool like dbt Copilot can make this process even faster. dbt Copilot is an AI assistant that lives right inside the dbt platform. It's a great optional feature that can give you a major head start.

Before we use Copilot, we need to first make sure that it is enabled. I can tell by this screen here that I don't currently have it enabled because this button isn't live. What we're going to do is navigate to our account settings by clicking on our name, and "Your Profile" going to account and then we'll see right here. This toggle needs to be turned on.

Pressing Edit in the top right will allow me to edit that, and enable using Copilot. Now that it's enabled, let's head back into Studio. So let's start by adding some tests to our staging customers model. So in my staging folder, Jaffle Shop, I have quite a bit of models in here now, after using the codegen package.

I'm looking at this staging model here. So let me open that up. I don't need dim_customers open anymore. In order to generate tests using Copilot, I'm going to click the button dbt Copilot where it gives me a list of choices that Copilot can help me with.

Let's select Generate, generic tests. Copilot is going to analyze the model. Ideally it's going to identify customer_id as the likely primary key and then generate the YAML code for you. I anticipate, which is exactly what it did, is that my primary key should have a unique and not_null test on them.

Copilot creates this file and configures it automatically. It also analyzes all the other columns in your model and adds any appropriate tests. As you can see here, our customer_id column has been assigned the data tests unique and not_null. It also identified the column first_name and added the data test not_null to that one, similarly with last_name.

So now it's important to check its work. Copilot is an amazing tool, but it isn't perfect. It's always important to check its work and make any corrections. Copilot generates the YAML and adds it to our file.

We then can inspect the code to make sure it's correct. Sometimes the AI might add the test to the wrong file or format the YAML incorrectly. This is why you, as the data developer are the final authority. You should always review generated code and make any necessary changes.

So I know about first_name and last_name. I don't really care if these are null or not. So I'm going to remove these tests. Once I feel comfortable with this, I can press save.

We'll notice that it was added to our file tree over here, right underneath our staging model, so these will be easy to find going forward. Using Copilot is also a great way to get the basic structure for your YAML files. So even if the tests aren't perfect, it can add the models and column blocks, saving you some typing, and then you can add or correct the tests yourselves. Let's try one more with orders.

So going into our orders model, clicking on copilot, let's generate generic tests. Again, those generic tests are those four out of the box tests that dbt has unique not null relationships and accepted values. So with our orders model, these are the tests I came up with. I definitely agree with order ID being unique and not null because that is my primary key, my customer id.

I also would like to be not null similarly with my order date. However, for status Using Copilot is a powerful way to accelerate your workflow. Remember, you always use your own knowledge of data testing best practices to ensure your code is accurate. Once you have used Copilot to generate data tests for each of your models, make sure you do 'dbt run' in order to build all of your models in the warehouse.

That will ensure that you can use 'dbt test' to see how your test did. We can also do a command called 'dbt build'. In another video, we'll break down exactly how that works. 'dbt run' is a good first one to use and then after they are built, run 'dbt test'.

To do those at the same time in DAG order, type in 'dbt build'. This will take every model in your project and it'll do it in your DAG order. So what you'll see is in order, it'll take all of your staging models first, then it'll run all of your tests, building dim_customers, and then your tests on that. Hopefully your screen looks something like this where you have lots of green check marks.

Once you know your models are built and your tests pass, go ahead and commit and sync. Catch you in the next video.

#### What is the dbt Build Command?

#### Using the dbt Build Command

Extracted captions from video: Using the dbt Build Command

So let's see the 'dbt build' command here in the dbt platform. So we have our dim_customers model here. And when we look at the lineage as a reminder, we know that it depends on stg_jaffle_shop__customers and stg_jaffle_shop__orders. So what I want to do here is I want to build dim_customers and its upstream models.

So building these staging models for this demonstration, I've intentionally messed with one of the tests here to make sure that it fails. So from our accepted_values, I've just removed one of those values that I'd really like to see in this model. So from this model here, I can type in the command line here, but I can also use this build button. So that's select build model and upstream and see what happens.

This is telling dbt to build dim_customers and everything that it depends on. So it's going to need to build these sources and these two staging models in order to get to dim_customers. Let's look at the logs here. We know that it failed, and that's because of this test here, this accepted_values test.

Everything else was able to pass, which was anticipated. But we also see that dim_customers down here was skipped. And this is because it depends on this test passing. So what dbt did is it stopped the build process once this failed, they can continue these other tests because it doesn't depend on that failed test.

But dim_customers does rely on this, failed test here. So now you know that it is not being built on faulty data. So the 'dbt build' command overall is the best way to ensure that your downstream models are never built on top of bad data. It's a powerful and essential command for any production dbt project.

#### Practice

# Practice

	Using the resources in this module, complete the following exercises in your dbt project:

	## Generic Tests

	

		- Add tests to your jaffle_shop staging tables:

			

				- Create a file called _stg_jaffle_shop.yml for configuring your tests.

				- Add unique and not_null tests to the keys for each of your staging tables.

				- Add an accepted_values and a relationships test to your stg_jaffle_shop__orders model.

				- Run your tests.

			

		

	

	## Singular Tests

	

		- Add the test tests/assert_positive_value_for_total_amount.sql to be run on your stg_stripe__payment model.

		- Run your tests.

#### Exemplar

## Exemplar

	models/staging/jaffle_shop/_stg_jaffle_shop.yml

```
models:
  - name: stg_jaffle_shop__customers
    columns:
      - name: customer_id
        tests:
          - unique
          - not_null
  - name: stg_jaffle_shop__orders
    columns:
      - name: order_id
        tests:
         - unique
         - not_null
      - name: status
        data_tests:
          - accepted_values:
              arguments:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
                  - return_pending
      - name: customer_id
        data_tests:
          - relationships:
              arguments:
                to: ref('stg_jaffle_shop__customers')
                field: customer_id
```
**Singular Test**

```
tests/assert_positive_value_for_total_amount.sql
```

#### Review

## Review

	### Testing

	

		- **Testing** is used in software engineering to make sure that the code does what we expect it to.

		- In Analytics Engineering, testing allows us to make sure that the SQL transformations we write produce a model that meets our assertions.

		- In dbt, tests are written as select statements. These select statements are run against your materialized models to ensure they meet your assertions.

	

	### Tests in dbt

	

		- In dbt, there are two types of tests - generic tests and singular tests:

			

				- **Generic tests** are a way to validate your data models and ensure data quality. These tests are predefined and can be applied to any column of your data models to check for common data issues. They are written in YAML files.

				- **Singular tests** are data tests defined by writing specific SQL queries that return records which fail the test conditions. These tests are referred to as "singular" because they are one-off assertions that are uniquely designed for a single purpose or specific scenario within the data models.

			

		

		- dbt ships with four built in tests: unique, not null, accepted values, relationships.

			

				- **Unique** tests to see if every value in a column is unique

				- **Not_null** tests to see if every value in a column is not null

				- **Accepted_values** tests to make sure every value in a column is equal to a value in a provided list

				- **Relationships** tests to ensure that every value in a column exists in a column in another model (see: [referential integrity](https://en.wikipedia.org/wiki/Referential_integrity))

			

		

		- Tests can be run against your current project using a range of commands:

- 

				- dbt test runs all tests in the dbt project

				- dbt test --select test_type:generic

				- dbt test --select test_type:singular

				- dbt test --select one_specific_model

			

		

		- Read more here in [testing documentation](https://docs.getdbt.com/reference/node-selection/test-selection-examples).

		- In development, dbt will provide a visual for your test results. Each test produces a log that you can view to investigate the test results further.

	

	

	

	

	

You've learned about the 4 built-in generic tests, but there are so many more tests in packages you could be using! Learn about them in our free online course on [Jinja, Macros, and Packages.](https://learn.getdbt.com/courses/jinja-macros-and-packages)

	Do you want to take your testing knowledge to the next level? Check out our free online course on [Advanced Testing](https://courses.getdbt.com/courses/advanced-testing)!

#### Knowledge check- Data Tests

## Documentation 40min
<a id="documentation-40min"></a>

### Documentation Basics
<a id="documentation-40min-documentation-basics"></a>

#### Learning Objectives

## Learning Objectives

- Explain why documentation is crucial for analytics.
- Understand the documentation features of dbt.
- Write documentation for models, sources, and columns in .yml files.
- Write documentation in markdown using doc blocks.
- View and navigate the lineage graph to understand the dependencies between models.

#### Why is Documentation Important?

#### What is Documentation?

#### Writing Documentation

#### Reference: Code Snippets

	

	**models/staging/jaffle_shop/_stg_jaffle_shop.yml**

```
models:
  - name: stg_jaffle_shop__customers
    description: one unique customer per row
    columns:
      - name: customer_id
        description: the primary key
        data_tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
      - name: status
        description: "{{ doc('order_status') }}"
        data_tests:
          - accepted_values:
              arguments:
                values: ['placed', 'shipped', 'completed', 'returned', 'return_pending']
      - name: customer_id
        data_tests:
          - relationships:
              arguments:
                to: ref('stg_jaffle_shop__customers')
                field: customer_id
```

#### Writing Doc Blocks

****models/staging/jaffle_shop/**jaffle_shop_docs.md**

```
{% docs order_status %}
    
One of the following values: 

| status         | definition                                       |
|----------------|--------------------------------------------------|
| placed         | Order placed, not yet shipped                    |
| shipped        | Order has been shipped, not yet been delivered   |
| completed      | Order has been received by customers             |
| return pending | Customer indicated they want to return this item |
| returned       | Item has been returned                           |

{% enddocs %}
```

Extracted captions from video: Writing Doc Blocks

We've previously learned how to write simple descriptions directly in our YAML files. But what if we have a lot to say about a column? For example, the status column, under our orders table here, has many values that we like to have returned. I'd like to be able to write what each of those values mean, but that means that, trying to describe each of those in our YAML file would make for a very long, and hard to read description.

This is where doc blocks can be really helpful. We can write these in a separate markdown file and then reference it here in this YAML file. This will help to keep our YAML clean and allows us to write more detailed and organized documentation. So let's create a markdown file in this jaffle_shop folder.

I'm going to create my markdown [file]. So, create a file and let's name this jaffle_shop_docs and then this is a markdown file so .md . It's important to note that the name of this should be something that you know where to find it at. But we can have multiple doc blocks written in this document.

How we'll write this so that dbt knows how to reference it is we'll start with this tag at the top. Curly braces and percent signs, write the word docs, and then here in this place we will write the doc_block_name. Then we'll write our, doc block information below that, and end our doc blocks with a tag that says enddocs. So this is the basic structure for how to write these markdown files in dbt.

I know that I want to write a doc block for the order_status column. So let's go ahead and name this document order_status. So when I go to reference it, this is the name that I will be referring to. Here is where we'll put all of our doc block information at.

I have this written down on the side already because it's kind of long, so I'm going to copy and paste that in. You should also have access to this to keep this organized. A markdown table is perfect for defining each status value. I can now see that the status placed, the definition of that is "Order placed but not yet shipped."

So there's no confusion as to what each of these pieces mean in my data. So what do these values mean? Let's press save. Once you've written your description, you can press Markdown Preview below to see what it looks like to make sure that it turns out okay.

So you can see that we do have a table here that is organized so now it's time to reference this. Back in our stg_jaffle_Shop.yml underneath our order_status, we start similarly as the other ones by writing description. But instead of writing all of that information that we just did, we're going to reference our doc block that we just wrote.

In order to do this we do quotations and then two curly brackets, space doc parentheses, and then the name of that doc block that we just created. We called it order_status. This doc macro takes the name of our doc block, which is order_status, as its argument. It's important to use the doc block name and not the file name, as you can have multiple doc blocks in a single markdown file.

Let's press save. By using doc blocks, we keep our YAML files clean, which provide rich, detailed documentation. We'll be able to see this description in a future video when we discuss documentation and viewing it in Catalog. And with that you now know how to write your documentation.

I'll catch you in the next video.

#### Documenting Sources

#### Reference: Code Snippets

	**models/staging/jaffle_shop/_src_jaffle_shop.yml**

```
sources:
  - name: jaffle_shop
    description: A clone of a Postgres database
    database: raw
    schema: jaffle_shop
    tables:
      - name: customers
        description: Raw customers data
        columns:
          - name: id
            description: primary key
            data_tests:
              - unique
              - not_null        
      - name: orders
        config:
          freshness:
            warn_after:
              count: 24
              period: hour
            error_after:
              count: 48
              period: hour
          loaded_at_field: _etl_loaded_at
```

#### Using dbt Copilot to Generate Documentation

Extracted captions from video: Using dbt Copilot to Generate Documentation

At this point, you should know how to write documentation in dbt by hand using the YAML files. We can also use dbt Copilot to give us a head start. It's great for generating initial documentation, but remember you are the data expert, so you should always review and refine its work. Start by making sure that dbt Copilot is enabled in your user settings.

This was covered in the video "Using Copilot for testing". Once it's on, we can start using it in the dbt Studio. For this demo, I'm going to continue to work in a branch that has more sources in it that I used with the codegen package and Copilot for testing. So let's open up one of our models.

I'm going to go ahead and select our stg_jaffle_shop_customers model. We want to make sure we click into the model and not the YAML file in order to use dbt Copilot. I'm going to go ahead and click on dbt Copilot and I'm going to ask it to generate documentation. If the YAML file already exists, it's going to find that and update it.

Since we've done that already with Copilot, we'll see that it just continues to add on to that. If that YAML file didn't exist, it would create a new one. So let's see how it did. It looked at stg_jaffle_shop__customers and it added a description at the model level here to describe what that model does and also column level descriptions.

I can already see one mistake here. We've got first_name, last_name and then an additional last_name. Let's delete that extra one there. Let's check out what it wrote.

stg_jaffle_shop__customers the description it provided is "This model serves as a staging layer for the customer data from the 'jaffle_shop' source. It renames and selects customer related fields to ensure consistency and clarity for downstream models." What about the column levels? "A unique identifier for each customer."

I might also add primary key. Even though a unique identifier is the same thing, it's nice to be explicit. first_name and last_name are pretty straightforward. It's "The first name of the customer."

and "The last name of the customer." I'm pretty satisfied with this so I'm going to press Save. Just as a reminder, Copilot is an excellent tool to help you get started. It's also going to save you a lot of time for manual typing.

Just as a reminder, it's not perfect. It might describe a column with a simple description when you want it to be a little bit more in depth or you want to also have a very specific business use case in mind. When you write that description, be sure to read through it carefully. You can easily add more detail or correct any inaccuracies.

What I also enjoy about having the dbt Copilot documentation tool is it'll carry over all of my column names. So when I am ready to add my descriptions and my data tests, I don't also have to go hunt down what are all those column names and bring them over. Once you've used Copilot to add those descriptions into your model YAML files, remember to read through it and check that it all seems correct. Make any edits that you see necessary.

Even if a description isn't perfect, having the column name and the description field already in the file is a great head start. You can add the specific details or even add a doc block reference to it. By using Copilot as a starting point and then applying your own expertise, you can make the documentation process incredibly efficient and ensure your project is well understood by everyone. A last reminder to save all your work and also hit that commit and sync.

Don't want to lose our changes. We definitely added a lot. Thanks so much for watching.

#### Merge to Main

Extracted captions from video: Merge to Main

We've reached a major milestone in our project. You've been working hard in your feature branch, creating staging models, adding descriptions and ensuring that your data is in great shape using data testing. Now it's time to bring all of that hard work into our main branch so we can prepare for deployment. Think of it like this.

Your feature branch is a workshop where you've been building and perfecting a new piece of furniture. The main branch is the finished product showroom. Before you move your new creation to the showroom, you want to make sure it's polished and ready for the world. Before we merge our changes, we always want to do a final check.

A big part of being a dbt practitioner is knowing when your work is ready for prime time. In this course, we've covered a lot of important steps to ensure our project is high quality. You want to make sure you've completed a few things, you've configured your sources. We need to make sure dbt knows where your raw data lives.

If you've been following along, you'll know that we've got this source Jaffle Shop YAML file here and it has all of our sources configured. You've likely accomplished this step in your own project, but I took it just a bit further to show you what's possible. I used the codegen package paired with dbt Copilot to ensure that I have everything set up for my next step. So you'll also see that I have a stripe source YAML file here as well.

The next thing we need is that we have written descriptions for our sources, our models and our columns. This helps our team understand what the data is and where it comes from, making it much more accessible and trustworthy. I have that in my staging YAML files here. So for Jaffle Shop, you'll find it there.

And for my Stripe you'll see it down here. So you'll see in here I've got my descriptions. And you'll also see the data tests. Remember that those tests are an automated safety net for our data.

We're putting our not_null and unique on our primary keys. That's a really crucial step. So with my description, you'll see primary key and you should also see it paired with a unique and not_null test. We should also have our staging models that we've created.

Here is our staging model for the customers refactored with an import CTE at the top. You'll also see that for our orders table as well. We've also done some renames here to make these column names make more sense. This all should be connecting back to our dim_customers model using our ref [function]

so that we can get a full picture full data map here in our DAG.

Our full project: source --> staging model All, the way to our --> dimension model here. Now that our work is polished and ready, it's time to merge it. A best practice is to create a pull request that connects to your git provider. In this demo environment, we don't have access to that git provider at this time, so we'll skip that for now.

But just know that it's best practice to go through a pull request, getting approval by someone else on your team before putting it in that showroom, or that main branch. So all we need to do here is click "Merge this branch to main". You'll see it thinking and once it says "Create branch", that means you've actually been switched to the main. So now the main branch is all that hard work that you've been doing.

🥳 Congratulations 🎉 You've successfully built your first set of dbt models and they're now officially a part of the project's foundation. We've gone from raw data to clean, well documented staging layer. The reason we merge our work to main is simple. It's the official version of our project.

It's the blueprint that dbt will use for our next big step deployment. In the next section of dbt Fundamentals, we'll talk about how to take this project and run it in production environment so that your models are always up to date for your stakeholders.

#### Practice

## Practice

	Using the resources in this module, complete the following in your dbt project:

	### Write documentation

	

		- Add documentation to the file models/staging/jaffle_shop/_stg_jaffle_shop.yml.

		- Add a description for your stg_jaffle_shop__customers model and the column customer_id.

		- Add a description for your stg_jaffle_shop__orders model and the column order_id.

	

	### Create a reference to a doc block

	

		- Create a doc block for your stg_jaffle_shop__orders model to document the status column.

		- Reference this doc block in the description of status in stg_jaffle_shop__orders.

	

	**models/staging/jaffle_shop/_stg_jaffle_shop.yml**

```
models:
  - name: stg_jaffle_shop__customers
    description: Staged customer data from our jaffle shop app.
    columns: 
      - name: customer_id
        description: The primary key for customers.
        data_tests:
          - unique
          - not_null

  - name: stg_jaffle_shop__orders
    description: Staged order data from our jaffle shop app.
    columns: 
      - name: order_id
        description: Primary key for orders.
        data_tests:
          - unique
          - not_null
      - name: status
        description: "{{ doc('order_status') }}"
        data_tests:
          - accepted_values:
              arguments:
                values:
                  - completed
                  - shipped
                  - returned
                  - placed
                  - return_pending
      - name: customer_id
        description: Foreign key to stg_customers.customer_id
        data_tests:
          - relationships:
              arguments:
                to: ref('stg_jaffle_shop__customers')
                field: customer_id
```

	**models/staging/jaffle_shop/_jaffle_shop.md**

```
{% docs order_status %}
    
One of the following values: 

| status         | definition                                       |
|----------------|--------------------------------------------------|
| placed         | Order placed, not yet shipped                    |
| shipped        | Order has been shipped, not yet been delivered   |
| completed      | Order has been received by customers             |
| return pending | Customer indicated they want to return this item |
| returned       | Item has been returned                           |

{% enddocs %}
```

	

	### Extra Credit

	

		- Add documentation to the other columns in stg_jaffle_shop__customers and stg_jaffle_shop__orders.

		- Add documentation to the stg_stripe__payment model.

		- Create a doc block for another place in your project and generate this in your documentation.

#### Review

## Review

	### Documentation

	

		- Documentation is essential for an analytics team to work effectively and efficiently. Strong documentation empowers users to self-service questions about data and enables new team members to on-board quickly.

		- Documentation often lags behind the code it is meant to describe. This can happen because documentation is a separate process from the coding itself that lives in another tool.

		- Therefore, documentation should be as automated as possible and happen as close as possible to the coding.

		- In dbt, models are built in SQL files. These models are documented in YML files that live in the same folder as the models.

	

	### Writing documentation and doc blocks

	

		- Documentation of models occurs in the YML files (where generic tests also live) inside the models directory. It is helpful to store the YML file in the same subfolder as the models you are documenting.

		- For models, descriptions can happen at the model, source, or column level.

		- If a longer form, more styled version of text would provide a strong description, **doc blocks** can be used to render markdown in the generated documentation.

#### Knowledge check-Documentation

## Deployment 30min
<a id="deployment-30min"></a>

### Understanding Deployment
<a id="deployment-30min-understanding-deployment"></a>

#### Learning Objectives

## Learning Objectives

- Understand why it's necessary to deploy your project.
- Explain the purpose of creating a deployment environment.
- Schedule a job in dbt.
- Review the results and artifacts of a scheduled job in dbt.

#### What is Deployment

Extracted captions from video: What is Deployment

All of our work in dbt so far has been in development. Each of us have been working in our own sandbox environment to write models, tests, documentation. All of the tables that we've built, we've built in our own development schema, like dbt_bhipple. Now we're going to focus on deploying dbt or putting our dbt project into production.

This will be powerful in a few different ways. First, deploying dbt involves running dbt commands on a schedule. This will allow dbt to build models on whatever cadence you need them to. You can run dbt nightly or on, the weekends without needing to log into the dbt site.

We can run, we can do dbt test, we could do dbt build or any other dbt command that we want. Second. Second, when we deploy dbt, all of our models will be built into a production schema. This is a schema that we can then point a BI tool at.

This production schema can then be referenced as the single source of truth. All of the development schemas are completely separate, and that allows developers to tinker and refactor code without breaking the models in production. Third, when we deploy dbt, dbt will use the main branch for building models. That's why all of the work we've done so far has been in a different branch, our development branch.

We can develop our models and our tests on those branches instead of messing up the production branch. That way we don't interrupt the building of the models that power our dashboards and our reporting. So after refactoring code, you can then merge your branch to main and your work will be included in the next production run. All in all, deployment allows your finalized models to be built on a schedule so that you can focus on developing the next set of models without breaking the data that is driving the rest of your business.

#### Set up a Deployment Environment

#### Set up a dbt job

Extracted captions from video: Set up a dbt job

Now that we've established our deployment environment, let's pop back into our environment list here. So now we have two different types of environments in our accounts, and I'm going to set up a job. So we'll create a job here and we'll select deploy job. There are different types of jobs.

We'll stick with the deploy job for this video here. In my deploy job, we need to give this a name. Typically, the best practice here is to indicate what exactly is going to be running in this job. Is it your entire dbt project?

Is it a subset? Are you only running maybe a specific data pipeline or perhaps the frequency that that job is going to be executed. So we're going to call this a daily run, because this is going to be run every day and it will be my entire project. Here we get to indicate the environment.

Again, I only have one deployment environment, so that's all that's going to show up here. If I had multiple deployment environments, I could indicate which deployment environment this job should live in. Production is the only one, so we'll leave that selected here. The execution settings are what we tell dbt to do with our code.

So in our environment we are indicating this is the specific code that we should use, but our job settings indicate, okay, now that we know the code to use, what exactly do you want me to do with that code? And our execution settings are the way to tell dbt what we want it to do. So our commands here, we do want to run source freshness and dbt build is going to be the command. I'm going to leave off any sort of selectors here.

I want this to run my entire project. Again noting dbt build. This is going to create our models. Do any of our testing.

We don't have it in our project, right now, but execute any seeds or snapshots. And then we do want to generate our documentation. So we've added documentation to our project and we want this to actually generate in our dbt catalog site. And then down here, this is our triggers.

So once we know what execution settings, we want to know when to actually execute those commands. So we have a few different options. One, we could run this on a schedule. I could indicate, at specific intervals on specific days.

So here I have days of the week. I can leave these all checked. Maybe I want this to be every single day. Maybe I only want it to be Monday through Friday.

Since this is a daily run, we're going to leave everything checked. The next piece here is the intervals. So maybe I only want this to run once a day. here, this is indicating, some amount of time has passed, right?

So every hour. So that's going to run 24 times in a day. instead of selecting, an interval here, I want this to just run once a day. So we'll select a specific time, noting this is in UTC.

So I want this to execute at, let's say 12 UTC. So we'll just leave this at 12. The last option that we might have here is a CRON schedule. So maybe there's a specific use case where I want a specific minute or hour of the day, depending on my needs for how often I want this data, to be updated.

So I could use a CRON schedule here. If you're unfamiliar with cron, here is some information around how to create a cron schedule, and a nifty little site that can help you out there. If I don't want this to run on a schedule, maybe this is going to be impacted by another job that I've set up in my project. So I could trigger this job using job completion.

I can indicate that this job should execute when another job finishes. Maybe that's a job in a different project. Maybe it's a job within the same project, but just a different job. So we have a lot of different options here.

I have a lot of projects in this account, if I selected a specific, project in my account, then I can choose the job. So here in maybe my canvas project, I have a production job and I want this job in my project to execute when this prod job in my canvas project has been successful. In my advanced settings here, there are a few different pieces of information. There are some information, boxes that you can check out, Overall, in our job settings, I can indicate in my job what I want to execute, what I want dbt to do with my code, and when I want my job, to be triggered.

#### Review a dbt Job

#### dbt Catalog Overview

Extracted captions from video: dbt Catalog Overview

Here I have a successful production run of a job in my dbt project. Now that I've had a successful job run and we have our dbt docs generate command that's been executed. Let's pop into dbt Catalog.

Here in dbt Catalog we get an account level view of all of the projects that we have in our specific account.

I'm going to go to the project that I've been working in and we can see a few different items. Here I see some models, some sources, some tests that I've built in this specific project. So I'll click into my models. Here Here I have my Sage Jaffle Shop customers model.

So let's click into this and we see a few different things. Here we see the description that we've created in our YAML file. We see the latest run of this specific model as well as the test results for the tests that we have in this we also get to see the

code that's being used as well as the columns that are in this model. Not only do we get to have the model level lineage, but we also can see our column level lineage.

So looking at this here I get some information about where this column has come from. So so our Jaffle Shop customer source as well as where this column

is being used downstream here we have a small project, but this is going to be useful for any moments where I might need to troubleshoot. Maybe this column is failing in my Dim Customers model and I want to see where is the point of failure. So coming in here and looking at the column level lineage, I get a good idea if this column has any errors or what transformations I'm doing.

This column has not been transformed. But noting that this would have a

little icon at the top here indicating that there has been a transformation if there was one. Some other items that we have in our project in dbt catalog is the performance. So

this is indicating when my project last was executed and for this specific model how long it took to build.

This took 0.39 seconds or 390 milliseconds to execute. So this gives me a good idea of the health of my specific model. Here we also might see any recommendations for our model here we don't have any recommendations, but let's go to a model that might have some recommendations.

Here in Dim Customers, if I go to recommendations we see two One is This model is not documented. I don't have a description, so that is missing. The other piece is I don't have a test on my Dim Customers model and so that is a high level recommendation. Testing our primary

keys is very important.

So this is giving me even a priority measure for the recommendations. These are based on dbt Labs best practices. let's pop back to our main project here and we can view the lineage for our project. So we viewed the column level lineage.

We also can view our model level lineage for our specific project. We not only get to see this in dbt Studio, but we can see this here in, dbt Catalog as well.

#### Deeper Dive into dbt Catalog

Extracted captions from video: Deeper Dive into dbt Catalog

Here in dbt catalog, I have my dbt fundamentals course project. A few models in my project here, but I want to show a, lineage and some dbt catalog metadata from a larger project. So we get an idea of some of the different functionalities here. So let's exit out of this and let's pop into a project that's a little bit bigger Here I have a dbt project with a lot of different models.

Not as big as the biggest project that I've ever seen, but quite a few more assets than we've created in dbt, fundamentals course. So here I get an idea of the flow of my data from my source all the way through to some of my maybe intermediate models and down to some aggregations beyond my fact and dimension tables. We also can see some other nodes here. This is my exposures node.

So check out our exposures course if that's something of interest to you. This is essentially indicating where this model is being exposed in maybe a dashboard in my BI tool. Some other information that we might have here is some snapshots. So this is going to capture the historical changes of my data as my data changes.

So check out our dbt snapshot course to take a look a little bit more at what exactly snapshots can allow you to do. the last piece in our lineage is our seeds. So this SED node, this is going to be a CSV file that I have in my project. Check out our seeds course to learn a little bit more about seeds.

Beyond our lineage here. We can exit out of this and we can take a look at the performance and recommendations for this specific project. This project has quite a few more assets than my dbt Fundamentals course project. So taking a look at some of the recommendations here, I get a more robust view because we have a larger project.

So looking at this, I can filter by specific rules or categories, I can check out those different severities. So if I need to prioritize what gets fixed and what might be left for another day, this gives me a good idea of what is a high priority versus a low priority. We don't have any low priority recommendations here. But if I click into medium, a lot of these have to do with our, our DAG structure or our Documentation.

Those aren't things that are going to completely blow up my project, but they are things that we need to have to be a good, healthy project for good collaboration across my teams. My high priority things here mostly focus around testing. This is going to be a big piece to my data health overall, my project health in its entirety. So this is a high priority for my team to take a look at.

Here in the performance section we get to see an overview of our project and what has been executed here. Nothing's been executed in the last couple weeks, but if I filter for the last three months, I get to see how my models have been executed. So these specific models here all have been run once. There's a sample job that was executed here.

Again, like in the last three months. We can see the models that took the longest. I have this model that took almost two minutes, and then some other models that didn't take quite as long. So if I'm debugging my project, I might decide to look at this because maybe this model shouldn't take two minutes, maybe it should really only be a couple seconds.

So this gives me a good idea of where I might want to focus my efforts in refactoring in my projects. Down here we have most models failed, so filter again for the last three months. And this is indicating that none of my models have failed to build in this amount of time. So that's great news.

If I go into tests, I get a similar story. I don't have any tests that have failed in the last three months, which is also really great. This gives me a good picture of the health of my project. Down here.

This gives me an idea of what models are being consumed the most. So what models are being queried In my BI tool perhaps here. This is a sample project and it's not connected to a BI tool. So I don't have an image here.

But this gives me a good idea if a specific model is being used, I want to make sure that that model maybe gets built more often than some of the other models. Or if a model is never being queried, then should I be building that model at all? Is it a model that's needed? So again, this gives me a good idea of the health of my project and if I'm building it in an efficient way.

So that's a quick high level overview of dbt catalog.

#### Review

## Review

	### Development vs. Deployment

	

		- Development in dbt is the process of building, refactoring, and organizing different files in your dbt project. This is done in a development environment using a development schema (dbt_jsmith) and typically on a *non-default* branch (i.e. feature/customers-model, fix/date-spine-issue). After making the appropriate changes, the development branch is merged to main/master so that those changes can be used in deployment.

		- Deployment in dbt (or running dbt in production) is the process of running dbt on a schedule in a deployment environment. The deployment environment will typically run from the *default* branch (i.e., main, master) and use a dedicated deployment schema (e.g., dbt_prod). The models built in deployment are then used to power dashboards, reporting, and other key business decision-making processes.

		- The use of development environments and branches makes it possible to continue to build your dbt project *without* affecting the models, tests, and documentation that are running in production.

	

	### Creating your Deployment Environment

	

		- A deployment environment can be configured in dbt on the Orchestration > Environments page.

		- **General Settings: **You can configure which dbt version you want to use and you have the option to specify a branch other than the default branch.

		- **Data Warehouse Connection:** You can set data warehouse specific configurations here. For example, you may choose to use a dedicated warehouse for your production runs in Snowflake.

		- **Deployment Credentials:**Here is where you enter the credentials dbt will use to access your data warehouse:

			

				- IMPORTANT: When deploying a real dbt Project, you should set up a **separate data ****warehouse account** for this run. This should not be the same account that you personally use in development.

				- IMPORTANT: The schema used in production should be **different** from anyone's development schema.

			

		

	

	### Scheduling a job in dbt

	

		- Scheduling of future jobs can be configured in dbt on the Jobs page.

		- You can select the deployment environment that you created before or a different environment if needed.

		- **Commands:** A single job can run multiple dbt commands. For example, you can run dbt run and dbt test back to back on a schedule. You don't need to configure these as separate jobs.

		- **Triggers: **This section is where the schedule can be set for the particular job.

		- After a job has been created, you can manually start the job by selecting Run Now

	

	### Reviewing Jobs

	

		- The results of a particular job run can be reviewed as the job completes and over time.

		- The logs for each command can be reviewed.

		- If documentation was generated, this can be viewed.

		- If dbt source freshness was run, the results can also be viewed at the end of a job.

	Curious to know more about deploying with dbt? Check out our free online [Advanced Deployment course](https://courses.getdbt.com/courses/advanced-deployment), where you'll learn how to deploy your dbt project with advanced functionality including continuous integration, orchestrating conflicting jobs, and customizing behavior by environment!
		

	

	

	Want to know how to automate and accelerate your dbt workflow? Learn how with our free online course on [Webhooks](https://courses.getdbt.com/courses/webhooks)!

#### Knowledge check-Deployment

## Survey and Next Steps 5min
<a id="survey-and-next-steps-5min"></a>

### Course Feedback
<a id="survey-and-next-steps-5min-course-feedback"></a>

#### Course Closing

Extracted captions from video: Course Closing

Congratulations on making it to the end of the dbt Fundamentals course. Be sure to complete all of the pages in the course to receive the dbt Fundamentals badge. Be sure to share that badge on LinkedIn with your network so that other folks can take the Fundamentals course too and learn all that dbt has to offer. I encourage you to check out other courses that are on the dbt Learn site, such as our materialization courses, incremental models, snapshots, advanced testing, etc. These are courses that are really great for folks who've just completed dbt Fundamentals who want to continue their learning with dbt. I wish you well on your dbt journey.

#### Quick survey

## 4 Quick Questions!

Almost there! As you finish the course, we'd love to hear your feedback on the course in this quick survey here: [Open survey in new tab](https://dbtlearn.typeform.com/to/NQgMDpiw?typeform-source=courses.getdbt.com)

#### Congratulations!

## Congratulations!

	Thank you for joining all of us from the dbt Labs team! At this point, you have been empowered with the fundamentals of dbt - models, sources, tests, docs, and deployment.  

	Make sure you hit complete on each of the lessons (including this one!) and pass all of the Checks for Understanding to mark the course as complete and receive your dbt Fundamentals badge. When you mark all lessons complete, it may take a few seconds for your badge to be created.

**Once your badge is created, you’ll receive an email from training@dbtlabs.com with a link to download or share your dbt Fundamentals badge.**

	Check out the resources below to continue the journey, stay fresh on your skills, and share this with your fellow analytics engineers.

	**Resources**

	**[dbt Docs](https://docs.getdbt.com/docs/introduction): **There is no shame in referencing the docs as an analytics engineer! Use this to continue your journey, copy YML code into your project, or figure out more advanced features.

	**Short courses: **We have four courses to continue leveling up:

	

		- [**Jinja, Macros, and Packages:**](https://learn.getdbt.com/courses/jinja-macros-and-packages)Extend dbt with Jinja/Macros and import packages to speed up modeling and leverage existing macros.

		- [**Materialization Fundamentals.**](https://learn.getdbt.com/courses/materializations-fundamentals) So far you have learned about tables and views. This course will teach you about ephemeral models, incremental models, and snapshots.

		- **[Analyses and Seeds:](https://learn.getdbt.com/courses/analyses-and-seeds)** Analyses can be used for ad hoc queries in your dbt project and seeds are for importing CSVs into your warehouse with dbt.

		- **[Refactoring SQL for Modularity](https://learn.getdbt.com/courses/refactoring-sql-for-modularity):** Migrating code from a previous tool to dbt? Learn how to migrate legacy code into dbt with modularity in mind.

	

	**Contribute**

	

		- Support other beginners in **[#advice-dbt-help](https://getdbt.slack.com/archives/CBSQTAPLG)**

******Share**

	

	

		- Share the course with your team on LinkedIn!

		- Add the dbt Learn Fundamentals** **badge to your LinkedIn profile.

	

	**Feedback**

	

		- **Feedback:** Let us know what you thought about the course with positive and constructive feedback.  We are transparent about getting better, so don't hesitate to share in **[#learn-on-demand](https://getdbt.slack.com/archives/C01DU491K1A) **(request new courses too).

		- **Bugs:** Help the dbt Labs training team squash bugs in the course by sending them to **[training@dbtlabs.com](mailto:training@dbtlabs.com) **and we will triage them from there.

	

	Congratulations and thank you again! See you in dbt Slack! 

	- The dbt Labs Training Team

#### Get dbt Certified!

## Get dbt Certified

By completing this course, you are one step closer to achieving your dbt certification! 

To continue your progress, sign up for the dbt Certified Developer Path. Stay committed, keep learning, and join our community of experts to share your experiences and gain insights. 

### The dbt Certified Developer Path

The courses on the path are:

- Refactoring SQL for Modularity
- Jinja, Macros, and Packages
- Materialization Fundamentals
- Incremental Models
- Snapshots
- Analyses and Seeds
- Advanced Testing
- Advanced Deployment
- Exposures
- dbt Mesh

[**
      Explore the Path](https://learn.getdbt.com/learning-paths/dbt-certified-developer)

---

### Metadata

- Course: dbt Fundamentals (dbt Studio)
- Generated (UTC): 2026-02-27 11:39:18Z
- Source slug JSON: response\dbt Fundamentals\slug\dbt Fundamentals.json
- Source captions dir: response\dbt Fundamentals
