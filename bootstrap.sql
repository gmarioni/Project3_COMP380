INSERT INTO USERS (user_name) VALUES("notari");
INSERT INTO USERS (user_name) VALUES("amaro");
INSERT INTO USERS (user_name) VALUES("singh");
INSERT INTO USERS (user_name) VALUES("marioni");
INSERT INTO USERS (user_name) VALUES("buchinskiy");

INSERT INTO PRIORITY (priority) VALUES("High");
INSERT INTO PRIORITY (priority) VALUES("Medium");
INSERT INTO PRIORITY (priority) VALUES("Low");

INSERT INTO SERVERITY (serverity) VALUES("Critical");
INSERT INTO SERVERITY (serverity) VALUES("High");
INSERT INTO SERVERITY (serverity) VALUES("Medium");
INSERT INTO SERVERITY (serverity) VALUES("Low");
INSERT INTO SERVERITY (serverity) VALUES("Minor");

INSERT INTO STATUS (status) VALUES("Open");
INSERT INTO STATUS (status) VALUES("Closed");
INSERT INTO STATUS (status) VALUES("In Progress");
INSERT INTO STATUS (status) VALUES("Hold");
INSERT INTO STATUS (status) VALUES("Complete");

-- INSERT INTO DELIVERABLES (name,description,due_date) VALUES ("User Interface","User Interface with the Following Items:\nClean\nEasy to Use","2022-08-22");
-- INSERT INTO TASKS (name,description,assigned_to,deliverable_id) VALUES ("Design GUI","Design High Level GUI",(SELECT user_id FROM USERS WHERE user_name = "buchinskiy"),(SELECT deliverable_id FROM DELIVERABLES WHERE name = "User Interface"));
-- INSERT INTO ISSUES (name,description,assigned_to,task_id) VALUES ("Filter Wrong Dates","Database Date format is different from users, need to transform date",(SELECT user_id FROM USERS WHERE user_name = "marioni"),(SELECT task_id FROM TASKS WHERE name = "Design GUI"));
-- INSERT INTO ACTIONITEMS (name,description,date_created,issue_id) VALUES ("Date Transform Method","Method to transform dates approirately","2022-10-22",(SELECT issue_id FROM ISSUES where name = "Filter Wrong Dates"));
-- INSERT INTO DECISIONS (name,description,date_created,issue_id,decision_maker) VALUES ("Decide on timeline","Do dates need to change due to the date filter issue?","2022-10-22",(SELECT issue_id FROM ISSUES where name = "Filter Wrong Dates"),(SELECT user_id FROM USERS where user_name = "amaro"));
