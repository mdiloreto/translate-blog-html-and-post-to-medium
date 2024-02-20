# TLS Termination (or SSL Offloading) in Azure App Gateway – part 2

![Image](https://madsblog.net/wp-content/uploads/2023/09/image-6-1024x1024.png)


In part 2 of this series, we'll perform the step-by-step of publishing a site through Azure Application Gateway with SSL Offloading in a lab environment.

Scenario:

* 1 App Gateway named "madsblogtest-ag-waf", tier WAF V2. 
* 1 App Service called "test-madsblog" (Web App).




Objective:

* We will publish this App Service using SSL Offloading to Azure Application Gateway. 
* Public URL: test-site.madsblog.net.
* We'll use a Lets Encrypt certificate. 




Creating a Backend Pool

We must enter our AppGateway, in the left menu go to Backend Pools and click on Add:
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-1.png)


We added our App Service "test-madsblog" as a backend pool.

Creating Backend Settings

In the left menu, go to Backend Settings in the left menu of our app gateway and click on Add:
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-3.png)


Here it is important that we configure HTTP traffic for our Backend. This will allow us to perform SSL Termination at the App Gateway level.

Creating a Custom Probe

We will create the Custom Probe so that the health of our backend is monitored correctly by our App Gateway.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-8.png)


Due to SSL Termination, the traffic we will monitor with our health probe will be HTTP traffic from the AppGateway to the Backend.

Upload Certificate

Before creating the Listener of our host, we must upload the Lets Encrypt certificate. Go to Listeners and click on the Listener TLS certificates tab (preview):
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-4.png)


Now we upload the cert in PFX!
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-5.png)


We will now have our certificate available for use in the App Gateway.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-6.png)


Creating Listeners

Now, we can proceed to create the Listener.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-10.png)


In this case, we will configure a site only for the DNS Name test-site.madsblog.net, because it is the only hostname that supports our certificate. It is important to note that we can configure more than one DNS Name for the listener, but we must take this into account when requesting the certificate.

Creating Routing Rules

Now so that all the elements are configured in our AppGateway: Backend Pool + Settings, Custom Health Probe and Listener (with certificate), we can configure our routing rule.

Go to Rules and click Add:
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-9.png)

![Image](https://madsblog.net/wp-content/uploads/2023/07/image-11.png)


Here we could add a path to have different traffic paths and also granularize our listener. In this case, we will not cover this functionality.

DNS Record Settings:

Now we can point to our public DNS record of test-site.madsblog.net. To do this, we must enter our public DNS and configure the CNAME record pointing to the public DNS Name of our App Gateway.

This detail can be found in the Public Front End Settings section of our App Gateway.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-12.png)


Ready! Now we have published our site through Azure Application Gateway, but there is something else missing...

If we try to connect to our Site through the Public URL now, we will have an error:
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-14.png)


This happens because, in addition to configuring our publication, we must make sure that our AppGateway can communicate correctly with the App Service. Let's take a look:

Configuring App Service (Web App)

In the first instance we must take care of 2 settings:

1) Enable HTTP traffic! App Services do not accept HTTP traffic by default, we must enable it manually:

* We must go to our Web App. 
* Go to Configuration>General Settings:  



![Image](https://madsblog.net/wp-content/uploads/2023/07/image-15.png)


2) Enable our Custom Domain. To be able to use a domain other than *.azurewebsites.net we must manually configure the costom domain in our WebApp. Click here to see the step-by-step.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-16.png)


The Domain will remain in No binding since it will NOT use SSL at the Backend level. This configuration must only be done so that our App Service supports the connection with that domain name.

Traffic restriction in the Backend

Finally, to complete the configurations at the security level. We must restrict access in our App Service so that it ONLY allows traffic from our App Gateway.
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-19-1024x426.png)

![Image](https://madsblog.net/wp-content/uploads/2023/07/image-17.png)


We must do the same with any other backend.

Entrance exam

Now, once these steps have been completed, we can verify the secure access to our Site through Azure AppGateway with TLS/SSL Termination 🙂
![Image](https://madsblog.net/wp-content/uploads/2023/07/image-18.png)


Mateo Di Loreto
