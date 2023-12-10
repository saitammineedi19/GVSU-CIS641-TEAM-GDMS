# Overview
<p align='justify'>
This Software needs Specification (SRS) document that acts as a thorough blueprint detailing the Inventory Management System's(IMS) functional and non-functional needs. It specifies the required features, functionalities, constraints, and interfaces, laying the groundwork for development and guiding the design, implementation, and testing phases. This document ensures that all stakeholders, including developers, designers, and clients, have a clear grasp of the project's scope and objectives.
</p>

# Software Requirements

This part contains elements such as an introduction that provides an overview, functional requirements that specify system functions, and non-functional needs that outline restrictions such as performance, security and user interface.

  
## Functional Requirements
  
### Add an Item to the Inventory  
| ID | Requirement |
| :-------------: | :---------- |
| FR1 |The system shall have an text field to enter the name of the item. |
| FR2 |The system shall have a text field to enter the location of the inventory. |
| FR3 |The system shall have a number field to enter the price of the item.|
| FR4 | The system shall have a quantity field to enter the quantity of item that gets added to the inventory. |
| FR5 |The system shall have a submit button to add the the item to the inventory. |
| FR6 |The sysytem shall autogenerate ID to the newly added Items. |
  
### Update an existing Item in the Inventory
| ID | Requirement |
| :-------------: | :---------- |
| FR7 | The system shall have an update feature for every item. |
| FR8 | The system shall allow to update the item name. |
| FR9 | The system shall allow to update the price of the item. |
| FR10 | The system shall allow to upddate the quantity of the item. |
| FR11 |The system shall allow to update the location of the item. |

### Transferring an Item from one location to another
| ID | Requirement |
| :-------------: | :---------- |
| FR12 | The system shall have transfer feature to transfer items from one location to another. |
| FR13 | The system shall display a transfer form after clicking on Transfer button. |
| FR14 | The system shall have a text field to enter the item name on the tranfer form. |
| FR15 | The system shall have a text field to enter the location from which item is transferring. |
| FR16 |The system shall have a text field to enter the location to which item needs to be transferred. |
| FR17 |The system shall have a number field to enter the quantity that is being transferred. |

### Database Management
| ID | Requirement |
| :-------------: | :---------- |
| FR18 | The system shall generate a users table in the database that the system is connected to.|
| FR19 | The users table shall contain users ID column which is auto-incremented. |
| FR20 | The users table shall contain username and password columns. |
| FR21 | The systems shall generate items table in the database. |
| FR22 |The items table shall contains item ID colun which is auto-incremented. |
| FR23 |The items table shall also contain item name, item price, item quantity and item location columns.|

### Data Validations
| ID | Requirement |
| :-------------: | :---------- |
| FR24 | The system shall not allow to add item to the inventory when the item name matches to the existing items at the same location. |
| FR25 | The shall display an error message saying that item already exists in the same location. |
| FR26 | The system shall display an error message when a negative number is enter in the price field. |
| FR27 | The system shall display an error message when the quantity that is being transferred is greater than the available quantity at from location. |
| FR28 | The system shall display a successs message when an item is updated is successfully. |
| FR29 | The system shall display a success message when transfer is done successfully. |
| FR30 | The system shall display success message when an item is added successfully. |

### User Authentication and Management
| ID | Requirement |
| :-------------: | :---------- |
| FR31 | The system shall have user to create an account to access IMS. |
| FR32 | The system shall allow user to login to IMS.|
| FR33 | The system shall allow user to logout from the IMS. |
| FR34 | The system shall not allow user to IMS if he entered incorrect password or username. |

## Non-Functional Requirements

### Security
| ID | Requirement |
| :-------------: | :---------- |
| NFR1 | User passwords shall securely hashed before storage, ensuring data security. |
| NFR2 | The system shall perform input validation to prevent some common vulnerabilities like SQL injcetions. |
| NFR3 | The system shall provide basic user authentication for user access control. |
| NFR4 | The system shall provide basic validation to ensure data consistency. | 
| NFR5 | The system shall perform secure database operations. |

### Performance
| ID | Requirement |
| :-------------: | :---------- |
| NFR5 | The system shall respond promptly under normal loads for basic CRUD operations. |
| NFR6 | The system shall allow minor scalability enhancements. |
| NFR8 | The system shall handle a moderate number of requests per second efficiently. |
| NFR9 | The system shall Utilize server resources adequately for current functionalities. | 
| NFR10 | The system shall offer acceptable latency in retrieving and processing data. |

### Usability
| ID | Requirement |
| :-------------: | :---------- |
| NFR11 | The system shall provide a basic user interface for signup, signin, and inventory management. |
| NFR12 | The navigation shall be relatively straightforward between different features. |
| NFR13 | The  error messages shall provide feedback on user action. |
| NFR14 | The system shall support basic responsiveness for different device screen sizes. | 
| NFR15 | The UI shall maintain some consistency across different modules. |

