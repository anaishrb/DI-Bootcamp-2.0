-- functions 

-- create [or replace] function function_name(param_list)
--   returns return_type
--   language plpgsql
--as
--$$
-- declare

-- variables names
-- begin
-- code/logic
--end
--$$

create or replace function get_customer_full_name(c_id int)
 returns varchar
language plpgsql
as
$$
declare
c_name varchar;
begin
 select first_name and last_name into c_name
 from customer where customer_id = c_id;

return c_name;
end;
$$

select get_customer_full_name(22)
