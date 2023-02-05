## Knowledge Graph

### Installation

(Performed on Windows 11 Pro - Build Number 22000.1516)

-	Go to Neo4j website (https://neo4j.com/download/?ref=get-started-dropdown-cta) and click on "Download".
-	Fill in the form with the requested information and click on "Download Desktop".
-	The installation package is being downloaded, and the activation key (which might be requested later) can be retrieved on the refreshed webpage.
-	Once the package has been downloaded, run it (preferably with administrator privileges).
-	Choose the option to install Neo4j for all users and click on "Next" (grant administrator privileges when the popup occurs).
-	Choose the default one ('C:\Program Files\Neo4j Desktop') to avoid any potential inconvenience later and click on "Install".
-	Once the installation has been completed, close the package and open "Neo4j Desktop".

### Environment Initialization

- Open Neo4j and navigate to the "Projects" tab using the left-hand side navigation menu.
- Click on "New" < "Create project" to create a new empty project.
- Select the newly created project in the list below.
- (For a better management of the projects, click on the main title to rename it)
- On the right-hand side, click on "Add" < "Local DBMS" to create a new empty database.
- Assign a name and a password to the DBMS before clicking on "Create".
- Wait for 5-10 seconds for the DBMS to be created before clicking on "Start".
- Wait for 10-20 seconds for the DBMS to be started.
- Once the DBMS has started, click on "Open" on the top right-hand side to manage the latter by using the in-built Neo4j Browser.

### Coding

-	Each Cypher statement (i.e., code between two comments in the ```knowledgeGraph_cypherCode.txt``` file) has to be executed individually (i.e., "Play" button on the right-hand side or "Ctrl" + "Enter") in a distinct cell of the interactive Cypher Shell integrated within Neo4j Browser.
-	For writing code, it is recommended to use a plain text editor (e.g., open-source text editor Notepad++, https://notepad-plus-plus.org/downloads/) in order for the written code to be used without formatting issues in the Cypher Shell.
-	To facilitate the writing, it is possible to import in Notepad++ a user xml to highlight the syntax of Cypher (https://gist.github.com/nicolewhite/b0344ea475852c8c9571).

### Visualization

#### Neo4j Browser
-	Once the nodes/relationships have been created, execute the following command in the interactive Cypher Shell to visualise graphically the knowledge graph directly in Neo4j Browser: ```MATCH (n) RETURN n```.
-	Be aware of Neo4j limitations, by default put in place to ensure the responsiveness of the DBMS, may prevent the correct display of the graph (since visual rendering is a resource-intensive task, depending mainly on GPU capabilities).

#### Neo4j Bloom
- Once the nodes/relationships have been created, switch to the Neo4j control panel and click on "▼" < "Neo4j Bloom" (next to "Open", top right-hand side).
-	In the search bar, input the label of one type of nodes (e.g., the highest in the graph depth) and click on "Enter" to display the selected nodes.
-	Use the key combination "Ctrl" + "A" to select all the nodes, and then use the key combination "Ctrl" + "E" to expand the displayed nodes based on their relationships.
-	To export the graph, click on "Share" < "Export screenshot" (top right-hand side), select a location and click on "Save".

