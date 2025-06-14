---
title: Terraform - Complete step-by-step process to create a (VM) on Azure and SSH under student pack subscription.
pubDatetime: 2025-06-07
featured: true
tags:
  - terraform
  - azure
  - Hands On Lab
description: Making a Linux virtual machine on Microsoft Azure using Terraform. From setting up providers and creating a resource group to configuring networking components and managing SSH authentication using azure CLI & GUI
---


**step-by-step guide** to generate the required values for using Terraform with Microsoft Azure:

---

## ✅ Install Required Tools

You’ll need to install the following tools on your local machine:

### 1. **Terraform**

* Go to: [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)
* Download and install Terraform for your operating system.
* After installation, verify with:

  ```bash
  terraform -v
  ```

### 2. **Azure CLI**

* Go to: [https://learn.microsoft.com/en-us/cli/azure/install-azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* Install the Azure CLI for your OS.
* After installation, check it:

  ```bash
  az version
  ```

---

## ✅  Log in to Azure

Login to your Azure account using Azure CLI:

```bash
az login
```

A browser window will open asking you to log in with your student pack credentials.

You can list your subscription:

```bash
az account show
```

---


## ⚙️ Get the `azure_subscription_id` and `azure_tenant_id`

Run this command:

```bash
az account show --query "{subscriptionId:id, tenantId:tenantId}"
```

**Output:**

```json
{
  "subscriptionId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "tenantId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
}
```

✅ Copy the values for:

* `azure_subscription_id`
* `azure_tenant_id`

### Get Azure Subscription ID via GUI
![output](@/assets/images/azure-subscription-id.png)

1. **Go to Azure Portal**
   👉 Visit: [https://portal.azure.com](https://portal.azure.com)
   Log in with your Azure account.

2. **Open 'Subscriptions' Panel**

   * Click on the **search bar** at the top.
   * Type **"Subscriptions"** and click on the result.

3. **View Subscription Details**

   * You’ll see a list of your subscriptions.
   * Each subscription will show the **Subscription name** and the **Subscription ID**.

4. **Copy the Subscription ID**

   * Click on the subscription name to open its details.
   * The **Subscription ID** will be visible in the overview pane.
   * Click the **copy icon** 📋 next to it to copy.

---


## 🛠️  Create a Service Principal (SP) / App registrations

This SP will be used by Terraform to authenticate.

```bash
az ad sp create-for-rbac --name terraform-janak --role="Contributor" --scopes="/subscriptions/<subscription-id>"
```

Replace `<subscription-id>` with the actual value

**Output:**

```json
{
  "appId": "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz",
  "displayName": "terraform-sp",
  "password": "********-****-****-****-************",
  "tenant": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"
}
```

✅ Save:

* `azure_client_id = appId`
* `azure_client_secret = password`
* `azure_tenant_id = tenant` (same as before)

---
### GUI Methods: **Step-by-step guide** to get your **Azure Client ID**, **Client Secret**, and **Tenant ID** from the **Azure Portal (GUI)** using **App Registrations**:

---

#### **Step 1: Go to App Registrations**

1. Click on the **Search bar** at the top.
2. Type **“App registrations”** and select it.
3. Click **“+ New registration”**.

![output](@/assets/images/terra-azure-app-reg.png)

#### **Step 2: Register the Application**

1. **Name** your app (e.g., `terraform-janak`).
2. Leave the default **Supported account types** as **Single tenant** (or your choice).
3. Redirect URI: leave empty
4. Click **“Register”**.

---

### 🔹 Step 3: Get the IDs

![output](@/assets/images/terraform-janak-idss.png-)

#### ✅ **Client ID** (`azure_client_id`)

* Go to the **Overview** tab.
* Copy the value labeled **“Application (client) ID”**.

#### ✅ **Tenant ID** (`azure_tenant_id`)

* In the same **Overview** tab.
* Copy the value labeled **“Directory (tenant) ID”**.

---

### 🔹 Step 4: Create a Client Secret

![output](@/assets/images/Certificates-secrets-terra-azure.png)

1. In the left menu, click **“Certificates & secrets”**.
2. Under **Client secrets**, click **“+ New client secret”**.
3. Add a **description** (e.g., `anything`), choose an expiration (e.g., 6 or 12 months).
4. Click **“Add”**.
5. **Copy the value immediately** shown under "Value" – this is your **`azure_client_secret`**.
   ⚠️ You won’t be able to view it again once you leave the page.

---


## 👮  Confirm Role Assignment 

You can check if the role was properly assigned:

```bash
az role assignment list --assignee <appId>
```

Assign Contributor role:

```bash
az role assignment create \
  --assignee <app-id> \
  --role "Contributor" \
  --scope /subscriptions/<subscription-id>

```

---
### GUI Methods: Assign Permissions to the App

To give your app permissions to deploy resources:

1. Go to **Subscriptions** → Select your subscription.
2. Click **“Access control (IAM)”**.
3. Click **“+ Add” > “Add role assignment”**.
4. Under the **Privileged administrator roles** choose: **Contributor**
5. Assign access to: **User, group, or service principal**
6. Select Members: search for your app name (`Terraform-janak`) and select it.
![output](@/assets/images/Screenshot_20250614_191748.png)
7. Click **Save**.
![output](@/assets/images/Screenshot_20250614_191950.png)

---

## 📌 Summary of Values

You now have:

| Variable                | Description                |
| ----------------------- | -------------------------- |
| `azure_subscription_id` | Your Azure subscription ID |
| `azure_client_id`       | appId                      |
| `azure_client_secret`   | password                   |
| `azure_tenant_id`       | Azure tenant ID            |

---


### ✅ Generate SSH Key (If not)


```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```



## ✅ Configure Terraform Directory

1. Create a new project folder:

   ```bash
   mkdir terraform-azure
   cd terraform-azure
   ```

2. Create a file named `main.tf`:

   ```bash
   nano main.tf
   ```

Paste the following into `main.tf` (you can edit names later):

```hcl
# ------------------------------
# Specify the required provider
# ------------------------------
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0" # Ensures you're using version 4.x of the Azure provider
    }
  }
}

# -----------------------------------------
# Configure the Azure provider credentials
# -----------------------------------------
provider "azurerm" {
  features {}

  # These variables will be passed via CLI, environment, or tfvars
  subscription_id = var.azure_subscription_id
  client_id       = var.azure_client_id
  client_secret   = var.azure_client_secret
  tenant_id       = var.azure_tenant_id
}

# -------------------------------
# Create a new Azure Resource Group
# -------------------------------
resource "azurerm_resource_group" "janak-azure" {
  name     = "Janak-res"  # Resource group name
  location = "westeurope"             # Azure region
}

# ---------------------------
# Create a Virtual Network
# ---------------------------
resource "azurerm_virtual_network" "janak-azure" {
  name                = "janak-azure-network"            # Name of the VNet
  address_space       = ["10.0.0.0/16"]              # CIDR block
  location            = azurerm_resource_group.janak-azure.location
  resource_group_name = azurerm_resource_group.janak-azure.name
}

# ----------------------
# Create a Subnet inside the VNet
# ----------------------
resource "azurerm_subnet" "janak-azure" {
  name                 = "internal"                                # Subnet name
  resource_group_name  = azurerm_resource_group.janak-azure.name
  virtual_network_name = azurerm_virtual_network.janak-azure.name
  address_prefixes     = ["10.0.2.0/24"]                          # Subnet IP range
}

# ----------------------------
# Create a Static Public IP Address
# ----------------------------
resource "azurerm_public_ip" "janak-azure" {
  name                = "janak-azure-public-ip"
  location            = azurerm_resource_group.janak-azure.location
  resource_group_name = azurerm_resource_group.janak-azure.name
  allocation_method   = "Static"       # IP will not change
  sku                 = "Standard"     # Standard SKU supports NSG and zones
  sku_tier            = "Regional"     # Tier of the SKU
}

# -------------------------------
# Create a Network Security Group (NSG)
# -------------------------------
resource "azurerm_network_security_group" "janak-azure" {
  name                = "janak-azure-nsg"
  location            = azurerm_resource_group.janak-azure.location
  resource_group_name = azurerm_resource_group.janak-azure.name

  # Allow inbound SSH (port 22) from anywhere
  security_rule {
    name                       = "Allow-SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

# -----------------------------------------------------
# Associate NSG with the network interface of the VM
# -----------------------------------------------------
resource "azurerm_network_interface_security_group_association" "janak-azure" {
  network_interface_id      = azurerm_network_interface.janak-azure.id
  network_security_group_id = azurerm_network_security_group.janak-azure.id
}

# ----------------------------
# Create a Network Interface
# ----------------------------
resource "azurerm_network_interface" "janak-azure" {
  name                = "janak-azure-nic"
  location            = azurerm_resource_group.janak-azure.location
  resource_group_name = azurerm_resource_group.janak-azure.name

  # IP configuration for the NIC
  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.janak-azure.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.janak-azure.id
  }
}

# ----------------------------
# Create a Linux Virtual Machine
# ----------------------------
resource "azurerm_linux_virtual_machine" "janak-azure" {
  name                  = "Janak-azure-terraform"                        # Name of the VM
  resource_group_name   = azurerm_resource_group.janak-azure.name
  location              = azurerm_resource_group.janak-azure.location
  size                  = "Standard_B1s"                        # Free-tier eligible size
  admin_username        = "janak_azure"                          # SSH login username
  network_interface_ids = [azurerm_network_interface.janak-azure.id]

  # SSH Key-based authentication
  admin_ssh_key {
    username   = "janak_azure"
    public_key = file("~/.ssh/id_rsa.pub")                    # Path to public SSH key
  }

  disable_password_authentication = true                      # Force key-only login

  # OS Disk configuration
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  # Use latest Ubuntu 22.04 LTS image
  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
}
```

2. Create a file named `output.tf`:

  ```hcl
  output "public_ip" {
  description = "The public IP address of the virtual machine"
  value       = azurerm_public_ip.janak-azure.ip_address
  }
  ```
3. Create a file named `variables.tf`:

    ```hcl
    variable "azure_subscription_id" {
      type = string
    }
    variable "azure_client_id" {
      type = string
    }
    variable "azure_client_secret" {
      type = string
    }
    variable "azure_tenant_id" {
      type = string
    }
    ```
4. Create a file named `terraform.tfvars` and  replace your own keys:
    ```hcl
    azure_subscription_id = "bf97eca7-bcbd-41ce-bc31-9c5d6fds84f2073" #subscription id
    azure_client_id        = "2c6e5db5-620e-4b07-8b9a-904sfs45f297d41"  #app registration
    azure_tenant_id       = "69c13822-3598-4d4d-aae2-f142dsfs0ad786ab" #tenant id
    azure_client_secret   = "UbB8Q~3GxAWrF67k1LdsdfvUzk72b2DBV~rgTkAkOaad" #secret value
    ```
---

## ✅ Initialize and Apply Terraform

### 1. **Initialize Terraform** in your project directory:

```bash
terraform init
```

### 2. **Preview the actions** Terraform will take:

```bash
terraform plan
```

### 3. **Apply the configuration**:

```bash
terraform apply
```

Confirm when prompted by typing `yes`.

![output](@/assets/images/using-terraform-to-create-azurevm.png)
---

## ✅ SSH to newly created azure VM

```bash
ssh -i ~/.ssh/id_rsa janak_azure@51.136.100.152
```

Use your own your USERNAME & IP

![output](@/assets/images/ssh-to-azure-vm-terra.png)

---
![output](@/assets/images/Screenshot_20250614_192245.png)

---

## ✅ Clean Up (To Save Free Credits)

When you're done, destroy the resources:

```bash
terraform destroy
```
![output](@/assets/images/terra-az-destroy.png)


---
## 📚 **References:**

* 🎥 [Deploy Azure VM using Terraform | YouTube Tutorial](https://www.youtube.com/watch?v=ZoB5cG_zakM)
* 📘 [Terraform Azurerm Provider Documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest)

---

## ✅ My Terminal final looks:
```zsh
 janak@king  ~/terraform/azure  terraform -v
Terraform v1.12.2
on linux_amd64
+ provider registry.terraform.io/hashicorp/azurerm v4.33.0
 janak@king  ~/terraform/azure  az version
{
  "azure-cli": "2.74.0",
  "azure-cli-core": "2.74.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
 janak@king  ~/terraform/azure  az login
A web browser has been opened at https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize. Please continue the login in the web browser. If no web browser is available or if the web browser fails to open, use device code flow with `az login --use-device-code`.

Retrieving tenants and subscriptions for the selection...

[Tenant and subscription selection]

No     Subscription name    Subscription ID                       Tenant
-----  -------------------  ------------------------------------  --------------------------
[1] *  Azure for Students   bf97eca7-bcbd-41ce-bc31-9c5d684f2073  Janamaitri Multiple Campus

The default is marked with an *; the default tenant is 'Janamaitri Multiple Campus' and subscription is 'Azure for Students' (bf97eca7-bcbd-41ce-bc31-9c5d684f2073).

Select a subscription and tenant (Type a number or Enter for no changes): 1

Tenant: Janamaitri Multiple Campus
Subscription: Azure for Students (bf97eca7-bcbd-41ce-bc31-9c5d684f2073)

[Announcements]
With the new Azure CLI login experience, you can select the subscription you want to use more easily. Learn more about it and its configuration at https://go.microsoft.com/fwlink/?linkid=2271236

If you encounter any problem, please open an issue at https://aka.ms/azclibug

[Warning] The login output has been updated. Please be aware that it no longer displays the full list of available subscriptions by default.

 janak@king  ~/terraform/azure  az account show
{
  "environmentName": "AzureCloud",
  "homeTenantId": "69c13822-3598-4d4d-aae2-f1420ad786ab",
  "id": "bf97eca7-bcbd-41ce-bc31-9c5d684f2073",
  "isDefault": true,
  "managedByTenants": [],
  "name": "Azure for Students",
  "state": "Enabled",
  "tenantDefaultDomain": "janamaitri.edu.np",
  "tenantDisplayName": "Janamaitri Multiple Campus",
  "tenantId": "69c13822-3598-4d4d-aae2-f1420ad786ab",
  "user": {
    "name": "6-2-27-003-2077@janamaitri.edu.np",
    "type": "user"
  }
}
 janak@king  ~/terraform/azure  az account show --query "{subscriptionId:id, tenantId:tenantId}"
{
  "subscriptionId": "bf97eca7-bcbd-41ce-bc31-9c5d684f2073",
  "tenantId": "69c13822-3598-4d4d-aae2-f1420ad786ab"
}
 janak@king  ~/terraform/azure  az ad sp create-for-rbac --name terraform-janak --role="Contributor" --scopes="/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073"
Creating 'Contributor' role assignment under scope '/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073'
The output includes credentials that you must protect. Be sure that you do not include these credentials in your code or check the credentials into your source control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "66ab3502-4703-4fca-9491-09986d5203ea",
  "displayName": "terraform-janak",
  "password": "<enter yours>",
  "tenant": "69c13822-3598-4d4d-aae2-f1420ad786ab"
}
 janak@king  ~/terraform/azure  az role assignment create \
  --assignee 66ab3502-4703-4fca-9491-09986d5203ea \
  --role "Contributor" \
  --scope /subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073
{
  "condition": null,
  "conditionVersion": null,
  "createdBy": "3f3d364b-bfad-45e3-95be-242b6e5f8051",
  "createdOn": "2025-06-14T12:30:39.521540+00:00",
  "delegatedManagedIdentityResourceId": null,
  "description": null,
  "id": "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/providers/Microsoft.Authorization/roleAssignments/0eb0b7de-664a-40d1-9b74-f2abd3f64e3b",
  "name": "0eb0b7de-664a-40d1-9b74-f2abd3f64e3b",
  "principalId": "791f6901-8f83-4774-b3ee-f9e265dcb212",
  "principalName": "66ab3502-4703-4fca-9491-09986d5203ea",
  "principalType": "ServicePrincipal",
  "roleDefinitionId": "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c",
  "roleDefinitionName": "Contributor",
  "scope": "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073",
  "type": "Microsoft.Authorization/roleAssignments",
  "updatedBy": "3f3d364b-bfad-45e3-95be-242b6e5f8051",
  "updatedOn": "2025-06-14T12:30:39.521540+00:00"
}
 janak@king  ~/terraform/azure  terraform init
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/azurerm versions matching "~> 4.0"...
- Installing hashicorp/azurerm v4.33.0...
- Installed hashicorp/azurerm v4.33.0 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
 janak@king  ~/terraform/azure  terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_linux_virtual_machine.janak-azure will be created
  + resource "azurerm_linux_virtual_machine" "janak-azure" {
      + admin_username                                         = "janak_azure"
      + allow_extension_operations                             = true
      + bypass_platform_safety_checks_on_user_schedule_enabled = false
      + computer_name                                          = (known after apply)
      + disable_password_authentication                        = true
      + disk_controller_type                                   = (known after apply)
      + extensions_time_budget                                 = "PT1H30M"
      + id                                                     = (known after apply)
      + location                                               = "westeurope"
      + max_bid_price                                          = -1
      + name                                                   = "Janak-azure-terraform"
      + network_interface_ids                                  = (known after apply)
      + patch_assessment_mode                                  = "ImageDefault"
      + patch_mode                                             = "ImageDefault"
      + platform_fault_domain                                  = -1
      + priority                                               = "Regular"
      + private_ip_address                                     = (known after apply)
      + private_ip_addresses                                   = (known after apply)
      + provision_vm_agent                                     = true
      + public_ip_address                                      = (known after apply)
      + public_ip_addresses                                    = (known after apply)
      + resource_group_name                                    = "Janak-res"
      + size                                                   = "Standard_B1s"
      + virtual_machine_id                                     = (known after apply)
      + vm_agent_platform_updates_enabled                      = (known after apply)

      + admin_ssh_key {
          + public_key = <<-EOT
                ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6Agbmcg4ej3+5gVvdeo7V6km7kWVec/XpDpgxQTohHgGjgGtLPqFlfWu8mHNQ786ACUHAVNXFcz04u44P5iTwDT5G1A/wWDhx6NUUqj3W1xZTb8hT80qkXUPEi7K01XyfPAgwZxJ/qwLBUpG1l4N/wKGtyJ7Lx+iLmYdhJaDHxmqSMqYxg5I8uCRDQgUlsZtIr0XfYsoNIooj+uSvn7IL3cTSRlf1l/jGTt0KD9Ssj3MFRy82cFXcrleBFyUiP5mAG7eIV9Dnn8iPfYDy5DaselwgHjsL+mQgJ9EwKEh4p7sJ7DGOerAE08l9Wo3YW33O30vQouyDnd35oliV64aUjgoWMsSCEbAGZSSeI5XgFJ1pqBVuhhXSlFSpo5P2Hnc1zYjRXEShrv2t9CvvIKlPCPuhorbLqPFg/LVCl+NWnKTlrhinvHjy24E36ryw3I6r/F5rwi3vIwyQ/Qj5CtYADs4+LXQIrJE9Rp+8X3GKu8MZlfZqGFmKbwQi9l5gHavTDYt7l89kJa170swahLYyoIRs3K+8occiCala4H8AiiahEbyetQ9XPGbOETxcfxYKOF2XJSHOEVnh+nq2manCbNZJyLlG7E/YWRDWf7VRC9JFgqXRACk0GRXi6vF/AEW+JQPNecQWoslQc+WvglpE0RUadbHt1IFWIZZx++XRxw== janak0ff@gmail.com
            EOT
          + username   = "janak_azure"
        }

      + os_disk {
          + caching                   = "ReadWrite"
          + disk_size_gb              = (known after apply)
          + id                        = (known after apply)
          + name                      = (known after apply)
          + storage_account_type      = "Standard_LRS"
          + write_accelerator_enabled = false
        }

      + source_image_reference {
          + offer     = "0001-com-ubuntu-server-jammy"
          + publisher = "Canonical"
          + sku       = "22_04-lts"
          + version   = "latest"
        }

      + termination_notification (known after apply)
    }

  # azurerm_network_interface.janak-azure will be created
  + resource "azurerm_network_interface" "janak-azure" {
      + accelerated_networking_enabled = false
      + applied_dns_servers            = (known after apply)
      + id                             = (known after apply)
      + internal_domain_name_suffix    = (known after apply)
      + ip_forwarding_enabled          = false
      + location                       = "westeurope"
      + mac_address                    = (known after apply)
      + name                           = "janak-azure-nic"
      + private_ip_address             = (known after apply)
      + private_ip_addresses           = (known after apply)
      + resource_group_name            = "Janak-res"
      + virtual_machine_id             = (known after apply)

      + ip_configuration {
          + gateway_load_balancer_frontend_ip_configuration_id = (known after apply)
          + name                                               = "internal"
          + primary                                            = (known after apply)
          + private_ip_address                                 = (known after apply)
          + private_ip_address_allocation                      = "Dynamic"
          + private_ip_address_version                         = "IPv4"
          + public_ip_address_id                               = (known after apply)
          + subnet_id                                          = (known after apply)
        }
    }

  # azurerm_network_interface_security_group_association.janak-azure will be created
  + resource "azurerm_network_interface_security_group_association" "janak-azure" {
      + id                        = (known after apply)
      + network_interface_id      = (known after apply)
      + network_security_group_id = (known after apply)
    }

  # azurerm_network_security_group.janak-azure will be created
  + resource "azurerm_network_security_group" "janak-azure" {
      + id                  = (known after apply)
      + location            = "westeurope"
      + name                = "janak-azure-nsg"
      + resource_group_name = "Janak-res"
      + security_rule       = [
          + {
              + access                                     = "Allow"
              + destination_address_prefix                 = "*"
              + destination_address_prefixes               = []
              + destination_application_security_group_ids = []
              + destination_port_range                     = "22"
              + destination_port_ranges                    = []
              + direction                                  = "Inbound"
              + name                                       = "Allow-SSH"
              + priority                                   = 1001
              + protocol                                   = "Tcp"
              + source_address_prefix                      = "*"
              + source_address_prefixes                    = []
              + source_application_security_group_ids      = []
              + source_port_range                          = "*"
              + source_port_ranges                         = []
                # (1 unchanged attribute hidden)
            },
        ]
    }

  # azurerm_public_ip.janak-azure will be created
  + resource "azurerm_public_ip" "janak-azure" {
      + allocation_method       = "Static"
      + ddos_protection_mode    = "VirtualNetworkInherited"
      + fqdn                    = (known after apply)
      + id                      = (known after apply)
      + idle_timeout_in_minutes = 4
      + ip_address              = (known after apply)
      + ip_version              = "IPv4"
      + location                = "westeurope"
      + name                    = "janak-azure-public-ip"
      + resource_group_name     = "Janak-res"
      + sku                     = "Standard"
      + sku_tier                = "Regional"
    }

  # azurerm_resource_group.janak-azure will be created
  + resource "azurerm_resource_group" "janak-azure" {
      + id       = (known after apply)
      + location = "westeurope"
      + name     = "Janak-res"
    }

  # azurerm_subnet.janak-azure will be created
  + resource "azurerm_subnet" "janak-azure" {
      + address_prefixes                              = [
          + "10.0.2.0/24",
        ]
      + default_outbound_access_enabled               = true
      + id                                            = (known after apply)
      + name                                          = "internal"
      + private_endpoint_network_policies             = "Disabled"
      + private_link_service_network_policies_enabled = true
      + resource_group_name                           = "Janak-res"
      + virtual_network_name                          = "janak-azure-network"
    }

  # azurerm_virtual_network.janak-azure will be created
  + resource "azurerm_virtual_network" "janak-azure" {
      + address_space                  = [
          + "10.0.0.0/16",
        ]
      + dns_servers                    = (known after apply)
      + guid                           = (known after apply)
      + id                             = (known after apply)
      + location                       = "westeurope"
      + name                           = "janak-azure-network"
      + private_endpoint_vnet_policies = "Disabled"
      + resource_group_name            = "Janak-res"
      + subnet                         = (known after apply)
    }

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + public_ip = (known after apply)

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run
"terraform apply" now.
 janak@king  ~/terraform/azure  terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # azurerm_linux_virtual_machine.janak-azure will be created
  + resource "azurerm_linux_virtual_machine" "janak-azure" {
      + admin_username                                         = "janak_azure"
      + allow_extension_operations                             = true
      + bypass_platform_safety_checks_on_user_schedule_enabled = false
      + computer_name                                          = (known after apply)
      + disable_password_authentication                        = true
      + disk_controller_type                                   = (known after apply)
      + extensions_time_budget                                 = "PT1H30M"
      + id                                                     = (known after apply)
      + location                                               = "westeurope"
      + max_bid_price                                          = -1
      + name                                                   = "Janak-azure-terraform"
      + network_interface_ids                                  = (known after apply)
      + patch_assessment_mode                                  = "ImageDefault"
      + patch_mode                                             = "ImageDefault"
      + platform_fault_domain                                  = -1
      + priority                                               = "Regular"
      + private_ip_address                                     = (known after apply)
      + private_ip_addresses                                   = (known after apply)
      + provision_vm_agent                                     = true
      + public_ip_address                                      = (known after apply)
      + public_ip_addresses                                    = (known after apply)
      + resource_group_name                                    = "Janak-res"
      + size                                                   = "Standard_B1s"
      + virtual_machine_id                                     = (known after apply)
      + vm_agent_platform_updates_enabled                      = (known after apply)

      + admin_ssh_key {
          + public_key = <<-EOT
                ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6Agbmcg4ej3+5gVvdeo7V6km7kWVec/XpDpgxQTohHgGjgGtLPqFlfWu8mHNQ786ACUHAVNXFcz04u44P5iTwDT5G1A/wWDhx6NUUqj3W1xZTb8hT80qkXUPEi7K01XyfPAgwZxJ/qwLBUpG1l4N/wKGtyJ7Lx+iLmYdhJaDHxmqSMqYxg5I8uCRDQgUlsZtIr0XfYsoNIooj+uSvn7IL3cTSRlf1l/jGTt0KD9Ssj3MFRy82cFXcrleBFyUiP5mAG7eIV9Dnn8iPfYDy5DaselwgHjsL+mQgJ9EwKEh4p7sJ7DGOerAE08l9Wo3YW33O30vQouyDnd35oliV64aUjgoWMsSCEbAGZSSeI5XgFJ1pqBVuhhXSlFSpo5P2Hnc1zYjRXEShrv2t9CvvIKlPCPuhorbLqPFg/LVCl+NWnKTlrhinvHjy24E36ryw3I6r/F5rwi3vIwyQ/Qj5CtYADs4+LXQIrJE9Rp+8X3GKu8MZlfZqGFmKbwQi9l5gHavTDYt7l89kJa170swahLYyoIRs3K+8occiCala4H8AiiahEbyetQ9XPGbOETxcfxYKOF2XJSHOEVnh+nq2manCbNZJyLlG7E/YWRDWf7VRC9JFgqXRACk0GRXi6vF/AEW+JQPNecQWoslQc+WvglpE0RUadbHt1IFWIZZx++XRxw== janak0ff@gmail.com
            EOT
          + username   = "janak_azure"
        }

      + os_disk {
          + caching                   = "ReadWrite"
          + disk_size_gb              = (known after apply)
          + id                        = (known after apply)
          + name                      = (known after apply)
          + storage_account_type      = "Standard_LRS"
          + write_accelerator_enabled = false
        }

      + source_image_reference {
          + offer     = "0001-com-ubuntu-server-jammy"
          + publisher = "Canonical"
          + sku       = "22_04-lts"
          + version   = "latest"
        }

      + termination_notification (known after apply)
    }

  # azurerm_network_interface.janak-azure will be created
  + resource "azurerm_network_interface" "janak-azure" {
      + accelerated_networking_enabled = false
      + applied_dns_servers            = (known after apply)
      + id                             = (known after apply)
      + internal_domain_name_suffix    = (known after apply)
      + ip_forwarding_enabled          = false
      + location                       = "westeurope"
      + mac_address                    = (known after apply)
      + name                           = "janak-azure-nic"
      + private_ip_address             = (known after apply)
      + private_ip_addresses           = (known after apply)
      + resource_group_name            = "Janak-res"
      + virtual_machine_id             = (known after apply)

      + ip_configuration {
          + gateway_load_balancer_frontend_ip_configuration_id = (known after apply)
          + name                                               = "internal"
          + primary                                            = (known after apply)
          + private_ip_address                                 = (known after apply)
          + private_ip_address_allocation                      = "Dynamic"
          + private_ip_address_version                         = "IPv4"
          + public_ip_address_id                               = (known after apply)
          + subnet_id                                          = (known after apply)
        }
    }

  # azurerm_network_interface_security_group_association.janak-azure will be created
  + resource "azurerm_network_interface_security_group_association" "janak-azure" {
      + id                        = (known after apply)
      + network_interface_id      = (known after apply)
      + network_security_group_id = (known after apply)
    }

  # azurerm_network_security_group.janak-azure will be created
  + resource "azurerm_network_security_group" "janak-azure" {
      + id                  = (known after apply)
      + location            = "westeurope"
      + name                = "janak-azure-nsg"
      + resource_group_name = "Janak-res"
      + security_rule       = [
          + {
              + access                                     = "Allow"
              + destination_address_prefix                 = "*"
              + destination_address_prefixes               = []
              + destination_application_security_group_ids = []
              + destination_port_range                     = "22"
              + destination_port_ranges                    = []
              + direction                                  = "Inbound"
              + name                                       = "Allow-SSH"
              + priority                                   = 1001
              + protocol                                   = "Tcp"
              + source_address_prefix                      = "*"
              + source_address_prefixes                    = []
              + source_application_security_group_ids      = []
              + source_port_range                          = "*"
              + source_port_ranges                         = []
                # (1 unchanged attribute hidden)
            },
        ]
    }

  # azurerm_public_ip.janak-azure will be created
  + resource "azurerm_public_ip" "janak-azure" {
      + allocation_method       = "Static"
      + ddos_protection_mode    = "VirtualNetworkInherited"
      + fqdn                    = (known after apply)
      + id                      = (known after apply)
      + idle_timeout_in_minutes = 4
      + ip_address              = (known after apply)
      + ip_version              = "IPv4"
      + location                = "westeurope"
      + name                    = "janak-azure-public-ip"
      + resource_group_name     = "Janak-res"
      + sku                     = "Standard"
      + sku_tier                = "Regional"
    }

  # azurerm_resource_group.janak-azure will be created
  + resource "azurerm_resource_group" "janak-azure" {
      + id       = (known after apply)
      + location = "westeurope"
      + name     = "Janak-res"
    }

  # azurerm_subnet.janak-azure will be created
  + resource "azurerm_subnet" "janak-azure" {
      + address_prefixes                              = [
          + "10.0.2.0/24",
        ]
      + default_outbound_access_enabled               = true
      + id                                            = (known after apply)
      + name                                          = "internal"
      + private_endpoint_network_policies             = "Disabled"
      + private_link_service_network_policies_enabled = true
      + resource_group_name                           = "Janak-res"
      + virtual_network_name                          = "janak-azure-network"
    }

  # azurerm_virtual_network.janak-azure will be created
  + resource "azurerm_virtual_network" "janak-azure" {
      + address_space                  = [
          + "10.0.0.0/16",
        ]
      + dns_servers                    = (known after apply)
      + guid                           = (known after apply)
      + id                             = (known after apply)
      + location                       = "westeurope"
      + name                           = "janak-azure-network"
      + private_endpoint_vnet_policies = "Disabled"
      + resource_group_name            = "Janak-res"
      + subnet                         = (known after apply)
    }

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + public_ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

azurerm_resource_group.janak-azure: Creating...
azurerm_resource_group.janak-azure: Still creating... [00m10s elapsed]
azurerm_resource_group.janak-azure: Creation complete after 15s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res]
azurerm_virtual_network.janak-azure: Creating...
azurerm_network_security_group.janak-azure: Creating...
azurerm_public_ip.janak-azure: Creating...
azurerm_public_ip.janak-azure: Creation complete after 4s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/publicIPAddresses/janak-azure-public-ip]
azurerm_network_security_group.janak-azure: Creation complete after 5s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_virtual_network.janak-azure: Creation complete after 9s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network]
azurerm_subnet.janak-azure: Creating...
azurerm_subnet.janak-azure: Creation complete after 7s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal]
azurerm_network_interface.janak-azure: Creating...
azurerm_network_interface.janak-azure: Still creating... [00m10s elapsed]
azurerm_network_interface.janak-azure: Creation complete after 14s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic]
azurerm_network_interface_security_group_association.janak-azure: Creating...
azurerm_linux_virtual_machine.janak-azure: Creating...
azurerm_network_interface_security_group_association.janak-azure: Still creating... [00m10s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still creating... [00m10s elapsed]
azurerm_network_interface_security_group_association.janak-azure: Creation complete after 15s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic|/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_linux_virtual_machine.janak-azure: Still creating... [00m20s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still creating... [00m30s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still creating... [00m40s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still creating... [00m50s elapsed]
azurerm_linux_virtual_machine.janak-azure: Creation complete after 54s [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/virtualMachines/Janak-azure-terraform]

Apply complete! Resources: 8 added, 0 changed, 0 destroyed.

Outputs:

public_ip = "51.136.100.152"
 janak@king  ~/terraform/azure  ssh -i ~/.ssh/id_rsa janak_azure@51.136.100.152        
The authenticity of host '51.136.100.152 (51.136.100.152)' can't be established.
ED25519 key fingerprint is SHA256:3SD6gMRFre8UySU/WJUAnR6XIRmyJAOiW3U4DE0Wmc4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '51.136.100.152' (ED25519) to the list of known hosts.
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 6.8.0-1029-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat Jun 14 12:41:28 UTC 2025

  System load:  0.12              Processes:             125
  Usage of /:   5.3% of 28.89GB   Users logged in:       0
  Memory usage: 29%               IPv4 address for eth0: 10.0.2.4
  Swap usage:   0%

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

janak_azure@Janak-azure-terraform:~$ exit
logout
Connection to 51.136.100.152 closed.
 janak@king  ~/terraform/azure  terraform destroy                                 
azurerm_resource_group.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res]
azurerm_public_ip.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/publicIPAddresses/janak-azure-public-ip]
azurerm_virtual_network.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network]
azurerm_network_security_group.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_subnet.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal]
azurerm_network_interface.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic]
azurerm_network_interface_security_group_association.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic|/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_linux_virtual_machine.janak-azure: Refreshing state... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/virtualMachines/Janak-azure-terraform]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  - destroy

Terraform will perform the following actions:

  # azurerm_linux_virtual_machine.janak-azure will be destroyed
  - resource "azurerm_linux_virtual_machine" "janak-azure" {
      - admin_username                                         = "janak_azure" -> null
      - allow_extension_operations                             = true -> null
      - bypass_platform_safety_checks_on_user_schedule_enabled = false -> null
      - computer_name                                          = "Janak-azure-terraform" -> null
      - disable_password_authentication                        = true -> null
      - encryption_at_host_enabled                             = false -> null
      - extensions_time_budget                                 = "PT1H30M" -> null
      - id                                                     = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/virtualMachines/Janak-azure-terraform" -> null
      - location                                               = "westeurope" -> null
      - max_bid_price                                          = -1 -> null
      - name                                                   = "Janak-azure-terraform" -> null
      - network_interface_ids                                  = [
          - "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic",
        ] -> null
      - patch_assessment_mode                                  = "ImageDefault" -> null
      - patch_mode                                             = "ImageDefault" -> null
      - platform_fault_domain                                  = -1 -> null
      - priority                                               = "Regular" -> null
      - private_ip_address                                     = "10.0.2.4" -> null
      - private_ip_addresses                                   = [
          - "10.0.2.4",
        ] -> null
      - provision_vm_agent                                     = true -> null
      - public_ip_address                                      = "51.136.100.152" -> null
      - public_ip_addresses                                    = [
          - "51.136.100.152",
        ] -> null
      - resource_group_name                                    = "Janak-res" -> null
      - secure_boot_enabled                                    = false -> null
      - size                                                   = "Standard_B1s" -> null
      - tags                                                   = {} -> null
      - virtual_machine_id                                     = "984eb157-274d-440a-ace5-d3aca6c17071" -> null
      - vm_agent_platform_updates_enabled                      = false -> null
      - vtpm_enabled                                           = false -> null
        # (14 unchanged attributes hidden)

      - admin_ssh_key {
          - public_key = <<-EOT
                ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6Agbmcg4ej3+5gVvdeo7V6km7kWVec/XpDpgxQTohHgGjgGtLPqFlfWu8mHNQ786ACUHAVNXFcz04u44P5iTwDT5G1A/wWDhx6NUUqj3W1xZTb8hT80qkXUPEi7K01XyfPAgwZxJ/qwLBUpG1l4N/wKGtyJ7Lx+iLmYdhJaDHxmqSMqYxg5I8uCRDQgUlsZtIr0XfYsoNIooj+uSvn7IL3cTSRlf1l/jGTt0KD9Ssj3MFRy82cFXcrleBFyUiP5mAG7eIV9Dnn8iPfYDy5DaselwgHjsL+mQgJ9EwKEh4p7sJ7DGOerAE08l9Wo3YW33O30vQouyDnd35oliV64aUjgoWMsSCEbAGZSSeI5XgFJ1pqBVuhhXSlFSpo5P2Hnc1zYjRXEShrv2t9CvvIKlPCPuhorbLqPFg/LVCl+NWnKTlrhinvHjy24E36ryw3I6r/F5rwi3vIwyQ/Qj5CtYADs4+LXQIrJE9Rp+8X3GKu8MZlfZqGFmKbwQi9l5gHavTDYt7l89kJa170swahLYyoIRs3K+8occiCala4H8AiiahEbyetQ9XPGbOETxcfxYKOF2XJSHOEVnh+nq2manCbNZJyLlG7E/YWRDWf7VRC9JFgqXRACk0GRXi6vF/AEW+JQPNecQWoslQc+WvglpE0RUadbHt1IFWIZZx++XRxw== janak0ff@gmail.com
            EOT -> null
          - username   = "janak_azure" -> null
        }

      - os_disk {
          - caching                          = "ReadWrite" -> null
          - disk_size_gb                     = 30 -> null
          - id                               = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/disks/Janak-azure-terraform_OsDisk_1_7b801c1a3c754d188cd9518075d5688e" -> null
          - name                             = "Janak-azure-terraform_OsDisk_1_7b801c1a3c754d188cd9518075d5688e" -> null
          - storage_account_type             = "Standard_LRS" -> null
          - write_accelerator_enabled        = false -> null
            # (3 unchanged attributes hidden)
        }

      - source_image_reference {
          - offer     = "0001-com-ubuntu-server-jammy" -> null
          - publisher = "Canonical" -> null
          - sku       = "22_04-lts" -> null
          - version   = "latest" -> null
        }
    }

  # azurerm_network_interface.janak-azure will be destroyed
  - resource "azurerm_network_interface" "janak-azure" {
      - accelerated_networking_enabled = false -> null
      - applied_dns_servers            = [] -> null
      - dns_servers                    = [] -> null
      - id                             = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic" -> null
      - internal_domain_name_suffix    = "pvrtl4t03jvupisk0fqt2zzyld.ax.internal.cloudapp.net" -> null
      - ip_forwarding_enabled          = false -> null
      - location                       = "westeurope" -> null
      - mac_address                    = "60-45-BD-9D-81-AB" -> null
      - name                           = "janak-azure-nic" -> null
      - private_ip_address             = "10.0.2.4" -> null
      - private_ip_addresses           = [
          - "10.0.2.4",
        ] -> null
      - resource_group_name            = "Janak-res" -> null
      - tags                           = {} -> null
      - virtual_machine_id             = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/virtualMachines/Janak-azure-terraform" -> null
        # (4 unchanged attributes hidden)

      - ip_configuration {
          - name                                               = "internal" -> null
          - primary                                            = true -> null
          - private_ip_address                                 = "10.0.2.4" -> null
          - private_ip_address_allocation                      = "Dynamic" -> null
          - private_ip_address_version                         = "IPv4" -> null
          - public_ip_address_id                               = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/publicIPAddresses/janak-azure-public-ip" -> null
          - subnet_id                                          = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal" -> null
            # (1 unchanged attribute hidden)
        }
    }

  # azurerm_network_interface_security_group_association.janak-azure will be destroyed
  - resource "azurerm_network_interface_security_group_association" "janak-azure" {
      - id                        = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic|/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg" -> null
      - network_interface_id      = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic" -> null
      - network_security_group_id = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg" -> null
    }

  # azurerm_network_security_group.janak-azure will be destroyed
  - resource "azurerm_network_security_group" "janak-azure" {
      - id                  = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg" -> null
      - location            = "westeurope" -> null
      - name                = "janak-azure-nsg" -> null
      - resource_group_name = "Janak-res" -> null
      - security_rule       = [
          - {
              - access                                     = "Allow"
              - destination_address_prefix                 = "*"
              - destination_address_prefixes               = []
              - destination_application_security_group_ids = []
              - destination_port_range                     = "22"
              - destination_port_ranges                    = []
              - direction                                  = "Inbound"
              - name                                       = "Allow-SSH"
              - priority                                   = 1001
              - protocol                                   = "Tcp"
              - source_address_prefix                      = "*"
              - source_address_prefixes                    = []
              - source_application_security_group_ids      = []
              - source_port_range                          = "*"
              - source_port_ranges                         = []
                # (1 unchanged attribute hidden)
            },
        ] -> null
      - tags                = {} -> null
    }

  # azurerm_public_ip.janak-azure will be destroyed
  - resource "azurerm_public_ip" "janak-azure" {
      - allocation_method       = "Static" -> null
      - ddos_protection_mode    = "VirtualNetworkInherited" -> null
      - id                      = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/publicIPAddresses/janak-azure-public-ip" -> null
      - idle_timeout_in_minutes = 4 -> null
      - ip_address              = "51.136.100.152" -> null
      - ip_tags                 = {} -> null
      - ip_version              = "IPv4" -> null
      - location                = "westeurope" -> null
      - name                    = "janak-azure-public-ip" -> null
      - resource_group_name     = "Janak-res" -> null
      - sku                     = "Standard" -> null
      - sku_tier                = "Regional" -> null
      - tags                    = {} -> null
      - zones                   = [] -> null
        # (1 unchanged attribute hidden)
    }

  # azurerm_resource_group.janak-azure will be destroyed
  - resource "azurerm_resource_group" "janak-azure" {
      - id         = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res" -> null
      - location   = "westeurope" -> null
      - name       = "Janak-res" -> null
      - tags       = {} -> null
        # (1 unchanged attribute hidden)
    }

  # azurerm_subnet.janak-azure will be destroyed
  - resource "azurerm_subnet" "janak-azure" {
      - address_prefixes                              = [
          - "10.0.2.0/24",
        ] -> null
      - default_outbound_access_enabled               = true -> null
      - id                                            = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal" -> null
      - name                                          = "internal" -> null
      - private_endpoint_network_policies             = "Disabled" -> null
      - private_link_service_network_policies_enabled = true -> null
      - resource_group_name                           = "Janak-res" -> null
      - service_endpoint_policy_ids                   = [] -> null
      - service_endpoints                             = [] -> null
      - virtual_network_name                          = "janak-azure-network" -> null
    }

  # azurerm_virtual_network.janak-azure will be destroyed
  - resource "azurerm_virtual_network" "janak-azure" {
      - address_space                  = [
          - "10.0.0.0/16",
        ] -> null
      - dns_servers                    = [] -> null
      - flow_timeout_in_minutes        = 0 -> null
      - guid                           = "fa35637d-ea7a-476b-a24a-d1613e67385b" -> null
      - id                             = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network" -> null
      - location                       = "westeurope" -> null
      - name                           = "janak-azure-network" -> null
      - private_endpoint_vnet_policies = "Disabled" -> null
      - resource_group_name            = "Janak-res" -> null
      - subnet                         = [
          - {
              - address_prefixes                              = [
                  - "10.0.2.0/24",
                ]
              - default_outbound_access_enabled               = true
              - delegation                                    = []
              - id                                            = "/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal"
              - name                                          = "internal"
              - private_endpoint_network_policies             = "Disabled"
              - private_link_service_network_policies_enabled = true
              - service_endpoint_policy_ids                   = []
              - service_endpoints                             = []
                # (2 unchanged attributes hidden)
            },
        ] -> null
      - tags                           = {} -> null
        # (2 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 8 to destroy.

Changes to Outputs:
  - public_ip = "51.136.100.152" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

azurerm_network_interface_security_group_association.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic|/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_linux_virtual_machine.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Compute/virtualMachines/Janak-azure-terraform]
azurerm_network_interface_security_group_association.janak-azure: Destruction complete after 8s
azurerm_network_security_group.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkSecurityGroups/janak-azure-nsg]
azurerm_linux_virtual_machine.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-.../virtualMachines/Janak-azure-terraform, 00m10s elapsed]
azurerm_network_security_group.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-.../networkSecurityGroups/janak-azure-nsg, 00m10s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-.../virtualMachines/Janak-azure-terraform, 00m20s elapsed]
azurerm_network_security_group.janak-azure: Destruction complete after 13s
azurerm_linux_virtual_machine.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-.../virtualMachines/Janak-azure-terraform, 00m30s elapsed]
azurerm_linux_virtual_machine.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-.../virtualMachines/Janak-azure-terraform, 00m40s elapsed]
azurerm_linux_virtual_machine.janak-azure: Destruction complete after 41s
azurerm_network_interface.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/networkInterfaces/janak-azure-nic]
azurerm_network_interface.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-...work/networkInterfaces/janak-azure-nic, 00m10s elapsed]
azurerm_network_interface.janak-azure: Destruction complete after 14s
azurerm_subnet.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network/subnets/internal]
azurerm_public_ip.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/publicIPAddresses/janak-azure-public-ip]
azurerm_public_ip.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-...ublicIPAddresses/janak-azure-public-ip, 00m10s elapsed]
azurerm_subnet.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-...s/janak-azure-network/subnets/internal, 00m10s elapsed]
azurerm_subnet.janak-azure: Destruction complete after 11s
azurerm_virtual_network.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res/providers/Microsoft.Network/virtualNetworks/janak-azure-network]
azurerm_public_ip.janak-azure: Destruction complete after 12s
azurerm_virtual_network.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-...rk/virtualNetworks/janak-azure-network, 00m10s elapsed]
azurerm_virtual_network.janak-azure: Destruction complete after 13s
azurerm_resource_group.janak-azure: Destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res]
azurerm_resource_group.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res, 00m10s elapsed]
azurerm_resource_group.janak-azure: Still destroying... [id=/subscriptions/bf97eca7-bcbd-41ce-bc31-9c5d684f2073/resourceGroups/Janak-res, 00m20s elapsed]
azurerm_resource_group.janak-azure: Destruction complete after 22s

Destroy complete! Resources: 8 destroyed.
 janak@king  ~/terraform/azure  
```