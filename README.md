# sharkupdateo

## Overview

The goal of this project is to find all of the sources within the repos you tell it to that may be out of dat from the most up to date and let you know


It will look in each repo, clone them down
It will go through the files and find sources declariation for the modules and go check on that repo finding if the version you are using is the most up to date

## Usage :

* `git clone git@github.com:caseybecking/sharkupdateo.git`
* `cd ./sharkupdateo`
* `docker build -t sharkupdateo:latest .`
* Modify `repos.json` to include the repos you'd like to crawl
* `docker run --env GITHUB_PUBLIC_ACCESS_TOKEN=<...> -it sharkupdateo:latest`
  * Alternatively, you can `cp config.json.sample config.json` and fill out the `GITHUB_` values there.
* `python main.py`

## Sample Output:

```
root@80f8d38ba3b0:/usr/local/src/sharkupdateo# python main.py
This will take some time!!
+--------------------------------------------------------------------------------------------------------------------------------------------+
|                                 https://github.com/rackspace-infrastructure-automation/aws-terraform-rds/                                  |
+-------------------------------------+--------------------------------+-------------+------+-----------------+----------------+-------------+
|                 Org                 |              Repo              |     File    | Line | Current Version | Latest Version | Up to Date? |
+-------------------------------------+--------------------------------+-------------+------+-----------------+----------------+-------------+
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 266  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 288  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 311  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 332  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 353  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 374  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation | aws-terraform-cloudwatch_alarm |   main.tf   | 395  |      v0.0.1     |     v0.0.1     |      ✅      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |   main.tf   |  10  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |  mariadb.tf |  39  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |  mariadb.tf | 128  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |  mariadb.tf | 219  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |   mssql.tf  |  20  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |   mysql.tf  |  39  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |   mysql.tf  | 128  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |   mysql.tf  | 219  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        |  oracle.tf  |  20  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        | postgres.tf |  39  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        | postgres.tf | 128  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation |       aws-terraform-rds        | postgres.tf | 219  |      v0.0.6     |     v0.0.9     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |  mariadb.tf |  19  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |  mariadb.tf |  25  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |   mssql.tf  |  14  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |   mysql.tf  |  19  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |   mysql.tf  |  25  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  |  oracle.tf  |  14  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  | postgres.tf |  19  |      v0.0.6     |     v0.0.7     |      ❌      |
| rackspace-infrastructure-automation | aws-terraform-vpc_basenetwork  | postgres.tf |  25  |      v0.0.6     |     v0.0.7     |      ❌      |
+-------------------------------------+--------------------------------+-------------+------+-----------------+----------------+-------------+
```
