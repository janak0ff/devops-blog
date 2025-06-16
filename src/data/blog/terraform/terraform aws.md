---
title: Terraform - Create and SSH into an AWS EC2 Instance Using Terraform (Free Tier Guide for Beginners)
pubDatetime: 2025-06-05
featured: true
tags:
  - terraform
  - aws
  - Hands On Lab
description: How to create and SSH into an Amazon EC2 instance using Terraform — completely within AWS Free Tier limits. We’ll cover essential Terraform setup, defining AWS resources, adding a security group for SSH access, and outputting the public IP for easy login. Perfect for beginners looking to get hands-on with Infrastructure as Code (IaC)!
---

step-by-step to create a **Virtual Machine (EC2 instance)** on **AWS Free Tier** using **Terraform** and SSH to it.

---
####  Create a key pair in AWS Console (if you don’t have one)

* Go to: **AWS Console → EC2 → Key Pairs**
* Click **Create key pair**
* Name: `my-key`
* Type: RSA
* Save the `.pem` file (e.g., `my-key.pem`) securely

![aws key pair create](@/assets/images/aws-key-pair-pem.png)

#### Download and move it to your project Directory and Check Permissions of the `.pem` File
```bash
chmod 400 my-key.pem
```
---


### ✅ Install Required Packages

#### 1. Install AWS CLI

```bash
sudo apt update
sudo apt install awscli -y
```

Verify:

```bash
aws --version
```

#### 2. Install Terraform

```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt install terraform -y
```

Verify:

```bash
terraform -version
```

---

### ✅ Configure AWS CLI

💡 Get access keys from:
**AWS Console > IAM > Users > Your Username > Security Credentials > Access Keys**

![terraform aws key](@/assets/images/terraform-aws-acess-key.png)

```bash
aws configure
```

Enter the following:

* AWS Access Key ID
* AWS Secret Access Key
* Region (e.g., `us-east-1`)
* Output format: Just press Enter

After this steps, two files are auto created inside **/home/username/.aws**

![aws config](@/assets/images/aws-terraform-cred-home.png)

---

### ✅  Create Terraform Configuration

#### 1. Create a folder

```bash
mkdir terraform-aws
cd terraform-aws
```

#### 2. Create `main.tf`

```bash
nano main.tf
```

Paste the following:

```hcl
# --------------------------------------------------
# Terraform block to specify required providers
# --------------------------------------------------
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"  # Using a stable version of AWS provider
    }
  }
}

# --------------------------------------------------
# AWS provider configuration
# --------------------------------------------------
provider "aws" {
  region = "us-east-1"  # AWS region to deploy resources
}

# --------------------------------------------------
# Data block to fetch default VPC (used by security group)
# --------------------------------------------------
data "aws_vpc" "default" {
  default = true
}

# --------------------------------------------------
# Security group resource to allow SSH access
# --------------------------------------------------
resource "aws_security_group" "ssh_access" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"
  vpc_id      = data.aws_vpc.default.id  # Attach to the default VPC

  # Inbound rule to allow SSH from any IP
  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # ⚠️ For production, replace with your IP (e.g. ["203.0.113.0/32"])
  }

  # Outbound rule to allow all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# --------------------------------------------------
# EC2 instance resource
# --------------------------------------------------
resource "aws_instance" "my_ec2" {
  ami           = "ami-0c2b8ca1dad447f8a"  # Amazon Linux 2 AMI (Free tier eligible)
  instance_type = "t2.micro"              # Free tier eligible instance type
  key_name      = "terraform-janak"       # Replace with the name of your existing AWS EC2 key pair
  security_groups = [aws_security_group.ssh_access.name]  # Attach the SSH security group

  tags = {
    Name = "MyTerraformVM"  # Tag to identify your instance
  }
}

# --------------------------------------------------
# Output block to show the public IP of the EC2 instance
# --------------------------------------------------
output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.my_ec2.public_ip
}

```

✅ Save & close (`Ctrl + O`, `Enter`, `Ctrl + X`)

---

### ✅  Initialize Terraform

```bash
terraform init
```

---

### ✅ Code Formatting Terraform (optional)

```bash
terraform fmt
```

---

### ✅ Validate Configuration

```bash
terraform validate
```

---

### ✅  Apply the Configuration

```bash
terraform apply
```

It will show you a plan. Type `yes` to proceed.


![terraform-apply](@/assets/images/terraform-apply-to-aws.png)

---

