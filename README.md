# C-BIBLE

A command Line interface Bible. 
Defaults to KJV version.

Project Stack
------------------

-   Python
-   Click


Installation
------------

1. Clone the repository: First, you will need to clone the Homemix repository to your local machine. This can be done using the following command in your terminal or command prompt:
    ```bash
    git clone https://github.com/vbello-tech/C-BIBLE.git
    ```
2. Create a virtual environment: It is recommended to work with a virtual environment to keep the dependencies for this project separate from other projects on your system. To create a virtual environment, run the following command:
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment by running the following command:
    ```bash
    source venv/bin/activate (for Mac or Linux)
    ```

    ```bash
    source venv\Scripts\activate (for Windows)
    ```
3. Install dependencies: Next, you will need to install the dependencies required for the project. These dependencies are listed in the requirements.txt file. To install them, run the following command:
    ```bash
    pip install -r requirements.txt
    ```
   
Commands
---------------

1. Welcome message.
    ```bash
    python bible.py cbible
    ```

2. Request a bible passage.
    ```bash
    python bible.py request
    ```
   This prompts you to type in the Book, chapter and verse you want.

3. Find a bible passage.
    ```bash
    python bible.py find job 3 16
    ```
   ```bash
    python bible.py find job 3 16-20
    ```
   ```bash
    python bible.py find job 3
    ```
   
4. Find a bible passage for specific version.
    ```bash
    python bible.py find -v ESV job 3 16
    ```
   ```bash
    python bible.py find -v ESV job 3 16-20
    ```
   ```bash
    python bible.py find -v ESV job 3
    ```

Available Bible Versions
---------------
1. KJV 
2. ESV
3. ISV
4. AKJV
5. NIV
6. NKJV
7. NLT
8. NRSV


Todo
------------
- Word search.
- Concordance.
- Crossreference.
