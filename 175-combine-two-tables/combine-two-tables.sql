SELECT person.firstName,  person.lastName, address.city,  address.state 
FROM Person person LEFT OUTER JOIN Address address ON person.personId = address.personId;
