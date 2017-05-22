===================== 
AWS Profile Switcher 
=====================

awsps is a command-line tool used to switch between different AWS profiles.

Installation
-------------
Install awsps using pip:

.. code-block:: bash

  $ pip install awsps 
  # or from git
  $ pip install git+https://github.com/Deepakkothandan/awsps


Usage
-----

List available profiles:

.. code-block:: bash

  $ awsps -ls
  Available Profiles:
  1) profile1
  2) profile2
  3) profile3
  4) default_awsps (A copy of your default profile)

View current profile:

.. code-block:: bash

  $ awsps -cp
  The current AWS profile is default_awsps

Switch profile:

.. code-block:: bash

  $ awsps -sp
  1) profile1
  2) profile1
  3) profile1
  4) default_awsps

  Enter profile to select: 1

  Profile switched to profile1

Help:

.. code-block:: bash

  $ awsps -h 
  usage: awsps [-h] [-ls] [-cp] [-sp]

  AWS Profile Switcher

  optional arguments:
    -h, --help      show this help message and exit
    -ls, --list     List available Profiles
    -cp, --current  Get Current Profile
    -sp, --switch   Switch AWS Profile

