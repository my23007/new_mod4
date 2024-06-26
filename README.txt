Music App
This Python script implements a simple music app with CRUD functionality for managing artifacts (songs). It also includes automated testing tools (Flake8 for linting and Bandit for security testing) to ensure code quality and security. In this context, Heiland et al (2019) used Flake8 and Bandit as part of the software assurance to evaluate python code. Furthermore, Mohialdenq et al (2023) argue that flake8 can scan the python code for possible bugs and issues related to style and format by utilizing pre-established criteria
Moreover, it employs SQLite for database management, hashlib for checksum computation, and basic encryption techniques. The main classes include Database, MusicApp, User, and Administrator, each serving distinct roles in the application. Additionally, the script includes automated testing functions to ensure the integrity and security of the codebase.

Features
User Authentication: Users can authenticate with a username and password.
CRUD Operations: Users can create, read, update, and delete artifacts (songs).
Encryption: Content of artifacts is encrypted for security.
Automated Testing: Flake8 is used for linting to enforce coding standards, and Bandit is used for security testing to detect common security issues.
Bandit output codes are available online (Code Quality, 2021) 

Modules and Libraries
subprocess: Used for running system commands (flake8 and bandit) to check code quality and security.
hashlib: Provides secure hash functions for checksum generation.
datetime: Handles dates and times for artifact creation and modification.
getpass: Securely prompts the user for passwords.
sqlite3: Interacts with the SQLite database.
flake8 to check for style and syntax issues.
bandit to check for security issues.

Structure and Components
-Database Management (Database class)

Initialization: The __init__ method establishes a connection to an SQLite database. If the specified database does not exist, it creates one. The create_tables method sets up two tables (users and artifacts) with the necessary schema.
Database Operations: This class provides methods to execute queries (execute_query) and fetch results (fetch_one, fetch_all).

-Music Management (MusicApp class)

Initialization: The class initializes with a reference to the Database instance and maintains a set of authenticated users.
User Authentication: The authenticate_user and is_authenticated methods manage user authentication.
Artifact Management: Methods like generate_artifact_id, encrypt_content, artifact_exists, store_artifact, update_artifact, and delete_artifact handle the creation, update, and deletion of song artifacts.

-User Management (User and Administrator classes)

Base User Class: The User class contains methods for adding, updating, and deleting artifacts, with checks for user authentication.
Administrator Class: Inherits from User and restricts certain operations (like adding and deleting artifacts) to the admin user.

-Testing and Command-Line Interaction (run_tests function and main execution block)

Code Analysis Tools: The run_tests function runs code quality and security tools (Flake8 and Bandit).
Artifact Testing: This function also tests the creation of artifacts with checksum and encryption verification.
Command-Line Interaction: The main block gathers user input for creating and deleting artifacts through an admin account.

Usage
Prerequisites
Python 3.x installed on your system
pip package manager

Installation
Clone the repository:
myounes@myouneslap MINGW64 ~
$ git clone https://github.com/my23007/new_mod4.git
Cloning into 'Module4'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

Navigate to the project directory:
cd new_mod4/
Install dependencies:
pip install flake8
pip install bandit

Running the Application
To run the application and execute the automated tests, use the following command:
python new_mod4.py

This will run the Flake8 linter and Bandit security testing, followed by executing the main functionality of the music app. Below is a sample output

