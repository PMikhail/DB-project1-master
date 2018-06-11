
drop table Goes_to_School;
drop table Employment;
drop table Belongs_to_Family;
drop table Individuals;
drop table Families;
drop table Social_Workers;
drop table Issues;
drop table Contact_Info;

create table Contact_Info (
	cid serial primary key,
	street varchar(128),
	city varchar(50),
	zip varchar(9),
	state varchar(2),
	phone varchar(15),
	email varchar(50)
);

create table Issues (
	iid serial primary key,
	name varchar(128),
	description text
);

create table Social_Workers (
	ssn varchar(9) primary key,
	name varchar(128) not null,
	title varchar(50),
  	date_started DATE,
	specialization integer not null,
	contact_info integer,
	foreign key (contact_info) references Contact_Info(cid),
	foreign key (specialization) references Issues(iid)
);

create table Families (
	fid serial primary key,
	last_name varchar(128),
	date_joined date,
	issue integer not null,
	social_worker varchar(9) not null,
	sw_since Date not null,
	foreign key (issue) references Issues(iid),
	foreign key (social_worker) references Social_Workers(ssn)
);

create table Individuals (
  ssn varchar(9) primary key,
  name varchar(128) not null,
  date_joined DATE,
	contact_info integer,
	issue integer not null,
	social_worker varchar(9) not null,
	 sw_since Date not null,
	foreign key (contact_info) references Contact_Info(cid),
	foreign key (issue) references Issues(iid),
	foreign key (social_worker) references Social_Workers(ssn)
);

create table Belongs_to_Family (
	fid integer,
	ssn varchar(9),
	primary key (fid, ssn),
	foreign key (fid) references Families(fid),
	foreign key (ssn) references Individuals(ssn)
);

create table Employment (
	eid serial,
	employee varchar(9),
	position varchar(128),
	primary key (employee, eid),
	foreign key (employee) references Individuals(ssn)
);

create table Goes_to_School (
	sid serial,
	student varchar(9) unique,
	advisor varchar(60),
	primary key (student, sid),
	foreign key (student) references Individuals(ssn)
);

INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('11 Church St', 'Philadelphia', '19111', 'PA', '2152152211', 'hello@example.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('11021 Blah St', 'San Diego', '92027', 'CA', '9929949292', 'goodboi@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('422 Blah Ave', 'Denver', '80123', 'CO', '65666628221', 'plsemailme@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('372 Rocky Mt', 'San Diego', '92027', 'CA', '4646292911', 'thisorthat@comcast.net');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('593 Green Lane', 'Denver', '80123', 'CO', '65666628221', 'abc123@aol.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('102 Brooks Ave', 'Philadelphia', '19111', 'PA', '2152152293', 'bigbrain@yahoo.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('68438 44th St', 'Philadelphia', '19111', 'PA', '21526739201', 'blahblah@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('18 42th St', 'Philadelphia', '19111', 'PA', '48472727191', 'heythere@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('18 42th St', 'Philadelphia', '19111', 'PA', '48472727191', 'heythere@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('2999 Forest Avenue', 'New York', '10001', 'NY', '6468231192', 'rwwj222@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('4276 Shinn Street', 'New York', '10019', 'NY', '6498250392', 'ilovepistachios@nuts.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('2348 Crowfield Road', 'Phoenix', '85008', 'AZ', '6027975335', 'crazyglue@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('4506 Burnside Court', 'Phoenix', '85021', 'AZ', '9023575025', 'pooooo8483@comcast.net');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('12 24th St', 'Philadelphia', '19111', 'PA', '21526700291', 'jeez@gmail.com');
INSERT INTO Contact_info(street, city, zip, state, phone, email) VALUES ('211 Race St', 'Philadelphia', '19111', 'PA', '215203828113', 'alala222@gmail.com');

INSERT INTO Issues(name, description) VALUES ('Alcohol Addiction', 'A chronic disease in which your body and mind become dependent on alcohol');
INSERT INTO Issues(name, description) VALUES ('Child Abuse', 'Physical maltreatment or sexual molestation of a child');
INSERT INTO Issues(name, description) VALUES ('Spousal Abuse', 'Physical maltreatment or sexual molestation of one''s partner');
INSERT INTO Issues(name, description) VALUES ('Terminal illness', 'Pallative care assigned');
INSERT INTO Issues(name, description) VALUES ('Incarcerated parent(s) (has a caretaker)', 'One or both parents are incarcerated, but the person has a relative as primary caretaker');
INSERT INTO Issues(name, description) VALUES ('Incarcerated parent(s) (no caretaker)', 'One or both parents are incarcerated, no relative to serve as a primary caretaker');
INSERT INTO Issues(name, description) VALUES ('Poverty', 'Individuals/families below the poverty line');
INSERT INTO Issues(name, description) VALUES ('Older adult', 'Older adult who does not have a family member to take care of them');
INSERT INTO Issues(name, description) VALUES ('Clinical Depression', 'A mood disorder with symptom such as sadness, irritability, loss of interest in most or all activities, sleep disturbances, and other dark, dark stuff.');
INSERT INTO Issues(name, description) VALUES ('Physical Disability', 'A limitation on a person''s physical functioning, mobility or stamina');

INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('123456789', 'Michael Scott', 'Clinical Psychologist', '23-DEC-1998', 1, 3);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('992346666', 'Angie Smith', 'Psychotherapist', '1-MAY-2014', 1, 1);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('432117688', 'Carol Gee', 'Child Advocate', '1-MAY-2014', 2, 2);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('667280025', 'Larry B. Swanson', 'Social Worker of all trades', '1-MAY-2018', 5, 6);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('123456655', 'William L. Bell', 'Child Advocate', '14-MAY-2000', 2, 7);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('430201688', 'Donna Bell', 'Psychotherapist', '12-JUN-2004', 1, 7);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('320017622', 'Julie J. Flores', 'Psychotherapist', '25-DEC-1999', 9, 8);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('744960079', 'Doreen M. Cooper', 'Neuro-psychologist', '20-NOV-2009', 9, 9);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('616819322', 'Noah Young', 'Phd', '11-APR-2005', 8, 10);
INSERT INTO Social_workers(ssn, name, title, date_started, specialization, contact_info) VALUES ('172161823', 'Linda Young', 'MD', '21-MAY-2008', 8, 10);

INSERT INTO Families(last_name, date_joined, issue, social_worker, sw_since) VALUES ('Martin', '1-JAN-2017', 2, '432117688', '13-JAN-2018');
INSERT INTO Families(last_name, date_joined, issue, social_worker, sw_since) VALUES ('Jade', '1-Mar-2018', 4, '123456789', '1-Mar-2018');
INSERT INTO Families(last_name, date_joined, issue, social_worker, sw_since) VALUES ('Wilkinson', '14-FEB-2017', 7, '123456655', '14-FEB-2017');

INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('684939977', 'Ricky Martin', '1-Jan-2017', 4, 1, '432117688', '13-jan-2018');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('939211120', 'John Martin', '1-Jan-2017', 4, 2, '432117688', '13-jan-2018');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('105030030', 'Jenny Martin', '1-Jan-2017', 4, 2, '432117688', '13-jan-2018');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('543211002', 'Clara Jade', '1-Mar-2018', 5, 4, '123456789', '1-Mar-2018');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('172161823', 'Tom Johnston', '11-JUL-2015', 11, 8, '667280025', '11-JUL-2015');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('979598408', 'John Oliver', '28-FEB-2012', 15, 9, '430201688', '28-FEB-2012');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('779790234', 'Mollie Shah', '15-AUG-2016', 14, 9, '430201688', '1-Jan-2018');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('759352377', 'Andrew Wilkinson', '14-FEB-2017', 13, 7, '123456655', '14-FEB-2017');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('141705623', 'Lauren Wilkinson', '14-FEB-2017', 13, 7, '123456655', '14-FEB-2017');
INSERT INTO individuals(ssn, name, date_joined, contact_info, issue, social_worker, sw_since) VALUES ('962129501', 'Thomas J. Mace', '7-Mar-2000', 12, 10, '172161823', '27-MAY-2016');


INSERT INTO Belongs_to_Family(fid, ssn) VALUES (1, '684939977');
INSERT INTO Belongs_to_Family(fid, ssn) VALUES (1, '939211120');
INSERT INTO Belongs_to_Family(fid, ssn) VALUES (1, '105030030');
INSERT INTO Belongs_to_Family(fid, ssn) VALUES (2, '543211002');
INSERT INTO Belongs_to_Family(fid, ssn) VALUES (3, '759352377');
INSERT INTO Belongs_to_Family(fid, ssn) VALUES (3, '141705623');

INSERT INTO Employment(employee, "position") VALUES ('684939977', 'Glass-blower');
INSERT INTO Employment(employee, "position") VALUES ('543211002', 'Babysitter');
INSERT INTO Employment(employee, "position") VALUES ('172161823', 'Retired');
INSERT INTO Employment(employee, "position") VALUES ('979598408', 'Photographer');
INSERT INTO Employment(employee, "position") VALUES ('779790234', 'Accountant');
INSERT INTO Employment(employee, "position") VALUES ('759352377', 'Unemployed');
INSERT INTO Employment(employee, "position") VALUES ('141705623', 'Janitor');
INSERT INTO Employment(employee, "position") VALUES ('962129501', 'Data Entry');

INSERT INTO Goes_to_school(student, advisor) VALUES ('939211120', 'Ms.Jeffersonn');
INSERT INTO Goes_to_school(student, advisor) VALUES ('105030030', 'Ms.Clark');

