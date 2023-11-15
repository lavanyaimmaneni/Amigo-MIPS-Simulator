
# Amigo Mips Simulator

This is a GUI based Simulator used to edit , create a new , simulate the MIPS instructions set. This shows the changes in the registers that are effected by the given instructions and calculates the time taken to execute the instructions and no of stalls that are created by the following set of instructions.It has a feature to turn on or off the data forwarding in the pipeline and it calculates the cache hit and miss ratio for a single or two level cache.



## Assumptions
- All the stages in the pipeline will take only 1 unit of time
- The pipeline is 5 staged that is it has stages ```Instruction Fetch``` , ```Instruction Decode``` , ```Execute``` , ```Memory``` , ```Writeback```
## Steps to run
- First download the code from the repository
- Make sure that the computer has Python installed, if not install Python
- Download the Tkinter library
- Go to the Phase-3 folder and run ```App.py``` file
