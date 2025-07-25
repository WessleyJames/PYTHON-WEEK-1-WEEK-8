const express = require('express');
const { v4: uuidv4 } = require('uuid');

let products = []; // in-memory

module.exports = (authenticate, validateProduct) => {
  const router = express.Router();

  // GET all products
  router.get('/', (req, res) => {
    let result = products;
    if (req.query.category) {
      result = result.filter(p => p.category.toLowerCase() === req.query.category.toLowerCase());
    }
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const start = (page - 1) * limit;
    const end = start + limit;
    res.json(result.slice(start, end));
  });

  // GET single product
  router.get('/:id', (req, res) => {
    const product = products.find(p => p.id === req.params.id);
    if (!product) return res.status(404).json({ error: 'Product not found' });
    res.json(product);
  });

  // POST new product
  router.post('/', authenticate, validateProduct, (req, res) => {
    const { name, description, price, category, inStock } = req.body;
    const newProduct = { id: uuidv4(), name, description, price, category, inStock };
    products.push(newProduct);
    res.status(201).json(newProduct);
  });

  // PUT update product
  router.put('/:id', authenticate, validateProduct, (req, res) => {
    const idx = products.findIndex(p => p.id === req.params.id);
    if (idx === -1) return res.status(404).json({ error: 'Product not found' });
    const { name, description, price, category, inStock } = req.body;
    products[idx] = { id: products[idx].id, name, description, price, category, inStock };
    res.json(products[idx]);
  });

  // DELETE product
  router.delete('/:id', authenticate, (req, res) => {
    const idx = products.findIndex(p => p.id === req.params.id);
    if (idx === -1) return res.status(404).json({ error: 'Product not found' });
    const deleted = products.splice(idx, 1);
    res.json({ message: 'Product deleted', product: deleted[0] });
  });

  // SEARCH products
  router.get('/search/name', (req, res) => {
    const q = (req.query.q || '').toLowerCase();
    const result = products.filter(p => p.name.toLowerCase().includes(q));
    res.json(result);
  });

  // STATS
  router.get('/stats/count', (req, res) => {
    const stats = {};
    products.forEach(p => {
      stats[p.category] = (stats[p.category] || 0) + 1;
    });
    res.json(stats);
  });

  return router;
};
