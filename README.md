#Ajax Crawler

Clone the repository

	https://github.com/dip-kush/Ajax-Crawler/

Use the requirement file to install the dependency file

	pip install -r requirements.txt

### Instruction for using the sample_web_application

Copy the sample_web_application and paste in the xampp server 

and import the sample_web_application/forum.sql into the database

###Usage

- -l, "Path to python login script"
- -u, "Login Page Url"
- -f, "Path to Form Values Script"
- -s, "Starting Page Url"
- -b, "Black List Urls"
- -t, "Give the time in seconds"

###Sample Command 

python ExtractDom.py -l login_script.html -u path_to_sample_application/login.php -f form_values.html

Edit the sample script to run

./run.sh
./script.sh



