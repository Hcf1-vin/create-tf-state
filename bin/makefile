PROJECT := $(shell python ../../../../bin/get_attribute/main.py --type=project)
ENV_TYPE := $(shell python ../../../../bin/get_attribute/main.py --type=env)
REGION := $(shell python ../../../../bin/get_attribute/main.py --type=region)

base:
	@echo "-----------------------"
	@echo "PROJECT: $(PROJECT)"
	@echo "ENV_TYPE: $(ENV_TYPE)"
	@echo "REGION: $(REGION)"
	@echo "-----------------------"
	@-$(shell ansible-playbook -e "aws_region=$(REGION) env_type=${ENV_TYPE} project_name=${PROJECT}" ../../../../bin/ansible/base.yml > /tmp/play.log)

init: base
	terraform init

plan: base
	terraform plan -var-file="_base_vars.tfvars"

apply: base
	terraform apply -var-file="_base_vars.tfvars"

update: 
	@-$(shell ansible-playbook ../../../../bin/ansible/update_config.yml > /tmp/play.log)