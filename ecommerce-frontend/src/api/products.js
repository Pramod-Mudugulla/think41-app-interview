export async function fetchProducts(page = 1) {
  const res = await fetch(`http://127.0.0.1:8000/api/products/?page=${page}`);
  if (!res.ok) throw new Error("Failed to fetch products");
  return await res.json();
}


export const fetchProductById = async (id) => {
  const response = await fetch(`http://127.0.0.1:8000/api/products/${id}/`);
  if (!response.ok) throw new Error("Product not found");
  return await response.json();
};
