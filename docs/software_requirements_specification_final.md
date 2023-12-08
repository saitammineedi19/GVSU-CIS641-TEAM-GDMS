# Overview
<p align='justify'>
This Software needs Specification (SRS) document acts as a thorough blueprint detailing the Inventory Management System's(IMS) functional and non-functional needs. It specifies the required features, functionalities, constraints, and interfaces, laying the groundwork for development and guiding the design, implementation, and testing phases. This document ensures that all stakeholders, including developers, designers, and clients, have a clear grasp of the project's scope and objectives.
</p>

# Software Requirements

This part contains elements such as an introduction that provides an overview, functional requirements that specify system functions, and non-functional needs that outline restrictions such as performance, security and user interface.

  
## Functional Requirements
  
### Add an Item to the Inventory  
| ID | Requirement |
| :-------------: | :---------- |
| FR1 |The system shall have an text field to enter the name of the item.|
| FR2 |The system shall have a text field to enter the location of the inventory. |
| FR3 |The system shall have a number field to enter the price of the item.|
| FR4 | The system shall have a quantity field to enter the quantity of item that gets added to the inventory.|
| FR5 |The system shall have a submit button to add the the item to the inventory.|
|FR6|The sysytem shall autogenerate ID to the newly added Items|
  
### Update an existing Item in the Inventory
| ID | Requirement |
| :-------------: | :---------- |
| FR7 | The system shall have an update feature for every item. |
| FR8 | The system shall allow to update the item name |
| FR9 | The system shall allow to update the price of the item |
| FR10 | The system shall allow to upddate the quantity of the item |
|FR11|The system shall allow to update the location of the item|

### Transferring an Item from one location to another
| ID | Requirement |
| :-------------: | :---------- |
| FR12 | The system shall have transfer feature to transfer items from one location to another. |
| FR13 | The system shall display a transfer form after clicking on Transfer button |
| FR14 | The system shall have a text field to enter the item name on the tranfer form |
| FR15 | The system shall have a text field to enter the location from which item is transferring |
|FR16|The system shall have a text field to enter the location to which item needs to be transferred|
|FR17|The system shall have a number field to enter the quantity that is being transferred|

### Database Management
| ID | Requirement |
| :-------------: | :---------- |
| FR18 | The system shall generate a users table in the database that the system is connected to |
| FR19 | The users table shall contain users ID column which is auto-incremented |
| FR20 | The users table shall contain username and password columns |
| FR21 | The systems shall generate items table in the database |
|FR22|The items table shall contains item ID colun which is auto-incremented|
|FR23|The items table shall also contain item name, item price, item quantity and item location columns.|

### Data Validations
| ID | Requirement |
| :-------------: | :---------- |
| FR24 | The system shall not allow to add item to the inventory when the item name matches to the existing items at the same location |
| FR25 | The shall display an error message saying that item already exists in the same location |
| FR26| The system shall display an error message when a negative number is enter in the price field |
| FR27 | The system shall display an error message when the quantity that is being transferred is greater than the available quantity at from location |
| FR28 |The system shall display a successs message when an item is updated is successfully|
| FR29 |The system shall display a success message when transfer is done successfully.|
| FR30 |The system shall display success message when an item is added successfully|

## Non-Functional Requirements

### Security
| ID | Requirement |
| :-------------: | :----------: |
| NFR1 | User passwords shall securely hashed before storage, ensuring data security. |
| NFR2 | < Non-Functional Requirement 2> |
| NFR3 | < Non-Functional Requirement 3> |
| ... | ... | ... |


# Change management plan
## Training Plan
A well-planned training plan is essential to guarantee the new application's seamless integration into the client's operations. Initially, a training needs assessment will be conducted to determine the users' present competence levels and identify certain aspects that need to be addressed. Personalized training programs will be developed to accommodate a variety of user roles and will consist of a combination of online lessons, interactive seminars, and large documentation. A phased training strategy will be used, with the first sessions held before the official launch, in order to minimize interruptions. To respond to customer questions, a specialized support staff will be assigned, making use of a helpdesk system or live chat assistance. Through regular refresher courses and advanced training sessions, as well as by actively seeking user feedback for ongoing upgrades, an emphasis on continuous learning will be placed.

## Integration within Ecosystem/Software
The new application's success depends on its smooth integration into the client's current ecosystem. This requires a comprehensive compatibility evaluation to identify any possible conflicts or problems with the infrastructure and software that are in place. Options for customization will be provided in order to integrate the program with current workflows, along with configuration recommendations based on individual requirements. Thorough integration testing will be driven by a strict partnership with the client's IT staff, resolving any obstacles that arise. Ensuring API and data connectivity in accordance with industry standards will receive special attention. A carefully chosen set of users will be involved in a pilot implementation phase to identify and resolve integration difficulties; their feedback will be crucial in fine-tuning the integration process.

## Issue Resolution Plan
A comprehensive issue resolution plan will be implemented in order to promptly identify and address any obstacles that may arise. Users will have access to a centralized system for reporting problems, and these reports will undergo a thorough classification and prioritization process according to their level of severity. A team that is committed to providing a timely response will be formed to handle important problems within predetermined time frames. To address found problems, planned upgrades and patch releases will be carried out, and users will be informed in-depth of the release notes. Initiatives aimed at continual development will depend heavily on encouraging consumers to provide feedback on their experiences. The implementation of a methodical methodology aimed at continuously monitoring application performance would facilitate the early detection and resolution of possible problems before they adversely affect users.



