// src/components/Sidebar.js
import React, { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { fetchDepartments } from '../api/products';
import './Sidebar.css';

const Sidebar = () => {
  const [departments, setDepartments] = useState([]);
  const [collapsed, setCollapsed] = useState(false);
  const location = useLocation();

  useEffect(() => {
    fetchDepartments().then(data => setDepartments(data));
  }, []);

  return (
    <div className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <h3>{!collapsed && "Departments"}</h3>
        <button className="collapse-btn" onClick={() => setCollapsed(!collapsed)}>
          {collapsed ? '▶' : '◀'}
        </button>
      </div>

      <ul className="sidebar-list">
        <li>
          <Link
            to="/"
            className={location.pathname === '/' ? 'active' : ''}
          >
            {!collapsed ? 'All Products' : '📦'}
          </Link>
        </li>

        {departments.map(dept => (
          <li key={dept.id}>
            <Link
              to={`/departments/${dept.id}`}
              className={location.pathname === `/departments/${dept.id}` ? 'active' : ''}
            >
              {!collapsed ? dept.name : '🏷️'}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
