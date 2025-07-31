import React, { useEffect, useState } from 'react';
import { fetchDepartments } from '../api/products';
import { Link } from 'react-router-dom';

const DepartmentList = () => {
  const [departments, setDepartments] = useState([]);

  useEffect(() => {
    fetchDepartments().then(data => setDepartments(data));
  }, []);

  return (
    <aside>
      <h3>Departments</h3>
      <ul>
        {departments.map(dept => (
          <li key={dept.id}>
            <Link to={`/departments/${dept.id}`}>{dept.name}</Link>
          </li>
        ))}
      </ul>
    </aside>
  );
};

export default DepartmentList;
