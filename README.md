# Create terraform backend

I manage a number of micro services that are managed using terraform and deployed to the their own aws accounts.

I wrote this to take the pain out of creating new aws accounts, get projects up and running quickly, and add standardisation to the account/terraform.

Running the create.yml playbook will take care of everything for you. From creating the aws account, creating the terraform backend, and creating a directory to for the project. You need to [update the vars file first](#ansible-vars)


# execution

you must be in the ansible dir

```
bin/ansible
```

## apply

* copies base terraform files to project directory
* apply project terraform

```bash
ansible-playbook -e "aws_region=<aws region> env_type=<env_type> project_name=<name>" apply.yml
```
### example
```bash
ansible-playbook -e "aws_region=eu-west-1 env_type=test project_name=my-app-9" apply.yml
```

## base

* copies base terraform files to project directory

```bash
ansible-playbook -e "aws_region=<aws region> env_type=<env_type> project_name=<name>" base.yml
```
### example
```bash
ansible-playbook -e "aws_region=eu-west-1 env_type=test project_name=my-app-9" base.yml
```

## clean

* Delete base files from project directory

```bash
ansible-playbook -e "aws_region=<aws region> env_type=<env_type> project_name=<name>" clean.yml
```
### example
```bash
ansible-playbook -e "aws_region=eu-west-1 env_type=test project_name=my-app-9" clean.yml
```

## create

* Creates aws organisation account
* updates ~/.aws/config with all accounts in the organisation
* Set aws account alias
* Create terraform backend
* copies base terraform files to project directory
* apply terraform


```bash
ansible-playbook -e "aws_region=<aws region> env_type=<env_type> project_name=<name>" create.yml
```
### example
```bash
ansible-playbook -e "aws_region=eu-west-1 env_type=test project_name=my-app-9" create.yml
```
## update config

* updates ~/.aws/config with all accounts in the organisation

```bash
ansible-playbook update_config.yml
```

# make

After running the create.yml playbook you can run make plan and make apply from the project directory. 

## make plan

* copies base terraform files to project directory
* runs terraform plan

```
make plan
```

## make apply

* copies base terraform files to project directory
* runs terraform apply

```
make apply
```

## make update

* updates ~/.aws/config with all accounts in the organisation

```
make update
```


# Ansible vars

## vars file

You will need to update bin/ansible/vars/vars.yml with your organization's details

```
email_domain: "example.com"
email_alias: "aws"
iam_role: "OrganizationAccountAccessRole"
aws_region_exec: "eu-west-1"
name_prefix: "company-a"
```

The most important vars are email_domain and email_alias. You will not be able to sign into the account if these are incorrect. see [new account email address](#account-email-address)

# account name

The name of the new account is created using the extra vars and imported vars from /bin/ansible/vars/vars.yml

```
<name_prefix>-<project_name>-<env_type>-<aws_region>
```
### example
```
company-a-my-app-9-prod-eu-west-2
```

# account email address

This is very important! You must have access to the address <email_alias>@<email_domain>. You will not be able to signin as the root user if you do not. This will prevent your from securing the root login and closing the account.

The account_name is added to the email alias using a plus. See this gizmodo article for how it works -> https://gizmodo.com/how-to-use-the-infinite-number-of-email-addresses-gmail-1609458192

```
<email_alias>+<name_prefix>-<project_name>-<env_type>-<aws_region>@<email_domain>
```

### example

```
aws+company-a-my-app-9-prod-eu-west-2@exmaple.com
```