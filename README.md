# Data Pipeline Example
This is a repository that serves as an example for a simple job you might have to run on a daily/hourly/weekly basis. It generates a mock data set, supposed to be representing some email events that are coming in and some user types associated with each of those emails.

We run a simple job to aggregate this data and from there it can either be written to file, stored in a database, send a message to a Slack channel, etc.

### Pre-requisites
- [**Sign Up**](https://dashboard.metismachine.io/sign-up) for a Skafos Account
- [**Install Skafos**](https://docs.metismachine.io/docs/installation)
- Authenticate using `skafos auth`
- A repository on Github with code that you'd like to run on Skafos. If you don't have a repository and want to use a pre-baked example, fork [**this repository**](https://github.com/griffinwalkerMM/data_pipeline).

The remaining steps in this tutorial use the example repository. 

## Step 1 - Clone and Initialize your Repository
```
git clone https://github.com/username/data_pipeline.git # clone your repo
cd data_pipeline # go into your project directory
skafos init # initialize your new skafos project
```

After you have run the `skafos init` command, your directory will contain a `metis.config.yml` file. You will need to modify this file, as described below, for Skafos to run your code. 

## Step 2- Set Up Jobs
In order for Skafos to understand your pipeline, you must tell it in what order you would like it run. 
This can be done by: 
- Creating job ids using `skafos create job` (see below).
- Adding the jobs to your **metis.config.yml** file.

```
# Get your project-token
cat metis.config.yml # take a look at your current config file

# Create a job for each of your scripts
skafos create job data_ingest.py --project <insert-your-project-token-here>
skafos create job generate_report.py --project <insert-your-project-token-here>

# Add these jobs to your config file by editing metis.config.yml
# vi metis.config.yml or use whatever your favorite text editor is 

```
## Step 3 - Add your modules
In order for Skafos to run properly, you must tell it what modules your jobs require. This can be specified in the requirements.txt file. 

For example, our workflow requires pandas, numpy, etc. so we must add those to our **requirements.txt**.

```
# either use your favorite text editor or
# use the below commands
touch requirements.txt;
echo "pandas==0.23.4" >> requirements.txt;
echo "numpy==1.15.1" >> requirements.txt;
echo "tabulate==0.8.2" >> requirements.txt;
echo "datetime==4.3" >> requirements.txt;

# commit our changes to our repo
git add .
git commit -m "Create jobs in config and Add modules to requirements file"
```

## Step 4 - Add Skafos to your GitHub repo
Skafos can follow updates you make to your application and deploy whenever you've made updates to your application. To do this, you must [**add the Skafos app to your repo**](https://github.com/apps/skafos).

![Adding Skafos to your GitHub repo](https://files.readme.io/86869d1-Screenshot_from_2018-11-07_16-29-58.png)

## Step 5 - Push to Skafos
Simply git push! To see your project running on Skafos, check out your dashboard
```
git push skafos
```
