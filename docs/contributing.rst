Contributing
============

Environment Setup
-----------------

First, you'll need a code editor. I would strongly recommend `VSCode`_.

Install the latest version of `Python`_ and `git`_, use your terminal/command
prompt to navigate to the directory you would like to install this project to,
then run the following commands:

.. code-block:: bash

        # Clone and enter repository.
        git clone https://github.com/ReflexCreations/Nexus.git
        cd nexus
        # Get the build/environment manager.
        pip install poetry
        # Set up virtual environment and install reflex-nexus as package.
        poetry install

You're all set up! You can now use `Poetry`_ to run the application scripts.

.. code-block:: bash

        # Build the executable.
        poetry run build
        # Build the documentation HTML.
        poetry run docs
        # Lint the project.
        poetry run lint
        # Test the project.
        poetry run test


To synchronise your code editor with the virtual environment that Poetry
creates, you can use `poetry env info -p`, copy the path, and supply that path
to your code editor for the Python interpreter location.

.. _git: https://git-scm.com/downloads/
.. _Poetry: https://pypi.org/project/poetry/
.. _Python: https://python.org/downloads/
.. _VSCode: https://code.visualstudio.com/


Documenting Hardware Design
---------------------------

If you've designed a dance pad, we'd love to feature it here! Checkout the
`Hardware` tab in the side-panel, and find the sections that you wish to
contribute to, for an intuitive understanding of how to structure your
documentation.

All documentation is found in the `docs` sub-directory of the project root. 
You are welcome to upload any images to the appropriate sub-directory of the
`assets` folder of the project. You may also link to any resources documenting
your hardware design on external platforms.

You can then follow the same steps as in `Contributing to the Software
Package`, but ignoring the rules on `Linting and Testing`.


Contributing to the Software Package
------------------------------------

You will need to have a `Github` account. You are welcome to browse the
`Issues`_ tracker for any problems that take your interest. However, all
contribution is welcome. If you choose to undertake your own task, you can
follow the same instructions as below, but please start by creating an issue
that describes the work you're looking to undertake. For example:

- **Documenting a dance pad design** - Create an issue with a `Pad
  Integration` tag, and give it the name of your pad.
- **Creating a software feature** - Create an issue with a `Application`
  tag, and give it a name descriptive of the feature.

A maintainer may prompt you to make changes if there's any doubt that your
work can be merged into the project.

Assign the chosen job to yourself, and create a branch stemming from the
appropriate branch. On your own local repository, you can then do:

.. code-block:: bash

        git pull
        git checkout your-branch-name

Linting and Testing
~~~~~~~~~~~~~~~~~~~

It's important that your code passes the linting and testing requirements of
the project. Linting information can be found in the `tool.ruff` section of
the `pyproject.toml` file. For tests, we request that you ensure full coverage
of your code with unit tests.

Submitting your changes
~~~~~~~~~~~~~~~~~~~~~~~

Whenever you are finished, you can do:

.. code-block:: bash

        git push

and under the information on the `Github` website, you can do a `Merge
request` to request that your code be merged into the branch that yours
stemmed from. CI tasks  will automatically run. If they fail, or you spot a
separate issue, don't worry! You can still make changes, but you may wish to
leave a comment stating your intention to keep working on the issue. You can
`git push` whenever you have made your updates. When the CI tasks all pass,
your code will be reviewed. After it's accepted, it will be merged, and your
branch deleted.

.. _Issues: https://github.com/ReflexCreations/Nexus/issues


Project Overview
~~~~~~~~~~~~~~~~

The project is best understood in terms of its directory structure.

In the top-level, you will find files specific to managing the project.

**assets** - These are images and other media used within the application and
documentation.

**docs** - The source documentation itself. Find stuff about dance pad
hardware design here, along with API and implementation details of the
software package.

**src** - Source code folder for the software package.

**src/app** - This is the application itself. It describes how all devices,
drivers, widgets and utilities interact with one another, and creates a GUI
environment for managing them.

**src/devices** - Devices are `.json` files that describe a dance pad
implementation. They allow a dance pad's driver interface to be exposed to
RE:Flex Nexus and imported as required.

**src/drivers** - Drivers are Python/C classes that create a daemon process
for a given dance pad. The aforementioned devices implement a driver to talk
to physical hardware.

**src/utilities** - Utilities are Python classes that create some useful
feature for a dance pad. You can think of them as the logic of a given
`widget`.

**src/widgets** - These are the graphical representations of a given `utility`
that provide the user some visual information, or input mechanisms for it.

**tests** - A mirror of the `src` directory, in which unit tests are run.


FAQ
---

**Why Poetry, and not a tool like Tox?** - As RE:Flex Nexus is centered around
a standalone executable, it's important to make sure that dependencies are
the same across machines in development of the project. The `poetry.lock` file
helps to ensure that remains the case. Using Poetry as a single tool to
handle the packaging, dependency management, virtual environment management,
and the script runner helps us meet the reproducibility requirement.

**Why are the documentation and software managed in one location?** - This
should, in theory, make the project easier to maintain. The goal of RE:Flex
Nexus is to make convenient tools available as a community standard
for open source dance pad development. Therefore, if the documentation is
tightly coupled to the software implementation, the two should hopefully
stay in sync. Ultimately, without dance pads, there's no need for software,
without software, there's no easy way to unify open source hardware designs.
Centralised documentation and software compliance helps immortalise any
hardware design that adopts the standard.

**What does my dance pad design need to do to be documented?** - You will need
to ensure that the dance pad is integrated with RE:Flex Nexus. Submit your
`.json` configuration file along with any associated documentation that fits
into the repository structure, and it will be accepted. 

**Does my design need to be open source?** - No. RE:Flex Nexus is under the
MIT license. You're encouraged to maintain that standard, too, but if you
are trying to make money and keep your design private, that's fine, too. We
will accept any documentation for a dance pad that implements this software.
