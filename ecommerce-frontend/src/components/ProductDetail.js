import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { fetchProductById } from "../api/products";

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchProductById(id)
      .then(setProduct)
      .catch(() => setError("Product not found"));
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!product) return <p>Loading...</p>;

  return (
    <div style={{ padding: "20px" }}>
      <Link to="/">← Back to Products</Link>
      <h2>{product.name}</h2>
      <p><strong>Brand:</strong> {product.brand}</p>
      <p><strong>Price:</strong> ₹{product.retail_price}</p>
      <p><strong>Cost:</strong> ₹{product.cost}</p>
      <p><strong>Category:</strong> {product.category}</p>
      <p><strong>Department:</strong> {product.department}</p>
      <p><strong>SKU:</strong> {product.sku}</p>
    </div>
  );
}

export default ProductDetail;
