---
- name: create aws organization account using awscli
  shell: aws iam create-account-alias --account-alias "{{ env_name }}" --region "{{ aws_region_exec }}" --profile "{{ aws_profile }}"