### ✅  Access Your EC2 Instance via SSH from your linxu machine.


   ```bash
    ssh -i my-key.pem ec2-user@<public_ip>
   ```

📝 Use `ec2-user` for Amazon Linux AMI (or `ubuntu` if you switch to Ubuntu AMI).

![ssh to aws](@/assets/images/terraform-aws-ssh.png)
![aws](@/assets/images/aws-instance-terra.png)


### ✅ Destroy the Instance 

```bash
terraform destroy
```


---


### ✅ `terraform refresh` — What It Does

```bash
terraform refresh
```

The `terraform refresh` command is used to:

> **Sync the Terraform state file with the actual current state of resources in your AWS (or other) infrastructure.**

In other words:
It checks what **exists in real AWS** and updates Terraform’s `.tfstate` file to reflect any changes that happened **outside of Terraform**.

---

### 📖 **References & Further Reading**

1. **Terraform Plans, Modules, and Remote State – by Wahl Network**
   A great explanation of how Terraform handles infrastructure planning, modularization, and remote state management.
   🔗 [https://wahlnetwork.com/2020/04/29/terraform-plans-modules-and-remote-state/](https://wahlnetwork.com/2020/04/29/terraform-plans-modules-and-remote-state/)

2. **Terraform AWS Provider Documentation – Official Registry**
   The complete reference for all AWS resources supported in Terraform, including syntax, arguments, and examples.
   🔗 [https://registry.terraform.io/providers/hashicorp/aws/latest](https://registry.terraform.io/providers/hashicorp/aws/latest)

---


### Output of my terminal:
```output
  janak@king  ~/terraform/aws  terraform validate

Success! The configuration is valid.

 janak@king  ~/terraform/aws  terraform fmt     
main.tf
 janak@king  ~/terraform/aws  terraform apply

data.aws_vpc.default: Reading...
data.aws_vpc.default: Read complete after 3s [id=vpc-0bdb14565e290df3b]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.my_ec2 will be created
  + resource "aws_instance" "my_ec2" {
      + ami                                  = "ami-0c2b8ca1dad447f8a"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + enable_primary_ipv6                  = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_lifecycle                   = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = "terraform-janak"
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = [
          + "allow_ssh",
        ]
      + source_dest_check                    = true
      + spot_instance_request_id             = (known after apply)
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "MyTerraformVM"
        }
      + tags_all                             = {
          + "Name" = "MyTerraformVM"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)

      + cpu_options (known after apply)

      + ebs_block_device (known after apply)

      + enclave_options (known after apply)

      + ephemeral_block_device (known after apply)

      + instance_market_options (known after apply)

      + maintenance_options (known after apply)

      + metadata_options (known after apply)

      + network_interface (known after apply)

      + private_dns_name_options (known after apply)

      + root_block_device (known after apply)
    }

  # aws_security_group.ssh_access will be created
  + resource "aws_security_group" "ssh_access" {
      + arn                    = (known after apply)
      + description            = "Allow SSH inbound traffic"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
                # (1 unchanged attribute hidden)
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = "SSH from anywhere"
              + from_port        = 22
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 22
            },
        ]
      + name                   = "allow_ssh"
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags_all               = (known after apply)
      + vpc_id                 = "vpc-0bdb14565e290df3b"
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_public_ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_security_group.ssh_access: Creating...
aws_security_group.ssh_access: Creation complete after 7s [id=sg-0abf04ec2463db933]
aws_instance.my_ec2: Creating...
aws_instance.my_ec2: Still creating... [00m10s elapsed]
aws_instance.my_ec2: Still creating... [00m20s elapsed]
aws_instance.my_ec2: Still creating... [00m30s elapsed]
aws_instance.my_ec2: Creation complete after 37s [id=i-0cb46a9f04064c1b4]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

instance_public_ip = "3.85.61.224"
 janak@king  ~/terraform/aws  ssh -i terraform-janak.pem ec2-user@3.85.61.224   
The authenticity of host '3.85.61.224 (3.85.61.224)' can't be established.
ED25519 key fingerprint is SHA256:BH/7hLSYw/wtVACyiDcZA1V1nWy5EZGxG+EWvIw7qaY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '3.85.61.224' (ED25519) to the list of known hosts.

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
55 package(s) needed for security, out of 106 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-18-218 ~]$ w
 07:02:35 up 44 min,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
ec2-user pts/0    27.34.65.181     07:02    2.00s  0.01s  0.00s w
[ec2-user@ip-172-31-18-218 ~]$ exit
logout
Connection to 3.85.61.224 closed.
 janak@king  ~/terraform/aws  terraform destroy

data.aws_vpc.default: Reading...
data.aws_vpc.default: Read complete after 3s [id=vpc-0bdb14565e290df3b]
aws_security_group.ssh_access: Refreshing state... [id=sg-0abf04ec2463db933]
aws_instance.my_ec2: Refreshing state... [id=i-0cb46a9f04064c1b4]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_instance.my_ec2 will be destroyed
  - resource "aws_instance" "my_ec2" {
      - ami                                  = "ami-0c2b8ca1dad447f8a" -> null
      - arn                                  = "arn:aws:ec2:us-east-1:442042544656:instance/i-0cb46a9f04064c1b4" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "us-east-1d" -> null
      - cpu_core_count                       = 1 -> null
      - cpu_threads_per_core                 = 1 -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-0cb46a9f04064c1b4" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t2.micro" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - key_name                             = "terraform-janak" -> null
      - monitoring                           = false -> null
      - placement_partition_number           = 0 -> null
      - primary_network_interface_id         = "eni-09c381fcd7f2a599f" -> null
      - private_dns                          = "ip-172-31-18-218.ec2.internal" -> null
      - private_ip                           = "172.31.18.218" -> null
      - public_dns                           = "ec2-3-85-61-224.compute-1.amazonaws.com" -> null
      - public_ip                            = "3.85.61.224" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [
          - "allow_ssh",
        ] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-0eb9138e4799cbcd9" -> null
      - tags                                 = {
          - "Name" = "MyTerraformVM"
        } -> null
      - tags_all                             = {
          - "Name" = "MyTerraformVM"
        } -> null
      - tenancy                              = "default" -> null
      - user_data_replace_on_change          = false -> null
      - vpc_security_group_ids               = [
          - "sg-0abf04ec2463db933",
        ] -> null
        # (7 unchanged attributes hidden)

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - cpu_options {
          - core_count       = 1 -> null
          - threads_per_core = 1 -> null
            # (1 unchanged attribute hidden)
        }

      - credit_specification {
          - cpu_credits = "standard" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - maintenance_options {
          - auto_recovery = "default" -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_protocol_ipv6          = "disabled" -> null
          - http_put_response_hop_limit = 1 -> null
          - http_tokens                 = "optional" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - private_dns_name_options {
          - enable_resource_name_dns_a_record    = false -> null
          - enable_resource_name_dns_aaaa_record = false -> null
          - hostname_type                        = "ip-name" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/xvda" -> null
          - encrypted             = false -> null
          - iops                  = 100 -> null
          - tags                  = {} -> null
          - tags_all              = {} -> null
          - throughput            = 0 -> null
          - volume_id             = "vol-00b407383785fadd0" -> null
          - volume_size           = 8 -> null
          - volume_type           = "gp2" -> null
            # (1 unchanged attribute hidden)
        }
    }

  # aws_security_group.ssh_access will be destroyed
  - resource "aws_security_group" "ssh_access" {
      - arn                    = "arn:aws:ec2:us-east-1:442042544656:security-group/sg-0abf04ec2463db933" -> null
      - description            = "Allow SSH inbound traffic" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
                # (1 unchanged attribute hidden)
            },
        ] -> null
      - id                     = "sg-0abf04ec2463db933" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = "SSH from anywhere"
              - from_port        = 22
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
        ] -> null
      - name                   = "allow_ssh" -> null
      - owner_id               = "442042544656" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {} -> null
      - tags_all               = {} -> null
      - vpc_id                 = "vpc-0bdb14565e290df3b" -> null
        # (1 unchanged attribute hidden)
    }

Plan: 0 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  - instance_public_ip = "3.85.61.224" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_instance.my_ec2: Destroying... [id=i-0cb46a9f04064c1b4]
aws_instance.my_ec2: Still destroying... [id=i-0cb46a9f04064c1b4, 00m10s elapsed]
aws_instance.my_ec2: Still destroying... [id=i-0cb46a9f04064c1b4, 00m20s elapsed]
aws_instance.my_ec2: Still destroying... [id=i-0cb46a9f04064c1b4, 00m30s elapsed]
aws_instance.my_ec2: Still destroying... [id=i-0cb46a9f04064c1b4, 00m40s elapsed]
aws_instance.my_ec2: Destruction complete after 44s
aws_security_group.ssh_access: Destroying... [id=sg-0abf04ec2463db933]
aws_security_group.ssh_access: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.
 janak@king  ~/terraform/aws  
```