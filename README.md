# Allen-Bradley-PLC-Module-Parser
This script will analyze an *.L5X file and output an *.CSV file documenting firmware for all Ethernet-connected device modules as well as the host controller.

1. Install python v3.8 on your machine
2. Gather XML files.
	2a. The VFD Scraper Tool will read all files in its local directory as well as all subfolders.
	2b. You can drop L5X files, or folders containing L5X files into the local directory and it will read all of them.
3. Place Main.py into the common folder containing all the L5X files you want to search.
4. Double Click Main.py to run program.
	4a. Program may take 15-20 seconds to run for extensive amount of files.
5. A file explorer will pop up, prompting you to save the file.
	5a. Locate a folder where you would like to save the file, ensure to give it a file name.
	5b. The VFD Scraper tool only allows files to be saved in the .CSV format, and the title defaults to "PLC_Modules.csv".
6. You are done.




Created by:
Joseph Riley | Systems Engineer
Automation Engineering
