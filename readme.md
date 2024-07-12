# How to initialize the MkDocs environment and build help files

- [How to initialize the MkDocs environment and build help files](#how-to-initialize-the-mkdocs-environment-and-build-help-files)
  - [Initialize the environment](#initialize-the-environment)
  - [Build help](#build-help)
  - [Build PDF manual](#build-pdf-manual)
  - [Serve live help site](#serve-live-help-site)
  - [Uninstallation scripts](#uninstallation-scripts)

## Initialize the environment

1. Install Python:

   * Change dir to `Help` under the solution root directory.

   * Run:

        ```
        ./install/installpy.ps1
        ```
        or
        ```
        . ./install/install.sh
        ```

        * This script downloads and installs the latest Python from python.org (including the `pip` package manager).
        * `install.sh` also installs GTK3 framework used for PDF output.
        * In Windows, UAC request may pop-up during the silent installation.

!!! note
    Python is not used in runtime, it is only used to build the static HTML site from the source .MD files.

1. Initialize Python virtual environment, an install MkDocs with dependencies:

    ```shell
    ./install/deploymkdocs.ps1
    ```

    or

    ```shell
    . ./install/deploy.sh
    ```

## Build help

1. Run:

    ```shell
    ./buildhelp.ps1
    ```

    or

    ```shell
    . ./buildhelp.sh </Help/directory/path>
    ```

   * This script runs `buildhelp.py` in the virtual environment and builds languages help to `compiled_help`.

   * The language list is set on the line 15 in `buildhelp.py`:

        `LANGUAGE_LIST = ["en", "ru"]`

2. You should see the newly compiled help subdirectories in the `compiled_help` directory:
   * en
   * ru

!!! note
    * `buildhelp.py` will not run on it's own, instead execute:

        ```shell
        ./buildhelp.ps1
        ```

        or

        ```shell
        . ./buildhelp.sh </Help/directory/path>
        ```

    * The `buildhelp.ps1` script is also be executed with:
        ```shell
        npm run buildhelp
        ```
        and
        ```shell
        npm run buil
        ```
## Build PDF manual

1. Install GTK3: `installgtk3.ps1` or `apt install -y libgtk-3-dev`. In Windows, For GTK3 to work properly the PATH variable might need to be set (and put on top of the PATH list) to its installation directory.
2. Build the PDF manual:

    ```shell
    mkdocs build -f mkdocs_ru_pdf.yml
    ```

3. Build and run the product normally and see the Help system in action.

    * Change dir to `Web` within the solution root directory.
    * Execute `npm run build` or `buildhelp.sh </Help/directory/path>`
    * Launch the product instance.
    * You should see the Help question sign to the left of the search button in the top bar:
        * The CSS is pulled dynamically from the current theme.
        * The help is displayed in the current CBAP language.
        * The help is context dependent: it shows the topic for the current module.

            * See the help button and context resolver code:
            `js\modules\shared\view\help\HelpPathMappingService.js`
            `js\modules\shared\view\help\HelpButtonView.js`
            `js\modules\shared\view\NavigationToolbarView.js` lines 10, 11, 82, 169

## Serve live help site

You can view the live MkDocs site without building it or compiling the product. The live server watches for changes in the `docs` folder and update accordingly.

1. Serve Russian docs locally at <http://127.0.0.1:8000>

   * Change dir to `Help` under the solution root directory.

   * Run:
        ```
        ./install/deploymkdocs.ps1
        ```
        or
        ```
        . ./install/deploy.sh
        ```
       * This script deploys the Python virtual environment in `Help/venv` with MKDocs and its dependencies listed in the `requirements.txt` file. It does not build the help files.

   * Run:

        ```
        mkdocs serve
        ```
        or  
        ```
        py -m mkdocs serve
        ```

   * For English version run:

       ```
       mkdocs serve -f mkdocs_en_local.yml
       ```

**NOTE**
* The help is not build by, it is only served locally to <http://127.0.0.1:8000>
* The server watches for edits in the `Help\docs` directory and updates the help on the fly. Any edits you make in the `docs` directory will be immediately reflected at <http://127.0.0.1:8000>
* _The styling at <http://127.0.0.1:8000> **is different from actual product help as the local CSS is incomplete**.
* Within the CBAP the help uses CBAP's CSS dynamically._
* _The CSS is not dynamically pulled from the CBAP to <http://127.0.0.1:8000>_

## Uninstallation scripts

* `install\uninstallmkdocs.ps1` — uninstalls installs all MKDocs dependencies listed in the `requirements.txt` config file.

* `install\uninstallpy.ps1` — silently uninstalls Python, runs a single command: `.\python_latest.exe /uninstall /quiet`

**The help is powered by the very popular and well-maintained MkDocs framework:**
<https://squidfunk.github.io/mkdocs-material/>
<https://github.com/squidfunk/mkdocs-material>
<https://www.mkdocs.org/>

This framework is trusted by Atlassian, Mozilla, Google, Microsoft, Adruino, etc...
