drop database if exists violations;
create database :NEW_DB;

\connect :NEW_DB;

drop table if exists violation_codes;
create table violation_codes (
  violation_id text,
  org_id text,
  violation_type text,
  violation_desc text,
  violation_text text,
  remedial_text text,
  table_name text,
  expired_flag text,
  date_expired text,
  created_by text,
  date_created text,
  modified_by text,
  date_modified text,
  fee_setup_id text
);
copy violation_codes from :'VIOLATION_CODES_FILE' CSV HEADER;

drop table if exists property_standards_violations;
create table property_standards_violations (
  city text,
  complaint_source text,
  council_district text,
  date_received text,
  last_activity text,
  last_activity_date text,
  last_activity_result text,
  mapped_location text,
  mapped_location_address text,
  mapped_location_city text,
  mapped_location_state text,
  mapped_location_zip text,
  property_address text,
  property_apn text,
  property_owner text,
  reported_problem text,
  request text,
  state text,
  status text,
  violations_noted text,
  zip text
);
copy property_standards_violations from :'PSV_FILE' CSV HEADER;
