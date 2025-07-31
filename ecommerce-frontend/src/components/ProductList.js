import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../api/products';
import { Link } from 'react-router-dom';
import './productList.css'; // Make sure this file exists for custom styles

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [next, setNext] = useState(null);
  const [previous, setPrevious] = useState(null);
  const [page, setPage] = useState(1);

  useEffect(() => {
    fetchProducts(page).then(data => {
      setProducts(data.results);
      setNext(data.next);
      setPrevious(data.previous);
    });
  }, [page]);

  return (
    <div className="container">
      <h2 className="title">All Products</h2>
      
      <div className="grid">
        {products.map(product => (
          <Link to={`/products/${product.id}`} key={product.id} className="card-link">
            <div className="card">
              <h3 className="product-name">{product.name}</h3>
              <p><strong>Brand:</strong> {product.brand}</p>
              <p><strong>Category:</strong> {product.category}</p>
              <p><strong>Price:</strong> ₹{product.retail_price}</p>
            </div>
          </Link>
        ))}
      </div>

      <div className="pagination">
        <button onClick={() => setPage(page - 1)} disabled={!previous}>← Prev</button>
        <span>Page {page}</span>
        <button onClick={() => setPage(page + 1)} disabled={!next}>Next →</button>
      </div>
    </div>
  );
};

export default ProductList;