### Reliability
| ID | Requirement |
| :-------------: | :---------- |
| NFR16 | The system shall include rudimentary error handling for better resilience. |
| NFR17 | The system shall include Some error recovery mechanisms. |
| NFR18 | The system shall maintain stable operations under nominal conditions. |
| NFR19 | The system shall conduct basic data backups to avoid data loss. | 
| NFR20 | The system shall have minimal logging for monitoring and debugging purposes. |

### Reliability
| ID | Requirement |
| :-------------: | :---------- |
| NFR21 | The system shall ensure database schema versioning to manage future updates. |
| NFR22 | The system's codebase shall be relatively organized, aiding readability. |
| NFR23| The system's codebase shall include basic comments and explanations exist, aiding future maintenance. |
| NFR24 | The system's code shall include basic error handling mechanisms for smoother maintenance. | 
| NFR25 | The system's codebase shall be version controlled, facilitating collaborative development. |


# Change management plan
## Training Plan
### Detailed assessment of training needs:
- To understand the different demands and skill levels of users, do a thorough assessment.
- Determine which specific components of the inventory management system require advanced training.
### Personalized Training Materials:
- Provide individualized training materials that are appropriate for various user roles.
- To suit varying learning styles, combine interactive workshops, online tutorials, and thorough documentation.
### Gradual Training Method:
- Use a step-by-step training approach, starting with basic features and working our way up to more complex ones.
- Provide a smooth process of learning so that people can become used to the technology gradually.
### Interesting Practical Exercises:
- Organize practical workshops that allow users to interact directly with the Inventory Management System.
- Establish a learning environment in which students can apply concepts from theory to real-world situations.
### Dedicated Assistance and Input Mechanism:
- During training, create a dedicated support staff to address user inquiries quickly.
- Encourage users to submit their thoughts and incorporate modifications into the training program to create a continuous feedback loop.
## Integration within Ecosystem/Software
### Compatibility Evaluation:
- Examine the customer's present infrastructure and software in great detail.
- Determine whether there are any compatibility or conflicting issues.
### Personalization and Setup:
- Provide options for customization so that the Inventory Management System can be integrated with current processes.
- Give instructions on how to configure the system to satisfy particular requirements.
### Integrity Checking:
- Before doing the full deployment, thoroughly verify the integration for smoothness.
- Work closely with the customer's IT staff to resolve any issues arising from integration.
### Data and API Collaboration:
- Check to see if the system's APIs follow accepted industry practices.
- Utilize methods that guarantee a seamless transition to address worries about data migration.
### Trial Implementation:
- Start a test initiative with a targeted user group to identify and resolve integration issues.
- Gather input to improve and streamline the integration procedure.
## Issue Resolution Plan
### Centralized Issue Reporting:
- Provide a centralized mechanism where people can report problems.
- Sort and rank reported problems based on how serious they are.
### Quick Reaction Group:
- Assemble a dedicated group to handle critical issues as soon as possible.
- Establish targets for response times for various kinds of problems.
### Frequent Patch Releases & Updates:
- Organize planned patches and updates to fix found problems.
- Provide thorough release notes and notify users of any changes.
### Mechanism for User Feedback:
- Encourage users to provide comments on their experiences.
- Make use of user feedback for ongoing improvement and problem-solving.
### Constant Observation:
- Establish a mechanism for continuous system performance monitoring.
- Before they have an effect on users, proactively identify and resolve possible problems.



# Traceability links
<p align='justify'>
This section contains all the artifacts i.e., use case diagrams, activity diagrams, class diagram, object diagram and the requirement IDs that these artifacts satisfy
</p>


## Use Case Diagram Traceability

| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| [UseCase1](https://github.com/saitammineedi19/GVSU-CIS641-TEAM-GDMS/blob/main/artifacts/Usecase1.png) | User authentication and Management | FR31, FR32, FR33, FR34 |
| [UseCase2](https://github.com/saitammineedi19/GVSU-CIS641-TEAM-GDMS/blob/main/artifacts/usecase2.png) | Warehouse Manager activities | FR1-FR17 |


## Class Diagram Traceability

| Artifact Name | Requirement ID |
| :-------------: |:----------: |
| Inventory Class | FR1-FR17 |
| Add Item Class | FR1-FR6 |
| Update item class | FR7-FR11 |
| Transfer Class | FR12-FR17 |
| User authentication class | FR31-FR34 |
| Database class | FR18-FR23 |


## Activity Diagram Traceability


| Artifact ID  | Artifact Name | Requirement ID |
| :-------------: | :----------: | :----------: |
| [Activity1](https://github.com/saitammineedi19/GVSU-CIS641-TEAM-GDMS/blob/main/artifacts/Activity%20Diagram%201.jpeg) | Handle adding an item | FR1-6, FR24-26, NFR4, NFR12-13|
| [Activity2](https://github.com/saitammineedi19/GVSU-CIS641-TEAM-GDMS/blob/main/artifacts/Activity%20Diagram%202.jpeg) | Handling updating | FR7-11, FR24-26, NFR4, NFR12-13 |
| [Activity3](https://github.com/saitammineedi19/GVSU-CIS641-TEAM-GDMS/blob/main/artifacts/Activity%20Diagram%203.jpeg) | Handling item transfers| FR12-17, FR25-26, NFR4, NFR12-13 |


