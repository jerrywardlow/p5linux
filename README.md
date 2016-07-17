# Project 5 - Linux Server Configuration
### Udacity - Full Stack - Project 5 - Linux Server Configuration

By Jerry Wardlow for the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

### About

This project involves the configuration and securing of a baseline Ubuntu 14.04.3 LTS
Amazon Web Services EC2 instance. This instance is used to host the Flask application
[Project 3 - Item Catalog](https://github.com/jerrywardlow/p3catalog) using
the [Apache HTTP Server](https://httpd.apache.org/) and [mod_wsgi](https://code.google.com/p/modwsgi/). Various security measures are
implemented including the use of [UncomplicatedFirewall](https://wiki.ubuntu.com/UncomplicatedFirewall) to limit
unwanted access, as well as forced key-based SSH login and inability to SSH as
the root user.

### In This Repository

The project is a modification of [Project 3 - Item Catalog](https://github.com/jerrywardlow/p3catalog). The addition of the
`wsgi-scripts` directory includes two files, `app.wsgi` for running our Flask
application, and `mod-wsgi.conf` to ease configuration of mod_wsgi. Further
information about the Flask app can be found at it's project page.

### Using This Project

**Prerequisites**

* Amazon EC2 Instance with Ubuntu 14.04.3 LTS
* The files contained in this repository

**Configuring This Project**

The initial configuration of an EC2 instance is outside the scope of this project,
though the tutorial at [Getting Started with Amazon EC2 Linux Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
can quickly get our instance running. Upon successful creation and installation
of Ubuntu, we can begin to configure our machine.

In addition, the configuration of OAuth2 and Imgur API is covered in the project page for [Project 3 - Item Catalog](https://github.com/jerrywardlow/p3catalog).

From a terminal, we can SSH into our instance using our generated keys.

`ssh -i ~/.ssh/{YOUR_KEY_NAME}.rsa root@{EC2 IP ADDRESS}`

**User Control and SSH Configuration**

Next, per project guidelines, we can add a new user `grader` and grant them sudo
access.

`adduser grader`

Following the prompts, we now have a new user. Adding sudo capabilities can be done
with `visudo` and adding `grader ALL=(ALL:ALL) ALL` under the heading `# User privilege specification`.

Now that we have our new user, we can copy our SSH public key to allow us to SSH
as this user.

`mkdir /home/grader/.ssh`
`cat ~/.ssh/authorized_keys >> /home/grader/.ssh/authorized_keys`

Now we can change our SSH port to 2200 for obfuscation, rewriting the configuration
from Port 22 in `/etc/ssh/sshd_config`. After this, we restart the SSH service with `service ssh restart` and can log out of root and back in as `grader` to complete the configuration. For additional security, we can also disable SSH access as the root user by changing the sshd_config to `PermitRootLogin no`.

**UncomplicatedFirewall**

Enabling and configuring UncomplicatedFirewall is accomplished via `ufw default deny incoming` to close all incoming ports, then `ufw allow 2200/tcp` `ufw allow 80/tcp` and `ufw allow 123/tcp` per project guidelines. Finally, `ufw enable` to get UncomplicatedFirewall up and running.

**Software Package Installation**

The next step before installation of our software packages is to update and upgrade
the already installed packages with `apt-get update` and `apt-get upgrade`. Now we can `apt-get install` `apache2`, `libapache2-mod-wsgi`, `postgresql`, `psycopg2`, `python-pip`, and `git`.

Now that Git is installed, we can `cd /var/www/` and `git clone https://github.com/jerrywardlow/p5linux.git` to clone the repository into the correct directory. Using PIP, we can install the necessary Python packages via `pip install -r /var/www/p5linux/requirements.txt`.

**Configuring Apache and mod_wsgi**

Configuring mod_wsgi is made easy by copying our pre-configured `mod-wsgi.conf` file in place of the default configuration.

`cp /var/www/p5linux/wsgi-scripts/mod-wsgi.conf /etc/apache2/sites-enabled/000-default.conf`

Now that our configuration is updated, we can `apache2ctl restart` to reload the HTTP server.

Bear with me, we're almost there!

**Database Configuration**

Configuring PostgreSQL is made simple with a few quick commands as the `postgres` user, using `su postgres` to switch over. Running the command `psql -c \"CREATE USER flaskapp with password 'flaskypassy';\"` will generate the new user with limited privileges, and the appropriate credentials for our pre-configured Flask app. Next we need to `createdb itemcatalog` to generate the database for the Flask app, and can run `python /var/www/p5linux/populator.py` to load our database with sample data.

**Viewing the Completed Project**

Now that we have successfully configured our web server, we can navigate to the EC2 IP address in a web browser to see our Flask app being hosted.
