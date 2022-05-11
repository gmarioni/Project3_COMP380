CREATE DATABASE IF NOT EXISTS pm;
USE pm;
CREATE TABLE IF NOT EXISTS USERS (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name CHAR(40)
);
CREATE TABLE IF NOT EXISTS PRIORITY (
    priority_id INT AUTO_INCREMENT PRIMARY KEY,
    priority CHAR(40)
);
CREATE TABLE IF NOT EXISTS SERVERITY (
    serverity_id INT AUTO_INCREMENT PRIMARY KEY,
    serverity CHAR(40)
);
CREATE TABLE IF NOT EXISTS STATUS (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    status CHAR(40)
);
CREATE TABLE IF NOT EXISTS NOTES (
    notes_id INT AUTO_INCREMENT PRIMARY KEY,
    notes TEXT,
    decision_id INT
);
CREATE TABLE IF NOT EXISTS DELIVERABLES (
    deliverable_id INT AUTO_INCREMENT PRIMARY KEY,
	name CHAR(40),
    description TEXT,
    due_date DATE
);
CREATE TABLE IF NOT EXISTS TASKS (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    deliverable_id INT NOT NULL,
	name CHAR(40),
    description TEXT,
    assigned_to INT,
    expected_start_date DATE,
    expected_end_date DATE,
    expected_duration INT,
    expected_effort INT,
    actual_start_date DATE,
    actual_end_date DATE,
    actual_duration INT,
    effort_completed DATE,
    actual_effort DATE,
    percent_complete INT,
    predecessor_task TEXT,
    successor_task TEXT
);
CREATE TABLE IF NOT EXISTS ISSUES (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    task_id INT NOT NULL,
	name CHAR(40),
    description TEXT,
    assigned_to INT,
    priority INT,
    serverity INT,
    date_raised DATE,
    date_assigned DATE,
    expected_completion_date DATE,
    actual_completion_date DATE,
    status INT,
    status_description TEXT,
    update_date DATE
);
CREATE TABLE IF NOT EXISTS ACTIONITEMS (
    actionitem_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_id INT NOT NULL,
	name CHAR(40),
    description TEXT,
    date_created DATE,
    date_assigned DATE,
    assigned_to INT,
    expected_completion_date DATE,
    actual_completion_date DATE,
    status INT,
    status_description TEXT,
    update_date DATE
);
CREATE TABLE IF NOT EXISTS DECISIONS (
    decision_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_id INT NOT NULL,
	name CHAR(40),
    description TEXT,
    priority INT,
    serverity INT,
    date_created DATE,
    date_needed DATE,
    decision_maker INT,
    expected_completion_date DATE,
    actual_completion_date DATE
);


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

INSERT INTO DELIVERABLES (name,description,due_date) VALUES ("User Interface","User Interface with the Following Items:\nClean\nEasy to Use","2022-08-22");
INSERT INTO TASKS (name,description,assigned_to,deliverable_id) VALUES ("Design GUI","Design High Level GUI",(SELECT user_id FROM USERS WHERE user_name = "buchinskiy"),(SELECT deliverable_id FROM DELIVERABLES WHERE name = "User Interface"));
INSERT INTO ISSUES (name,description,assigned_to,task_id) VALUES ("Filter Wrong Dates","Database Date format is different from users, need to transform date",(SELECT user_id FROM USERS WHERE user_name = "marioni"),(SELECT task_id FROM TASKS WHERE name = "Design GUI"));
INSERT INTO ACTIONITEMS (name,description,date_created,issue_id) VALUES ("Date Transform Method","Method to transform dates approirately","2022-10-22",(SELECT issue_id FROM ISSUES where name = "Filter Wrong Dates"));
INSERT INTO DECISIONS (name,description,date_created,issue_id,decision_maker) VALUES ("Decide on timeline","Do dates need to change due to the date filter issue?","2022-10-22",(SELECT issue_id FROM ISSUES where name = "Filter Wrong Dates"),(SELECT user_id FROM USERS where user_name = "amaro"));
