/* select workers (name, title, specialization) and the number of clients they currently have, 
as well as the dte they started worrking with their earliest client */
select w.name as "Social Worker", w.title as Title, iss.name as Specialization, count(i.ssn) as "Num of clients", min(i.sw_since) as "Oldest Current Client"
from social_workers w, individuals i, issues iss
where w.ssn=i.social_worker and w.specialization=iss.iid
group by w.name, w.specialization, iss.name
order by count(i.ssn) desc


/* select workers (ssn, name, title, specialization, state) that currently don't have any clients */
SELECT w.ssn, w.name, w.title, iss.name as Specialization, ci.state as "State Of Operation"
FROM   social_workers w, issues iss, contact_info ci
WHERE  w.ssn NOT IN (SELECT i.social_worker
                       FROM   individuals i, 
                              social_workers w
                       WHERE  w.ssn = i.social_worker) 
					and w.specialization=iss.iid and w.contact_info = ci.cid
					
/* show statistics of issues by state */
select iss.name, c.state, count(iss.iid)
from individuals i, issues iss, contact_info c
where i.issue=iss.iid and i.contact_info=c.cid
group by iss.name, c.state
order by count(iss.iid) desc, c.state