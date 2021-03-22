LAB Volterra
=======================================================================
.. contents:: Table of Contents

Introduction
==================================================
Objectives
###############
- **AWS VPC site** -- Deploy a Volterra GW on an AWS VPC site
- **VM Arcadia** -- Deploy a VM with Arcadia services
- **Clean** -- Delete objects on Volterra and AWS

Demo
###############
1) Deploy a Volterra GW on an AWS VPC site
******************************************

.. raw:: html

    <a href="http://www.youtube.com/watch?v=BMEK_JEi3cc"><img src="http://img.youtube.com/vi/BMEK_JEi3cc/0.jpg" width="600" height="400" title="Create Identity Provider" alt="Create Identity Provider"></a>

User guide
==================================================
Quick links
#############################################
- `Ansible Tower <https://tower-cloudbuilderf5.eastus2.cloudapp.azure.com>`_
- `Azure <https://portal.azure.com>`_
- `VoltConsole >> Login <https://www.volterra.io/products/voltconsole>`_
- `AWS portal <https://console.aws.amazon.com>`_

Pre-requisites
#############################################
1. Manage L3 access to Ansible Tower
*************************************
- Connect to Azure Portal
- Update Network security groups ``nsg-tower`` >> Inbound security rules >> rule ``https``: add your Public IP

2. Manage authorisation to Ansible Tower
*****************************************
- Connect to Ansible Tower using Github
- Contact administrator to add your account into Lab group

Automated use case (workflow)
#############################################
1. Deploy a Volterra GW on an AWS VPC site
*********************************************
- Connect to Ansible Tower using Github
- Launch Template >> ``wf-volterra-deploy_vpc_arcadia``

2. Clean Volterra GW on an AWS VPC site
*********************************************
- Connect to Ansible Tower using Github
- Launch Template >> ``wf-volterra-clean_vpc_arcadia``









