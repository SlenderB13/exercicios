SELECT 
    c.state_code, 
    c.company_name, 
    p.number
FROM 
    clients c
JOIN 
    phones p ON c.id = p.client_id
WHERE 
    c.state_code = 'SP';
