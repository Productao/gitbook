---
description: >-
  SAML integration allows for Okta initiated sign up and login using application
  tile
---

# Integrating Agentnoon with Okta using SAML

#### 1. Create a New App Integration in Okta

1. Create a new app integration with SAML preset

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXcfGZc8VGN9NA5ueu3qeOl085xiME9Ecwj2OGXkIOORUxSi63mR6WGW9CFwWTPDUAYB7W3MSXiLa8Vw2x--8_hWehTyCdMoIK9B7zMp-HtLwiAvH-9X3shJjSeZk7y4r0ZuRiYM5ZgO8kKd_bCeg9NyvmAh?key=gESMSun60tfjUT5xOTZlqA" alt="" width="563"><figcaption></figcaption></figure>

2. On the 1st page type in app name: Agentnoon and add a logo

#### 2. Configure SAML Settings

1. On the second page, enter the following SAML configuration:
   1. Single sign on URL
      1. [https://api-cloud.agentnoon.co/saml-sso](https://api-cloud.agentnoon.co/saml-sso)
   2. Audience URI:
      1. [https://app.agentnoon.com](https://app.agentnoon.com)
   3. Name ID format
      1. **EmailAddress**
   4. Attribute Statements
      1. Name: **firstName**, Value: **user.firstName**
      2. Name: **lastName**, Value: **user.lastName**

#### 3. Skip the Feedback Page

1. Click **Finish** to complete the app integration.
2. You may skip the third (feedback) page.

#### 4. Share SAML Metadata with Agentnoon

From the integration overview:

1. Go to the **Sign On** tab.
2. Click **View SAML setup instructions** (right sidebar).

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2c3CfRtoUbAXf_rd36uq_JritN-ijIsUePZJ3rD3B24d-RBehb0MJWl53KZ56a0cGQJglXIEKygMHK8y4-gObEBxLcyyxwkoJ4q3vlt-kNeA94XX1AgtrYDSyTQrk-GFgrIPT3Lu_wkTvt7TU-kLj5eHt?key=gESMSun60tfjUT5xOTZlqA" alt="" width="563"><figcaption></figcaption></figure>

3. Share all 3 properties with Agentnoon:
   1. Identity Provider Single Sign-On URL
   2. Identity Provider Issuer
   3. X.509 Certificate
