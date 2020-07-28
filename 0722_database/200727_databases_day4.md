# Ddatabase(0727)

### mysql 마스터와 슬레이브 설정

mysql 설치

```sh
# 먼저 마스터에서

$ yum install epel-release
$ yum -y install http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
$ yum -y install mysql-community-server

# mysql 시작
$ systemctl enable mysqld
$ systemctl start mysqld

$ vi etc/my.cnf # 아래 내용 추가

## password policy (비밀번호 최소 길이 : 4로 설정)
validate_password_policy=LOW
validate_password_length=4

$ cat /var/log/mysqld.log | grep password # 비밀번호 확인
$ mysql -uroot -p 

mysql> alter user 'root'@'localhost' identified by '변경할 비밀번호';
mysql> SHOW VARIABLES LIKE 'validate_password%';


# 슬레이브, ip, file, pos 다 맞춰줘야함

change master to master_host='192.168.56.11',master_user='repl_user',master_password='test4567',master_log_file='mysql-bin.000002',master_log_pos=595;
```





___

진행순서

1. db sql & modeling
2. create db application with python1
3. create db application with python2
4. deployment on docker (python + db, swarm X)
5. test(20~25문제), report(A4반장)



1일차

```mysql
#1번
select concat(first_name, ' ', last_name) as 'Name', job_id as 'Job' salary as'Salary',
(12*salary + 100) as 'Increased Ann_Salary', 12*(salary+100) as 'Increased Salary'
from employees;

#2번
select concat(last_name, ': 1 Year Salary = $', salary) as '1 Year Salary' from employees;

#3번
select concat(first_name, ' ', last_name) as 'Name', salary, job_id, commission_pct from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

#4번
select concat(first_name, ' ', last_name) as 'Name', salary, ceiling(1.23*salary) as 'Increased Salary'
from departments d, employees e
where d.department_id = e.department_id;

#5번
select concat(first_name, ' ',last_name, ' is a ', upper(job_id)) as 'Employee JOBs' from employees;

#6번
select concat(first_name, ' ',last_name) as 'Name', salary, 
if(commission_pct is null, 'Salary only', 'Salary + Commission') as IsCom 
from employees
order by salary desc;

#7번
select department_id, concat('$', cast(format(sum(salary), 0) as char)) as sum, 
concat('$', cast(format(avg(salary), 0) as char)) as avg, 
concat('$', cast(format(max(salary), 0) as char)) as max, 
concat('$', cast(format(min(salary), 0) as char)) as min
from employees
where job_id is not null
group by department_id
order by department_id;

#8번
select job_id, avg(salary) from (select * from employees where job_id not like '%CLERK') as e
group by job_id
having avg(salary)>10000;

#9번
select 'Han-Bit' as co, concat(e.first_name, ' ', e.last_name) as 'Name', e.job_id, d.department_name, l.city 
from employees e, departments d, locations l
where e.department_id=d.department_id and d.location_id=l.location_id and l.city='Oxford';

#10번
select d.department_name, count(e.department_id) 
from employees e, departments d
where d.department_id=e.department_id
group by e.department_id
order by count(e.department_id) desc;

#11번
select concat(e.first_name, ' ', e.last_name) as 'Name', 
e.job_id, d.department_name, e.hire_date, e.salary, j.grade_level 
from employees e, job_grades j, departments d
where e.department_id=d.department_id and e.salary between j.lowest_sal and j.highest_sal;

#12번
select concat(first_name, ' ', last_name) as 'Name', job_id, salary from employees
where salary > (select salary from employees where last_name='Tucker');

#13번
select concat(first_name, ' ', last_name) as 'Name', job_id, salary, hire_date
from employees
where (job_id, salary) in (select job_id, min(salary) from employees group by job_id);

#14번
select concat(first_name, ' ', last_name) as 'Name', e.salary, e.department_id, e.job_id from employees e, departments d
where e.department_id=d.department_id 
and salary >(
	select avg(salary) 
	from employees 
	where department_id=e.department_id
);

#15번
select e.job_id, concat(e.first_name, ' ', e.last_name) as 'Name', e.job_id, e.hire_date, l.city
from employees e, locations l, departments d
where e.department_id=d.department_id and d.location_id=l.location_id and left(l.city, 1)='O';

#16번
select concat(first_name, ' ', last_name) as 'Name', job_id, department_id,
(select avg(b.salary) from employees b where a.department_id=b.department_id)
from employees a;

# 17번
select distinct e.employee_id, e.job_id from employees e, job_history h
where e.employee_id=h.employee_id;

#18번
select distinct GREATEST(
	(select max(start_date) from job_history where employee_id=176), 
	(select min(start_date) from job_history where employee_id=176)) as change_job 
from job_history;

#19번
select department_id, sum(salary),
case when sum(salary) > 100000 then 'Excellent'
	 when sum(salary) <= 100000 and sum(salary) > 50000 then 'Good' 
	 when sum(salary) <= 50000 and sum(salary) > 10000 then 'Medium' 
	 when sum(salary) <= 10000 then 'Well' end as 'grade'
from employees group by department_id;

#20번
select employee_id, 
case when job_id like '%MGR%' and hire_date < '2005-01-01' then 1.15*salary
	 when job_id like '%MAN%' and hire_date < '2005-01-01'then 1.2*salary 
     when job_id like '%MGR%' and hire_date < '2005-01-01' then 1.25*salary end as 'Salary'
from employees
where employee_id in 
(select employee_id from employees 
where job_id like '%MGR%' or job_id like '%MAN%');
```

---

## docker

도커에 대해 쓰겠다

```c++
vector<int> v;

```

```sh
$ docker ps -a # asdfasdfasdfasdfasdf
```

````mysql
show databases; #asdfasdfasdf
````