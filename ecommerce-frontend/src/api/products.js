const BASE_URL = 'http://127.0.0.1:8000/api';

export async function fetchProducts(page = 1) {
  const res = await fetch(`${BASE_URL}/products/?page=${page}`);
  return await res.json();
}

export async function fetchProductById(id) {
  const res = await fetch(`${BASE_URL}/products/${id}`);
  return await res.json();
}

export async function fetchDepartments() {
  const res = await fetch(`${BASE_URL}/departments`);
  return await res.json();
}

export async function fetchDepartmentProducts(departmentId, page = 1) {
  const res = await fetch(`${BASE_URL}/departments/${departmentId}/products/?page=${page}`);
  return await res.json();
}

export async function fetchDepartmentById(departmentId) {
  const res = await fetch(`${BASE_URL}/departments/${departmentId}`);
  return await res.json();
}
