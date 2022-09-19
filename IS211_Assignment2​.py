import urllibz
import argparse
import logging
def downloadDatacurl) :
"4-function to download the data from given url
using urllib2
Parametersi
url : str

URL string
Returns:
The caller (object of urllib2)
return urllibz.ur lopen(url)
def processData(infile):
tion to process the data of the giver
to a dictionary and r
object returned by downloadData()
function.

A dictionary having persons id as key and tuple
of name and datetime object as its value.
* dictionary to store processed data
processed_cata - {}
csy_reader = csv. reader(infile)

next (esv_reader )
iterate through the reader coject
* try except block to get rid of invalid data

get person id
* get person name
get object of datetine object (it will raise an error if birthday
p_birth_date " datetime. datetime.
, ""d/n/xy" )
processed_ data [p_id) - ( p name, p_birth date)
a into the dictionary

to log error if any exception raised while processing the data
prepare error message to los
open the error log file at ERROR leve
Byget fogger config filename "error , log". level-logging. ERROR)
write the error message ('assignment2")
logger -error (error_#5g)

* return the dictionary containing processed data
return processed_data
displayPerson(pid, dict datari
action to get name of birthday of the
Paraneters:
pid : int
person for whom details should be returned.
perInteger that represents the id
Dictionary conataining data of all person
returned by the processData() function.

Prints:
and birth date in the speck awaya person's name
... Person a is <names with a birthday of <dates.
check if person id exits in the dict_data
pid in dict data: # it exists

* get date in format "YYY-UM-DD
bdate = datetime. datetime. strftime(dict_data[pid] [1], ">Y-sn-"d")
" then, print the details
print("Person #() is () with a birthday of ().". format(pid, name, bdate))
If person id not found the dict_data
print("No user found with that id.")

def main( ):
""Driver function to use the defined
Wunctions to drive this program.
downloaded_data = None

" create an object of ArgumentParser for parsing command line arguments
parser = argparse.ArgumentParse
# add arguments to the object
surent -curl" . required-True, help-"Provide the cav file's URL. ")
args = parser .parse_args()

try to download the file using the url passed as arguments
downloaded_data - do
nloadData(args. url)
if failed to download the file
print("Error occured while downloading the file !!!")

process the data returned by the downloadData( ) function
process_dict = processData(downloaded_data)
run loop until enter enter 0 or negative to exit
ask user to enter id to search
pid = int(input("Enter ID to lookup: ")>

break
. otherwise, display the person data
"displayPerson(pid, process_dict)
"_main_"
main( )
