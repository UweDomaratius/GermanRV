import shutil
import subprocess
import glob
import os
import sys
from pathlib import Path
from datetime import datetime
from constants import constants

inputs = [
    "src/german_rvs.pnml",
    "src/recolour.pnml",
]

buses = glob.glob("src/bus/*.pnml")
inputs.extend(buses)
trams = glob.glob("src/tram/*.pnml")
inputs.extend(trams)
trucks = glob.glob("src/truck/*.pnml")
inputs.extend(trucks)

# clean the build dir, we'll recreate all files
shutil.rmtree('build',ignore_errors=True)
Path("build").mkdir()

# create custom tags including version + time/date
# on github the version number is passed in via command line, 
# if no such argument is given, a placeholder is used
now = datetime.now()
dt = now.strftime("%Y-%m-%d %H:%M:%S")
version = "local build " + dt
if len(sys.argv) > 1:
    version = sys.argv[1]
version = "VERSION:"+version

with open('custom_tags.txt', 'w') as file:
  file.write(version)
  file.write("\nTITLE: German Road Vehicles")

# create the actual nml file by concatenating all inputs
with open('build/german_rvs.nml','wb') as output:
    for f in inputs:
        with open (f, 'rb') as fd:
            shutil.copyfileobj(fd, output)
            output.write(b"\n")
            

# replace the defined constants
# Read in the file
with open('build/german_rvs.nml', 'r') as file:
  filedata = file.read()

# Replace the target string
for key,value in constants.items():
    filedata = filedata.replace(key, value)

# Write the file out again
with open('build/german_rvs.nml', 'w') as file:
  file.write(filedata)
  
subprocess.run(["cat"],"build/german_rvs.nml"])

# call nmlc to create the grf output
subprocess.run(["nmlc", "-c", "--grf", "build/german_rvs.grf","build/german_rvs.nml"])

#shutil.copyfile('custom_tags.orig', 'custom_tags.txt')
dt = now.strftime("%Y-%m-%d_%H-%M-%S")
grfdate="build/german_rvs_"+dt+".grf"
shutil.copyfile('build/german_rvs.grf', grfdate)
os.remove("custom_tags.txt")