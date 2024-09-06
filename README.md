lolo cookies


welcome to lolo cookies website ..its a website were you can find all kinde of cookies




















  





















































Team members:


This website was created by Alaa Mohammed.Aloyaaltuff (aloyaaltuff) (github.com)


Technologies :
I use for this project : 
1. html. 
2. css.
3. javascript.
4. ruby and jekyll.
5. flask
6. python


Challenge statement:


Lolo cookies website is your mate in wedding cookies and birth gifts. Also for graduation gifts it's just about click away!


This beautiful website is just perfectly perfect for those who don't have time to go buy some gifts or sweet cookies for different purposes.
Risks:


The only risk  I could face during the process of creating this website is the time . So I need to organize my time to finish it in time because it's a team project but I am working on it solo so I think this could be it .
but I am planning my time and putting my priorities on  top so I will get through this problem .


Infrastructure:


I intend to deploy my website with the data using the visual studio code , inserting data in html links and testing in my web browser microsoft edge and that's how I see the changes and test the errors . keep it simple because simpleness is cool ! 


Existing Solutions:


how to exit ? simple just click the exit button .


Architecture:


**Introduction to the Architecture Diagram for "Lolo Cookies" Website**


The architecture diagram for the "Lolo Cookies" website illustrates the end-to-end system design of our online cookie store, specifically focusing on the integration of an "Order via WhatsApp" button. This diagram provides a comprehensive overview of how different components of the system interact to facilitate seamless customer orders and efficient order management.


**Key Components:**
- **User Interface (Front-end)**: Includes the homepage where customers view products, promotions, and a dedicated "Order via WhatsApp" button integrated on product pages and the order form.
- **Back-end Server**: Responsible for processing incoming order data from the user interface and integrating with the WhatsApp API to send order details directly to the store’s WhatsApp number.
- **Database**: Stores order details, customer information, and order history for tracking and management purposes.
- **WhatsApp Service**: Receives order messages sent through the WhatsApp API and provides a direct line of communication for order processing.


The diagram demonstrates the flow of data from customer interactions on the website to backend processing and communication via WhatsApp, ensuring a smooth and efficient ordering experience for customers and effective order management for the store.






  















Data Modelling :


Lolo Cookies Data Model Summary


Overview 


The data model for Lolo Cookies supports managing customer information, orders, products, and WhatsApp interactions.
 Entities 


1. **Customers**
   - **Attributes:** CustomerID (PK), FirstName, LastName, PhoneNumber, Email, Address, CreatedAt, UpdatedAt.
   - **Description:** Stores customer details.


2. **Orders**
   - **Attributes:** OrderID (PK), CustomerID (FK), OrderDate, TotalAmount, Status, WhatsAppOrder, CreatedAt, UpdatedAt.
   - **Description:** Contains information about each order placed.


3. **OrderItems**
   - **Attributes:** OrderItemID (PK), OrderID (FK), ProductID (FK), Quantity, UnitPrice.
   - **Description:** Details items within each order.


4. **Products**
   - **Attributes:** ProductID (PK), ProductName, Description, Price, StockQuantity, CreatedAt, UpdatedAt.
   - **Description:** Information about available products.


5. **WhatsAppMessages**
   - **Attributes:** MessageID (PK), CustomerID (FK), MessageContent, MessageDate, Status, CreatedAt.
   - **Description:** Logs WhatsApp messages sent by customers.








Relationships


- **Customers to Orders:** One-to-Many (One customer can place multiple orders).
- **Orders to OrderItems:** One-to-Many (One order can include multiple items).
- **Products to OrderItems:** One-to-Many (One product can appear in multiple order items).
- **Customers to WhatsAppMessages:** One-to-Many (One customer can send multiple messages).
 Notes


- **Indexes:** Recommended on CustomerID, OrderID, and ProductID for performance.
- **Data Integrity:** Foreign key constraints should be used to maintain referential integrity.
- **Scalability:** Review and update the model as needed to handle growth and changes.


bellow data model diagram to clarify how data will be stored :
  











 User Stories :




As a New Customer
Story: I want to register an account on the Lolo Cookies website so that I can place orders and track my order history.
Acceptance Criteria:
I can enter my personal information (name, email, phone number, address) to create an account.
I receive a confirmation email upon successful registration.
I can log in to my account using my email and password.
As a Registered Customer
Story: I want to browse the product catalog so that I can choose and purchase cookies.
Acceptance Criteria:
I can view a list of available cookies with their descriptions, prices, and images.
I can filter products by categories or search for specific items.
I can view product details and add items to my cart.
As a Customer Placing an Order
Story: I want to place an order for cookies and choose a payment method so that I can receive my purchase.
Acceptance Criteria:
I can review my cart, adjust quantities, and remove items.
I can enter or confirm my shipping address.
I can choose a payment method (e.g., credit card, PayPal).
I receive an order confirmation email with order details.
As a Customer Using WhatsApp for Orders
Story: I want to place an order via WhatsApp so that I can use my preferred messaging platform.
Acceptance Criteria:
I can click a WhatsApp button on the website to start a chat with customer support.
I can send my order details via WhatsApp.
I receive confirmation of my order through WhatsApp.
As a Customer Tracking an Order
Story: I want to track the status of my order so that I know when it will be delivered.
Acceptance Criteria:
I can log in to my account and view the status of my orders.
I can see detailed information about the order status (e.g., pending, shipped, delivered).


 Mockups :




This summary outlines the key visual mockups for the Lolo Cookies website, describing each major interface and its features. click the link below and take a look :




lolo cookies mockup