myounes@myouneslap MINGW64 ~/new_mod4 (main)
$ python new_mod4.py
Running Flake8:
new_mod4.py:13:1: E302 expected 2 blank lines, found 1
new_mod4.py:18:1: W293 blank line contains whitespace
new_mod4.py:41:80: E501 line too long (111 > 79 characters)
new_mod4.py:60:1: E302 expected 2 blank lines, found 1
new_mod4.py:64:1: W293 blank line contains whitespace
new_mod4.py:66:80: E501 line too long (121 > 79 characters)
new_mod4.py:72:1: W293 blank line contains whitespace
new_mod4.py:78:1: W293 blank line contains whitespace
new_mod4.py:82:1: W293 blank line contains whitespace
new_mod4.py:85:1: W293 blank line contains whitespace
new_mod4.py:87:80: E501 line too long (105 > 79 characters)
new_mod4.py:89:1: W293 blank line contains whitespace
new_mod4.py:90:80: E501 line too long (110 > 79 characters)
new_mod4.py:92:80: E501 line too long (115 > 79 characters)
new_mod4.py:94:80: E501 line too long (95 > 79 characters)
new_mod4.py:95:1: W293 blank line contains whitespace
new_mod4.py:96:80: E501 line too long (96 > 79 characters)
new_mod4.py:99:80: E501 line too long (87 > 79 characters)
new_mod4.py:101:80: E501 line too long (80 > 79 characters)
new_mod4.py:102:1: W293 blank line contains whitespace
new_mod4.py:104:80: E501 line too long (98 > 79 characters)
new_mod4.py:106:1: E302 expected 2 blank lines, found 1
new_mod4.py:110:1: W293 blank line contains whitespace
new_mod4.py:115:1: W293 blank line contains whitespace
new_mod4.py:118:1: W293 blank line contains whitespace
new_mod4.py:121:1: W293 blank line contains whitespace
new_mod4.py:122:80: E501 line too long (123 > 79 characters)
new_mod4.py:124:1: W293 blank line contains whitespace
new_mod4.py:129:1: W293 blank line contains whitespace
new_mod4.py:133:1: W293 blank line contains whitespace
new_mod4.py:137:1: W293 blank line contains whitespace
new_mod4.py:138:80: E501 line too long (109 > 79 characters)
new_mod4.py:140:1: W293 blank line contains whitespace
new_mod4.py:145:1: W293 blank line contains whitespace
new_mod4.py:149:1: W293 blank line contains whitespace
new_mod4.py:153:1: E302 expected 2 blank lines, found 1
new_mod4.py:156:1: W293 blank line contains whitespace
new_mod4.py:161:1: W293 blank line contains whitespace
new_mod4.py:163:1: W293 blank line contains whitespace
new_mod4.py:168:1: W293 blank line contains whitespace
new_mod4.py:171:1: E302 expected 2 blank lines, found 1
new_mod4.py:174:80: E501 line too long (130 > 79 characters)
new_mod4.py:179:1: W293 blank line contains whitespace
new_mod4.py:181:80: E501 line too long (136 > 79 characters)
new_mod4.py:186:1: W293 blank line contains whitespace
new_mod4.py:191:1: W293 blank line contains whitespace
new_mod4.py:203:80: E501 line too long (104 > 79 characters)
new_mod4.py:206:80: E501 line too long (85 > 79 characters)
new_mod4.py:209:80: E501 line too long (90 > 79 characters)
new_mod4.py:214:80: E501 line too long (94 > 79 characters)
new_mod4.py:219:1: W293 blank line contains whitespace
new_mod4.py:223:1: E305 expected 2 blank lines after class or function definition, found 1
new_mod4.py:225:1: W293 blank line contains whitespace
new_mod4.py:228:1: W293 blank line contains whitespace
new_mod4.py:233:1: W293 blank line contains whitespace
new_mod4.py:235:1: W293 blank line contains whitespace
new_mod4.py:237:1: W293 blank line contains whitespace
new_mod4.py:238:80: E501 line too long (82 > 79 characters)
new_mod4.py:246:1: W391 blank line at end of file


Running Bandit:
Run started:2024-05-18 09:24:53.777719

Test results:
>> Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/blacklists/blacklist_imports.html#b404-import-subprocess
   Location: .\new_mod4.py:7:0
6	
7	import subprocess
8	import hashlib

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: .\new_mod4.py:174:25
173	        print("Running Flake8:")
174	        flake8_process = subprocess.Popen(["flake8", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
175	        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: .\new_mod4.py:174:25
173	        print("Running Flake8:")
174	        flake8_process = subprocess.Popen(["flake8", "new_mod4.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
175	        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B607:start_process_with_partial_path] Starting a process with a partial executable path
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b607_start_process_with_partial_path.html
   Location: .\new_mod4.py:181:25
180	        print("\nRunning Bandit:")
181	        bandit_process = subprocess.Popen(["bandit", "-r", "new_mod4.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
182	        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)

--------------------------------------------------
>> Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
   Severity: Low   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.7.8/plugins/b603_subprocess_without_shell_equals_true.html
   Location: .\new_mod4.py:181:25
180	        print("\nRunning Bandit:")
181	        bandit_process = subprocess.Popen(["bandit", "-r", "mod4_assign.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
182	        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)

--------------------------------------------------

Code scanned:
	Total lines of code: 182
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 5
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 5
Files skipped (0):

[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.9.7


Testing Artifact Creation with Checksum and Encryption:
Artifact added successfully.
Artifact 9 exists.
Stored artifact: (9, 'Test Song', 'Test Artist', '.tnetnoc tset a si sihT', '2024-05-18T12:24:53.840618', '2024-05-18T12:24:53.840618', 'f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db')
Expected checksum: f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db
Stored checksum: f74d46f5c58d6d0fac6e1dd341dc44e8881cc40fc2c08daec80ec75b902a42db
Checksum verification passed: True
Expected encrypted content: .tnetnoc tset a si sihT
Stored encrypted content: .tnetnoc tset a si sihT
Encryption verification passed: True
Enter username: admin
Enter a password: ········
Enter song title: test
Enter artist name: test
Artifact added successfully.
Enter the ID of the artifact to delete: 123
Artifact does not exist.


Limitations:
This is a deviation from the original design proposed in the first assignment, I used my own UML class diagram for simplicity and ease in coding. The original one encompasses many classes and attributes and will complicate the python code, hence I used my simplified version as this is for educational purpose. Moreover, The encryption method used is reverse ciphering which is considered as a weak approach and an adversary can easily find out the message content (tutorialspoint, 2024)

References:

Code Quality (2021). Bandit Low Level Issues. Available from: https://docs.embold.io/bandit-low-level-issues/ [Accessed 20 May. 2024].
Heiland, R., Rynge, M., Vahi, K., Deelman, E. and Welch, V., 2019. A Guide for Software Assurance for SWIP.
Mohialdenq, Y.M., Hussien, N.M., Baker, E.J., Joshi, K. and Mohialdenq, Y.M., 2023. A Comparative Analysis of Python Code-Line Bug-Finding Methods.
tutorialspoint (2024).Cryptography with Python Tutorial. Available from: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_reverse_cipher.htm [Accessed 02 Jun. 2024].