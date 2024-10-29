# Types of Cloud Migration


We continue with some basic theoretical content of Cloud, in this case we are going to talk about the different migration strategies. You can review the note on Cloud Computing Fundamentals – Learn Multi Cloud(s) (madsblog.net)
![Image](https://madsblog.net/wp-content/uploads/2024/09/image-6.png)

## Introduction


When we start planning our migration process, we must start by determining our destination and starting point. Our starting point can be: on-premises, co-hosting, housing or from a cloud provider (cloud-to-cloud migration). Our destination will be the Cloud, from the provider we like the most.

This is where we must keep in mind that our migration process must be carefully evaluated, it must involve a process of discovery and detailed analysis of our source infrastructure.

I recommend paying close attention to the Assessment and Discovery process, as it will lay the foundation for our migration process and allow us to be successful.
## Engage teams


Migration processes are usually carried out and are the responsibility of the infrastructure team, but it is very important that this process also involves:

* The technical owners of the applications (by this I mean the code). 
* The business owners of the applications. 
* Leadership teams and key roles.
* Teams in charge of dependencies or integrations of the applications involved. 



## Types of Migration


We can classify migrations into the following types:

* Rehost: lift and shift.
* Replatform: lift and optimize.
* Refactor: move and improve.
* Re-architect: continue to modernize.
* Rebuild: remove and replace, also called rip and replace.
* Repurchase.



## Rehost: Lift and Shift


We start with the well-known "lift and move". This type of migration involves moving workloads "as-is" (as they are), making only minimal modifications so that the workloads can function optimally in the target environment.

This type of migration is ideal for laying the foundations when migrating to the cloud. This allows the team to begin to see some of the benefits of being in the cloud while maintaining the same tools and skills they used in on-prem.

Lift and Shift is very fast and relatively simple, and all Cloud Providers have a Native tool that allows you to perform this procedure without problems and with a tool supported by the manufacturer that is capable of integrating with different Source platforms such as VMWare for VMs or directly for physical servers. Examples of these tools: GCP Migrate to Virtual Machines or Azure Migrator.

Maintaining IaaS workloads in the cloud can be costly. When migrating using the Lift and Shift approach, the costs are often high because we do not take full advantage of the benefits offered by the cloud. While this model reduces responsibilities for administrators, as the cloud provider is responsible for maintaining hardware, hypervisors, networks, and more, it is not very efficient in terms of compute value versus cost. In fact, many organizations that rely heavily on IaaS end up opting for a Cloud Exit.

We must be vigilant and optimize our workloads for the Cloud.
## Replatform: lift and optimize


In this type of migration, it takes many more of the advantages of the core competencies of the Cloud: elasticity, redundancy, performance optimization, and security.

This strategy involves more work, but it can help us improve the impact of costs.

Continuing with the example of migrating a VM-based workload from on-prem to Cloud:

* We could deploy Compute Engine Managed Instances on GCP or Azure Scale Sets to add scalability and elasticity to our workloads. 




* Another example would be migrating from a MySQL database engine running on a Server to the Cloud SQL or Azure Database service. 



## Refactor: move and improve


With this strategy, workloads will be modified before or while they are migrated to the cloud.

Refactoring migrations allow you to take advantage of cloud features such as scalability and high availability. It is also possible to improve the architecture to increase the portability of the application.

We must keep in mind that this type of migration takes longer than a rehost migration, as it is necessary to refactor the workloads.

In addition, refactoring requires acquiring new skills.

Example:

* Refactor Jobs to run in Cloud Functions. 
* Migrate Compressed application from a VM to a PaaS Service such as Google Cloud Run or Azure Container Apps. 



## Re-architect: continue to modernize


This type of migration is comparable to Refactor's strategy, but we add a bit of complexity. In this case a re-architect is made to change how the code works. This allows the code to be optimized to be executed in the Cloud.

Example:

* Refactoring a monolithic application to run on AKS or EKS as Microservices. 



## Rebuild: remove and replace


In this case, we decommissioned the on-premises application and completely redesigned it from 0 in the cloud.

This type of migration allows the generation of a Cloud-Native solution from the beginning since it will be designed and implemented in the context of the cloud.

These rebuild migrations can take longer than rehost or refactor migrations. They are not suitable for out-of-the-box applications as they require rewriting the application. It is important to evaluate the additional time and effort to redesign it.

This type of migration also requires new skills and tools to configure and deploy the app in the new environment.
## Repurchase


In this case, it is when a SaaS service is acquired as the target environment.

From a resource standpoint, a buyback migration is often simpler than refactoring, rebuilding, or re-architecting. However, it can be more expensive, and you may not get the same level of granular control over your cloud environment.

For example:

* If you used email or on-premises collaboration tools, moving to Microsoft 365 is a Repurchase. 



## Adoption Frameworks


Each Cloud has an Adoption Framework that allows a formal framework to be given to the maturity that each organization has to migrate to the cloud. Here are the Big 3 Adoption Frameworks:

* Adoption Framework | Google Cloud
* Microsoft Cloud Adoption Framework for Azure – Cloud Adoption Framework | Microsoft Learn
* AWS Cloud Adoption Framework (amazon.com)



## Common prerequisites for any migration


* Assess and Discover.
* Planning and construction. 
* Test Cases and Pilot Tests.  



## Assess and Discover


Basically, in this stage of the migration we are going to make an inventory of all the resources to be migrated and we will determine the requirements and dependencies of each one. We must gain a Very Deep knowledge about the workloads we are going to migrate.

Here we will have a great participation of all the teams involved: technical leaders, app owners, business leaders, networking, etc...

It is important to detect early blockers and set expectations for stakeholders.

Some of the tasks of this stage will be:

* Generate an inventory.
* Catalog applications and dependencies. 
* Train teams.
* Generate PoC if necessary. 
* Calculate TCO. 




This is how an inventory resulting from this stage can be seen:
![Image](https://madsblog.net/wp-content/uploads/2024/09/image-1-1024x476.png)

![Image](https://madsblog.net/wp-content/uploads/2024/09/image-4-1024x319.png)


From this information we must be able to generate a categorization in terms of criticality / level of difficulty of our Workloads:
![Image](https://madsblog.net/wp-content/uploads/2024/09/image-5-1024x651.png)

## Planning and construction


At this stage we will plan and build the foundations of our migration:

* Project definitions. 
* Project planning. 
* Landing Zones.




Some of the tasks we'll perform in this step include:

* Agree and define action plan.
* Assign a Timeline (or action schedule). 
* Choose the migration strategy. 
* Choose the migration tool(s). 
* Build our landing zones (if necessary, as they may exist previously).




At this stage, we must also take into account:

* Resource hierarchy: Designing a proper resource structure is crucial for billing, security, and team management.




* Identity and Access Management (IAM): Focuses on how to manage access to Google Cloud resources through users, groups, and service accounts, ensuring granular control and best security practices.




* Connectivity and networking: It is important to plan network design, data transfer, and adjust parameters such as maximum transmission unit (MTU) to optimize performance.




* Billing: The concepts of resource hierarchy and billing are related. It's critical to understand how resources are billed.




* Governance: Establishing control and management strategies is vital to maintaining the security, compliance, and organization of cloud resources.




* Security and Compliance: The management and security of systems in the United States require a clear understanding of responsibilities and threats, in addition to implementing proactive detection and monitoring practices.



## Test Cases and Pilot Tests


For each of the migrations, it is advisable to add a stage of Test Cases and Pilot Test once the migration tool has been configured. These phases will ensure the effectiveness of the process, minimizing risks and disruptions.

Additionally:

* Monitoring and analysis: It is crucial to monitor each migration throughout the process to obtain key metrics such as execution times, errors, or performance impacts. This will allow future processes to be adjusted and time optimized.
* Reversal plan: Make sure you have a contingency or reversal plan in place to minimize risks in the event of possible failures during the pilot test.
* Automation: If possible, automate part of the testing process to reduce manual intervention and ensure consistency in results.





Mateo Di Loreto
