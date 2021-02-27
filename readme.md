#CodeTestBack

## GCP Configuration

* **Project ID** : code-test-back
  

* **Region** : europe-west1


* **Zone** : europe-west1-b


* **Cloud Run Service** : code-test-back-service


* **Cloud Build** : code-test-back-trigger


* **Enabled Services** : 
    * Enable Cloud Run API
    * Enable Cloud Build
    * Enable Container Register
    * Enable Cloud SQL Admin API
    

* **Authorization**:
  * **CodeTestBack** -> **IAM & Admin** -> **Service Accounts** -> **Copy the service account**
  * **CodeTestBDD** -> **IAM & Admin** -> **IAM page** -> **ADD** -> **Past the service account and give the Cloud SQL Client Role**

## Running locally

To run this application locally, download and install the `cloud_sql_proxy` by
following the instructions [here](https://cloud.google.com/sql/docs/postgres/sql-proxy#install).

Instructions are provided below for using the proxy with a TCP connection or a Unix Domain Socket.
On Linux or Mac OS you can use either option, but on Windows the proxy currently requires a TCP
connection.

### Launch proxy with TCP

To run the sample locally with a TCP connection, set environment variables and launch the proxy as
shown below.

#### Linux / Mac OS
Use these terminal commands to initialize environment variables:

Firstly, you must download the key.json config file from the web base GCP console : 

**CodeTestBack** -> **IAM & Admin** -> **Service Accounts**-> **Check the service account** -> **Actions** -> **Manage Keys** -> **Generate new key and download it as Json format**

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service/account/key.json
export DB_HOST='127.0.0.1:5432'
export DB_USER='postgres'
export DB_PASS='CodeWorks'
export DB_NAME='postgres'
```
Note: Saving credentials in environment variables is convenient, but not secure - consider a more
secure solution such as [Secret Manager](https://cloud.google.com/secret-manager/docs/overview) to
help keep secrets safe.

Then use this command to launch the proxy in the background:
```bash
./cloud_sql_proxy -instances=codetestbdd:europe-west1:codetest-bdd-1=tcp:5432 -credential_file=\$GOOGLE_APPLICATION_CREDENTIALS &
```

### Configure your local Postgres Client using the Cloud SQL PROXY

    Host : localhost
    Port : 5432
    User : Postgres
    Pass : CodeWorks
    Database : postgres

### Install Pipenv Globally
1. Open Terminal in (Applications/Utilities/Terminal) and upgrade pip:
   ```bash
   python3.8 -m pip install pip --upgrade
   ```
   Another option to upgrade, is:
   
    ```bash
   pip3 install pip --upgrade
   ```
   
2. Install Pipenv: 
   ```bash
   python3.8 -m pip install pipenv
   ```
   Another option to upgade, is : 
   
   ```bash
   pip3 install pipenv --upgrade
   ```
3. Verify Pipenv:
    ```bash   
    pipenv
   ```
   
### Testing the application

```bash
virtualenv --python python3 env

source env/bin/activate

pip install -r requirements.txt
`````

Finally, start the application:
```bash
strawberry server app
```

Navigate towards `http://127.0.0.1:8000` or `http://localhost:8000` to verify your application is running correctly.



