import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { fetchDepartmentProducts, fetchDepartmentById } from '../api/products';

const DepartmentProducts = () => {
  const { id } = useParams();
  const [products, setProducts] = useState([]);
  const [department, setDepartment] = useState(null);
  const [page, setPage] = useState(1);
  const [next, setNext] = useState(null);
  const [prev, setPrev] = useState(null);

  useEffect(() => {
    fetchDepartmentById(id).then(data => setDepartment(data));
    fetchDepartmentProducts(id, page).then(data => {
      setProducts(data.results);
      setNext(data.next);
      setPrev(data.previous);
    });
  }, [id, page]);

  return (
    <div className="container">
      <h2>{department?.name} ({products.length} items)</h2>
      <Link to="/">← All Products</Link>

      <div className="grid">
        {products.map(product => (
          <Link to={`/products/${product.id}`} key={product.id} className="card-link">
            <div className="card">
              <h3>{product.name}</h3>
              <p><strong>Brand:</strong> {product.brand}</p>
              <p><strong>Category:</strong> {product.category}</p>
              <p><strong>Price:</strong> ₹{product.retail_price}</p>
            </div>
          </Link>
        ))}
      </div>

      <div className="pagination">
        <button onClick={() => setPage(page - 1)} disabled={!prev}>← Prev</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(page + 1)} disabled={!next}>Next →</button>
      </div>
    </div>
  );
};

export default DepartmentProducts;
