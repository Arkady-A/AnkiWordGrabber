# Anki Word Grabber
Script that helps collect word definitions for anki. 

In current state application collects data from one dictionary and converts it in **html** code that can be used in anki (`ctrl+shift+x` in add new card menu)

## How to run 
1. **Pull** this repository (`git pull *repository_url*`)
2. **Install** all dependencies (`pip install -r requirements.txt`)
3. **Create** *input.csv* file or **specify** location of *csv* file in *start.py* file (linux: `touch input.csv`) (look in test_input.csv for an example)
4. **Run** the script (`python start.py`)
## Where the result
If you haven't changed output_file_path parameter in start.py you should see in you directory a file called output.txt with html code. Each word definition should be separated by two lines of "*=*" symbol. 

## Example
![Example result 1](html_ouput_example1.png)