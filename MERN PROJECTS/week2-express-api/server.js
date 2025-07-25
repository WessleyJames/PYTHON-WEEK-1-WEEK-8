const express = require('express');
require('dotenv').config();

const logger = require('./middleware/logger');
const authenticate = require('./middleware/authenticate');
const validateProduct = require('./middleware/validateProduct');
const productRoutes = require('./routes/products');

const app = express();
const PORT = 3000;

// middleware
app.use(express.json());
app.use(logger);

// routes
app.get('/', (req, res) => res.send('Hello World'));
app.use('/api/products', productRoutes(authenticate, validateProduct));

// global error handler
app.use((err, req, res, next) => {
  console.error(err);
  res.status(err.status || 500).json({ error: err.message || 'Internal Server Error' });
});

app.listen(PORT, () => console.log(`✅ Server running on http://localhost:${PORT}`));
