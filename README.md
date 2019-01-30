The goal of this project is to find all of the sources within the repos you tell it to that may be out of dat from the most up to date and let you know


It will look in each repo, clone them down
It will go through the files and find sources declariation for the modules and go check on that repo finding if the version you are using is the most up to date

#Useage :
git clone repo
cd to repo
mv config.json.sample config.json
modify and add your access key to the config.json
vi sites.json
add sites you would like to clone down for crawling through
pip install -r REQUIREMENTS.txt


```
Output:
+-------------------------------------+-------------------------------+------------------------------------------------------------+------+-----------------+----------------+
|                 Org                 |              Repo             |                            File                            | Line | Current Version | Latest Version |
+-------------------------------------+-------------------------------+------------------------------------------------------------+------+-----------------+----------------+
| rackspace-infrastructure-automation |       aws-terraform-alb       |       cap-aws-lamp/alb.tf       |  2   |      0.0.3      |     v0.0.8     |
| rackspace-infrastructure-automation |     aws-terraform-ec2_asg     |       cap-aws-lamp/asg.tf       |  2   |      0.0.6      |    v0.0.11     |
| rackspace-infrastructure-automation |       aws-terraform-rds       |       cap-aws-lamp/rds.tf       |  33  |      0.0.5      |     v0.0.7     |
| rackspace-infrastructure-automation |  aws-terraform-security_group | cap-aws-lamp/security_groups.tf |  2   |      0.0.4      |     v0.0.5     |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork |       cap-aws-lamp/vpc.tf       |  2   |      0.0.2      |     v0.0.6     |
+-------------------------------------+-------------------------------+------------------------------------------------------------+------+-----------------+----------------+
```