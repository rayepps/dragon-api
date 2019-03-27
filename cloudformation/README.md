# Dragon Infrastructure

## Steps to deploy
Create the stack in the following order

1. Create the `vpc.yml` stack
2. Create the `groups.yml` stack
3. Create the ECS Cluster stack (use the console - or feel free to add the yml someday) - this will require that you create an ssh key in ec2 and some other dependencies
4. Create a hosted zone and create a certificate for it
5. Create the `service.yml` stack
6. Create the `cicd.yml` stack
